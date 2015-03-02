// -*- C++ -*-
//
// Package:    FracJet/FracJet
// Class:      FracJet
// 
/**\class FracJet FracJet.cc FracJet/FracJet/plugins/FracJet.cc
   
   Description: [one line class summary]
   
   Implementation:
   [Notes on implementation]
*/
//
// Original Author:  Yacine Haddad
//         Created:  Mon, 23 Feb 2015 10:42:12 GMT
//
//


// system include files
#include <memory>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/Ptr.h"
#include "DataFormats/Common/interface/PtrVector.h"

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"

#include "flashgg/MicroAODAlgos/interface/VertexSelectorBase.h"
#include "flashgg/MicroAODFormats/interface/Photon.h"
#include "flashgg/MicroAODFormats/interface/DiPhotonCandidate.h"

#include "flashgg/MicroAODAlgos/interface/PhotonIdUtils.h"

#include "flashgg/MicroAODFormats/interface/VertexCandidateMap.h"
#include "flashgg/MicroAODFormats/interface/Jet.h"

#include "DataFormats/Math/interface/deltaR.h"


#include "TTree.h"

//
// class declaration
//
using namespace std;
using namespace edm;
using namespace flashgg;


struct jetInfo {
  float pt;
  float energy;
  float mass;
  float eta;
  float phi;
  
  float genJetPt;
  float genJetEta;
  float genJetPhi;
  int   genJetMatch;
  
  double D;
  double Cmean;
  double Rmean;
  
};


class FracJet : public edm::EDAnalyzer {
public:
  explicit FracJet(const edm::ParameterSet&);
  ~FracJet();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


private:
  
  edm::Service<TFileService> fs_;
  
  virtual void beginJob() override;
  virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
  virtual void endJob() override;
  
  //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
  //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
  //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
  //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
  
  EDGetTokenT< edm::View<reco::GenJet> >              genJetToken_;
  EDGetTokenT< edm::View<flashgg::Jet> >              recoJetToken_;
  EDGetTokenT< View<reco::Vertex> >                   vertexToken_;
  
  // ----------member data ---------------------------
  Int_t       event_number;
  jetInfo jet_info;
  TTree  *jetTree;
  
  std::string jetCollectionName; 
  // ---------- internal functions--------------------
  
};


FracJet::FracJet(const edm::ParameterSet& iConfig):
  genJetToken_  (consumes<View<reco::GenJet> >(iConfig.getUntrackedParameter<InputTag> ("GenJetTag", InputTag("slimmedGenJets")))),
  recoJetToken_ (consumes<View<flashgg::Jet> >(iConfig.getParameter<InputTag>("JetTagDz"))),
  vertexToken_  (consumes<View<reco::Vertex> >(iConfig.getUntrackedParameter<InputTag> ("VertexTag", InputTag("offlineSlimmedPrimaryVertices"))))
{
  //now do what ever initialization is needed
  event_number = 0;
  jetCollectionName = iConfig.getParameter<string>("StringTag");
}


FracJet::~FracJet()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
  event_number = 0;
}




//
// member functions
//
// ------------ method called for each event  ------------
void
FracJet::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  
  Handle<View<reco::Vertex> > primaryVertices;
  iEvent.getByToken(vertexToken_,primaryVertices);
  const PtrVector<reco::Vertex>& vtxs = primaryVertices->ptrVector();
  
  Handle<View<reco::GenJet> > genJet;
  iEvent.getByToken(genJetToken_,genJet);
  const PtrVector<reco::GenJet>& genJets = genJet->ptrVector();
  
  Handle<View<flashgg::Jet> > jets;
  iEvent.getByToken(recoJetToken_,jets);
  const PtrVector<flashgg::Jet>& recoJets = jets->ptrVector();
  
  genJets.size();
  vtxs.size();
  //recoJets.size();
  
  for (unsigned int j = 0 ; j < recoJets.size() ; j++) {
    // fill jet information
    jet_info.pt      = recoJets[j]->pt();
    
    if( recoJets[j]->genJet()){
      jet_info.genJetMatch           = 1;
      jet_info.genJetPt              = recoJets[j]->genJet()->pt();
      jet_info.genJetEta             = recoJets[j]->genJet()->eta();
      jet_info.genJetPhi             = recoJets[j]->genJet()->phi();
    } else {
      jet_info.genJetPt              = -9999.;
      jet_info.genJetEta             = -9999.;
      jet_info.genJetPhi             = -9999.;
      jet_info.genJetMatch           = 0;
    }
    jet_info.energy           = recoJets[j]->energy() ;
    jet_info.mass             = recoJets[j]->mass() ;
    jet_info.eta              = recoJets[j]->eta();
    jet_info.phi              = recoJets[j]->phi();
    
    std::vector<edm::Ptr<reco::Candidate> > pfcand = recoJets[j]->getJetConstituents();
    double Rstep =  0.1;
    double Rmax  =  0.4;
    unsigned int nstep =  (Rmax/Rstep);
    
    std::map<double,double> CorrVsR;
    double Rmean = 0;
    double Cmean = 0;
    for(unsigned int i=0; i < nstep; i++){
      double R = i*Rstep;
      double C = 0;
      
      for (unsigned int ip=0; ip < pfcand.size(); ip++){
  	for (unsigned int jp=0; jp < pfcand.size(); jp++){
  	  if (ip == jp ) continue;
  	  
  	  double dphi   = deltaPhi(pfcand[ip]->phi(),pfcand[jp]->phi());
  	  double deta   = pfcand[ip]->eta() - pfcand[jp]->eta();
  	  double DeltaR = std::sqrt(deta*deta + dphi*dphi);
  	  
  	  if ( DeltaR > R ) continue; // resolution condition 
  	  C += std::min(pow(pfcand[ip]->pt(),2),pow(pfcand[jp]->pt(),2)) * DeltaR *DeltaR ;
	}
      }
      CorrVsR.insert(std::make_pair(R, C));
      Rmean += R;
      Cmean += C;
      
    }
    Rmean = Rmean/nstep;
    Cmean = Cmean/nstep;
    
    jet_info.Rmean = Rmean;
    jet_info.Cmean = Cmean;
    
    double sumD = 0;
    double sumN = 0;
    for(std::map<double,double>::iterator it = CorrVsR.begin();it != CorrVsR.end(); it++){
      sumD += (it->first*it->second) - nstep * Rmean * Cmean;
      sumN += (it->first*it->first ) - nstep * Rmean * Rmean;
    }
    jet_info.D = sumD/sumN;
    
    jetTree->Fill();
  }
  event_number++;
}


// ------------ method called once each job just before starting event loop  ------------
void 
FracJet::beginJob()
{
  std::string typeJet("FracJet_");
  typeJet += jetCollectionName;
  jetTree = fs_->make<TTree>(typeJet.c_str(),jetCollectionName.c_str());
  jetTree->Branch("pt"              ,&jet_info.pt           ,"pt/F" );
  jetTree->Branch("energy"          ,&jet_info.energy       ,"energy/F" );
  jetTree->Branch("mass"            ,&jet_info.mass         ,"mass/F" );
  jetTree->Branch("eta"             ,&jet_info.eta          ,"eta/F");
  jetTree->Branch("phi"             ,&jet_info.phi          ,"phi/F");

  jetTree->Branch("D"               ,&jet_info.D            ,"D/F");
  jetTree->Branch("Cmean"           ,&jet_info.Cmean        ,"Cmean/F");
  jetTree->Branch("Rmean"           ,&jet_info.Rmean        ,"Rmean/F");
  
  jetTree->Branch("genJetPt"        ,&jet_info.genJetPt     ,"genJetPt/F" );
  jetTree->Branch("genJetEta"       ,&jet_info.genJetEta    ,"genJetEta/F" );
  jetTree->Branch("genJetPhi"       ,&jet_info.genJetPhi    ,"genJetPhi/F" );
  jetTree->Branch("genJetMatch"     ,&jet_info.genJetMatch  ,"genJetMatch/I" );
  
}

// ------------ method called once each job just after ending the event loop  ------------
void 
FracJet::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
/*
  void 
  FracJet::beginRun(edm::Run const&, edm::EventSetup const&)
  {
  }
*/

// ------------ method called when ending the processing of a run  ------------
/*
  void 
  FracJet::endRun(edm::Run const&, edm::EventSetup const&)
  {
  }
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
  void 
  FracJet::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
  {
  }
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
  void 
  FracJet::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
  {
  }
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
FracJet::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(FracJet);
