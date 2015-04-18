// -----------------------
// By Y.Haddad & L.Corpe  12/2014
//
// Jet validation analyzer: tree maker for the jet studies in flashgg
// 
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
//#include "DataFormats/Common/interface/PtrVector.h"

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"

#include "flashgg/MicroAOD/interface/VertexSelectorBase.h"
#include "flashgg/DataFormats/interface/Photon.h"
#include "flashgg/DataFormats/interface/DiPhotonCandidate.h"

#include "flashgg/MicroAOD/interface/PhotonIdUtils.h"

#include "flashgg/DataFormats/interface/VertexCandidateMap.h"
#include "flashgg/DataFormats/interface/Jet.h"

#include "DataFormats/Math/interface/deltaR.h"


#include "TTree.h"

// **********************************************************************

struct eventInfo {

    float genVertexZ;
    float zerothVertexZ;
    float diphotonVertexZ;
    int legacyEqZeroth;
    int nDiphotons;

    unsigned int nJet;
    unsigned int nPV;
    unsigned int nSV;

    float higgsPt;

    void init()
    {
        genVertexZ      = -999.;
        zerothVertexZ   = -999.;
        diphotonVertexZ = -999.;
        higgsPt         = -999.;
    }
};

// per-vertex tree
struct GenPartInfo {
    float pt;
    float eta;
    float phi;
    int   pdgid;
    int   status;

    void init()
    {
        pt  = -999;
        eta = -999;
    }
};

// per-genJet tree
struct GenJetInfo {
    float pt;
    float eta;
    float phi;
    float recoJetPt    ; 
    float recoJetRawPt ;
    float recoJetBestPt;
    int   recoJetMatch ;
    float recoJetEta   ;
    float dRmin        ;
    float dR           ;
    int   legacyEqZeroth ;
    int   nDiphotons     ;
    float PUJetID_betaStar;
    float PUJetID_rms;
    int   passesPUJetID;
  
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
    float jet_betaClassic;
    float jet_betaStarClassic;
  
    float PUJetID_betaStar;
    float PUJetID_beta;
    float PUJetID_rms;
  
    float mybetaStar;
    float mybeta;
  
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
    float genJetPhi;
    float genJetdRmin;
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

struct GenPhotonInfo {
    float pt;
    float phi;
    float eta;
    float DRmin;
    void init()
    {
        pt  = -999;
        eta = -999;
    }

};

// **********************************************************************

using namespace std;
using namespace edm;
using namespace flashgg;

// **********************************************************************

class JetValidationTreeMaker : public edm::EDAnalyzer
{
public:
    explicit JetValidationTreeMaker( const edm::ParameterSet & );
    ~JetValidationTreeMaker();

    static void fillDescriptions( edm::ConfigurationDescriptions &descriptions );


private:

    edm::Service<TFileService> fs_;

    virtual void beginJob() override;
    virtual void analyze( const edm::Event &, const edm::EventSetup & ) override;
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
    oEDGetTokenT< VertexCandidateMap > vertexCandidateMapToken_;
    
    TTree     *eventTree;
    TTree     *jetTree;
    TTree     *genPartTree;
    TTree     *genJetTree;

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

JetValidationTreeMaker::JetValidationTreeMaker( const edm::ParameterSet &iConfig ):
    genPartToken_( consumes<View<reco::GenParticle> >( iConfig.getUntrackedParameter<InputTag> ( "GenParticleTag", InputTag( "prunedGenParticles" ) ) ) ),
    genJetToken_( consumes<View<reco::GenJet> >( iConfig.getUntrackedParameter<InputTag> ( "GenJetTag", InputTag( "slimmedGenJets" ) ) ) ),
    jetDzToken_( consumes<View<flashgg::Jet> >( iConfig.getParameter<InputTag>( "JetTagDz" ) ) ),
    diPhotonToken_( consumes<View<flashgg::DiPhotonCandidate> >( iConfig.getUntrackedParameter<InputTag> ( "DiPhotonTag", InputTag( "flashggDiPhotons" ) ) ) ),
    vertexToken_( consumes<View<reco::Vertex> >( iConfig.getUntrackedParameter<InputTag> ( "VertexTag", InputTag( "offlineSlimmedPrimaryVertices" ) ) ) ),
    usePUJetID( iConfig.getUntrackedParameter<bool>( "UsePUJetID", false ) ),
    photonJetVeto (iConfig.getUntrackedParameter<bool>("PhotonJetVeto",true))
{
    event_number = 0;
    jetCollectionName = iConfig.getParameter<string>( "StringTag" );
}

JetValidationTreeMaker::~JetValidationTreeMaker()
{
    event_number = 0;
}

void
JetValidationTreeMaker::analyze( const edm::Event &iEvent, const edm::EventSetup &iSetup ){
    Handle<View<reco::Vertex> > primaryVertices;
    iEvent.getByToken( vertexToken_, primaryVertices );
    //  const PtrVector<reco::Vertex>& vtxs = primaryVertices->ptrVector();

    Handle<View<flashgg::DiPhotonCandidate> > diPhotons;
    iEvent.getByToken( diPhotonToken_, diPhotons );
    //  const PtrVector<flashgg::DiPhotonCandidate>& diPhotonPointers = diPhotons->ptrVector();

    Handle<View<reco::GenParticle> > genParticles;
    iEvent.getByToken( genPartToken_, genParticles );
    //  const PtrVector<reco::GenParticle>& gens = genParticles->ptrVector();

    Handle<View<reco::GenJet> > genJet;
    iEvent.getByToken( genJetToken_, genJet );
    //  const PtrVector<reco::GenJet>& genJets = genJet->ptrVector();

    Handle<View<flashgg::Jet> > jetsDz;
    iEvent.getByToken( jetDzToken_, jetsDz );
    //  const PtrVector<flashgg::Jet>& jetsDzPointers = jetsDz->ptrVector();

    int legacyEqZeroth = 0;
    int nDiphotons = 0;

    //std::cout <<" DEBUG 1"<<std::endl;
    nDiphotons = diPhotons->size();
    if( diPhotons->size() == 0 ) {
        legacyEqZeroth = 1; //if there is no diphoton, we use 0th vertex anyway.
    } else {
        if( fabs( diPhotons->ptrAt( 0 )->vtx()->z() - primaryVertices->ptrAt( 0 )->z() ) < 0.01 ) {
            legacyEqZeroth = 1;
        }
    }

    eInfo.nDiphotons = nDiphotons;
    eInfo.legacyEqZeroth = legacyEqZeroth;

    initEventStructure();

    eInfo.nJet = jetsDz->size();
    eInfo.nPV  = primaryVertices->size();
    eInfo.nSV  = 0;

    // ++  finding the photon-jet overlaping
    
    std::vector<edm::Ptr<reco::GenParticle> > genPhoton;
    std::vector<edm::Ptr<reco::GenParticle> > genParton;
    
    for( unsigned int genLoop = 0 ; genLoop < genParticles->size(); genLoop++ ) {
        genInfo.pt     = genParticles->ptrAt( genLoop )->pt() ;
        genInfo.eta    = genParticles->ptrAt( genLoop )->eta();
        genInfo.phi    = genParticles->ptrAt( genLoop )->phi();
        genInfo.status = genParticles->ptrAt( genLoop )->status();
        genInfo.pdgid  = int( genParticles->ptrAt( genLoop )->pdgId() );
        if (gens[genLoop]->pdgId() == 22 && gens[genLoop]-> mother(0)->pdgId() == 25){ 
            genPhoton.push_back(gens[genLoop]);
        }
        
        // select the quark and gluon 
        if (std::abs(gens[genLoop]->pdgId()) == 21 || // gluons
            std::abs(gens[genLoop]->pdgId()) <= 5     // quarks
            ){
            if(gens[genLoop]->status()==3){ // another condition about the status 3
                genParton.push_back(gens[genLoop]);
                std::cout << " ---> the status 3 parton :: "<< gens[genLoop]->pdgId() << std::endl;
            }
        }
        // fill the tree
        genPartTree->Fill();
    }
    
    std::map<unsigned int, GenPhotonInfo> photonJet_id;
    std::map<unsigned int, bool>             _isPhoton;
    
    for( unsigned int jetLoop =0 ; jetLoop < jetsDzPointers.size(); jetLoop++){
        float minDr = 1000;
        std::map<float,unsigned int> minim;
        GenPhotonInfo tmp_info;
        
        for( unsigned int ig=0; ig < genPhoton.size(); ig++){
            float dphi  = deltaPhi(jetsDzPointers[jetLoop]->phi(),genPhoton[ig]->phi());
            float deta  = jetsDzPointers[jetLoop]->eta() -  genPhoton[ig]->eta();
            float dr    =  std::sqrt(deta*deta + dphi*dphi);
            minDr = std::min(dr, minDr);
            minim[dr] = ig; 
        }
        unsigned int close_gid = minim.find(minDr)->second;
        
        tmp_info.pt     = genPhoton[close_gid]->pt ();
        tmp_info.eta    = genPhoton[close_gid]->eta();
        tmp_info.phi    = genPhoton[close_gid]->phi();
        tmp_info.DRmin  = minDr;
        
        _isPhoton[jetLoop] = false;
        if(minDr < 0.3){
            _isPhoton[jetLoop] = true;
        }
        
        //std ::cout << "DEBUG:: tmp_info.pt == " << tmp_info.pt << std::endl;
        photonJet_id[jetLoop] =  tmp_info;
    }
    // Parton -> jet matcing
    std::map<unsigned int, GenJetInfo>     genJet_id;
    std::map<unsigned int, bool>          _isMatched;
    std::map<unsigned int, unsigned int>   pairs;
    for( unsigned int jetLoop =0; jetLoop < jetsDzPointers.size(); jetLoop++){
        float minDr = 1000;
        std::map<float,unsigned int> minim;
        GenJetInfo tmp_info;
        
        for( unsigned int ig=0; ig < genJets.size(); ig++){
            float dphi  = deltaPhi(jetsDzPointers[jetLoop]->phi(),genJets[ig]->phi());
            float deta  = jetsDzPointers[jetLoop]->eta() -  genJets[ig]->eta();
            float dr    =  std::sqrt(deta*deta + dphi*dphi);
            minDr = std::min(dr, minDr);
            minim[dr] = ig; 
        }
        
        unsigned int close_genjet_id = minim.find(minDr)->second;
        tmp_info.pt     = genJets[close_genjet_id]->pt ();
        tmp_info.eta    = genJets[close_genjet_id]->eta();
        tmp_info.phi    = genJets[close_genjet_id]->phi();
        tmp_info.dRmin  = minDr;
        
        _isMatched[jetLoop] = false;
        if(minDr < 0.4 && pairs.find(close_genjet_id)==pairs.end()){
            _isMatched[jetLoop] = true;
            pairs[close_genjet_id] = jetLoop;
            
            std ::cout << "DEBUG:: jet("<< jetLoop
                       <<") == genJet(" << close_genjet_id
                       << ") pt = "     << tmp_info.pt 
                       << "DEBUG::  Dr min     == " << minDr 
                       << std::endl;
            
        }
        
        genJet_id[jetLoop] =  tmp_info;
    }
    
    std::cout << " number of parton :: " << genParton.size() << std::endl;
    std::cout << " number of mathes :: " << _isMatched.size() << std::endl;
    std::cout << " number of genJet :: " << genJets.size() << std::endl;
    
    
    std::map<unsigned int, jetInfo> recojetmap;
    for( unsigned int jdz = 0 ; jdz < jetsDz->size() ; jdz++ ) {
        jInfo.id            = jdz;
        jInfo.photonMatch   = int(_isPhoton[jdz]); 
        
        GenPhotonInfo tmp_info = photonJet_id.find(jdz)->second; // call find ones
        
        jInfo.GenPhotonPt  = tmp_info.pt   ;
        jInfo.GenPhotonEta = tmp_info.eta  ;
        jInfo.GenPhotonPhi = tmp_info.phi  ;
        jInfo.photondRmin  = tmp_info.DRmin;
        
        
        
        jInfo.genJetMatch             = int(_isMatched[jdz]);
        
        GenJetInfo tmp_genjet_info    = genJet_id.find(jdz)->second;
        jInfo.genJetPt                = tmp_genjet_info.pt ;
        jInfo.genJetEta               = tmp_genjet_info.eta;
        jInfo.genJetPhi               = tmp_genjet_info.phi;
        jInfo.genJetdRmin             = tmp_genjet_info.dRmin;
        
        //jInfo.photondRmin = 999.;
        //if( photonJet_id.find( jdz ) != photonJet_id.end() ) {
        //    GenPhotonInfo tmp_info = photonJet_id.find( jdz )->second; // call find ones
        //    jInfo.photondRmin  = tmp_info.DRmin;
        //    jInfo.GenPhotonPt  = tmp_info.pt   ;
        //    jInfo.GenPhotonEta = tmp_info.eta  ;
        //    jInfo.GenPhotonPhi = tmp_info.phi  ;
        //    jInfo.photonMatch  = 1;
        //} else {
        //    jInfo.photondRmin  = -999.;
        //    jInfo.GenPhotonPt  = -999.;
        //    jInfo.GenPhotonEta = -999.;
        //    jInfo.GenPhotonPhi = -999.;
        //    jInfo.photonMatch  =  0   ;
        //    jInfo.photondRmin  = -999.;
        //}

        jInfo.pt            = jetsDz->ptrAt( jdz )->pt();
        jInfo.rawPt         = jetsDz->ptrAt( jdz )->correctedJet( "Uncorrected" ).pt() ;

        if( jetCollectionName.find( "PPI" ) > 1 && jetCollectionName.find( "PPI" ) < jetCollectionName.size() ) {
            jInfo.bestPt      = jetsDz->ptrAt( jdz )->correctedJet( "Uncorrected" ).pt() ;
        } else {
            jInfo.bestPt      = jetsDz->ptrAt( jdz )->pt() ;
        }

        
        //if( jetsDz->ptrAt( jdz )->genJet() ) {
        //    jInfo.genJetMatch           = 1;
        //    jInfo.genJetPt              = jetsDz->ptrAt( jdz )->genJet()->pt();
        //    jInfo.genJetEta             = jetsDz->ptrAt( jdz )->genJet()->eta();
        //
        //} else {
        //    jInfo.genJetPt              = -9999.;
        //    jInfo.genJetEta             = -9999.;
        //    jInfo.genJetMatch           = 0;
        //}

        if( jetsDz->ptrAt( jdz )->genParton() ) {
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
        
        if( !( jetCollectionName.find( "PPI" ) > 1 && jetCollectionName.find( "PPI" ) < jetCollectionName.size() ) ) {
            // use the di-photon vertex if the di-photon existe otherwise use the Vtx0
            
            if( ( diPhotons->size() > 0 ) &&
                ( ( jetCollectionName.find( "Leg" ) > 1 && jetCollectionName.find( "Leg" ) < jetCollectionName.size() ) || ( jetCollectionName.length()   < 3 ) ) ) { // for PF

                jInfo.PUJetID_betaStar        = jetsDz->ptrAt( jdz )->betaStar( diPhotons->ptrAt( 0 )->vtx() );
                jInfo.PUJetID_rms             = jetsDz->ptrAt( jdz )->rms( diPhotons->ptrAt( 0 )->vtx() );
                jInfo.passesPUJetID           = jetsDz->ptrAt( jdz )->passesPuJetId( diPhotons->ptrAt( 0 )->vtx() );
                

                // chngs from 72X
                jInfo.jet_W       = SortedPtJets[jdz]->pileupJetIdentifier(diPhotonPointers[0]->getVertex()).jetW();
                jInfo.jet_dR2Mean = SortedPtJets[jdz]->pileupJetIdentifier(diPhotonPointers[0]->getVertex()).dR2Mean();
                jInfo.jet_dRMean  = SortedPtJets[jdz]->pileupJetIdentifier(diPhotonPointers[0]->getVertex()).dRMean();
                jInfo.jet_dZ      = SortedPtJets[jdz]->pileupJetIdentifier(diPhotonPointers[0]->getVertex()).dZ();
                jInfo.jet_ptD     = SortedPtJets[jdz]->pileupJetIdentifier(diPhotonPointers[0]->getVertex()).ptD();
                
                jInfo.jet_betaClassic    = SortedPtJets[jdz]->pileupJetIdentifier(diPhotonPointers[0]->getVertex()).betaClassic();
                jInfo.jet_betaStarClassic= SortedPtJets[jdz]->pileupJetIdentifier(diPhotonPointers[0]->getVertex()).betaStarClassic();

            } else {

                jInfo.PUJetID_betaStar        = jetsDz->ptrAt( jdz )->betaStar( primaryVertices->ptrAt( 0 ) );
                jInfo.PUJetID_rms             = jetsDz->ptrAt( jdz )->rms( primaryVertices->ptrAt( 0 ) );
                jInfo.passesPUJetID           = jetsDz->ptrAt( jdz )->passesPuJetId( primaryVertices->ptrAt( 0 ) );
                

                jInfo.jet_W       = SortedPtJets[jdz]->pileupJetIdentifier(vtxs[0]).jetW();
                jInfo.jet_dR2Mean = SortedPtJets[jdz]->pileupJetIdentifier(vtxs[0]).dR2Mean();
                jInfo.jet_dRMean  = SortedPtJets[jdz]->pileupJetIdentifier(vtxs[0]).dRMean();
                jInfo.jet_dZ      = SortedPtJets[jdz]->pileupJetIdentifier(vtxs[0]).dZ();
                jInfo.jet_ptD     = SortedPtJets[jdz]->pileupJetIdentifier(vtxs[0]).ptD();
                
                jInfo.jet_betaClassic    = SortedPtJets[jdz]->pileupJetIdentifier(vtxs[0]).betaClassic();
                jInfo.jet_betaStarClassic= SortedPtJets[jdz]->pileupJetIdentifier(vtxs[0]).betaStarClassic();
            }
        } else {
            
            jInfo.PUJetID_betaStar        = -999.;
            jInfo.PUJetID_rms             = -999.;
            jInfo.passesPUJetID           = -999;
        }
        
        jInfo.nDiphotons                = nDiphotons;
        jInfo.legacyEqZeroth            = legacyEqZeroth;

        // Get constituants information
        jInfo.nPart     = SortedPtJets[jdz]->numberOfDaughters  ();
        jInfo.nCharged  = SortedPtJets[jdz]->chargedMultiplicity();
        jInfo.nNeutral  = SortedPtJets[jdz]->neutralMultiplicity();
        jInfo.chgEmFrac = SortedPtJets[jdz]->chargedEmEnergy()/SortedPtJets[jdz]->energy(); //
        jInfo.neuEmFrac = SortedPtJets[jdz]->neutralEmEnergy()/SortedPtJets[jdz]->energy(); //
        
        double sumTkPt = 0;
        
        double beta     = 0;
        double betaStar = 0;
        
        for (unsigned int i = 0 ; i < SortedPtJets[jdz]->numberOfDaughters()  ; i++){
            edm::Ptr<pat::PackedCandidate> icand = edm::Ptr<pat::PackedCandidate> ( SortedPtJets[jdz]->daughterPtr(i) );
            if ( icand->charge() == 0 ) continue ;
            
            float tkpt = icand->pt();
            sumTkPt += tkpt;
            // 'classic' beta definition based on track-vertex association
            //bool inVtx0 = std::abs(icand->dz(vtxs[0]->position())) < 0.02;
            
            bool inAnyOther = false;
            // alternative beta definition based on track-vertex distance of closest approach
            double dZ0 = std::abs(icand->dz(vtxs[0]->position()));
            double dZ  = dZ0;
            //for(reco::VertexCollection::const_iterator  vi=vtxs.begin(); vi!=vtxs.end(); ++vi ) {
            //for(unsigned int iv=0; iv < vtxs.size(); ++iv) {
            for (std::map<edm::Ptr<reco::Vertex>,edm::PtrVector<pat::PackedCandidate> >::const_iterator vi=vtxmap.begin();vi!=vtxmap.end();vi++){
                const reco::Vertex & iv = *(vi->first);
                if( iv.isFake() || iv.ndof() < 4 ) { continue; }
                // the primary vertex may have been copied by the user: check identity by position  
                bool isVtx0  = (iv.position() - vtxs[0]->position()).r() < 0.02;
                if( !isVtx0 && ! inAnyOther ) {
                    inAnyOther = std::count(vi->second.begin(),vi->second.end(),icand);
                }
                dZ = std::min<double>(dZ,std::abs(icand->dz(iv.position())));
            }
            
            bool isdroped  = false;
            bool isnothing = false;
            
            if( dZ0 < 0.2 ) {
                isdroped = false;
                beta += tkpt;
            } else if( dZ < 0.2 ) {
                isdroped=true;
                betaStar += tkpt;
            } else {
                isnothing = true;
            }
            
            float candPt                 = icand->pt();
            if(!(jInfo.photonMatch) && SortedPtJets[jdz]->pt() > 20 ){
                std::cout <<"\t ["<< i << "] pdg(" << icand->pdgId() 
                          << ") pt("               << candPt 
                          << ") dz0 to PV0("       << dZ0
                          << ") from other PV ("   << isdroped
                          << ") no belong (" << isnothing
                          <<")"<< std::endl;
            }
            
        }
        
        if( sumTkPt != 0. ) {
            beta     = beta    /sumTkPt;
            betaStar = betaStar/sumTkPt;
        }else{
            beta     = -1;
            betaStar = -1;
        }
        
        
        jInfo.mybetaStar = betaStar;
        jInfo.mybeta     = beta;
        
        if(!(jInfo.photonMatch) && SortedPtJets[jdz]->pt() > 20 ){
            std::cout << " JetId ["        << jdz
                      <<"]  genJet ("      << jInfo.genJetMatch
                      <<")  DR min ("      << jInfo.genJetdRmin
                      <<")  betaStar ("    << jInfo.PUJetID_betaStar
                      <<")  betaStarNew (" << jInfo.mybetaStar
                      <<")  beta ("        << jInfo.PUJetID_beta
                      <<")  betaNew ("     << jInfo.mybeta
                      << ") pt("           << SortedPtJets[jdz]->pt() 
                      << ") eta("          << SortedPtJets[jdz]->eta()
                      << ") drphoton("     << jInfo.photondRmin
                      << ")"<< std::endl;
        }
        
        
        recojetmap[jdz] = jInfo;
        jetTree->Fill();
    }
    
   
    
    //
    //for( unsigned int genLoop = 0 ; genLoop < genJet->size(); genLoop++ ) {
    //
    //    genJetInfo.recoJetPt       = -999.;
    //    genJetInfo.recoJetRawPt    = -999.;
    //    genJetInfo.recoJetBestPt   = -999.;
    //    genJetInfo.recoJetMatch    =  0   ;
    //    genJetInfo.recoJetEta      = -999.;
    //    genJetInfo.dR              = -999.;
    //    genJetInfo.pt              = -999.;
    //    genJetInfo.eta             = -999.;
    //    genJetInfo.phi             = -999.;
    //    genJetInfo.PUJetID_betaStar = -999.;
    //    genJetInfo.PUJetID_rms     = -999.;
    //    genJetInfo.passesPUJetID   = -999;
    //    genJetInfo.nDiphotons      = nDiphotons;
    //
    //    if( genJet->ptrAt( genLoop )->pt() < 20 ) { continue;}
    //
    //    genJetInfo.pt     = genJet->ptrAt( genLoop )->pt() ;
    //    genJetInfo.eta    = genJet->ptrAt( genLoop )->eta();
    //    genJetInfo.phi    = genJet->ptrAt( genLoop )->phi();
    //
    //    float deta;
    //    float dphi;
    //    float dr  ;
    //
    //    for( unsigned int recoLoop = 0; recoLoop <  jetsDz->size(); recoLoop++ ) {
    //
    //
    //        if( jetsDz->ptrAt( recoLoop )->pt() < 5 ) { continue; }
    //
    //        deta = jetsDz->ptrAt( recoLoop )->eta() - 	 genJet->ptrAt( genLoop )->eta();
    //        dphi = deltaPhi( jetsDz->ptrAt( recoLoop )->phi(), genJet->ptrAt( genLoop )->phi() );
    //        dr = std::sqrt( deta * deta + dphi * dphi );
    //
    //        if( dr < 0.4 ) {
    //            genJetInfo.dR      =  dr;
    //            genJetInfo.recoJetPt       = jetsDz->ptrAt( recoLoop )->pt() ;
    //            genJetInfo.recoJetRawPt    = jetsDz->ptrAt( recoLoop )->correctedJet( "Uncorrected" ).pt()  ;
    //
    //            // add the photon overlaping info
    //            jetInfo tmpjetinfo = recojetmap[recoLoop];
    //            genJetInfo.photonMatch     = tmpjetinfo.photonMatch;
    //            genJetInfo.GenPhotonPt     = tmpjetinfo.GenPhotonPt;//recojetmap[recojetmap].GenPhotonPt  ;
    //            genJetInfo.photondRmin     = tmpjetinfo.photondRmin;//recojetmap[recojetmap].photondRmin  ;
    //
    //
    //
    //            if( !( jetCollectionName.find( "PPI" ) > 1 && jetCollectionName.find( "PPI" ) < jetCollectionName.size() ) ) {
    //                genJetInfo.recoJetBestPt   =  jetsDz->ptrAt( recoLoop )->correctedJet( "Uncorrected" ).pt() ;
    //                if( ( diPhotons->size() > 0 ) &&
    //                        ( ( jetCollectionName.find( "Leg" ) > 1 && jetCollectionName.find( "Leg" ) < jetCollectionName.size() ) || ( jetCollectionName.length()   < 3 ) ) ) { // for PF
    //
    //                    genJetInfo.PUJetID_betaStar        = jetsDz->ptrAt( recoLoop )->betaStar( diPhotons->ptrAt( 0 )->vtx() );
    //                    genJetInfo.PUJetID_rms             = jetsDz->ptrAt( recoLoop )->rms( diPhotons->ptrAt( 0 )->vtx() );
    //                    genJetInfo.passesPUJetID           = jetsDz->ptrAt( recoLoop )->passesPuJetId( diPhotons->ptrAt( 0 )->vtx() );
    //
    //                } else {
    //
    //                    genJetInfo.PUJetID_betaStar        = jetsDz->ptrAt( recoLoop )->betaStar( primaryVertices->ptrAt( 0 ) );
    //                    genJetInfo.PUJetID_rms             = jetsDz->ptrAt( recoLoop )->rms( primaryVertices->ptrAt( 0 ) );
    //                    genJetInfo.passesPUJetID           = jetsDz->ptrAt( recoLoop )->passesPuJetId( primaryVertices->ptrAt( 0 ) );
    //
    //                }
    //            } else {
    //
    //                genJetInfo.recoJetBestPt   = jetsDz->ptrAt( recoLoop )->pt()  ;
    //                genJetInfo.PUJetID_betaStar  = -999.;
    //                genJetInfo.PUJetID_rms       = -999.;
    //                genJetInfo.passesPUJetID     = -999;
    //
    //            }
    //
    //            genJetInfo.recoJetMatch    = 1 ;
    //            break;
    //        }
    //    }
    //
    //    genJetTree->Fill();
    //}
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
        




        std::map<float,unsigned int> minim;
        for (unsigned int recoLoop=0; recoLoop <  SortedPtJets.size(); recoLoop++){
            if(SortedPtJets[recoLoop]->pt() < 5) continue;
            
            double deta= SortedPtJets[recoLoop]->eta() - 	 genJets[genLoop]->eta();
            double dphi= SortedPtJets[recoLoop]->phi() - 	 genJets[genLoop]->phi();
            double dr = std::sqrt(deta*deta + dphi*dphi);
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
    jetTree->Branch("betaStar"        ,&jInfo.PUJetID_betaStar    ,"betaStar/F");
    jetTree->Branch("betaClassic"     ,&jInfo.jet_betaClassic     ,"betaClassic/F");
    jetTree->Branch("betaStarClassic" ,&jInfo.jet_betaStarClassic ,"betaStarClassic/F");
  
    jetTree->Branch("mybetaStar"      ,&jInfo.mybetaStar    ,"mybetaStar/F");
    jetTree->Branch("mybeta"          ,&jInfo.mybeta        ,"mybetaS/F");
  
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


void JetValidationTreeMaker::fillDescriptions( edm::ConfigurationDescriptions &descriptions )
{
    // The following says we do not know what parameters are allowed so do no validation
    // Please change this to state exactly what you do use, even if it is no parameters
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault( desc );
}

typedef JetValidationTreeMaker FlashggJetValidationTreeMaker;
DEFINE_FWK_MODULE( FlashggJetValidationTreeMaker );
// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

