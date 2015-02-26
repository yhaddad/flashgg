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


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
//
// class declaration
//

class VertexForJetValidation : public edm::EDAnalyzer {
public:
  explicit VertexForJetValidation(const edm::ParameterSet&);
  ~VertexForJetValidation();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


private:
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
  EDGetTokenT<edm::View<flashgg::DiPhotonCandidate> > diPhotonToken_;
  
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
  diPhotonsToken_(consumes<View<flashgg::DiPhotonCandidate> >(iConfig.getUntrackedParameter<InputTag> ("DiPhotonTag", InputTag("flashggDiPhotons"))))
{
  //now do what ever initialization is needed
  
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
  Handle<View<flashgg::DiPhotonCandidate> > diphoton_;
  evt.getByToken(diPhotonsToken_,diphoton);
  const PtrVector<flashgg::DiPhotonCandidate>& diphoton = diphotons_->ptrVector();
  
  Handle<View<reco::Vertex> > primaryVertices;
  evt.getByToken(vertexToken_,primaryVertices);
  const PtrVector<reco::Vertex>& pvertex = primaryVertices->ptrVector();
  
  Handle<View<pat::PackedCandidate> > pfCandidates;
  evt.getByToken(packedToken_,pfCandidates);
  const PtrVector<pat::PackedCandidate>& pfcand = pfCandidates->ptrVector();
  
  Handle<VertexCandidateMap> vtxmap;
  evt.getByToken(vertexCandidateMapToken_,vtxmap);
  edm::Ptr<reco::Vertex> flashVertex;
  
  //-------- 
  edm::Ptr<reco::Vertex> flashVertex;
  if ( diPhotonPointers.size()==0 ){
    flashVertex = pvertex[0];
  }
  if ( diPhotonPointers.size()>=1 ){
    flashVertex = diphotons[0]->getVertex();
  }
  
  for(unsigned int ipf =0 ; ipf < pfcand.size() ; ipf++){
    if(pfcand[ipf]->charge() ==0) continue ; 
    
    
  }
  
}


// ------------ method called once each job just before starting event loop  ------------
void 
VertexForJetValidation::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
VertexForJetValidation::endJob() 
{
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
