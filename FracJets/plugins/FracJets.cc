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

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Utilities/interface/InputTag.h"

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

#include "DataFormats/JetReco/interface/PileupJetIdentifier.h"

#include "TTree.h"
#include "TMatrix.h"
#include "TVector.h"
#include "TLorentzVector.h"

//
// class declaration
//

class FracJet : public edm::EDAnalyzer {
public:
  explicit FracJet(const edm::ParameterSet&);
  ~FracJet();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


private:
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
  
  // ---------- internal functions--------------------
  double correlationFct(const PtrVector<flashgg::Jet>& recoJets);
  
};

FracJet::FracJet(const edm::ParameterSet& iConfig):
  genJetToken_  (consumes<View<reco::GenJet> >(iConfig.getUntrackedParameter<InputTag> ("GenJetTag", InputTag("slimmedGenJets")))),
  recoJetToken_ (consumes<View<flashgg::Jet> >(iConfig.getParameter<InputTag>("JetTagDz"))),
  vertexToken_  (consumes<View<reco::Vertex> >(iConfig.getUntrackedParameter<InputTag> ("VertexTag", InputTag("offlineSlimmedPrimaryVertices")))),
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

double FracJet::correlationFct(const PtrVector<flashgg::Jet>& recoJets, double R){
  
}

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
  
  
  for (unsigned int j = 0 ; j < recoJets.size() ; j++) {
    PtrVector<reco::Candidate>& pfcand = SortedPtJets[j]->getJetConstituentsQuick();
    for (unsigned int i = 0 ; i < pfcand.size() ; i++){
      for (unsigned int i = 0 ; i < pfcand.size() ; i++){
	
      }
    }
    
    tree->Fill();
  }
}


// ------------ method called once each job just before starting event loop  ------------
void 
FracJet::beginJob()
{
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
