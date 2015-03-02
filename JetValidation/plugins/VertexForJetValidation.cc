// -*- C++ -*-
//
// Package:    TmpPackage/VertexForJetValidation
// Class:      VertexForJetValidation
// 
/**\class VertexForJetValidation VertexForJetValidation.cc TmpPackage/VertexForJetValidation/plugins/VertexForJetValidation.cc
   
   Description: [one line class summary]
   
   Implementation:
   [Notes on implementation]
*/
//
// Original Author:  Yacine Haddad
//         Created:  Thu, 26 Feb 2015 17:21:49 GMT
//
//

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

#include "DataFormats/JetReco/interface/PileupJetIdentifier.h"

#include "TTree.h"
#include "TMatrix.h"
#include "TVector.h"
#include "TLorentzVector.h"


using namespace std;
using namespace edm;
using namespace flashgg;

struct pfcand_t{
  //void setTrack(){
  //  
  //}
  //void FillTree(){
  //  
  //}
  int   event;
  
  float pt;
  float phi;
  float eta;
  float z;
  float pv0z;
  float pvLegz;
  float dzLeg;
  float dz0;
  float npv;
};

struct vertex_t{
  //tree->Branch("z"      ,&v.z       ,"");
  //tree->Branch("dz"     ,$v.dz      ,"");
  //tree->Branch("isPV"   ,$v.isPV    ,"");
  //tree->Branch("nTracks",$v.nTracks ,"");
  int   event;
  
  float z;
  float dzToLeg; // distance to the legacy vertex
  int   isPV;    // is it the leading vertex
  int   nTracks;
  int   npv;
};


class VertexForJetValidation : public edm::EDAnalyzer {
public:
  explicit VertexForJetValidation(const edm::ParameterSet&);
  ~VertexForJetValidation();

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
  
  // ----------member data ---------------------------
  
  // ----------member data ---------------------------
  EDGetTokenT<View<pat::PackedCandidate> >   packedPFToken_;
  //EDGetTokenT<View<reco::Candidate> >        canPFToken_   ;
  EDGetTokenT<View<reco::Vertex> >           vertexToken_  ;
  EDGetTokenT<edm::View<flashgg::DiPhotonCandidate> > diphotonsToken_;
  

  pfcand_t pfcand_info;
  vertex_t vertex_info;
  std::string collName; 
  
  TTree *vertex_tree;
  TTree *pfcand_tree;

  unsigned int eventNo_;
  
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
VertexForJetValidation::VertexForJetValidation(const edm::ParameterSet& iConfig):
  packedPFToken_ (consumes<View<pat::PackedCandidate> >(iConfig.getUntrackedParameter<InputTag> ("PFCandidatesTag", InputTag("packedPFCandidates")))),
  vertexToken_   (consumes<View<reco::Vertex> >(iConfig.getUntrackedParameter<InputTag> ("VertexTag", InputTag("offlineSlimmedPrimaryVertices")))),
  diphotonsToken_(consumes<View<flashgg::DiPhotonCandidate> >(iConfig.getUntrackedParameter<InputTag> ("DiPhotonTag", InputTag("flashggDiPhotons"))))
{
  //now do what ever initialization is needed
  collName = iConfig.getParameter<string>("StringTag");
}


VertexForJetValidation::~VertexForJetValidation()
{
  
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
VertexForJetValidation::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  
  // ------- retrive all the collection ---------
  Handle<View<flashgg::DiPhotonCandidate> > diphotons_;
  iEvent.getByToken(diphotonsToken_,diphotons_);
  const PtrVector<flashgg::DiPhotonCandidate>& diphotons = diphotons_->ptrVector();
  
  Handle<View<reco::Vertex> > primaryVertices;
  iEvent.getByToken(vertexToken_,primaryVertices);
  const PtrVector<reco::Vertex>& pvertex = primaryVertices->ptrVector();
  
  Handle<View<pat::PackedCandidate> > pfCandidates;
  iEvent.getByToken(packedPFToken_,pfCandidates);
  const PtrVector<pat::PackedCandidate>& pfcand = pfCandidates->ptrVector();
  
  //Handle<VertexCandidateMap> vtxmap;
  //iEvent.getByToken(vertexToken_,vtxmap);
  //edm::Ptr<reco::Vertex> flashVertex;
  
  std::cout << "event :: "<< eventNo_ << std::endl;
  
  //-------- 
  edm::Ptr<reco::Vertex> ggvertex;
  
  if ( diphotons.size()==0){
    return ; // skip the event where there is no di-photon
  }
  
  if ( diphotons.size()>=1 ){
    ggvertex = diphotons[0]->getVertex();
  }
  
  
  for(unsigned int ivx =0 ; ivx < pvertex.size() ; ivx++){
    vertex_info.event   = eventNo_;
    vertex_info.z       = pvertex[ivx]->position().z();
    vertex_info.dzToLeg = pvertex[ivx]->position().z() - ggvertex->position().z();
    if(ivx==0) vertex_info.isPV    = 1; // is it the leading vertex
    else       vertex_info.isPV    = 0; // is it the leading vertex
    vertex_info.nTracks = pvertex[ivx]->nTracks(); // nbr of track with weight of 0.5 
    vertex_info.npv     = pvertex.size();
    
    vertex_tree->Fill();
  }
  
  // studies for the track-vertex association
  
  for(unsigned int ipf =0 ; ipf < pfcand.size() ; ipf++){
    if(pfcand[ipf]->charge() ==0 ) continue ; // drop neutral particles
    //  //++ fill the standard information 
    //  //++ about the track
    pfcand_info.event   = eventNo_;
    pfcand_info.pt      = pfcand[ipf]->pt();
    pfcand_info.eta     = pfcand[ipf]->eta();
    pfcand_info.phi     = pfcand[ipf]->phi();
    
    float z = pfcand[ipf]->vertex().z();
    
    pfcand_info.z       = z;
    pfcand_info.pv0z    = pvertex[0]->position().z();
    pfcand_info.pvLegz  = ggvertex  ->position().z();
    pfcand_info.dzLeg   = z - ggvertex  ->position().z();
    pfcand_info.dz0     = z - pvertex[0]->position().z();
    pfcand_info.npv     = pvertex.size();
    
    pfcand_tree->Fill();
    //  
  }
  
  // check the vertexing CHS in flashgg
  
  
  eventNo_++;
}
// ------------ method called once each job just before starting event loop  ------------
void 
VertexForJetValidation::beginJob()
{
  pfcand_tree = fs_->make<TTree>(("pfcand_"+collName).c_str(),collName.c_str());
  
  pfcand_tree->Branch("event"  ,&pfcand_info.event ,"event/I");
  pfcand_tree->Branch("pt"     ,&pfcand_info.pt    ,"pt/F");
  pfcand_tree->Branch("eta"    ,&pfcand_info.eta   ,"eta/F");
  pfcand_tree->Branch("phi"    ,&pfcand_info.phi   ,"phi/F");
  pfcand_tree->Branch("z"      ,&pfcand_info.z     ,"z/F");
  pfcand_tree->Branch("pv0z"   ,&pfcand_info.pv0z  ,"pv0z/F");
  pfcand_tree->Branch("pvLegz" ,&pfcand_info.pvLegz,"pvLegz/F");
  pfcand_tree->Branch("dzLeg"  ,&pfcand_info.dzLeg ,"dzLeg/F");
  pfcand_tree->Branch("dz0"    ,&pfcand_info.dz0   ,"dz0/F");
  pfcand_tree->Branch("npv"    ,&pfcand_info.npv   ,"npv/I");
  
  vertex_tree = fs_->make<TTree>(("vertex_"+collName).c_str(),collName.c_str());
  
  vertex_tree->Branch("event"  ,&vertex_info.event   ,"event/I");
  vertex_tree->Branch("z"      ,&vertex_info.z       ,"z/F");
  vertex_tree->Branch("npv"    ,&vertex_info.npv     ,"npv/I");
  vertex_tree->Branch("dzToLeg",&vertex_info.dzToLeg ,"dzToLeg/F");
  vertex_tree->Branch("isPV"   ,&vertex_info.isPV    ,"isPV/I");
  vertex_tree->Branch("nTrack" ,&vertex_info.nTracks ,"nTracks/I");
  
  eventNo_ = 0;
}

// ------------ method called once each job just after ending the event loop  ------------
void 
VertexForJetValidation::endJob() 
{
  eventNo_ = 0;
}

// ------------ method called when starting to processes a run  ------------
/*
  void 
  VertexForJetValidation::beginRun(edm::Run const&, edm::EventSetup const&)
  {
  }
*/

// ------------ method called when ending the processing of a run  ------------
/*
  void 
  VertexForJetValidation::endRun(edm::Run const&, edm::EventSetup const&)
  {
  }
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
  void 
  VertexForJetValidation::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
  {
  }
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
  void 
  VertexForJetValidation::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
  {
  }
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
VertexForJetValidation::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(VertexForJetValidation);
