// -----------------------
// By Y.Haddad & L.Corpe  12/2014
// 
// Jet validation analyzer: tree maker for the jet studies in flashgg
// -----------------------

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

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "flashgg/MicroAOD/interface/VertexSelectorBase.h"
#include "flashgg/DataFormats/interface/Photon.h"
#include "flashgg/DataFormats/interface/DiPhotonCandidate.h"
#include "flashgg/MicroAOD/interface/PhotonIdUtils.h"

#include "flashgg/DataFormats/interface/VertexCandidateMap.h"
#include "flashgg/DataFormats/interface/Jet.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "DataFormats/JetReco/interface/PileupJetIdentifier.h"


#include "TTree.h"
#include "TMatrix.h"
#include "TVector.h"
#include "TLorentzVector.h"

// **********************************************************************

struct eventInfo {
  
  float genVertexZ;
  float zerothVertexZ;
  float diphotonVertexZ;
  int   legacyEqZeroth;
  int   nDiphotons;
  
  unsigned int nJet;
  unsigned int nPV;
  unsigned int nSV;
  
  float leadJet_pt;
  float leadJet_eta;
  float leadJet_phi;
  
  float subleadJet_pt;
  float subleadJet_eta;
  float subleadJet_phi;
  
  float higgsPt;
  
  void init()  { 
    genVertexZ      =-999.;
    zerothVertexZ   =-999.;
    diphotonVertexZ =-999.;
    higgsPt         =-999.;
  }
};

// per-vertex tree
struct GenPartInfo {
  float pt;
  float eta;
  float y;
  float phi;
  int   pdgid;
  int   status;
  

  
  void init(){
    pt  =-999;
    eta =-999; 
  }
};

// per-genJet tree
struct GenJetInfo {
  float pt;
  float eta;
  float phi;
  float recoJetPt   ; 
  float recoJetRawPt ;
  float recoJetBestPt;
  int   recoJetMatch ;
  float recoJetEta   ;
  float dR   ;
  int legacyEqZeroth;
  int nDiphotons;
  float PUJetID_betaStar;
  float PUJetID_rms;
  int passesPUJetID;
  

  int   photonMatch;
  float photondRmin;
  float GenPhotonPt;
  
  
  void init(){
    pt  =-999;
    eta =-999; 
  }
};
// per recoJet tree
struct jetInfo {
  float pt;
  float rawPt;
  float bestPt;
  float energy;
  float mass;
  float area;
  float eta;
  float phi;
  int   PDG;
  
  
  float PlanarFlow;
  float S;
  float Q;
  
  float jet_W;
  float jet_dR2Mean;
  float jet_dRMean;
  float jet_dZ;
  float jet_ptD;
  
  float PUJetID_betaStar;
  float PUJetID_rms;
  int   passesPUJetID;
  int   LegIsPV0;
  int   nDiphotons;
  
  int   nPV;
  int   nJets;
  
  int   nPart ;  
  int   nCharged ; // number of particles at pt>0
  int   nNeutral ;  // number of particles at pt>0
  
  float chgEmFrac;
  float neuEmFrac;
  
  float genJetPt;
  float genJetEta;
  int   genJetMatch;
  float genQuarkPt;
  float genQuarkEta;
  int   genQuarkMatch;
  int   genQuarkPdgId;
  void init(){
    pt  =-999;
    eta =-999; 
  }
  // jets Id
  int id;
  // photon matching part
  int   photonMatch;
  float photondRmin;
  float GenPhotonEta;
  float GenPhotonPhi;
  float GenPhotonPt;
  
};  

struct GenPhotonInfo{
  float pt;
  float phi;
  float eta;
  float DRmin;
  void init(){
    pt  =-999;
    eta =-999; 
  }
  
};

// **********************************************************************

using namespace std;
using namespace edm;
using namespace flashgg;

// **********************************************************************

class JetValidationTreeMaker : public edm::EDAnalyzer {
public:
  explicit JetValidationTreeMaker(const edm::ParameterSet&);
  ~JetValidationTreeMaker();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

  
private:
  
  edm::Service<TFileService> fs_;
  
  virtual void beginJob() override;
  virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
  virtual void endJob() override;
  
  // Additional methods
  void initEventStructure();
  
  
  //bool GenRecoMatching(reco::GenJet genjet, const PtrVector<flashgg::Jet>& RecoJets){}
  //EDGetTokenT< VertexCandidateMap > vertexCandidateMapTokenDz_;
  //EDGetTokenT< VertexCandidateMap > vertexCandidateMapTokenAOD_;
  
  EDGetTokenT< edm::View<reco::GenParticle> > genPartToken_;
  EDGetTokenT< edm::View<reco::GenJet> >      genJetToken_;
  EDGetTokenT< edm::View<flashgg::Jet> >      jetDzToken_;
  EDGetTokenT<edm::View<flashgg::DiPhotonCandidate> > diPhotonToken_;
  EDGetTokenT< View<reco::Vertex> >           vertexToken_;
  
  TTree*     eventTree;
  TTree*     jetTree;
  TTree*     genPartTree;
  TTree*     genJetTree;
  
  eventInfo   eInfo;
  jetInfo     jInfo;
  GenPartInfo genInfo;
  GenJetInfo  genJetInfo;
  Int_t       event_number;
  std::string jetCollectionName; 
  
  GenPartInfo jGenPhotonInfo;
  
  bool        usePUJetID;
  bool        photonJetVeto;
};

JetValidationTreeMaker::JetValidationTreeMaker(const edm::ParameterSet& iConfig):
  genPartToken_ (consumes<View<reco::GenParticle> >(iConfig.getUntrackedParameter<InputTag> ("GenParticleTag", InputTag("prunedGenParticles")))),
  genJetToken_  (consumes<View<reco::GenJet> >(iConfig.getUntrackedParameter<InputTag> ("GenJetTag", InputTag("slimmedGenJets")))),
  jetDzToken_   (consumes<View<flashgg::Jet> >(iConfig.getParameter<InputTag>("JetTagDz"))),
  diPhotonToken_(consumes<View<flashgg::DiPhotonCandidate> >(iConfig.getUntrackedParameter<InputTag> ("DiPhotonTag", InputTag("flashggDiPhotons")))),
  vertexToken_  (consumes<View<reco::Vertex> >(iConfig.getUntrackedParameter<InputTag> ("VertexTag", InputTag("offlineSlimmedPrimaryVertices")))),
  usePUJetID    (iConfig.getUntrackedParameter<bool>("UsePUJetID"   ,false)),
  photonJetVeto (iConfig.getUntrackedParameter<bool>("PhotonJetVeto",true))
{
  event_number = 0;
  jetCollectionName = iConfig.getParameter<string>("StringTag");
}

//double JetPtSorter(std::vector<>){

//}


JetValidationTreeMaker::~JetValidationTreeMaker()
{
  event_number = 0;
}


void
JetValidationTreeMaker::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  
  Handle<View<reco::Vertex> > vtxs;
  iEvent.getByToken(vertexToken_,vtxs);
  //const PtrVector<reco::Vertex>& vtxs = primaryVertices->ptrVector();
  
  Handle<View<flashgg::DiPhotonCandidate> > diPhotons;
  iEvent.getByToken(diPhotonToken_,diPhotons);
  //const PtrVector<flashgg::DiPhotonCandidate>& diPhotons = diPhotons->ptrVector();
  
  Handle<View<reco::GenParticle> > gens;
  iEvent.getByToken(genPartToken_,gens);
  //const PtrVector<reco::GenParticle>& gens = genParticles->ptrVector();
  
  Handle<View<reco::GenJet> > genJets;
  iEvent.getByToken(genJetToken_,genJets);
  //const PtrVector<reco::GenJet>& genJets = genJet->ptrVector();
  
  Handle<View<flashgg::Jet> > jetsDz;
  iEvent.getByToken(jetDzToken_,jetsDz);
  //const PtrVector<flashgg::Jet>& jetsDzPointers = jetsDz->ptrVector();
  
  int legacyEqZeroth =0;
  int nDiphotons =0;
  
  if(event_number%5000 == 0) 
    std::cout <<"Run["  << iEvent.run() 
	      <<"]=evt["<< event_number << "]" 
	      << std::endl;
  
  nDiphotons = diPhotons->size();
  
  if(diPhotons->size()==0){
    legacyEqZeroth =1; //if there is no diphoton, we use 0th vertex anyway.
  } else {
    if(fabs(diPhotons->ptrAt(0)->vtx()->z() - vtxs->ptrAt(0)->z())<0.01){
      legacyEqZeroth =1;
    }
  }
  
  eInfo.nDiphotons     = nDiphotons;
  eInfo.legacyEqZeroth = legacyEqZeroth;
  
  initEventStructure();
  
  jInfo.nJets = jetsDz->size();
  jInfo.nPV   = vtxs->size();
  eInfo.nSV   = 0;
  
  // ++  finding the photon-jet overlaping
  std::map<unsigned int, GenPhotonInfo> photonJet_id;
  std::map<unsigned int, bool> _isPhoton;
  unsigned int nGenPhoton = 0;
  for( unsigned int genLoop =0 ; genLoop < gens->size(); genLoop++){
    genInfo.pt     = gens->ptrAt( genLoop )->pt() ;
    genInfo.eta    = gens->ptrAt( genLoop )->eta();
    genInfo.phi    = gens->ptrAt( genLoop )->phi();
    genInfo.status = gens->ptrAt( genLoop )->status();
    genInfo.pdgid  = int(gens->ptrAt( genLoop )->pdgId());
    
    std::map<float,unsigned int> minim;
    std::map<unsigned int,GenPhotonInfo> minim_info;
    float DeltaRmin=999.;
    
    if (gens->ptrAt( genLoop )->pdgId() == 22 && 
	gens->ptrAt( genLoop )->mother(0)->pdgId() == 25){ 
      
      nGenPhoton++;
      for( unsigned int jetLoop =0 ; jetLoop < jetsDz->size(); jetLoop++){
	GenPhotonInfo tmp_info;
	
	float dphi  = deltaPhi(jetsDz->ptrAt( jetLoop )->phi(),gens->ptrAt( genLoop )->phi());
	float deta  = jetsDz->ptrAt( jetLoop )->eta() -  gens->ptrAt( genLoop )->eta();
	float dr    =  std::sqrt(deta*deta + dphi*dphi);
	
	DeltaRmin = std::min (dr, DeltaRmin);
	minim[dr] = jetLoop; 
	
	// fill the info
	tmp_info.pt     = gens->ptrAt( genLoop )->pt ();
	tmp_info.eta    = gens->ptrAt( genLoop )->eta();
	tmp_info.phi    = gens->ptrAt( genLoop )->phi();	
	tmp_info.DRmin  = DeltaRmin;
	
	_isPhoton[jetLoop]  = false;
	minim_info[jetLoop] = tmp_info;
      }
      unsigned int bestjetid = minim.find(DeltaRmin)->second;
      if(DeltaRmin < 0.3){
	photonJet_id[bestjetid] = minim_info[bestjetid];
	_isPhoton[bestjetid] = true;
      }
    }
    genPartTree->Fill();
  }
  
  //std::cout << "============================" << std::endl;
  
  // +++ jets info  
  std::map<unsigned int, jetInfo> recojetmap;
  
  // +++ loop on the reconstructed jets
  for (unsigned int jdz = 0 ; jdz < jetsDz->size() ; jdz++) {
    jInfo.id            = jdz;
    jInfo.photonMatch   = int(_isPhoton[jdz]); 
    
    if( _isPhoton[jdz] ){
      GenPhotonInfo tmp_info = photonJet_id.find(jdz)->second; // call find ones 
      jInfo.photondRmin  = tmp_info.DRmin;
      jInfo.GenPhotonPt  = tmp_info.pt   ;
      jInfo.GenPhotonEta = tmp_info.eta  ;
      jInfo.GenPhotonPhi = tmp_info.phi  ;
    }else{
      jInfo.photondRmin  = -999.;
      jInfo.GenPhotonPt  = -999.;
      jInfo.GenPhotonEta = -999.;
      jInfo.GenPhotonPhi = -999.;
      jInfo.photondRmin  = -999.;
    }
    
    jInfo.pt            = jetsDz->ptrAt( jdz )->pt();
    jInfo.rawPt         = jetsDz->ptrAt( jdz )->correctedJet("Uncorrected").pt() ;
    
    if(jetCollectionName.find("PPI")>1 && jetCollectionName.find("PPI")<jetCollectionName.size()){
      jInfo.bestPt      = jetsDz->ptrAt( jdz )->correctedJet("Uncorrected").pt() ;
    } else {
      jInfo.bestPt      = jetsDz->ptrAt( jdz )->pt() ;
    }
    
    if( jetsDz->ptrAt( jdz )->genJet()){
      jInfo.genJetMatch           = 1;
      jInfo.genJetPt              = jetsDz->ptrAt( jdz )->genJet()->pt();
      jInfo.genJetEta             = jetsDz->ptrAt( jdz )->genJet()->eta();
      jInfo.genJetEta             = jetsDz->ptrAt( jdz )->genJet()->eta();
    } else {
      jInfo.genJetPt              = -9999.;
      jInfo.genJetEta             = -9999.;
      jInfo.genJetMatch           = 0;
    }
    
    if( jetsDz->ptrAt( jdz )->genParton()){
      jInfo.genQuarkMatch           = 1;
      jInfo.genQuarkPt              = jetsDz->ptrAt( jdz )->genParton()->pt();
      jInfo.genQuarkEta             = jetsDz->ptrAt( jdz )->genParton()->eta();
      jInfo.genQuarkPdgId           = jetsDz->ptrAt( jdz )->genParton()->pdgId();
    } else {
      jInfo.genQuarkPt              = -9999.;
      jInfo.genQuarkEta             = -9999.;
      jInfo.genQuarkMatch           = 0;
      jInfo.genQuarkPdgId           = -9999;
    }
    //----------------------
    jInfo.energy           = jetsDz->ptrAt( jdz )->energy() ;
    jInfo.mass             = jetsDz->ptrAt( jdz )->mass() ;
    jInfo.eta              = jetsDz->ptrAt( jdz )->eta();
    jInfo.phi              = jetsDz->ptrAt( jdz )->phi();
    jInfo.area             = jetsDz->ptrAt( jdz )->jetArea();
    
    
    if(!(jetCollectionName.find("PPI")>1 && jetCollectionName.find("PPI")<jetCollectionName.size()) )
      {
	// use the di-photon vertex if the di-photon existe otherwise use the Vtx0
	
	if((diPhotons->size() > 0 ) && 
	   ((jetCollectionName.find("Leg")>1 && jetCollectionName.find("Leg")<jetCollectionName.size())||(jetCollectionName.length()<3))){
	  
	  jInfo.PUJetID_betaStar   = jetsDz->ptrAt( jdz )->betaStar(diPhotons->ptrAt(0)->vtx());
	  jInfo.PUJetID_rms        = jetsDz->ptrAt( jdz )->rms(diPhotons->ptrAt(0)->vtx());
	  jInfo.passesPUJetID      = jetsDz->ptrAt( jdz )->passesPuJetId(diPhotons->ptrAt(0)->vtx());
	  
	  jInfo.jet_W       = jetsDz->ptrAt( jdz )->pileupJetIdentifier(diPhotons->ptrAt(0)->vtx()).jetW();
	  jInfo.jet_dR2Mean = jetsDz->ptrAt( jdz )->pileupJetIdentifier(diPhotons->ptrAt(0)->vtx()).dR2Mean();
	  jInfo.jet_dRMean  = jetsDz->ptrAt( jdz )->pileupJetIdentifier(diPhotons->ptrAt(0)->vtx()).dRMean();
	  jInfo.jet_dZ      = jetsDz->ptrAt( jdz )->pileupJetIdentifier(diPhotons->ptrAt(0)->vtx()).dZ();
	  jInfo.jet_ptD     = jetsDz->ptrAt( jdz )->pileupJetIdentifier(diPhotons->ptrAt(0)->vtx()).ptD();
	  
	  
	} else {
	  
	  jInfo.PUJetID_betaStar   = jetsDz->ptrAt( jdz )->betaStar(vtxs->ptrAt(0));
	  jInfo.PUJetID_rms        = jetsDz->ptrAt( jdz )->rms(vtxs->ptrAt(0));
	  jInfo.passesPUJetID      = jetsDz->ptrAt( jdz )->passesPuJetId(vtxs->ptrAt(0));
	  
	  jInfo.jet_W       = jetsDz->ptrAt( jdz )->pileupJetIdentifier(vtxs->ptrAt(0)).jetW();
	  jInfo.jet_dR2Mean = jetsDz->ptrAt( jdz )->pileupJetIdentifier(vtxs->ptrAt(0)).dR2Mean();
	  jInfo.jet_dRMean  = jetsDz->ptrAt( jdz )->pileupJetIdentifier(vtxs->ptrAt(0)).dRMean();
	  jInfo.jet_dZ      = jetsDz->ptrAt( jdz )->pileupJetIdentifier(vtxs->ptrAt(0)).dZ();
	  jInfo.jet_ptD     = jetsDz->ptrAt( jdz )->pileupJetIdentifier(vtxs->ptrAt(0)).ptD();
	  
	}
      } else {
      
      jInfo.PUJetID_betaStar       = -999.;
      jInfo.PUJetID_rms            = -999.;
      jInfo.passesPUJetID          = -999;
    }
    
    jInfo.nDiphotons = nDiphotons;
    jInfo.LegIsPV0   = legacyEqZeroth;
    //std::cout << "----> matched photon jet["<< jdz <<"] == "<< jInfo.legacyEqZeroth <<std::endl;
    
    // Get constituants information
    jInfo.nPart     = jetsDz->ptrAt( jdz )->numberOfDaughters  ();
    jInfo.nCharged  = jetsDz->ptrAt( jdz )->chargedMultiplicity();
    jInfo.nNeutral  = jetsDz->ptrAt( jdz )->neutralMultiplicity();
    jInfo.chgEmFrac = jetsDz->ptrAt( jdz )->chargedEmEnergy()/jetsDz->ptrAt( jdz )->energy(); //
    jInfo.neuEmFrac = jetsDz->ptrAt( jdz )->neutralEmEnergy()/jetsDz->ptrAt( jdz )->energy(); //
    
    /*  this part sould be introduced in RecoJets tools
    // loop over consitutuants
    jInfo.S      = -1.; // entropy to zero 
    jInfo.Q      = -100.; // Jet charge
    //jInfo.Weight = -1.;
    
    float jetPt_tmp = jetsDz->ptrAt( jdz )->pt();
    float M_ab =0 , M_aa = 0, M_bb = 0;
    
    for (unsigned int i = 0 ; i < jetsDz->ptrAt( jdz )->getJetConstituentsQuick().size() ; i++){
      const reco::Candidate* icand = jetsDz->ptrAt( jdz )->getJetConstituentsQuick()[i];
      float candPt                 = icand->pt();
      float candCharge             = icand->charge();
      jInfo.S      += (candPt/jetPt_tmp) * TMath::Log(candPt/jetPt_tmp); 
      jInfo.Q      += candCharge * TMath::Log(candPt/jetPt_tmp); 
      //jInfo.Weight += candCharge * TMath::Log(candPt/jetPt_tmp); 
      
      M_ab +=  candPt * (jetsDz->ptrAt( jdz )->eta() - icand->eta()) * (jetsDz->ptrAt( jdz )->phi() - icand->phi());
      M_aa +=  candPt * (jetsDz->ptrAt( jdz )->eta() - icand->eta()) * (jetsDz->ptrAt( jdz )->eta() - icand->eta());
      M_bb +=  candPt * (jetsDz->ptrAt( jdz )->phi() - icand->phi()) * (jetsDz->ptrAt( jdz )->eta() - icand->phi());
    }
    
    TMatrix M(2,2);
    M[0][0] = M_aa;
    M[1][1] = M_bb;
    M[0][1] = M_ab;
    M[1][0] = M_ab;
    
    TVector eigenvalues;
    TMatrix eigenvectors = M.EigenVectors(eigenvalues);
    
    jInfo.PlanarFlow = 4 * eigenvalues[0]*eigenvalues[1] / pow(eigenvalues[0] + eigenvalues[1],2);
    
    jInfo.S = - jInfo.S;
    jInfo.Q = - jInfo.Q;
    */
    
    recojetmap[jdz] = jInfo;
    jetTree->Fill();
  }// ++++ end loop reco jets
  

  
  // loop over the GenJets
  for( unsigned int genLoop =0 ; genLoop < genJets->size(); genLoop++){
    
    genJetInfo.recoJetPt       = -999.;
    genJetInfo.recoJetRawPt    = -999.;
    genJetInfo.recoJetBestPt   = -999.;
    genJetInfo.recoJetMatch    =  0   ;
    genJetInfo.recoJetEta      = -999.;
    genJetInfo.dR              = -999.;
    genJetInfo.pt              = -999.;
    genJetInfo.eta             = -999.;
    genJetInfo.phi             = -999.;
    genJetInfo.PUJetID_betaStar= -999.;
    genJetInfo.PUJetID_rms     = -999.;
    genJetInfo.passesPUJetID   = -999;
    genJetInfo.nDiphotons      = nDiphotons;

    if (genJets->ptrAt( genLoop )->pt() <20) { continue;}
    
    genJetInfo.pt     = genJets->ptrAt( genLoop )->pt() ;
    genJetInfo.eta    = genJets->ptrAt( genLoop )->eta();
    genJetInfo.phi    = genJets->ptrAt( genLoop )->phi();
    
    // ===========================
    // +++ new code for the matching based on the minimum
    // as the one I used for the photon overlaping
    
    std::map<float,unsigned int> minim;
    //float DeltaRmin=999.;
    // take only the jets without photons
    /*
    for( unsigned int jetLoop =0 ; jetLoop < jetsDz->size(); jetLoop++){
      float dphi  = jetsDz[jetLoop]->phi() -  gens->ptrAt( genLoop )->phi();
      float deta  = jetsDz[jetLoop]->eta() -  gens->ptrAt( genLoop )->eta();
      float dr    =  std::sqrt(deta*deta + dphi*dphi);
      
      DeltaRmin = std::min (dr, DeltaRmin);
      minim[dr] = jetLoop; 
    }
    
    unsigned int bestjetid = minim.find(DeltaRmin)->second;
    if(DeltaRmin < 100){
      genJetInfo.dR              = DeltaRmin;
      genJetInfo.recoJetPt       = jetsDz[bestjetid]->pt() ;
      genJetInfo.recoJetRawPt    = jetsDz[bestjetid]->correctedJet("Uncorrected").pt()  ;
      
      
      // ABOUT THE OVERLAPING PHOTON
      genJetInfo.photonMatch       = _isPhoton[bestjetid];
      if (_isPhoton[bestjetid]){ 
	jetInfo tmpjetinfo          = recojetmap[bestjetid];
	genJetInfo.GenPhotonPt     = tmpjetinfo.GenPhotonPt;
	genJetInfo.photondRmin     = tmpjetinfo.photondRmin;
      }else{
	genJetInfo.GenPhotonPt     = -999;
	genJetInfo.photondRmin     = -999;
      }
      
      if(!(jetCollectionName.find("PPI")>1 && jetCollectionName.find("PPI")<jetCollectionName.size())){
	genJetInfo.recoJetBestPt   =  jetsDz[bestjetid]->correctedJet("Uncorrected").pt() ;
	if( (diPhotons.size() > 0 ) && 
	    ((jetCollectionName.find("Leg")>1 && jetCollectionName.find("Leg")<jetCollectionName.size())||(jetCollectionName.length()   <3 )) ) { // for PF
	  
	  genJetInfo.PUJetID_betaStar        = jetsDz[bestjetid]->betaStar(diPhotons->ptrAt(0)->getvtx());
	  genJetInfo.PUJetID_rms             = jetsDz[bestjetid]->RMS(diPhotons->ptrAt(0)->getvtx());
	  genJetInfo.passesPUJetID           = jetsDz[bestjetid]->passesPuJetId(diPhotons->ptrAt(0)->getvtx());
	} else {
	  genJetInfo.PUJetID_betaStar        = jetsDz[bestjetid]->betaStar(vtxs->ptrAt(0));
	  genJetInfo.PUJetID_rms             = jetsDz[bestjetid]->RMS(vtxs->ptrAt(0));
	  genJetInfo.passesPUJetID           = jetsDz[bestjetid]->passesPuJetId(vtxs->ptrAt(0));
	  
	}
      } else {
	genJetInfo.recoJetBestPt   = jetsDz[bestjetid]->pt()  ;
	genJetInfo.PUJetID_betaStar  = -999.;
	genJetInfo.PUJetID_rms       = -999.;
	genJetInfo.passesPUJetID     = -999;
      }
      
      genJetInfo.recoJetMatch    = 1 ;
    }
    */
    // ===========================
    
    for (unsigned int recoLoop=0; recoLoop <  jetsDz->size(); recoLoop++){
      if(jetsDz->ptrAt( recoLoop )->pt() < 5) continue;

      double deta= jetsDz->ptrAt( recoLoop )->eta() - 	 genJets->ptrAt( genLoop )->eta();
      double dphi= jetsDz->ptrAt( recoLoop )->phi() - 	 genJets->ptrAt( genLoop )->phi();
      double dr = std::sqrt(deta*deta + dphi*dphi);
      if (dr < 0.4 ) {
	genJetInfo.dR      =  dr;
	genJetInfo.recoJetPt       = jetsDz->ptrAt( recoLoop )->pt() ;
	genJetInfo.recoJetRawPt    = jetsDz->ptrAt( recoLoop )->correctedJet("Uncorrected").pt()  ;

	// add the photon overlaping info 
	jetInfo tmpjetinfo = recojetmap[recoLoop];
	genJetInfo.photonMatch     = tmpjetinfo.photonMatch;
	genJetInfo.GenPhotonPt     = tmpjetinfo.GenPhotonPt;//recojetmap[recojetmap].GenPhotonPt  ;
	genJetInfo.photondRmin     = tmpjetinfo.photondRmin;//recojetmap[recojetmap].photondRmin  ;
	
	if(!(jetCollectionName.find("PPI")>1 && jetCollectionName.find("PPI")<jetCollectionName.size())){
	  genJetInfo.recoJetBestPt   =  jetsDz->ptrAt( recoLoop )->correctedJet("Uncorrected").pt() ;
	  if( (diPhotons->size() > 0 ) && 
	      ((jetCollectionName.find("Leg")>1 && jetCollectionName.find("Leg")<jetCollectionName.size())||(jetCollectionName.length()   <3 )) ) {
	    
	    genJetInfo.PUJetID_betaStar        = jetsDz->ptrAt( recoLoop )->betaStar(diPhotons->ptrAt(0)->vtx());
	    genJetInfo.PUJetID_rms             = jetsDz->ptrAt( recoLoop )->rms(diPhotons->ptrAt(0)->vtx());
	    genJetInfo.passesPUJetID           = jetsDz->ptrAt( recoLoop )->passesPuJetId(diPhotons->ptrAt(0)->vtx());
	  } else {
	    genJetInfo.PUJetID_betaStar        = jetsDz->ptrAt( recoLoop )->betaStar(vtxs->ptrAt(0));
	    genJetInfo.PUJetID_rms             = jetsDz->ptrAt( recoLoop )->rms(vtxs->ptrAt(0));
	    genJetInfo.passesPUJetID           = jetsDz->ptrAt( recoLoop )->passesPuJetId(vtxs->ptrAt(0));
	  }
	} else {
	  genJetInfo.recoJetBestPt   = jetsDz->ptrAt( recoLoop )->pt()  ;
	    genJetInfo.PUJetID_betaStar  = -999.;
	    genJetInfo.PUJetID_rms       = -999.;
	    genJetInfo.passesPUJetID     = -999;
	}
	
	genJetInfo.recoJetMatch    = 1 ;
	break;
      }
    }
    genJetTree->Fill();
  }

  eventTree->Fill();
  event_number++;
}

void 
JetValidationTreeMaker::beginJob()
{
  // +++ trees 
  std::string type("eventTree_");
  type += jetCollectionName;

  eventTree = fs_->make<TTree>(type.c_str(),jetCollectionName.c_str());
  eventTree->Branch("eventBranch",&eInfo.legacyEqZeroth,"legacyEqZeroth/I:nDiphotons/I");

  std::string typeJet("jetTree_");
  typeJet += jetCollectionName;
  jetTree = fs_->make<TTree>(typeJet.c_str(),jetCollectionName.c_str());
  jetTree->Branch("pt"              ,&jInfo.pt                ,"pt/F" );
  jetTree->Branch("rawPt"           ,&jInfo.rawPt             ,"rawPt/F" );
  jetTree->Branch("bestPt"          ,&jInfo.bestPt            ,"bestPt/F" );
  jetTree->Branch("energy"          ,&jInfo.energy            ,"energy/F" );
  jetTree->Branch("mass"            ,&jInfo.mass              ,"mass/F" );
  jetTree->Branch("eta"             ,&jInfo.eta               ,"eta/F");
  jetTree->Branch("phi"             ,&jInfo.phi               ,"phi/F");
  
  jetTree->Branch("PlanarFlow"      ,&jInfo.PlanarFlow        ,"PlanarFlow/F");
  jetTree->Branch("S"               ,&jInfo.S                 ,"S/F");
  jetTree->Branch("Q"               ,&jInfo.Q                 ,"Q/F");
  
  jetTree->Branch("passesPUJetID"   ,&jInfo.passesPUJetID     ,"passesPUJetID/I");
  jetTree->Branch("JetArea"         ,&jInfo.area              ,"area/F");
  jetTree->Branch("nDiphotons"      ,&jInfo.nDiphotons        ,"nDiphotons/I");
  jetTree->Branch("nPV"             ,&jInfo.nPV               ,"nPV/I");
  jetTree->Branch("nJets"           ,&jInfo.nJets             ,"nJets/I");
  jetTree->Branch("LegIsPV0"        ,&jInfo.LegIsPV0          ,"LegIsPV0/I");
  
  
  // ===== PUJID variables
  jetTree->Branch("betaStar" ,&jInfo.PUJetID_betaStar ,"betaStar/F");
  jetTree->Branch("rms"      ,&jInfo.PUJetID_rms      ,"rms/F");
  jetTree->Branch("W"        ,&jInfo.jet_W            ,"W/F");
  jetTree->Branch("dR2Mean"  ,&jInfo.jet_dR2Mean      ,"dR2Mean/F");
  jetTree->Branch("dRMean"   ,&jInfo.jet_dRMean       ,"dRMean/F");
  jetTree->Branch("dZ"       ,&jInfo.jet_dZ           ,"dZ/F");
  jetTree->Branch("ptD"      ,&jInfo.jet_ptD          ,"ptD/F");
  // =====
  
  jetTree->Branch("id"        ,&jInfo.id        ,"id/I");
  jetTree->Branch("nPart"     ,&jInfo.nPart     ,"nPart/I");
  jetTree->Branch("nCharged"  ,&jInfo.nCharged  ,"nCharged/I");
  jetTree->Branch("nNeutral"  ,&jInfo.nNeutral  ,"nNeutral/F");
  jetTree->Branch("chgEmFrac" ,&jInfo.chgEmFrac ,"chgEmFrac/F");
  jetTree->Branch("neuEmFrac" ,&jInfo.neuEmFrac ,"neuEmFrac/F");
  
  jetTree->Branch("genJetPt"       ,&jInfo.genJetPt     ,"genJetPt/F" );
  jetTree->Branch("genJetEta"      ,&jInfo.genJetEta    ,"genJetEta/F" );
  jetTree->Branch("genJetMatch"    ,&jInfo.genJetMatch  ,"genJetMatch/I" );
  jetTree->Branch("genQuarkPt"     ,&jInfo.genQuarkPt   ,"genQuarkPt/F" );
  jetTree->Branch("genQuarkEta"    ,&jInfo.genQuarkEta  ,"genQuarkEta/F" );
  jetTree->Branch("genQuarkMatch"  ,&jInfo.genQuarkMatch,"genQuarkMatch/I" );
  jetTree->Branch("genQuarkPdgId"  ,&jInfo.genQuarkPdgId,"genQuarkPdfId/I" );
  
  jetTree->Branch("photonMatch"    ,&jInfo.photonMatch  ,"photonMatch/I" );
  jetTree->Branch("photondRmin"    ,&jInfo.photondRmin  ,"photondRmin/F" );
  jetTree->Branch("GenPhotonPt"    ,&jInfo.GenPhotonPt   ,"GenPhotonPt/F" );
  jetTree->Branch("GenPhotonEta"   ,&jInfo.GenPhotonEta  ,"GenPhotonEta/F" );
  jetTree->Branch("GenPhotonPhi"   ,&jInfo.GenPhotonPhi  ,"GenPhotonPhi/F" );
  
  genPartTree = fs_->make<TTree>("genPartTree","Check per-jet tree");
  genPartTree->Branch("pt"     ,&genInfo.pt      ,"pt/F" );
  genPartTree->Branch("eta"    ,&genInfo.eta     ,"eta/F");
  genPartTree->Branch("phi"    ,&genInfo.phi     ,"phi/F");
  genPartTree->Branch("status" ,&genInfo.status  ,"status/I" );
  genPartTree->Branch("pdgid"  ,&genInfo.pdgid   ,"pdgid/I");
  genPartTree->Branch("y"      ,&genInfo.y       ,"y/F");   
  
  //genPartTree->SetBranchStatus( 'p4.*', 1 );
  
  std::string typeGenJet("genJetTree_");
  typeGenJet += jetCollectionName;
  genJetTree = fs_->make<TTree>(typeGenJet.c_str(),jetCollectionName.c_str());
  genJetTree->Branch("pt"     ,&genJetInfo.pt      ,"pt/F" );
  genJetTree->Branch("eta"    ,&genJetInfo.eta     ,"eta/F");
  genJetTree->Branch("phi"    ,&genJetInfo.phi     ,"phi/F");

  genJetTree->Branch("recoJetPt"        ,&genJetInfo.recoJetPt        ,"recoJetPt/F" );
  genJetTree->Branch("recoJetRawPt"     ,&genJetInfo.recoJetRawPt     ,"recoJetRawPt/F" );
  genJetTree->Branch("recoJetBestPt"    ,&genJetInfo.recoJetBestPt    ,"recoJetBestPt/F");
  genJetTree->Branch("recoJetMatch"     ,&genJetInfo.recoJetMatch     ,"recoJetMatch/I");
  genJetTree->Branch("recoJetEta"       ,&genJetInfo.recoJetEta       ,"recoJetEta/F" );
  genJetTree->Branch("dR"               ,&genJetInfo.dR               ,"dR/F" );
  genJetTree->Branch("PUJetID_betaStar" ,&genJetInfo.PUJetID_betaStar ,"PUJetID_betaStar/F");
  genJetTree->Branch("PUJetID_rms"      ,&genJetInfo.PUJetID_rms      ,"PUJetID_rms/F");
  genJetTree->Branch("passesPUJetID"    ,&genJetInfo.passesPUJetID    ,"passesPUJetID/I");
  genJetTree->Branch("nDiphotons"       ,&genJetInfo.nDiphotons        ,"nDiphotons/I");

  genJetTree->Branch("photonMatch"      ,&genJetInfo.photonMatch  ,"photonMatch/I" );
  genJetTree->Branch("photondRmin"      ,&genJetInfo.photondRmin  ,"photondRmin/F" );
  genJetTree->Branch("GenPhotonPt"      ,&genJetInfo.GenPhotonPt  ,"GenPhotonPt/F" );

}

void JetValidationTreeMaker::endJob() 
{

}

void JetValidationTreeMaker::initEventStructure() 
{

}


void JetValidationTreeMaker::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  // The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

typedef JetValidationTreeMaker FlashggJetValidationTreeMaker;
DEFINE_FWK_MODULE(FlashggJetValidationTreeMaker);
