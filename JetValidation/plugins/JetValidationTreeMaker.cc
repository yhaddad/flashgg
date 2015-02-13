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
  
  int nPV;
  int nJets;
  
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
  
  //EDGetTokenT< VertexCandidateMap > vertexCandidateMapTokenDz_;
  //EDGetTokenT< VertexCandidateMap > vertexCandidateMapTokenAOD_;
  
  EDGetTokenT< edm::View<reco::GenParticle> > genPartToken_;
  EDGetTokenT< edm::View<reco::GenJet> >      genJetToken_;
  EDGetTokenT< edm::View<flashgg::Jet> >      jetDzToken_;
  EDGetTokenT<edm::View<flashgg::DiPhotonCandidate> > diPhotonToken_;
  EDGetTokenT< View<reco::Vertex> > vertexToken_;
  
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
  
  Handle<View<reco::Vertex> > primaryVertices;
  iEvent.getByToken(vertexToken_,primaryVertices);
  const PtrVector<reco::Vertex>& vtxs = primaryVertices->ptrVector();
  
  Handle<View<flashgg::DiPhotonCandidate> > diPhotons;
  iEvent.getByToken(diPhotonToken_,diPhotons);
  const PtrVector<flashgg::DiPhotonCandidate>& diPhotonPointers = diPhotons->ptrVector();
  
  Handle<View<reco::GenParticle> > genParticles;
  iEvent.getByToken(genPartToken_,genParticles);
  const PtrVector<reco::GenParticle>& gens = genParticles->ptrVector();
  
  Handle<View<reco::GenJet> > genJet;
  iEvent.getByToken(genJetToken_,genJet);
  const PtrVector<reco::GenJet>& genJets = genJet->ptrVector();
  
  Handle<View<flashgg::Jet> > jetsDz;
  iEvent.getByToken(jetDzToken_,jetsDz);
  const PtrVector<flashgg::Jet>& jetsDzPointers = jetsDz->ptrVector();
  
  int legacyEqZeroth =0;
  int nDiphotons =0;

  //std::cout <<"Event == "<< <<std::endl;
  
  if(event_number%5000 == 0) 
    std::cout <<"Run["  << iEvent.run() 
	      <<"]=evt["<< event_number << "]" 
	      << std::endl;
  
  
  nDiphotons = diPhotonPointers.size();
  if(diPhotonPointers.size()==0){
    legacyEqZeroth =1; //if there is no diphoton, we use 0th vertex anyway.
  } else {
    if(fabs(diPhotonPointers[0]->getVertex()->z() - vtxs[0]->z())<0.01){
      legacyEqZeroth =1;
    }
  }
  eInfo.nDiphotons     = nDiphotons;
  eInfo.legacyEqZeroth = legacyEqZeroth;
    
  initEventStructure();
  
  jInfo.nJets = jetsDzPointers.size();
  jInfo.nPV   = vtxs.size();
  eInfo.nSV   = 0;
  
  // ++  finding the photon-jet overlaping
  
  std::map<unsigned int, GenPhotonInfo> photonJet_id;
  std::map<unsigned int, bool> _isPhoton;
  unsigned int nGenPhoton = 0;
  for( unsigned int genLoop =0 ; genLoop < gens.size(); genLoop++){
    genInfo.pt     = gens[genLoop]->pt() ;
    genInfo.eta    = gens[genLoop]->eta();
    genInfo.phi    = gens[genLoop]->phi();
    genInfo.status = gens[genLoop]->status();
    genInfo.pdgid  = int(gens[genLoop]->pdgId());
    
    TLorentzVector p;
    p.SetPxPyPzE( gens[genLoop]->px(), gens[genLoop]->py(), gens[genLoop]->pz(), gens[genLoop]->pt());
    genInfo.y = p.Rapidity(); 
    
    std::map<float,unsigned int> minim;
    std::map<unsigned int,GenPhotonInfo> minim_info;
    float DeltaRmin=999.;
    //std::cout << " status(pdg == "<< gens[genLoop]->pdgId() <<")== "<< gens[genLoop]->status() << std::endl;
    if (gens[genLoop]->pdgId() == 22 && gens[genLoop]-> mother(0)->pdgId() == 25){ // be sure that the photons comes from the higgs
      nGenPhoton++;
      for( unsigned int jetLoop =0 ; jetLoop < jetsDzPointers.size(); jetLoop++){
	GenPhotonInfo tmp_info;
	
	float dphi  = jetsDzPointers[jetLoop]->phi() -  gens[genLoop]->phi();
	float deta  = jetsDzPointers[jetLoop]->eta() -  gens[genLoop]->eta();
	float dr    =  std::sqrt(deta*deta + dphi*dphi);
	
	DeltaRmin = std::min (dr, DeltaRmin);
	minim[dr] = jetLoop; 
	
	// fill the info
	tmp_info.pt     = gens[genLoop]->pt ();
	tmp_info.eta    = gens[genLoop]->eta();
	tmp_info.phi    = gens[genLoop]->phi();	
	tmp_info.DRmin  = DeltaRmin;
	
	_isPhoton[jetLoop] = false;
	minim_info[jetLoop] = tmp_info;
      }
      unsigned int bestjetid = minim.find(DeltaRmin)->second;
      if(DeltaRmin < 0.3){
	//std::cout << " ---> realy found["<< bestjetid << "]"<<std::endl;
	photonJet_id[bestjetid] = minim_info[bestjetid];
	_isPhoton[bestjetid] = true;
      }
    }
    genPartTree->Fill();
  }
  //std::cout << "============================" << std::endl;
  
  // jets pt sorters 
  PtrVector<flashgg::Jet> SortedPtJets;
  for (unsigned int jdz = 0 ; jdz < jetsDzPointers.size() ; jdz++) {
    edm::Ptr<flashgg::Jet> tmp_jet= jetsDzPointers[jdz];
    if(photonJetVeto){
      if(!(photonJet_id.find(jdz) != photonJet_id.end())){
	SortedPtJets.push_back(tmp_jet);
      }
    }else{
      SortedPtJets.push_back(tmp_jet);
    }
  }
  
  //std::cout << "(njet-idphotn) = (" << jetsDzPointers.size() - SortedPtJets.size() 
  //  	    <<")---> Gen("<< nGenPhoton 
  //   	    <<std::endl;
  
  // +++ jets info  
  std::map<unsigned int, jetInfo> recojetmap;
  
  for (unsigned int jdz = 0 ; jdz < SortedPtJets.size() ; jdz++) {
    jInfo.id = jdz;
    
    //jInfo.photondRmin = 999.;
    //if( photonJet_id.find(jdz) != photonJet_id.end()){
    //  GenPhotonInfo tmp_info = photonJet_id.find(jdz)->second; // call find ones 
    //  std::cout << "----> matched photon jet["<< jdz <<"]"<< std::endl;
    //  jInfo.photondRmin  = tmp_info.DRmin;
    //  jInfo.GenPhotonPt  = tmp_info.pt   ;
    //  jInfo.GenPhotonEta = tmp_info.eta  ;
    //  jInfo.GenPhotonPhi = tmp_info.phi  ;
    //  jInfo.photonMatch  = 1;
    //}else{
    //  jInfo.photondRmin  = -999.;
    //  jInfo.GenPhotonPt  = -999.;
    //  jInfo.GenPhotonEta = -999.;
    //  jInfo.GenPhotonPhi = -999.;
    //  jInfo.photonMatch  =  0   ;
    //  jInfo.photondRmin  = -999.;
    //}
    
    jInfo.pt            = SortedPtJets[jdz]->pt();
    jInfo.rawPt         = SortedPtJets[jdz]->correctedJet("Uncorrected").pt() ;
    
    if(jetCollectionName.find("PPI")>1 && jetCollectionName.find("PPI")<jetCollectionName.size()){
      jInfo.bestPt      = SortedPtJets[jdz]->correctedJet("Uncorrected").pt() ;
    } else {
      jInfo.bestPt      = SortedPtJets[jdz]->pt() ;
    }
    
    if( SortedPtJets[jdz]->genJet()){
      jInfo.genJetMatch           = 1;
      jInfo.genJetPt              = SortedPtJets[jdz]->genJet()->pt();
      jInfo.genJetEta             = SortedPtJets[jdz]->genJet()->eta();
      jInfo.genJetEta             = SortedPtJets[jdz]->genJet()->eta();
    } else {
      jInfo.genJetPt              = -9999.;
      jInfo.genJetEta             = -9999.;
      jInfo.genJetMatch           = 0;
    }
    
    if( SortedPtJets[jdz]->genParton()){
      jInfo.genQuarkMatch           = 1;
      jInfo.genQuarkPt              = SortedPtJets[jdz]->genParton()->pt();
      jInfo.genQuarkEta             = SortedPtJets[jdz]->genParton()->eta();
      jInfo.genQuarkPdgId           = SortedPtJets[jdz]->genParton()->pdgId();
    } else {
      jInfo.genQuarkPt              = -9999.;
      jInfo.genQuarkEta             = -9999.;
      jInfo.genQuarkMatch           = 0;
      jInfo.genQuarkPdgId           = -9999;
    }
    //----------------------
    jInfo.energy           = SortedPtJets[jdz]->energy() ;
    jInfo.mass             = SortedPtJets[jdz]->mass() ;
    jInfo.eta              = SortedPtJets[jdz]->eta();
    jInfo.phi              = SortedPtJets[jdz]->phi();
    jInfo.area             = SortedPtJets[jdz]->jetArea();
    
    
    if(!(jetCollectionName.find("PPI")>1 && jetCollectionName.find("PPI")<jetCollectionName.size()) )
      {
	// use the di-photon vertex if the di-photon existe otherwise use the Vtx0
	
	if((diPhotonPointers.size() > 0 ) && 
	   ((jetCollectionName.find("Leg")>1 && jetCollectionName.find("Leg")<jetCollectionName.size())||(jetCollectionName.length()<3))){
	  
	  jInfo.PUJetID_betaStar   = SortedPtJets[jdz]->betaStar(diPhotonPointers[0]->getVertex());
	  jInfo.PUJetID_rms        = SortedPtJets[jdz]->RMS(diPhotonPointers[0]->getVertex());
	  jInfo.passesPUJetID      = SortedPtJets[jdz]->passesPuJetId(diPhotonPointers[0]->getVertex());
	  
	  jInfo.jet_W       = SortedPtJets[jdz]->pileupJetIdentifier(diPhotonPointers[0]->getVertex()).jetW();
	  jInfo.jet_dR2Mean = SortedPtJets[jdz]->pileupJetIdentifier(diPhotonPointers[0]->getVertex()).dR2Mean();
	  jInfo.jet_dRMean  = SortedPtJets[jdz]->pileupJetIdentifier(diPhotonPointers[0]->getVertex()).dRMean();
	  jInfo.jet_dZ      = SortedPtJets[jdz]->pileupJetIdentifier(diPhotonPointers[0]->getVertex()).dZ();
	  jInfo.jet_ptD     = SortedPtJets[jdz]->pileupJetIdentifier(diPhotonPointers[0]->getVertex()).ptD();
	  
	  
	} else {
	  
	  jInfo.PUJetID_betaStar   = SortedPtJets[jdz]->betaStar(vtxs[0]);
	  jInfo.PUJetID_rms        = SortedPtJets[jdz]->RMS(vtxs[0]);
	  jInfo.passesPUJetID      = SortedPtJets[jdz]->passesPuJetId(vtxs[0]);
	  
	  jInfo.jet_W       = SortedPtJets[jdz]->pileupJetIdentifier(vtxs[0]).jetW();
	  jInfo.jet_dR2Mean = SortedPtJets[jdz]->pileupJetIdentifier(vtxs[0]).dR2Mean();
	  jInfo.jet_dRMean  = SortedPtJets[jdz]->pileupJetIdentifier(vtxs[0]).dRMean();
	  jInfo.jet_dZ      = SortedPtJets[jdz]->pileupJetIdentifier(vtxs[0]).dZ();
	  jInfo.jet_ptD     = SortedPtJets[jdz]->pileupJetIdentifier(vtxs[0]).ptD();
	  
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
    jInfo.nPart     = SortedPtJets[jdz]->numberOfDaughters  ();
    jInfo.nCharged  = SortedPtJets[jdz]->chargedMultiplicity();
    jInfo.nNeutral  = SortedPtJets[jdz]->neutralMultiplicity();
    jInfo.chgEmFrac = SortedPtJets[jdz]->chargedEmEnergy()/SortedPtJets[jdz]->energy(); //
    jInfo.neuEmFrac = SortedPtJets[jdz]->neutralEmEnergy()/SortedPtJets[jdz]->energy(); //
    
    /*  this part sould be introduced in RecoJets tools
    // loop over consitutuants
    jInfo.S      = -1.; // entropy to zero 
    jInfo.Q      = -100.; // Jet charge
    //jInfo.Weight = -1.;
    
    float jetPt_tmp = SortedPtJets[jdz]->pt();
    float M_ab =0 , M_aa = 0, M_bb = 0;
    
    for (unsigned int i = 0 ; i < SortedPtJets[jdz]->getJetConstituentsQuick().size() ; i++){
      const reco::Candidate* icand = SortedPtJets[jdz]->getJetConstituentsQuick()[i];
      float candPt                 = icand->pt();
      float candCharge             = icand->charge();
      jInfo.S      += (candPt/jetPt_tmp) * TMath::Log(candPt/jetPt_tmp); 
      jInfo.Q      += candCharge * TMath::Log(candPt/jetPt_tmp); 
      //jInfo.Weight += candCharge * TMath::Log(candPt/jetPt_tmp); 
      
      M_ab +=  candPt * (SortedPtJets[jdz]->eta() - icand->eta()) * (SortedPtJets[jdz]->phi() - icand->phi());
      M_aa +=  candPt * (SortedPtJets[jdz]->eta() - icand->eta()) * (SortedPtJets[jdz]->eta() - icand->eta());
      M_bb +=  candPt * (SortedPtJets[jdz]->phi() - icand->phi()) * (SortedPtJets[jdz]->eta() - icand->phi());
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
  }

  for( unsigned int genLoop =0 ; genLoop < genJets.size(); genLoop++){

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

    if (genJets[genLoop]->pt() <20) { continue;}
    
    genJetInfo.pt     = genJets[genLoop]->pt() ;
    genJetInfo.eta    = genJets[genLoop]->eta();
    genJetInfo.phi    = genJets[genLoop]->phi();
    
    float deta;
    float dphi;
    float dr  ;

    for (unsigned int recoLoop=0; recoLoop <  SortedPtJets.size(); recoLoop++){


      if(SortedPtJets[recoLoop]->pt() < 5) continue;

      deta= SortedPtJets[recoLoop]->eta() - 	 genJets[genLoop]->eta();
      dphi= SortedPtJets[recoLoop]->phi() - 	 genJets[genLoop]->phi();
      dr = std::sqrt(deta*deta + dphi*dphi);

      if (dr < 0.4 ) {
	genJetInfo.dR      =  dr;
	genJetInfo.recoJetPt       = SortedPtJets[recoLoop]->pt() ;
	genJetInfo.recoJetRawPt    = SortedPtJets[recoLoop]->correctedJet("Uncorrected").pt()  ;

	// add the photon overlaping info 
	jetInfo tmpjetinfo = recojetmap[recoLoop];
	genJetInfo.photonMatch     = tmpjetinfo.photonMatch;
	genJetInfo.GenPhotonPt     = tmpjetinfo.GenPhotonPt;//recojetmap[recojetmap].GenPhotonPt  ;
	genJetInfo.photondRmin     = tmpjetinfo.photondRmin;//recojetmap[recojetmap].photondRmin  ;



	if(!(jetCollectionName.find("PPI")>1 && jetCollectionName.find("PPI")<jetCollectionName.size())){
	  genJetInfo.recoJetBestPt   =  SortedPtJets[recoLoop]->correctedJet("Uncorrected").pt() ;
	  if( (diPhotonPointers.size() > 0 ) && 
	      ((jetCollectionName.find("Leg")>1 && jetCollectionName.find("Leg")<jetCollectionName.size())||(jetCollectionName.length()   <3 )) ) { // for PF
	    
	    genJetInfo.PUJetID_betaStar        = SortedPtJets[recoLoop]->betaStar(diPhotonPointers[0]->getVertex());
	    genJetInfo.PUJetID_rms             = SortedPtJets[recoLoop]->RMS(diPhotonPointers[0]->getVertex());
	    genJetInfo.passesPUJetID           = SortedPtJets[recoLoop]->passesPuJetId(diPhotonPointers[0]->getVertex());
	  } else {
	    genJetInfo.PUJetID_betaStar        = SortedPtJets[recoLoop]->betaStar(vtxs[0]);
	    genJetInfo.PUJetID_rms             = SortedPtJets[recoLoop]->RMS(vtxs[0]);
	    genJetInfo.passesPUJetID           = SortedPtJets[recoLoop]->passesPuJetId(vtxs[0]);
	    
	  }
	} else {
	  genJetInfo.recoJetBestPt   = SortedPtJets[recoLoop]->pt()  ;
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
  
  //jetTree->Branch("photonMatch"    ,&jInfo.photonMatch  ,"photonMatch/I" );
  //jetTree->Branch("photondRmin"    ,&jInfo.photondRmin  ,"photondRmin/F" );
  //
  //jetTree->Branch("GenPhotonPt"    ,&jInfo.GenPhotonPt   ,"GenPhotonPt/F" );
  //jetTree->Branch("GenPhotonEta"   ,&jInfo.GenPhotonEta  ,"GenPhotonEta/F" );
  //jetTree->Branch("GenPhotonPhi"   ,&jInfo.GenPhotonPhi  ,"GenPhotonPhi/F" );
  
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
