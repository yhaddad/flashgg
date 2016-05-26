// -----------------------
// By Y.Haddad & L.Corpe  12/2014
// Modified by E.Scott    04/2016
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

#include "flashgg/DataFormats/interface/DiPhotonMVAResult.h" // Ed Ed
#include "flashgg/DataFormats/interface/VBFMVAResult.h" // Ed Ed

#include "TTree.h"
#include "TH1.h"
#include "TH2.h"
#include "TMatrix.h"
#include "TVector.h"
#include "TLorentzVector.h"
#include "TRandom3.h"

// **********************************************************************
#ifndef FLASHgg_VertexCandidateMap_h
#define FLASHgg_VertexCandidateMap_h
namespace flashgg {
    // typedef std::map<edm::Ptr<reco::Vertex>,edm::PtrVector<pat::PackedCandidate> > VertexCandidateMap;
    typedef std::pair<edm::Ptr<reco::Vertex>, edm::Ptr<pat::PackedCandidate> > VertexCandidatePair;
    typedef std::vector<VertexCandidatePair> VertexCandidateMap;

    struct compare_by_vtx {
        bool operator()( const VertexCandidatePair &left, const VertexCandidatePair &right )
        {
            return ( left.first < right.first );
        }
    };

    struct compare_with_vtx {
        bool operator()( const VertexCandidatePair &left, const edm::Ptr<reco::Vertex> &right )
        {
            return ( left.first < right );
        }
        bool operator()( const edm::Ptr<reco::Vertex> &left, const VertexCandidatePair &right )
        {
            return( left < right.first );
        }
    };

    struct compare_by_cand {
        bool operator()( const VertexCandidatePair &left, const VertexCandidatePair &right )
        {
            return ( left.second < right.second );
        }
    };

    struct compare_with_cand {
        bool operator()( const VertexCandidatePair &left, const edm::Ptr<pat::PackedCandidate> &right )
        {
            return ( left.second < right );
        }
        bool operator()( const edm::Ptr<pat::PackedCandidate> &left, const VertexCandidatePair &right )
        {
            return( left < right.second );
        }
    };
}
#endif


double delta_R( const reco::GenJet *genJet, edm::Ptr<flashgg::Jet> jet )
{
    float dphi  = deltaPhi( genJet->phi(), jet->phi() );
    float deta  = genJet->eta() -  jet->eta();
    return std::sqrt( deta * deta + dphi * dphi );
}

struct eventInfo {
    int   eventID;

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
    int   eventID;
    float pt;
    float eta;
    float y;
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
    int   eventID;
    float pt;
    float eta;
    float phi;
    float recoJetPt   ;
    float recoJetRawPt ;
    float recoJetBestPt;
    int   recoJetMatch ;
    float recoJetEta   ;
    float dRmin        ;
    float dR   ;
    int   legacyEqZeroth;
    int   nDiphotons;
    float PUJetID_betaStar;
    float PUJetID_rms;
    int   passesPUJetID;

    int   diphotonIndex;
    int   smartIndex;
    int   jetIndex;

    int   LegIsPV0;

    int   nPV;
    int   nJets;

    int   photonMatch;
    float photondRmin;
    float GenPhotonPt;


    void init()
    {
        pt  = -999;
        eta = -999;
    }
};
// per recoJet tree
struct jetInfo {
    int   eventID;
    float pt;
    float rawPt;
    float bestPt;
    float energy;
    float mass;
    float area;
    float eta;
    float phi;

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
    float jet_qgLikelihood;

    float PUJetID_betaStar;
    float PUJetID_beta;
    float PUJetID_rms;

    float mybetaStar;
    float mybeta;

    int   passesPUJetID;
    int   LegIsPV0;
    int   nDiphotons;
    int   diphotonIndex;
    int   smartIndex;
    int   jetIndex; // now modified to refer only to real jets (not photons) 
    int   passesRMSIndex; // to aid comparison with VBFTag


    int   nPV;
    int   nJets;

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
    void init()
    {
        pt  = -999;
        eta = -999;
    }
    // jets Id
    int id;
    // photon matching part
    int   photonMatch;
    float photondRmin;
    float GenPhotonEta;
    float GenPhotonPhi;
    float GenPhotonPt;

    // Added to help with plotting in Heppi
    // Set to 1 by default
    float weight; 

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

// info re PromptFake events
struct PromptFakeInfo {
    int eventID;
    //float weight; 
    float fakeWeight; 
    //
    float diphoMass;
    float diphoPt;
    float diphoLeadingPt;
    float diphoSubleadingPt;
    
    float promptFakeDeltaR;

    float promptPt;
    float promptEnergy;
    float promptEta;
    float promptPhi;
    int   promptPdgId;
    float promptIDMVA;
    float fakePt;
    float fakeEnergy;
    float fakeEta;
    float fakePhi;
    int   fakePdgId;
    float fakeIDMVA;

    float promptGenPhotonPt;
    float promptGenPhotonEnergy;
    float promptTotalGenPhoEnergy;
    float promptGenPhotonEta;
    float promptGenPhotonPhi;
    float promptGenPhotonDr;
    int   promptNumGenPhotons;
    float fakeGenPhotonPt;
    float fakeGenPhotonEnergy;
    float fakeTotalGenPhoEnergy;
    float fakeGenPhotonEta;
    float fakeGenPhotonPhi;
    float fakeGenPhotonDr;
    int   fakeNumGenPhotons;

    float promptGenJetPt;
    float promptGenJetEnergy;
    float promptGenJetEta;
    float promptGenJetPhi;
    float promptGenJetDr;
    int   promptNumGenJets;
    float fakeGenJetPt;
    float fakeGenJetEnergy;
    float fakeGenJetEta;
    float fakeGenJetPhi;
    float fakeGenJetDr;
    int   fakeNumGenJets;

    float promptRecoJetPt;
    float promptRecoJetEnergy;
    float promptRecoJetEta;
    float promptRecoJetPhi;
    float promptRecoJetDr;
    int   promptNumRecoJets;
    float fakeRecoJetPt;
    float fakeRecoJetEnergy;
    float fakeRecoJetEta;
    float fakeRecoJetPhi;
    float fakeRecoJetDr;
    int   fakeNumRecoJets;

    float promptPartonPt;
    float promptPartonEnergy;
    float promptPartonEta;
    float promptPartonPhi;
    float promptPartonDr;
    int   promptPartonMatchType;
    float fakePartonPt;
    float fakePartonEnergy;
    float fakePartonEta;
    float fakePartonPhi;
    float fakePartonDr;
    int   fakePartonMatchType;

    /*float sigmarv;
    float sigmawv;
    float CosPhi;
    float vtxprob;*/

    float dijet_leadEta;
    float dijet_subleadEta;
    float dijet_abs_dEta;
    float dijet_LeadJPt;
    float dijet_SubJPt;
    float dijet_Zep;
    float dijet_dphi_trunc;
    float dijet_dipho_dphi;
    float dijet_Mjj;
    float dijet_dy;
    float dijet_leady;
    float dijet_subleady;
    float dijet_dipho_pt;
    float dijet_minDRJetPho;

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


    //bool GenRecoMatching(reco::GenJet genjet, const PtrVector<flashgg::Jet>& RecoJets){}
    //EDGetTokenT< VertexCandidateMap > vertexCandidateMapTokenDz_;
    //EDGetTokenT< VertexCandidateMap > vertexCandidateMapTokenAOD_;

    EDGetTokenT< edm::View<reco::GenParticle> >          genPartToken_;
    EDGetTokenT< edm::View<pat::PackedGenParticle> >     genPhoToken_; // Ed
    EDGetTokenT< edm::View<reco::GenJet> >               genJetToken_;
    //EDGetTokenT< edm::View<flashgg::Jet> >               jetDzToken_;
    std::vector<edm::EDGetTokenT<View<flashgg::Jet> > >  tokenJets_;
    std::vector<edm::InputTag>                           inputTagJets_;
    EDGetTokenT< edm::View<flashgg::DiPhotonCandidate> > diPhotonToken_;
    EDGetTokenT< View<reco::Vertex> >                    vertexToken_;
    //EDGetTokenT< VertexCandidateMap > vertexCandidateMapToken_;
    
    EDGetTokenT<View<VBFMVAResult> > vbfMvaResultToken_; // Ed Ed
    //EDGetTokenT<View<DiPhotonMVAResult> > mvaResultToken_; // Ed Ed

    edm::InputTag 					qgVariablesInputTag;
    //edm::EDGetTokenT<edm::ValueMap<float>> 		qgToken;

    typedef std::vector<edm::Handle<edm::View<flashgg::Jet> > > JetCollectionVector;

    TTree     *eventTree;
    TTree     *jetTree;
    //TTree     *genPartTree; // Ed
    TTree     *genJetTree;
    TTree     *promptFakeTree;

    eventInfo   eInfo;
    jetInfo     jInfo;
    //GenPartInfo genInfo; // Ed
    GenJetInfo  genJetInfo;
    PromptFakeInfo pfInfo;
    Int_t       event_number;
    std::string jetCollectionName;

    GenPartInfo jGenPhotonInfo;

    bool        usePUJetID;
    bool        photonJetVeto;
    bool        homeGenJetMatching_;
    bool        ZeroVertexOnly_;
    bool        debug_;
    bool        useVBFTagPhotonMatching_;

    TRandom3 *randomDiphoIndex;   
};

JetValidationTreeMaker::JetValidationTreeMaker( const edm::ParameterSet &iConfig ):
    genPartToken_( consumes<View<reco::GenParticle> >( iConfig.getUntrackedParameter<InputTag> ( "GenParticleTag", InputTag( "prunedGenParticles" ) ) ) ),
    genPhoToken_( consumes<View<pat::PackedGenParticle> >( iConfig.getUntrackedParameter<InputTag> ( "GenPhotonTag", InputTag( "packedGenParticles" ) ) ) ),
    genJetToken_( consumes<View<reco::GenJet> >( iConfig.getUntrackedParameter<InputTag> ( "GenJetTag", InputTag( "slimmedGenJets" ) ) ) ),
    //jetDzToken_   ( consumes<View<flashgg::Jet> >( iConfig.getParameter<InputTag>( "JetTagDz" ) ) ),
    inputTagJets_( iConfig.getParameter<std::vector<edm::InputTag> >( "inputTagJets" ) ),
    diPhotonToken_( consumes<View<flashgg::DiPhotonCandidate> >( iConfig.getParameter<InputTag> ( "DiPhotonTag" ) ) ),
    vertexToken_( consumes<View<reco::Vertex> >( iConfig.getUntrackedParameter<InputTag> ( "VertexTag", InputTag( "offlineSlimmedPrimaryVertices" ) ) ) ),
    //vertexCandidateMapToken_( consumes<VertexCandidateMap>( iConfig.getParameter<InputTag>( "VertexCandidateMapTag" ) ) ),
    
    vbfMvaResultToken_( consumes<View<flashgg::VBFMVAResult> >( iConfig.getParameter<InputTag> ( "VBFMVAResultTag" ) ) ), // Ed Ed
    //mvaResultToken_( consumes<View<flashgg::DiPhotonMVAResult> >( iConfig.getParameter<InputTag> ( "MVAResultTag" ) ) ), // Ed Ed

    //qgVariablesInputTag( iConfig.getParameter<edm::InputTag>( "qgVariablesInputTag" ) ),

    usePUJetID( iConfig.getUntrackedParameter<bool>( "UsePUJetID"   , false ) ),
    photonJetVeto( iConfig.getUntrackedParameter<bool>( "PhotonJetVeto", true ) ),
    homeGenJetMatching_( iConfig.getUntrackedParameter<bool>( "homeGenJetMatching", false ) ),
    ZeroVertexOnly_( iConfig.getUntrackedParameter<bool>( "ZeroVertexOnly", false ) ),
    debug_( iConfig.getUntrackedParameter<bool>( "debug", false ) ),
    useVBFTagPhotonMatching_( iConfig.getUntrackedParameter<bool>( "useVBFTagPhotonMatching", false ) )

{
    cout << "Inside constructor of JetValidationTreeMaker" << endl;
    for( uint i = 0; i < inputTagJets_.size(); i++ ) {
        auto token = consumes<View<flashgg::Jet> >(inputTagJets_[i]);
        tokenJets_.push_back(token); 
    }

    event_number = 0;
    jetCollectionName = iConfig.getParameter<string>( "StringTag" );
    //qgToken	= consumes<edm::ValueMap<float>>( edm::InputTag( qgVariablesInputTag.label(), "qgLikelihood" ) );

    randomDiphoIndex = new TRandom3( 2395124 );
}

JetValidationTreeMaker::~JetValidationTreeMaker()
{
    event_number = 0;
}


void
JetValidationTreeMaker::analyze( const edm::Event &iEvent, const edm::EventSetup &iSetup )
{
    //cout << "Inside JetValTreeMaker analyze method" << endl;

    if( debug_ ) {
        std::cout << "\e[0;31m";
        std::cout << setw( 6 )  << "========================= "            << std::endl;
        std::cout << setw( 12 ) << "Event" << setw( 12 ) << event_number   << std::endl;
        std::cout << setw( 6 )  << "------------------------- "            << std::endl;
        std::cout << "\e[0m" << std::endl;
    }


    Handle<View<reco::Vertex> > vtxs;
    iEvent.getByToken( vertexToken_, vtxs );
    //const PtrVector<reco::Vertex>& vtxs = primaryVertices->ptrVector();

    Handle<View<flashgg::DiPhotonCandidate> > diPhotons;
    iEvent.getByToken( diPhotonToken_, diPhotons );
    //const PtrVector<flashgg::DiPhotonCandidate>& diPhotons = diPhotons->ptrVector();

    Handle<View<reco::GenParticle> > gens;
    iEvent.getByToken( genPartToken_, gens );
    //const PtrVector<reco::GenParticle>& gens = genParticles->ptrVector();

    Handle<View<pat::PackedGenParticle> > genPhotons; // Ed
    iEvent.getByToken( genPhoToken_, genPhotons ); // Ed

    Handle<View<reco::GenJet> > genJets;
    iEvent.getByToken( genJetToken_, genJets );
    //const PtrVector<reco::GenJet>& genJets = genJet->ptrVector();
    
    Handle<View<flashgg::VBFMVAResult> > vbfMvaResults; // Ed Ed
    iEvent.getByToken( vbfMvaResultToken_, vbfMvaResults );
    //Handle<View<flashgg::DiPhotonMVAResult> > mvaResults;
    //iEvent.getByToken( mvaResultToken_, mvaResults ); // Ed Ed

    //Handle<View<flashgg::Jet> > jetsDz;
    //iEvent.getByToken( jetDzToken_, jetsDz );
    //const PtrVector<flashgg::Jet>& jetsDzPointers = jetsDz->ptrVector();
    JetCollectionVector Jets( inputTagJets_.size() );
    for( size_t j = 0; j < inputTagJets_.size(); ++j ) {
        //iEvent.getByLabel( inputTagJets_[j], Jets[j] );
        iEvent.getByToken( tokenJets_[j], Jets[j] );
    }


    //edm::Handle<edm::ValueMap<float>> qgHandle;
    //if(!isPatJetCollection(jets))
    //iEvent.getByToken( qgToken, qgHandle );

    //Handle<VertexCandidateMap> vtxmap;
    //if( debug_ ) {
    //    iEvent.getByToken( vertexCandidateMapToken_, vtxmap );
    //}
    int legacyEqZeroth = 0;
    int nDiphotons = 0;

    nDiphotons = diPhotons->size();
    //if ( nDiphotons > 0 ) cout << "nDiphotons = " << nDiphotons << "!!!" << endl;
    if( diPhotons->size() == 0 ) {
        legacyEqZeroth = 1; //if there is no diphoton, we use 0th vertex anyway.
    } else {
        if( fabs( diPhotons->ptrAt( 0 )->vtx()->z() - vtxs->ptrAt( 0 )->z() ) < 0.01 ) {
            legacyEqZeroth = 1;
        }
    }

    eInfo.nDiphotons     = nDiphotons;
    eInfo.legacyEqZeroth = legacyEqZeroth;
    initEventStructure();
    eInfo.eventID    = event_number;
    genJetInfo.nPV   = vtxs->size();
    eInfo.nSV        = 0;

    if( debug_ ) {
        std::cout << "\e[0;31m";
        std::cout << setw( 12 ) << "nVtxs"    << setw( 12 ) << vtxs->size()     << std::endl;
        std::cout << setw( 12 ) << "nGenJet"  << setw( 12 ) << genJets->size()  << std::endl;
        std::cout << setw( 12 ) << "PV0==Leg" << setw( 12 ) << legacyEqZeroth   << std::endl;
        std::cout << setw( 12 ) << "nDiPhoto" << setw( 12 ) << diPhotons->size() << std::endl;
        std::cout << setw( 6 )  << "========================= "     << std::endl;
        std::cout << "\e[0m" << std::endl;
    }
    // photon eoverlaping removal
    std::vector<edm::Ptr<reco::GenParticle> > genPhoton;
    std::vector<edm::Ptr<reco::GenParticle> > genParton;

    for( unsigned int genLoop = 0 ; genLoop < gens->size(); genLoop++ ) {
        /*genInfo.pt     = gens->ptrAt( genLoop )->pt() ;
        genInfo.eta    = gens->ptrAt( genLoop )->eta();
        genInfo.phi    = gens->ptrAt( genLoop )->phi();
        genInfo.status = gens->ptrAt( genLoop )->status();
        genInfo.pdgid  = int( gens->ptrAt( genLoop )->pdgId() );*/ // Ed

        // be sure that the photons comes from the higgs
        if( gens->ptrAt( genLoop )->pdgId() == 22 && gens->ptrAt( genLoop )-> mother( 0 )->pdgId() == 25 ) {
            cout << " a gen photon!!! " << endl;
            genPhoton.push_back( gens->ptrAt( genLoop ) );
        }

        // select the quark and gluon
        if( std::abs( gens->ptrAt( genLoop )->pdgId() ) == 21 || // gluons
                std::abs( gens->ptrAt( genLoop )->pdgId() ) <= 5 ) { // quarks
            if( gens->ptrAt( genLoop )->status() == 3 ) { // another condition about the status 3
                genParton.push_back( gens->ptrAt( genLoop ) );
            }
        }
        // fill the tree
        //genPartTree->Fill(); // Ed
    }
    // find tag the jets close to the photons
    std::map<unsigned int, GenPhotonInfo> photonJet_id;
    std::map<unsigned int, bool>             _isPhoton;

    size_t diPhotonsSize = diPhotons->size();
    if( ZeroVertexOnly_ ) { diPhotonsSize = 1; }

    unsigned int actualDiphoIndex = randomDiphoIndex->Integer( diPhotonsSize );
    //cout << "actualDiphoIndex = " << actualDiphoIndex << endl;
    //cout << "diPhotonsSize = " << diPhotonsSize << endl;

    for( unsigned int diphoIndex = 0; diphoIndex < diPhotonsSize; diphoIndex++ ) {

        unsigned int jetCollectionIndex = 0;
        if( !ZeroVertexOnly_ ) { jetCollectionIndex = diPhotons->ptrAt( diphoIndex )->jetCollectionIndex(); }

        //edm::Ptr<flashgg::DiPhotonMVAResult> dipho_mvares = mvaResults->ptrAt( diphoIndex ); // Ed Ed
        edm::Ptr<flashgg::VBFMVAResult> vbf_mvares = vbfMvaResults->ptrAt( diphoIndex ); // Ed Ed

        //--------------------------------------------------------------------------------------------------
        // Begin analysis of prompt-fake events // Ed
        
        /*pfInfo.sigmarv = dipho_mvares->sigmarv;
        pfInfo.sigmawv = dipho_mvares->sigmawv;
        pfInfo.CosPhi  = dipho_mvares->CosPhi;
        pfInfo.vtxprob = dipho_mvares->vtxprob;*/

        pfInfo.dijet_leadEta = vbf_mvares->dijet_leadEta;
        pfInfo.dijet_subleadEta = vbf_mvares->dijet_subleadEta;
        pfInfo.dijet_abs_dEta = vbf_mvares->dijet_abs_dEta;
        pfInfo.dijet_LeadJPt = vbf_mvares->dijet_LeadJPt;
        pfInfo.dijet_SubJPt = vbf_mvares->dijet_SubJPt;
        pfInfo.dijet_Zep = vbf_mvares->dijet_Zep;
        pfInfo.dijet_dphi_trunc = vbf_mvares->dijet_dphi_trunc;
        pfInfo.dijet_dipho_dphi = vbf_mvares->dijet_dipho_dphi;
        pfInfo.dijet_Mjj = vbf_mvares->dijet_Mjj;
        pfInfo.dijet_dy = vbf_mvares->dijet_dy;
        pfInfo.dijet_leady = vbf_mvares->dijet_leady;
        pfInfo.dijet_subleady = vbf_mvares->dijet_subleady;
        pfInfo.dijet_dipho_pt = vbf_mvares->dijet_dipho_pt;
        pfInfo.dijet_minDRJetPho = vbf_mvares->dijet_minDRJetPho;

        pfInfo.eventID = event_number;
        //  pfInfo.weight  = desiredLumi * xs * BR / numberMCevents;
        // "QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8"  : {"xs":108000000.0 , "br" : 0.000225,"itype":30},
        // "QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8"  : {"xs":54120000.0 , "br" : 0.002,"itype":32},
        //pfInfo.weight  = 1.0 * 108000000.0 * 0.000225 / numberMCevents; //30to40
        //pfInfo.weight  = 1.0 *  54120000.0 * 0.002    / numberMCevents; //40toInf
        
        // NEEDS ATTENTION // Ed
        auto printDipho = diPhotons->ptrAt( diphoIndex );
        //auto printDipho = diPhotons->ptrAt( 0 );
        // select only diphoton candidate with highest IDMVA score
        /*if( diPhotonsSize > 1 ) {
            float max_phoIDMVA_sum = -3.0;
            for( uint secondDiphoIndex = 0; secondDiphoIndex < diPhotonsSize; secondDiphoIndex++ ) {
                float temp_phoIDMVA_sum =  diPhotons->ptrAt( secondDiphoIndex )->leadPhotonId() + diPhotons->ptrAt( secondDiphoIndex )->subLeadPhotonId();
                if( temp_phoIDMVA_sum > max_phoIDMVA_sum ) {
                    printDipho = diPhotons->ptrAt( secondDiphoIndex );
                    max_phoIDMVA_sum = temp_phoIDMVA_sum;
                }
            }
        }*/

        //if( printDipho->mass() < 100 || printDipho->mass() > 180 ) continue;
        /*if( genJets->size()    < 2 ) continue;
        if( genPhotons->size() < 2 ) continue;
        if( gens->size()       < 2 ) continue;
        cout << "Num Gen Jets    = " << genJets->size() << endl;
        cout << "Num Gen Photons = " << genPhotons->size() << endl;
        cout << "Num Gen Partons = " << gens->size() << endl;*/
        //cout << "At the continue point in JetValTreeMaker" << endl;

        pfInfo.diphoMass         = printDipho->mass();
        pfInfo.diphoPt           = printDipho->pt();
        pfInfo.diphoLeadingPt    = printDipho->leadingPhoton()->pt();
        pfInfo.diphoSubleadingPt = printDipho->subLeadingPhoton()->pt();

        auto printLeadPho    = printDipho->leadingPhoton();
        auto printSubLeadPho = printDipho->subLeadingPhoton();
        flashgg::Photon::mcMatch_t leadMatchType    = printLeadPho->genMatchType();
        //cout << "lead match type is " << leadMatchType << endl;
        flashgg::Photon::mcMatch_t subleadMatchType = printSubLeadPho->genMatchType();
        //cout << "sublead match type is " << subleadMatchType << endl;
        bool eventIsPromptFake = ( (!(leadMatchType==1 && subleadMatchType==1)) && (leadMatchType==1 || subleadMatchType==1) );
        auto promptPhoton      = printLeadPho;
        auto fakePhoton        = printSubLeadPho;
        //bool reversed          = false;
        float promptIDMVA      = printDipho->leadPhotonId();
        float fakeIDMVA        = printDipho->subLeadPhotonId();
        if( leadMatchType != 1 ) {
            promptPhoton = printSubLeadPho;
            fakePhoton   = printLeadPho;
            //reversed     = true;
            promptIDMVA  = printDipho->subLeadPhotonId();
            fakeIDMVA    = printDipho->leadPhotonId();
        }
        pfInfo.promptPdgId = promptPhoton->pdgId();
        //cout << "prompt pdgid is " << promptPhoton->pdgId() << endl;
        pfInfo.fakePdgId   = fakePhoton->pdgId();
        //cout << "fake pdgid is " << fakePhoton->pdgId() << endl;
        
        pfInfo.fakeWeight = fakePhoton->weight( "fakeWeight" );

        auto  genPhotonNearestPrompt  = genPhotons->ptrAt(0);
        auto  genPhotonNearestFake    = genPhotons->ptrAt(1);
        int   genPhotonsInPrompt      = 0;
        int   genPhotonsInFake        = 0;
        float promptTotalGenPhoEnergy = 0.;
        float fakeTotalGenPhoEnergy   = 0.;
        auto  genJetNearestPrompt     = genJets->ptrAt(0);
        auto  genJetNearestFake       = genJets->ptrAt(1);
        int   promptNumGenJets        = 0;
        int   fakeNumGenJets          = 0;
        auto  recoJets                = Jets[jetCollectionIndex];
        auto  recoJetNearestPrompt    = recoJets->ptrAt(0);
        auto  recoJetNearestFake      = recoJets->ptrAt(1);
        int   recoJetsInPrompt        = 0;
        int   recoJetsInFake          = 0;
        auto  partonNearestPrompt     = gens->ptrAt(0);
        auto  partonNearestFake       = gens->ptrAt(1);
        int   promptPartonMatchType   = 0;
        int   fakePartonMatchType     = 0;

        //cout << "fakePhoton->eta() = " << fakePhoton->eta() << endl << endl;

        if( eventIsPromptFake ) {
            float promptEta   = promptPhoton->eta();
            //float promptEta   = promptPhoton->superCluster()->eta();
            float promptPhi   = promptPhoton->phi();
            float fakeEta     = fakePhoton->eta();
            //float fakeEta     = fakePhoton->superCluster()->eta();
            float fakePhi     = fakePhoton->phi();
            float minDrPrompt = 10.0;
            float minDrFake   = 10.0;

            pfInfo.promptFakeDeltaR = deltaR( promptEta, promptPhi, fakeEta, fakePhi );

            // find nearest genPhoton and number of photons within dR of 0.4
            minDrPrompt = 10.0;
            minDrFake   = 10.0;
            for( uint genPhotonIndex = 0; genPhotonIndex < genPhotons->size(); genPhotonIndex++ ) {
                float tempEta  = genPhotons->ptrAt( genPhotonIndex )->eta();
                float tempPhi  = genPhotons->ptrAt( genPhotonIndex )->phi();
                float drPrompt = deltaR( tempEta, tempPhi, promptEta, promptPhi );
                float drFake   = deltaR( tempEta, tempPhi, fakeEta,   fakePhi   );
                //float drPrompt = sqrt( (tempEta-promptEta)*(tempEta-promptEta) + (tempPhi-promptPhi)*(tempPhi-promptPhi) );
                //float drFake   = sqrt( (tempEta-fakeEta)*(tempEta-fakeEta)     + (tempPhi-fakePhi)*(tempPhi-fakePhi)     );
                if( drPrompt < minDrPrompt ) {
                    minDrPrompt = drPrompt;
                    genPhotonNearestPrompt = genPhotons->ptrAt( genPhotonIndex );
                }
                if( drPrompt < 0.4 ) { 
                    genPhotonsInPrompt++;
                    promptTotalGenPhoEnergy += genPhotons->ptrAt( genPhotonIndex )->energy();
                }
                if( drFake < minDrFake ) {
                    minDrFake = drFake;
                    genPhotonNearestFake = genPhotons->ptrAt( genPhotonIndex );
                }
                if( drFake < 0.4 ) { 
                    genPhotonsInFake++;
                    fakeTotalGenPhoEnergy += genPhotons->ptrAt( genPhotonIndex )->energy();
                }
            } // end of genPhoton matching and counting
            float promptGenPhotonDr = minDrPrompt;
            float fakeGenPhotonDr   = minDrFake;


            // Print nearest genJet and whether it is within dR of 0.4
            minDrPrompt = 10.0;
            minDrFake   = 10.0;
            for( uint genJetIndex = 0; genJetIndex < genJets->size(); genJetIndex++ ) {
                float tempEta  = genJets->ptrAt( genJetIndex )->eta();
                float tempPhi  = genJets->ptrAt( genJetIndex )->phi();
                float drPrompt = deltaR( tempEta, tempPhi, promptEta, promptPhi );
                float drFake   = deltaR( tempEta, tempPhi, fakeEta,   fakePhi   );
                //float drPrompt = sqrt( (tempEta-promptEta)*(tempEta-promptEta) + (tempPhi-promptPhi)*(tempPhi-promptPhi) );
                //float drFake   = sqrt( (tempEta-fakeEta)*(tempEta-fakeEta)     + (tempPhi-fakePhi)*(tempPhi-fakePhi)     );
                if( drPrompt < minDrPrompt ) {
                    minDrPrompt = drPrompt;
                    genJetNearestPrompt = genJets->ptrAt( genJetIndex );
                    if ( drPrompt < 0.4 ) promptNumGenJets++;
                }
                else if( drPrompt < 0.4 ) promptNumGenJets++;
                if( drFake < minDrFake ) {
                    minDrFake = drFake;
                    genJetNearestFake = genJets->ptrAt( genJetIndex );
                    if ( drFake < 0.4 ) fakeNumGenJets++;
                }
                else if( drFake < 0.4 ) fakeNumGenJets++;
            } // end of genJet matching
            float promptGenJetDr = minDrPrompt;
            float fakeGenJetDr   = minDrFake;

            // print out the reco jet info
            minDrPrompt = 10.0;
            minDrFake   = 10.0;
            for( uint recoJetIndex = 0; recoJetIndex < recoJets->size(); recoJetIndex++ ) {
                float tempEta  = recoJets->ptrAt( recoJetIndex )->eta();
                float tempPhi  = recoJets->ptrAt( recoJetIndex )->phi();
                float drPrompt = deltaR( tempEta, tempPhi, promptEta, promptPhi );
                float drFake   = deltaR( tempEta, tempPhi, fakeEta,   fakePhi   );
                //float drPrompt = sqrt( (tempEta-promptEta)*(tempEta-promptEta) + (tempPhi-promptPhi)*(tempPhi-promptPhi) );
                //float drFake   = sqrt( (tempEta-fakeEta)*(tempEta-fakeEta)     + (tempPhi-fakePhi)*(tempPhi-fakePhi)     );
                if( drPrompt < minDrPrompt ) {
                    minDrPrompt = drPrompt;
                    recoJetNearestPrompt = recoJets->ptrAt( recoJetIndex );
                    if ( drPrompt < 0.4 ) recoJetsInPrompt++;
                }
                else if( drPrompt < 0.4 ) recoJetsInPrompt++;
                if( drFake < minDrFake ) {
                    minDrFake = drFake;
                    recoJetNearestFake = recoJets->ptrAt( recoJetIndex );
                    if ( drFake < 0.4 ) recoJetsInFake++;
                }
                else if( drFake < 0.4 ) recoJetsInFake++;
            } // end of recoJet matching 
            float promptRecoJetDr = minDrPrompt;
            float fakeRecoJetDr   = minDrFake;

            // loop over partons from matrix element
            minDrPrompt = 10.0;
            minDrFake   = 10.0;
            for( uint genParticleIndex = 0; genParticleIndex < gens->size(); genParticleIndex++ ) {
                //cout << "gen particle " << genParticleIndex << " has status " <<  gens->ptrAt( genParticleIndex )->status() << endl;
                float tempEta  = gens->ptrAt( genParticleIndex )->eta();
                float tempPhi  = gens->ptrAt( genParticleIndex )->phi();
                float drPrompt = deltaR( tempEta, tempPhi, promptEta, promptPhi );
                float drFake   = deltaR( tempEta, tempPhi, fakeEta,   fakePhi   );
                //float drPrompt = sqrt( (tempEta-promptEta)*(tempEta-promptEta) + (tempPhi-promptPhi)*(tempPhi-promptPhi) );
                //float drFake   = sqrt( (tempEta-fakeEta)*(tempEta-fakeEta)     + (tempPhi-fakePhi)*(tempPhi-fakePhi)     );
                if( drPrompt < minDrPrompt ) {
                    minDrPrompt = drPrompt;
                    partonNearestPrompt = gens->ptrAt( genParticleIndex );
                    int pdgID = gens->ptrAt( genParticleIndex )->pdgId();
                    if( pdgID < 7 && pdgID > -7 ) promptPartonMatchType = -1;
                    if( pdgID == 21 )             promptPartonMatchType = -2;
                    if ( drPrompt < 0.4) {
                        if( pdgID < 7 && pdgID > -7 ) promptPartonMatchType = 1;
                        if( pdgID == 21 )             promptPartonMatchType = 2;
                    }
                }
                if( drFake < minDrFake ) {
                    minDrFake = drFake;
                    partonNearestFake = gens->ptrAt( genParticleIndex );
                    int pdgID = gens->ptrAt( genParticleIndex )->pdgId();
                    if( pdgID < 7 && pdgID > -7 ) fakePartonMatchType = -1;
                    if( pdgID == 21 )             fakePartonMatchType = -2;
                    if ( drFake < 0.4 ) {
                        if( pdgID < 7 && pdgID > -7 ) fakePartonMatchType = 1;
                        if( pdgID == 21 )             fakePartonMatchType = 2;
                    }
                }
            } // end of parton matching
            float promptPartonDr = minDrPrompt;
            float fakePartonDr   = minDrFake;

            pfInfo.promptPt     = promptPhoton->pt();
            pfInfo.promptEnergy = promptPhoton->energy();
            pfInfo.promptEta    = promptEta;
            pfInfo.promptPhi    = promptPhi;
            pfInfo.promptIDMVA  = promptIDMVA;
            pfInfo.fakePt       = fakePhoton->pt();
            pfInfo.fakeEnergy   = fakePhoton->energy();
            pfInfo.fakeEta      = fakeEta;
            pfInfo.fakePhi      = fakePhi;
            pfInfo.fakeIDMVA    = fakeIDMVA;

            pfInfo.promptGenPhotonPt       = genPhotonNearestPrompt->pt();
            pfInfo.promptGenPhotonEnergy   = genPhotonNearestPrompt->energy();
            pfInfo.promptTotalGenPhoEnergy = promptTotalGenPhoEnergy;
            pfInfo.promptGenPhotonEta      = genPhotonNearestPrompt->eta();
            pfInfo.promptGenPhotonPhi      = genPhotonNearestPrompt->phi();
            pfInfo.promptGenPhotonDr       = promptGenPhotonDr;
            pfInfo.promptNumGenPhotons     = genPhotonsInPrompt;
            pfInfo.fakeGenPhotonPt         = genPhotonNearestFake->pt();
            pfInfo.fakeGenPhotonEnergy     = genPhotonNearestFake->energy();
            pfInfo.fakeTotalGenPhoEnergy   = fakeTotalGenPhoEnergy;
            pfInfo.fakeGenPhotonEta        = genPhotonNearestFake->eta();
            pfInfo.fakeGenPhotonPhi        = genPhotonNearestFake->phi();
            pfInfo.fakeGenPhotonDr         = fakeGenPhotonDr;
            pfInfo.fakeNumGenPhotons       = genPhotonsInFake;

            pfInfo.promptGenJetPt     = genJetNearestPrompt->pt();
            pfInfo.promptGenJetEnergy = genJetNearestPrompt->energy();
            pfInfo.promptGenJetEta    = genJetNearestPrompt->eta();
            pfInfo.promptGenJetPhi    = genJetNearestPrompt->phi();
            pfInfo.promptGenJetDr     = promptGenJetDr;
            pfInfo.promptNumGenJets   = promptNumGenJets;
            pfInfo.fakeGenJetPt       = genJetNearestFake->pt();
            pfInfo.fakeGenJetEnergy   = genJetNearestFake->energy();
            pfInfo.fakeGenJetEta      = genJetNearestFake->eta();
            pfInfo.fakeGenJetPhi      = genJetNearestFake->phi();
            pfInfo.fakeGenJetDr       = fakeGenJetDr;
            pfInfo.fakeNumGenJets     = fakeNumGenJets;

            pfInfo.promptRecoJetPt     = recoJetNearestPrompt->pt();
            pfInfo.promptRecoJetEnergy = recoJetNearestPrompt->energy();
            pfInfo.promptRecoJetEta    = recoJetNearestPrompt->eta();
            pfInfo.promptRecoJetPhi    = recoJetNearestPrompt->phi();
            pfInfo.promptRecoJetDr     = promptRecoJetDr;
            pfInfo.promptNumRecoJets   = recoJetsInPrompt;
            pfInfo.fakeRecoJetPt       = recoJetNearestFake->pt();
            pfInfo.fakeRecoJetEnergy   = recoJetNearestFake->energy();
            pfInfo.fakeRecoJetEta      = recoJetNearestFake->eta();
            pfInfo.fakeRecoJetPhi      = recoJetNearestFake->phi();
            pfInfo.fakeRecoJetDr       = fakeRecoJetDr;
            pfInfo.fakeNumRecoJets     = recoJetsInFake;

            pfInfo.promptPartonPt        = partonNearestPrompt->pt();
            pfInfo.promptPartonEnergy    = partonNearestPrompt->energy();
            pfInfo.promptPartonEta       = partonNearestPrompt->eta();
            pfInfo.promptPartonPhi       = partonNearestPrompt->phi();
            pfInfo.promptPartonDr        = promptPartonDr;
            pfInfo.promptPartonMatchType = promptPartonMatchType;
            pfInfo.fakePartonPt          = partonNearestFake->pt();
            pfInfo.fakePartonEnergy      = partonNearestFake->energy();
            pfInfo.fakePartonEta         = partonNearestFake->eta();
            pfInfo.fakePartonPhi         = partonNearestFake->phi();
            pfInfo.fakePartonDr          = fakePartonDr;
            pfInfo.fakePartonMatchType   = fakePartonMatchType;

            if( diphoIndex == actualDiphoIndex ) promptFakeTree->Fill();
            //promptFakeTree->Fill();
        } // End of prompt-fake events */ // Ed
        //--------------------------------------------------------------------------------------------------

        jInfo.nJets      = Jets[jetCollectionIndex]->size();
        jInfo.nPV        = vtxs->size();
        genJetInfo.nJets = Jets[jetCollectionIndex]->size();
        for( unsigned int jetLoop = 0 ; jetLoop < Jets[jetCollectionIndex]->size(); jetLoop++ ) {
            float minDr = 1000;
            std::map<float, unsigned int> minim;
            GenPhotonInfo tmp_info;
            if( genPhoton.size() != 0 && !useVBFTagPhotonMatching_) {
                for( unsigned int ig = 0; ig < genPhoton.size(); ig++ ) {
                    float dphi  = deltaPhi( Jets[jetCollectionIndex]->ptrAt( jetLoop )->phi(), genPhoton[ig]->phi() );
                    float deta  = Jets[jetCollectionIndex]->ptrAt( jetLoop )->eta() -  genPhoton[ig]->eta();
                    float dr    =  std::sqrt( deta * deta + dphi * dphi );
                    minDr = std::min( dr, minDr );
                    minim[dr] = ig;
                }
                unsigned int close_gid = minim.find( minDr )->second;

                tmp_info.pt     = genPhoton[close_gid]->pt();
                tmp_info.eta    = genPhoton[close_gid]->eta();
                tmp_info.phi    = genPhoton[close_gid]->phi();
                tmp_info.DRmin  = minDr;

                _isPhoton[jetLoop] = false;
                if( minDr < 0.3 ) {
                    _isPhoton[jetLoop] = true;
                }
                photonJet_id[jetLoop] =  tmp_info;
            }
            else if( genPhoton.size() == 0 && !useVBFTagPhotonMatching_) {
                tmp_info.pt     = -999.;
                tmp_info.eta    = -999.;
                tmp_info.phi    = -999.;
                tmp_info.DRmin  = -999.;

                _isPhoton[jetLoop] = false;
                photonJet_id[jetLoop] =  tmp_info;
            } 
            else {
                tmp_info.pt     = -999.;
                tmp_info.eta    = -999.;
                tmp_info.phi    = -999.;
                tmp_info.DRmin  = -999.; 
                photonJet_id[jetLoop] =  tmp_info; // This currently means if we do VBFTag style photon matching, we have no gen photon info
                
                // Check if jet is near to either of the two leading photons
                float dphi1  = deltaPhi( Jets[jetCollectionIndex]->ptrAt( jetLoop )->phi(), diPhotons->ptrAt( diphoIndex )->leadingPhoton()->phi() );
                float deta1  = Jets[jetCollectionIndex]->ptrAt( jetLoop )->eta() - diPhotons->ptrAt( diphoIndex )->leadingPhoton()->eta();
                float dr1    =  std::sqrt( deta1 * deta1 + dphi1 * dphi1 );

                float dphi2  = deltaPhi( Jets[jetCollectionIndex]->ptrAt( jetLoop )->phi(), diPhotons->ptrAt( diphoIndex )->subLeadingPhoton()->phi() );
                float deta2  = Jets[jetCollectionIndex]->ptrAt( jetLoop )->eta() - diPhotons->ptrAt( diphoIndex )->subLeadingPhoton()->eta();
                float dr2    =  std::sqrt( deta2 * deta2 + dphi2 * dphi2 );

                if( dr1 < 0.5 || dr2 < 0.5 ) { _isPhoton[jetLoop] = true; }
                else { _isPhoton[jetLoop] = false; }
            }

            //    if(debug_){
            //      std::cout << "\e[0;31m";
            //
            //      std::cout << setw(12) << "jet id"
            //		<< setw(12) << "Photon match"
            //		<< std::endl;
            //
            //      std::cout << setw(12) << jetLoop
            //		<< setw(12) << _isPhoton[jetLoop]
            //		<< std::endl;
            //
            //      std::cout <<"\e[0m"<< std::endl;
            //}
        }

        //if(debug_){
        //  std::cout << "\e[0;31m";
        //  std::cout << setw(12) << "PhoMatch"  << setw(12) << _isPhoton.size()  << std::endl;
        //  std::cout <<"\e[0m"<< std::endl;
        //}

        //+++ GenJet Matching
        std::map<unsigned int, GenJetInfo>     genJet_id;
        std::map<unsigned int, bool>          _isMatched;
        std::map<unsigned int, unsigned int>   pairs;

        for( unsigned int jetLoop = 0; jetLoop < Jets[jetCollectionIndex]->size(); jetLoop++ ) {
            float minDr = 1000;
            std::map<float, unsigned int> minim;
            GenJetInfo tmp_info;
            if( genJets->size() != 0 ) {
                for( unsigned int ig = 0; ig < genJets->size(); ig++ ) {
                    float dphi  = deltaPhi( Jets[jetCollectionIndex]->ptrAt( jetLoop )->phi(), genJets->ptrAt( ig )->phi() );
                    float deta  = Jets[jetCollectionIndex]->ptrAt( jetLoop )->eta() - genJets->ptrAt( ig )->eta();
                    float dr    =  std::sqrt( deta * deta + dphi * dphi );
                    minDr = std::min( dr, minDr );
                    minim[dr] = ig;
                }

                unsigned int close_genjet_id = minim.find( minDr )->second;
                tmp_info.pt     = genJets->ptrAt( close_genjet_id )->pt();
                tmp_info.eta    = genJets->ptrAt( close_genjet_id )->eta();
                tmp_info.phi    = genJets->ptrAt( close_genjet_id )->phi();
                tmp_info.dRmin  = minDr;

                _isMatched[jetLoop] = false;
                if( minDr < 0.4 && pairs.find( close_genjet_id ) == pairs.end() ) {
                    _isMatched[jetLoop] = true;
                    pairs[close_genjet_id] = jetLoop;
                }
                genJet_id[jetLoop] =  tmp_info;
            } else {
                tmp_info.pt     = -999.;
                tmp_info.eta    = -999.;//genJets->ptrAt( close_genjet_id )->eta();
                tmp_info.phi    = -999.;//genJets->ptrAt( close_genjet_id )->phi();
                tmp_info.dRmin  = -999.;//minDr;
                genJet_id[jetLoop] =  tmp_info;
            }
        }

        std::map<unsigned int, jetInfo> recojetmap;

        // +++ loop on the reconstructed jets
        unsigned int jetCounter = 0;   
        unsigned int rmsCounter = 0;   
        const float  rms_cut    = 0.03;
        for( unsigned int jdz = 0 ; jdz < Jets[jetCollectionIndex]->size() ; jdz++ ) {
            jInfo.eventID        = event_number;
            jInfo.weight         = 1.0; 
            jInfo.id             = jdz;
            jInfo.photonMatch    = int( _isPhoton[jdz] );
            jInfo.smartIndex     = jetCollectionIndex;
            jInfo.diphotonIndex  = diphoIndex;

            if( !_isPhoton[jdz] ) { jInfo.jetIndex = jetCounter++; }
            else { jInfo.jetIndex = -1; }

            // Only include if eta less than 4.7
            float tmp_eta = Jets[jetCollectionIndex]->ptrAt( jdz )->eta();
            if( fabs(tmp_eta) > 4.7 ) { continue; }

            // New index indicating if jet passed rms cut (for VBFTag comparison)
            float tmp_rms = Jets[jetCollectionIndex]->ptrAt( jdz )->rms();
            if( !_isPhoton[jdz] && fabs(tmp_eta) > 2.5 && tmp_rms < rms_cut ) { jInfo.passesRMSIndex = rmsCounter++; }
            else if( !_isPhoton[jdz] && fabs(tmp_eta) < 2.5 ) { jInfo.passesRMSIndex = rmsCounter++; }
            else { jInfo.passesRMSIndex = -1; }

            //jInfo.jet_qgLikelihood = ( *qgHandle )[Jets[jetCollectionIndex]->refAt( jdz )];

            if( Jets[jetCollectionIndex]->ptrAt( jdz )->hasUserFloat("QGTagger:qgLikelihood") ) {
                jInfo.jet_qgLikelihood = Jets[jetCollectionIndex]->ptrAt( jdz )->userFloat("QGTagger:qgLikelihood");
            } else {
                jInfo.jet_qgLikelihood = -999.; // does not exist
            }
            //std::cout << "QGL::"<< jInfo.jet_qgLikelihood << std::endl;
            GenPhotonInfo tmp_info = photonJet_id.find( jdz )->second; // call find ones

            jInfo.GenPhotonPt  = tmp_info.pt   ;
            jInfo.GenPhotonEta = tmp_info.eta  ;
            jInfo.GenPhotonPhi = tmp_info.phi  ;
            jInfo.photondRmin  = tmp_info.DRmin;

            jInfo.pt            = Jets[jetCollectionIndex]->ptrAt( jdz )->pt();
            jInfo.rawPt         = Jets[jetCollectionIndex]->ptrAt( jdz )->correctedJet( "Uncorrected" ).pt() ;

            if( jetCollectionName.find( "PPI" ) > 1 && jetCollectionName.find( "PPI" ) < jetCollectionName.size() ) {
                jInfo.bestPt      = Jets[jetCollectionIndex]->ptrAt( jdz )->correctedJet( "Uncorrected" ).pt() ;
            } else {
                jInfo.bestPt      = Jets[jetCollectionIndex]->ptrAt( jdz )->pt() ;
            }

            //if(debug_) std::cout << "jet correction:: uncorected pt("
            /*std::cout << "jet correction:: uncorected pt("
                      <<  Jets[jetCollectionIndex]->ptrAt( jdz )->correctedJet( "Uncorrected" ).pt()
                      << ") corrected pt("
                      << Jets[jetCollectionIndex]->ptrAt( jdz )->pt()
                      << std::endl; */

            if( homeGenJetMatching_ ) {
                jInfo.genJetMatch             = int( _isMatched[jdz] );

                GenJetInfo tmp_genjet_info    = genJet_id.find( jdz )->second;
                jInfo.genJetPt                = tmp_genjet_info.pt ;
                jInfo.genJetEta               = tmp_genjet_info.eta;
                jInfo.genJetPhi               = tmp_genjet_info.phi;
                jInfo.genJetdRmin             = tmp_genjet_info.dRmin;
            } else {
                //std::cout << "test 1"<< std::endl;
                if( Jets[jetCollectionIndex]->ptrAt( jdz )->genJet() ) {
                    jInfo.genJetMatch           = 1;
                    jInfo.genJetPt              = Jets[jetCollectionIndex]->ptrAt( jdz )->genJet()->pt();
                    jInfo.genJetEta             = Jets[jetCollectionIndex]->ptrAt( jdz )->genJet()->eta();
                    jInfo.genJetEta             = Jets[jetCollectionIndex]->ptrAt( jdz )->genJet()->eta();
                    jInfo.genJetdRmin           = delta_R( Jets[jetCollectionIndex]->ptrAt( jdz )->genJet(), Jets[jetCollectionIndex]->ptrAt( jdz ) );
                    //std::cout << "test 2"<< std::endl;
                } else {
                    jInfo.genJetPt              = -9999.;
                    jInfo.genJetEta             = -9999.;
                    jInfo.genJetMatch           = 0;
                    jInfo.genJetdRmin           = -9999.;
                }
            }

            if( Jets[jetCollectionIndex]->ptrAt( jdz )->genParton() ) {
                jInfo.genQuarkMatch           = 1;
                jInfo.genQuarkPt              = Jets[jetCollectionIndex]->ptrAt( jdz )->genParton()->pt();
                jInfo.genQuarkEta             = Jets[jetCollectionIndex]->ptrAt( jdz )->genParton()->eta();
                jInfo.genQuarkPdgId           = Jets[jetCollectionIndex]->ptrAt( jdz )->genParton()->pdgId();
            } else {
                jInfo.genQuarkPt              = -9999.;
                jInfo.genQuarkEta             = -9999.;
                jInfo.genQuarkMatch           = 0;
                jInfo.genQuarkPdgId           = -9999;
            }
            //----------------------
            jInfo.energy           = Jets[jetCollectionIndex]->ptrAt( jdz )->energy() ;
            jInfo.mass             = Jets[jetCollectionIndex]->ptrAt( jdz )->mass() ;
            jInfo.eta              = Jets[jetCollectionIndex]->ptrAt( jdz )->eta();
            jInfo.phi              = Jets[jetCollectionIndex]->ptrAt( jdz )->phi();
            jInfo.area             = Jets[jetCollectionIndex]->ptrAt( jdz )->jetArea();


            if( !( jetCollectionName.find( "PPI" ) > 1 && jetCollectionName.find( "PPI" ) < jetCollectionName.size() ) ) {

                if( ( diPhotons->size() > 0 ) && ( jetCollectionName.find( "Leg" ) != std::string::npos ) ) {
                    jInfo.PUJetID_betaStar   = Jets[jetCollectionIndex]->ptrAt( jdz )->betaStar( diPhotons->ptrAt( 0 )->vtx() );
                    jInfo.PUJetID_rms        = Jets[jetCollectionIndex]->ptrAt( jdz )->rms( diPhotons->ptrAt( 0 )->vtx() );
                    jInfo.passesPUJetID      = Jets[jetCollectionIndex]->ptrAt( jdz )->passesPuJetId( diPhotons->ptrAt( 0 )->vtx() );

                    //jInfo.jet_W       = Jets[jetCollectionIndex]->ptrAt( jdz )->pileupJetIdentifier(diPhotons->ptrAt(0)->vtx()).jetW();
                    //jInfo.jet_dR2Mean = Jets[jetCollectionIndex]->ptrAt( jdz )->pileupJetIdentifier(diPhotons->ptrAt(0)->vtx()).dR2Mean();
                    //jInfo.jet_dRMean  = Jets[jetCollectionIndex]->ptrAt( jdz )->pileupJetIdentifier(diPhotons->ptrAt(0)->vtx()).dRMean();
                    //jInfo.jet_dZ      = Jets[jetCollectionIndex]->ptrAt( jdz )->pileupJetIdentifier(diPhotons->ptrAt(0)->vtx()).dZ();
                    //jInfo.jet_ptD     = Jets[jetCollectionIndex]->ptrAt( jdz )->pileupJetIdentifier(diPhotons->ptrAt(0)->vtx()).ptD();

                } else {

                    //TString name_tmp(jetCollectionName.c_str()) ;
                    //name_tmp.Replace("flashggJetValidationTreeMakerPF","");
                    //std::cout << " ------- [1][jet collection]" << jetCollectionName << std::endl;
                    if( jetCollectionName == "PF" && ( diPhotons->size() > 0 ) ) {
                        //std::cout << " ------- [0][jet collection] " << jetCollectionName << std::endl;
                        jInfo.PUJetID_betaStar   = Jets[jetCollectionIndex]->ptrAt( jdz )->betaStar( diPhotons->ptrAt( 0 )->vtx() );
                        jInfo.PUJetID_rms        = Jets[jetCollectionIndex]->ptrAt( jdz )->rms( diPhotons->ptrAt( 0 )->vtx() );
                        jInfo.passesPUJetID      = Jets[jetCollectionIndex]->ptrAt( jdz )->passesPuJetId( diPhotons->ptrAt( 0 )->vtx() );
                    } else {
                        jInfo.PUJetID_betaStar   = Jets[jetCollectionIndex]->ptrAt( jdz )->betaStar( vtxs->ptrAt( 0 ) );
                        jInfo.PUJetID_rms        = Jets[jetCollectionIndex]->ptrAt( jdz )->rms( vtxs->ptrAt( 0 ) );
                        jInfo.passesPUJetID      = Jets[jetCollectionIndex]->ptrAt( jdz )->passesPuJetId( vtxs->ptrAt( 0 ) );
                    }
                    //jInfo.jet_W       = Jets[jetCollectionIndex]->ptrAt( jdz )->pileupJetIdentifier(vtxs->ptrAt(0)).jetW();
                    //jInfo.jet_dR2Mean = Jets[jetCollectionIndex]->ptrAt( jdz )->pileupJetIdentifier(vtxs->ptrAt(0)).dR2Mean();
                    //jInfo.jet_dRMean  = Jets[jetCollectionIndex]->ptrAt( jdz )->pileupJetIdentifier(vtxs->ptrAt(0)).dRMean();
                    //jInfo.jet_dZ        = Jets[jetCollectionIndex]->ptrAt( jdz )->pileupJetIdentifier(vtxs->ptrAt(0)).dZ();
                    //jInfo.jet_ptD     = Jets[jetCollectionIndex]->ptrAt( jdz )->pileupJetIdentifier(vtxs->ptrAt(0)).ptD();

                }
            } else {

                jInfo.PUJetID_betaStar       = -999.;
                jInfo.PUJetID_rms            = -999.;
                jInfo.passesPUJetID          = -999;
            }
            jInfo.nDiphotons = nDiphotons;
            jInfo.LegIsPV0   = legacyEqZeroth;

            genJetInfo.nDiphotons = nDiphotons;
            genJetInfo.LegIsPV0   = legacyEqZeroth;

            // Get constituants information
            jInfo.nPart     = Jets[jetCollectionIndex]->ptrAt( jdz )->numberOfDaughters();
            jInfo.nCharged  = Jets[jetCollectionIndex]->ptrAt( jdz )->chargedMultiplicity();
            jInfo.nNeutral  = Jets[jetCollectionIndex]->ptrAt( jdz )->neutralMultiplicity();
            jInfo.chgEmFrac = Jets[jetCollectionIndex]->ptrAt( jdz )->chargedEmEnergy() / Jets[jetCollectionIndex]->ptrAt( jdz )->energy(); //
            jInfo.neuEmFrac = Jets[jetCollectionIndex]->ptrAt( jdz )->neutralEmEnergy() / Jets[jetCollectionIndex]->ptrAt( jdz )->energy(); //

            // study of the pile-up jet id
            //double sumTkPt  = 0;
            //double beta     = 0;
            //double betaStar = 0;
            ////if(debug_ && std::abs(Jets[jetCollectionIndex]->ptrAt( jdz )->eta())<2.5){
            //if( debug_ && std::abs( Jets[jetCollectionIndex]->ptrAt( jdz )->eta() ) < 2.5 && Jets[jetCollectionIndex]->ptrAt( jdz )->pt() > 20.0 ) {
            //    std::cout << setw( 12 ) << "jet[" << jdz
            //              << "] vtx0==vtxgg( " << jInfo.LegIsPV0 << " )"
            //              << std::endl ;
            //    std::cout << setw( 6 ) << "";
            //    std::cout << setw( 6 ) << "=======================================================" << std::endl;
            //
            //    std::cout << setw( 12 ) << "index";
            //    std::cout << setw( 12 ) << "PDG";
            //    std::cout << setw( 12 ) << "pt";
            //    std::cout << setw( 12 ) << "dZ0";
            //    std::cout << setw( 12 ) << "dZ";
            //    std::cout << setw( 12 ) << "inVtx0";
            //    std::cout << setw( 12 ) << "inOtherVtx";
            //    std::cout << std::endl;
            //}

            //debug_ && vtxmap.isValid() ) {
            //const std::vector<std::pair<edm::Ptr<reco::Vertex>, edm::Ptr<pat::PackedCandidate> > >  &vtxmap_ = *vtxmap;
            //for( unsigned int i = 0 ; i < Jets[jetCollectionIndex]->ptrAt( jdz )->numberOfDaughters()  ; i++ ) {
            //    edm::Ptr<pat::PackedCandidate> icand = edm::Ptr<pat::PackedCandidate> ( Jets[jetCollectionIndex]->ptrAt( jdz )->daughterPtr( i ) );
            //    if( icand->charge() == 0 ) { continue ; }
            //
            //    float tkpt = icand->pt();
            //    sumTkPt   += tkpt;
            //
            //    double dZ0 = std::abs( icand->dz( vtxs->ptrAt( 0 )->position() ) );
            //    double dZ  = dZ0;
            //    for( flashgg::VertexCandidateMap::const_iterator vi = vtxmap_.begin() ; vi != vtxmap_.end() ; vi++ ) {
            //        const edm::Ptr<reco::Vertex> iv = ( vi->first );
            //        if( iv->isFake() || iv->ndof() < 4 ) { continue; }
            //        dZ = std::min<double>( dZ, std::abs( icand->dz( iv->position() ) ) );
            //    }
            //
            //    bool inVtx0       = false;
            //    bool inAnotherVtx = false;
            //
            //    if( dZ0 < 0.2 ) {
            //        inVtx0 = true;
            //        beta += tkpt;
            //    } else if( dZ < 0.2 ) {
            //        inAnotherVtx = true;
            //        betaStar += tkpt;
            //    }
            //
            //    if( debug_ && std::abs( Jets[jetCollectionIndex]->ptrAt( jdz )->eta() ) < 2.5 && Jets[jetCollectionIndex]->ptrAt( jdz )->pt() > 20.0 ) {
            //        std::cout << setw( 12 ) << i;
            //        std::cout << setw( 12 ) << icand->pdgId();
            //        std::cout << setw( 12 ) << icand->pt();
            //        std::cout << setw( 12 ) << dZ0;
            //        std::cout << setw( 12 ) << dZ;
            //        std::cout << setw( 12 ) << inVtx0;
            //        std::cout << setw( 12 ) << inAnotherVtx;
            //        std::cout << std::endl;
            //    }
            //
            //}
            //if( sumTkPt != 0. ) {
            //    beta     = beta    / sumTkPt;
            //    betaStar = betaStar / sumTkPt;
            //} else {
            //    beta     = -1;
            //    betaStar = -1;
            //}
            //}

            //jInfo.mybetaStar = betaStar;
            //jInfo.mybeta     = beta;

            if( debug_ && std::abs( Jets[jetCollectionIndex]->ptrAt( jdz )->eta() ) < 2.5 && Jets[jetCollectionIndex]->ptrAt( jdz )->pt() > 20.0 ) {
                std::cout << setw( 6 )  << "";
                std::cout << setw( 6 )  << "-------------------------------------------------------" << std::endl;
                std::cout << setw( 12 ) << "id";
                std::cout << setw( 12 ) << "pt";
                std::cout << setw( 12 ) << "eta";
                std::cout << setw( 12 ) << "genMatch";
                std::cout << setw( 12 ) << "DrMatch";
                std::cout << setw( 12 ) << "betaStar";
                std::cout << setw( 12 ) << "newBetaStar";
                std::cout << setw( 12 ) << "isPhoton";
                std::cout << setw( 12 ) << "vtx_0";
                std::cout << setw( 12 ) << "vtx_gg";
                std::cout << std::endl;

                std::cout << setw( 12 ) << jdz;
                std::cout << setw( 12 ) << Jets[jetCollectionIndex]->ptrAt( jdz )->pt();
                std::cout << setw( 12 ) << Jets[jetCollectionIndex]->ptrAt( jdz )->eta();
                std::cout << setw( 12 ) << jInfo.genJetMatch;
                std::cout << setw( 12 ) << jInfo.genJetdRmin;
                std::cout << setw( 12 ) << jInfo.PUJetID_betaStar;
                std::cout << setw( 12 ) << jInfo.mybetaStar;
                std::cout << setw( 12 ) << jInfo.photonMatch;
                std::cout << setw( 12 ) << vtxs->ptrAt( 0 )->position().z();

                if( diPhotons->size() > 0 ) { std::cout << setw( 12 ) << diPhotons->ptrAt( 0 )->vtx()->position().z(); }
                else                    { std::cout << setw( 12 ) << "no gg"; }

                std::cout << std::endl;
                std::cout << setw( 6 ) << "";
                std::cout << setw( 6 ) << "=======================================================" << std::endl;
            }

            recojetmap[jdz] = jInfo;
            jetTree->Fill();
        } // ++++ end loop reco jets



        // loop over the GenJets
        for( unsigned int genLoop = 0 ; genLoop < genJets->size(); genLoop++ ) {
            genJetInfo.eventID         = event_number;
            genJetInfo.recoJetPt       = -999.;
            genJetInfo.recoJetRawPt    = -999.;
            genJetInfo.recoJetBestPt   = -999.;
            genJetInfo.recoJetMatch    =  0   ;
            genJetInfo.recoJetEta      = -999.;
            genJetInfo.dR              = -999.;
            genJetInfo.pt              = -999.;
            genJetInfo.eta             = -999.;
            genJetInfo.phi             = -999.;
            genJetInfo.PUJetID_betaStar = -999.;
            genJetInfo.PUJetID_rms     = -999.;
            genJetInfo.passesPUJetID   = -999;
            genJetInfo.nDiphotons      = nDiphotons;

            if( genJets->ptrAt( genLoop )->pt() < 20 ) { continue;}

            genJetInfo.pt     = genJets->ptrAt( genLoop )->pt() ;
            genJetInfo.eta    = genJets->ptrAt( genLoop )->eta();
            genJetInfo.phi    = genJets->ptrAt( genLoop )->phi();

            for( unsigned int diphoIndex = 0; diphoIndex < diPhotonsSize ; diphoIndex++ ) {
                unsigned int jetCollectionIndex = 0;
                if( !ZeroVertexOnly_ ) { jetCollectionIndex = diPhotons->ptrAt( diphoIndex )->jetCollectionIndex(); }
                for( unsigned int recoLoop = 0; recoLoop <  Jets[jetCollectionIndex]->size(); recoLoop++ ) {
                    if( Jets[jetCollectionIndex]->ptrAt( recoLoop )->pt() < 5 ) { continue; }

                    double deta = Jets[jetCollectionIndex]->ptrAt( recoLoop )->eta() - 	 genJets->ptrAt( genLoop )->eta();
                    double dphi = Jets[jetCollectionIndex]->ptrAt( recoLoop )->phi() - 	 genJets->ptrAt( genLoop )->phi();
                    double dr = std::sqrt( deta * deta + dphi * dphi );

                    if( dr < 0.4 ) {
                        genJetInfo.dR              =  dr;
                        genJetInfo.recoJetPt       = Jets[jetCollectionIndex]->ptrAt( recoLoop )->pt() ;
                        genJetInfo.recoJetRawPt    = Jets[jetCollectionIndex]->ptrAt( recoLoop )->correctedJet( "Uncorrected" ).pt()  ;

                        //-- add  he photon overlaping info
                        jetInfo tmpjetinfo         = recojetmap[recoLoop];
                        genJetInfo.photonMatch     = tmpjetinfo.photonMatch;
                        genJetInfo.GenPhotonPt     = tmpjetinfo.GenPhotonPt;
                        genJetInfo.photondRmin     = tmpjetinfo.photondRmin;
                        genJetInfo.smartIndex     = jetCollectionIndex;
                        genJetInfo.diphotonIndex  = diphoIndex;
                        //std::cout << " test ["<< recoLoop << "]--> (" << tmpjetinfo.photonMatch <<")"<<std::endl;

                        if( !( jetCollectionName.find( "PPI" ) > 1 && jetCollectionName.find( "PPI" ) < jetCollectionName.size() ) ) {
                            genJetInfo.recoJetBestPt   =  Jets[jetCollectionIndex]->ptrAt( recoLoop )->correctedJet( "Uncorrected" ).pt() ;

                            if( ( diPhotons->size() > 0 ) && ( jetCollectionName.find( "Leg" ) != std::string::npos ) ) {
                                genJetInfo.PUJetID_betaStar        = Jets[jetCollectionIndex]->ptrAt( recoLoop )->betaStar( diPhotons->ptrAt( 0 )->vtx() );
                                genJetInfo.PUJetID_rms             = Jets[jetCollectionIndex]->ptrAt( recoLoop )->rms( diPhotons->ptrAt( 0 )->vtx() );
                                genJetInfo.passesPUJetID           = Jets[jetCollectionIndex]->ptrAt( recoLoop )->passesPuJetId( diPhotons->ptrAt( 0 )->vtx() );
                            } else {
                                genJetInfo.PUJetID_betaStar        = Jets[jetCollectionIndex]->ptrAt( recoLoop )->betaStar( vtxs->ptrAt( 0 ) );
                                genJetInfo.PUJetID_rms             = Jets[jetCollectionIndex]->ptrAt( recoLoop )->rms( vtxs->ptrAt( 0 ) );
                                genJetInfo.passesPUJetID           = Jets[jetCollectionIndex]->ptrAt( recoLoop )->passesPuJetId( vtxs->ptrAt( 0 ) );
                            }
                        } else {
                            genJetInfo.recoJetBestPt   = Jets[jetCollectionIndex]->ptrAt( recoLoop )->pt()  ;
                            genJetInfo.PUJetID_betaStar  = -999.;
                            genJetInfo.PUJetID_rms       = -999.;
                            genJetInfo.passesPUJetID     = -999;
                        }

                        genJetInfo.recoJetMatch    = 1 ;
                        break;
                    }
                }
            }
            genJetTree->Fill();
        } // end of loop over genJets
    } //  end of loop over the diphotons
    eventTree->Fill();
    event_number++;
    //cout << "Exiting JetValTreeMaker analyze method" << endl;
}

void
JetValidationTreeMaker::beginJob()
{
    // +++ trees
    std::string type( "eventTree_" );
    type += jetCollectionName;

    eventTree = fs_->make<TTree>( type.c_str(), jetCollectionName.c_str() );
    eventTree->Branch( "eventID"    , &eInfo.eventID       , "eventID/I" );
    eventTree->Branch( "eventBranch", &eInfo.legacyEqZeroth, "legacyEqZeroth/I:nDiphotons/I" );

    std::string typeJet( "jetTree_" );
    typeJet += jetCollectionName;
    jetTree = fs_->make<TTree>( typeJet.c_str(), jetCollectionName.c_str() );

    jetTree->Branch( "eventID"         , &jInfo.eventID           , "eventID/I" );
    jetTree->Branch( "pt"              , &jInfo.pt                , "pt/F" );
    jetTree->Branch( "rawPt"           , &jInfo.rawPt             , "rawPt/F" );
    jetTree->Branch( "bestPt"          , &jInfo.bestPt            , "bestPt/F" );
    jetTree->Branch( "energy"          , &jInfo.energy            , "energy/F" );
    jetTree->Branch( "mass"            , &jInfo.mass              , "mass/F" );
    jetTree->Branch( "eta"             , &jInfo.eta               , "eta/F" );
    jetTree->Branch( "phi"             , &jInfo.phi               , "phi/F" );

    jetTree->Branch( "PlanarFlow"      , &jInfo.PlanarFlow        , "PlanarFlow/F" );
    jetTree->Branch( "S"               , &jInfo.S                 , "S/F" );
    jetTree->Branch( "Q"               , &jInfo.Q                 , "Q/F" );

    jetTree->Branch( "passesPUJetID"   , &jInfo.passesPUJetID     , "passesPUJetID/I" );
    jetTree->Branch( "JetArea"         , &jInfo.area              , "area/F" );
    jetTree->Branch( "nDiphotons"      , &jInfo.nDiphotons        , "nDiphotons/I" );

    jetTree->Branch( "diphotonIndex"   , &jInfo.diphotonIndex     , "diphotonIndex/I" );
    jetTree->Branch( "smartIndex"      , &jInfo.smartIndex        , "smartIndex/I" );
    jetTree->Branch( "jetIndex"        , &jInfo.jetIndex          , "jetIndex/I" );
    jetTree->Branch( "passesRMSIndex"  , &jInfo.passesRMSIndex    , "passesRMSIndex/I" );

    jetTree->Branch( "nPV"             , &jInfo.nPV               , "nPV/I" );
    jetTree->Branch( "nJets"           , &jInfo.nJets             , "nJets/I" );
    jetTree->Branch( "LegIsPV0"        , &jInfo.LegIsPV0          , "LegIsPV0/I" );

    // ===== PUJID variables
    jetTree->Branch( "betaStar" , &jInfo.PUJetID_betaStar , "betaStar/F" );
    jetTree->Branch( "rms"      , &jInfo.PUJetID_rms      , "rms/F" );
    jetTree->Branch( "W"        , &jInfo.jet_W            , "W/F" );
    jetTree->Branch( "dR2Mean"  , &jInfo.jet_dR2Mean      , "dR2Mean/F" );
    jetTree->Branch( "dRMean"   , &jInfo.jet_dRMean       , "dRMean/F" );
    jetTree->Branch( "dZ"       , &jInfo.jet_dZ           , "dZ/F" );
    jetTree->Branch( "ptD"      , &jInfo.jet_ptD          , "ptD/F" );

    // =====
    jetTree->Branch( "id"        , &jInfo.id        , "id/I" );
    jetTree->Branch( "nPart"     , &jInfo.nPart     , "nPart/I" );
    jetTree->Branch( "nCharged"  , &jInfo.nCharged  , "nCharged/I" );
    jetTree->Branch( "nNeutral"  , &jInfo.nNeutral  , "nNeutral/F" );
    jetTree->Branch( "chgEmFrac" , &jInfo.chgEmFrac , "chgEmFrac/F" );
    jetTree->Branch( "neuEmFrac" , &jInfo.neuEmFrac , "neuEmFrac/F" );
    jetTree->Branch( "qgLikelihood" , &jInfo.jet_qgLikelihood , "qgLikelihood/F" );

    jetTree->Branch( "genJetPt"       , &jInfo.genJetPt     , "genJetPt/F" );
    jetTree->Branch( "genJetEta"      , &jInfo.genJetEta    , "genJetEta/F" );
    jetTree->Branch( "genJetMatch"    , &jInfo.genJetMatch  , "genJetMatch/I" );
    jetTree->Branch( "genQuarkPt"     , &jInfo.genQuarkPt   , "genQuarkPt/F" );
    jetTree->Branch( "genQuarkEta"    , &jInfo.genQuarkEta  , "genQuarkEta/F" );
    jetTree->Branch( "genQuarkMatch"  , &jInfo.genQuarkMatch, "genQuarkMatch/I" );
    jetTree->Branch( "genQuarkPdgId"  , &jInfo.genQuarkPdgId, "genQuarkPdfId/I" );

    jetTree->Branch( "photonMatch"    , &jInfo.photonMatch  , "photonMatch/I" );
    jetTree->Branch( "photondRmin"    , &jInfo.photondRmin  , "photondRmin/F" );
    jetTree->Branch( "GenPhotonPt"    , &jInfo.GenPhotonPt   , "GenPhotonPt/F" );
    jetTree->Branch( "GenPhotonEta"   , &jInfo.GenPhotonEta  , "GenPhotonEta/F" );
    jetTree->Branch( "GenPhotonPhi"   , &jInfo.GenPhotonPhi  , "GenPhotonPhi/F" );

    jetTree->Branch( "weight"   , &jInfo.weight , "weight/F" );

    /*genPartTree = fs_->make<TTree>( "genPartTree", "Check per-jet tree" );
    genPartTree->Branch( "pt"     , &genInfo.pt      , "pt/F" );
    genPartTree->Branch( "eta"    , &genInfo.eta     , "eta/F" );
    genPartTree->Branch( "phi"    , &genInfo.phi     , "phi/F" );
    genPartTree->Branch( "status" , &genInfo.status  , "status/I" );
    genPartTree->Branch( "pdgid"  , &genInfo.pdgid   , "pdgid/I" );
    genPartTree->Branch( "y"      , &genInfo.y       , "y/F" ); */ // Ed

    //genPartTree->SetBranchStatus( 'p4.*', 1 );

    std::string typeGenJet( "genJetTree_" );
    typeGenJet += jetCollectionName;
    genJetTree = fs_->make<TTree>( typeGenJet.c_str(), jetCollectionName.c_str() );
    genJetTree->Branch( "eventID", &genJetInfo.eventID , "eventID/I" );
    genJetTree->Branch( "pt"     , &genJetInfo.pt      , "pt/F" );
    genJetTree->Branch( "eta"    , &genJetInfo.eta     , "eta/F" );
    genJetTree->Branch( "phi"    , &genJetInfo.phi     , "phi/F" );

    genJetTree->Branch( "recoJetPt"        , &genJetInfo.recoJetPt        , "recoJetPt/F" );
    genJetTree->Branch( "recoJetRawPt"     , &genJetInfo.recoJetRawPt     , "recoJetRawPt/F" );
    genJetTree->Branch( "recoJetBestPt"    , &genJetInfo.recoJetBestPt    , "recoJetBestPt/F" );
    genJetTree->Branch( "recoJetMatch"     , &genJetInfo.recoJetMatch     , "recoJetMatch/I" );
    genJetTree->Branch( "recoJetEta"       , &genJetInfo.recoJetEta       , "recoJetEta/F" );
    genJetTree->Branch( "dR"               , &genJetInfo.dR               , "dR/F" );
    genJetTree->Branch( "PUJetID_betaStar" , &genJetInfo.PUJetID_betaStar , "PUJetID_betaStar/F" );
    genJetTree->Branch( "PUJetID_rms"      , &genJetInfo.PUJetID_rms      , "PUJetID_rms/F" );
    genJetTree->Branch( "passesPUJetID"    , &genJetInfo.passesPUJetID    , "passesPUJetID/I" );
    genJetTree->Branch( "nDiphotons"       , &genJetInfo.nDiphotons        , "nDiphotons/I" );

    genJetTree->Branch( "diphotonIndex"   , &genJetInfo.diphotonIndex     , "diphotonIndex/I" );
    genJetTree->Branch( "smartIndex"      , &genJetInfo.smartIndex        , "smartIndex/I" );

    genJetTree->Branch( "nPV"              , &genJetInfo.nPV               , "nPV/I" );
    genJetTree->Branch( "nJets"            , &genJetInfo.nJets             , "nJets/I" );
    genJetTree->Branch( "LegIsPV0"         , &genJetInfo.LegIsPV0          , "LegIsPV0/I" );

    genJetTree->Branch( "photonMatch"      , &genJetInfo.photonMatch  , "photonMatch/I" );
    genJetTree->Branch( "photondRmin"      , &genJetInfo.photondRmin  , "photondRmin/F" );
    genJetTree->Branch( "GenPhotonPt"      , &genJetInfo.GenPhotonPt  , "GenPhotonPt/F" );

    // tree containing info of prompt-fake events only
    promptFakeTree = fs_->make<TTree>( "promptFakeTree", "Tree for prompt-fake events only" );

    promptFakeTree->Branch( "eventID"      , &pfInfo.eventID, "eventID/I" );
    //promptFakeTree->Branch( "weight"      , &pfInfo.weight, "weight/F" );
    promptFakeTree->Branch( "fakeWeight"      , &pfInfo.fakeWeight, "fakeWeight/F" );
    
    promptFakeTree->Branch( "diphoMass"        , &pfInfo.diphoMass        , "diphoMass/F"         );
    promptFakeTree->Branch( "diphoPt"        , &pfInfo.diphoPt        , "diphoPt/F"         );
    promptFakeTree->Branch( "diphoLeadingPt"   , &pfInfo.diphoLeadingPt   , "diphoLeadingPt/F"    );
    promptFakeTree->Branch( "diphoSubleadingPt", &pfInfo.diphoSubleadingPt, "diphoSubleadingPt/F" );
    
    promptFakeTree->Branch( "promptFakeDeltaR"      , &pfInfo.promptFakeDeltaR, "promptFakeDeltaR/F" );

    promptFakeTree->Branch( "promptPt"      , &pfInfo.promptPt    , "promptPt/F" );
    promptFakeTree->Branch( "promptEnergy"  , &pfInfo.promptEnergy, "promptEnergy/F" );
    promptFakeTree->Branch( "promptEta"     , &pfInfo.promptEta   , "promptEta/F" );
    promptFakeTree->Branch( "promptPhi"     , &pfInfo.promptPhi   , "promptPhi/F" );
    promptFakeTree->Branch( "promptPdgId"   , &pfInfo.promptPdgId , "promptPdgId/I" );
    promptFakeTree->Branch( "promptIDMVA"   , &pfInfo.promptIDMVA , "promptIDMVA/F" );
    promptFakeTree->Branch( "fakePt"      , &pfInfo.fakePt    , "fakePt/F" );
    promptFakeTree->Branch( "fakeEnergy"  , &pfInfo.fakeEnergy, "fakeEnergy/F" );
    promptFakeTree->Branch( "fakeEta"     , &pfInfo.fakeEta   , "fakeEta/F" );
    promptFakeTree->Branch( "fakePhi"     , &pfInfo.fakePhi   , "fakePhi/F" );
    promptFakeTree->Branch( "fakePdgId"   , &pfInfo.fakePdgId , "fakePdgId/I" );
    promptFakeTree->Branch( "fakeIDMVA"   , &pfInfo.fakeIDMVA , "fakeIDMVA/F" );

    promptFakeTree->Branch( "promptGenPhotonPt"      , &pfInfo.promptGenPhotonPt    , "promptGenPhotonPt/F" );
    promptFakeTree->Branch( "promptGenPhotonEnergy"  , &pfInfo.promptGenPhotonEnergy, "promptGenPhotonEnergy/F" );
    promptFakeTree->Branch( "promptTotalGenPhoEnergy"  , &pfInfo.promptTotalGenPhoEnergy, "promptTotalGenPhoEnergy/F" );
    promptFakeTree->Branch( "promptGenPhotonEta"     , &pfInfo.promptGenPhotonEta   , "promptGenPhotonEta/F" );
    promptFakeTree->Branch( "promptGenPhotonPhi"     , &pfInfo.promptGenPhotonPhi   , "promptGenPhotonPhi/F" );
    promptFakeTree->Branch( "promptGenPhotonDr"      , &pfInfo.promptGenPhotonDr     , "promptGenPhotonDr/F" );
    promptFakeTree->Branch( "promptNumGenPhotons"   , &pfInfo.promptNumGenPhotons, "promptNumGenPhotons/I" );
    promptFakeTree->Branch( "fakeGenPhotonPt"      , &pfInfo.fakeGenPhotonPt    , "fakeGenPhotonPt/F" );
    promptFakeTree->Branch( "fakeGenPhotonEnergy"  , &pfInfo.fakeGenPhotonEnergy, "fakeGenPhotonEnergy/F" );
    promptFakeTree->Branch( "fakeTotalGenPhoEnergy"  , &pfInfo.fakeTotalGenPhoEnergy, "fakeTotalGenPhoEnergy/F" );
    promptFakeTree->Branch( "fakeGenPhotonEta"     , &pfInfo.fakeGenPhotonEta   , "fakeGenPhotonEta/F" );
    promptFakeTree->Branch( "fakeGenPhotonPhi"     , &pfInfo.fakeGenPhotonPhi   , "fakeGenPhotonPhi/F" );
    promptFakeTree->Branch( "fakeGenPhotonDr"      , &pfInfo.fakeGenPhotonDr     , "fakeGenPhotonDr/F" );
    promptFakeTree->Branch( "fakeNumGenPhotons"   , &pfInfo.fakeNumGenPhotons, "fakeNumGenPhotons/I" );

    promptFakeTree->Branch( "promptGenJetPt"      , &pfInfo.promptGenJetPt    , "promptGenJetPt/F" );
    promptFakeTree->Branch( "promptGenJetEnergy"  , &pfInfo.promptGenJetEnergy, "promptGenJetEnergy/F" );
    promptFakeTree->Branch( "promptGenJetEta"     , &pfInfo.promptGenJetEta   , "promptGenJetEta/F" );
    promptFakeTree->Branch( "promptGenJetPhi"     , &pfInfo.promptGenJetPhi   , "promptGenJetPhi/F" );
    promptFakeTree->Branch( "promptGenJetDr"      , &pfInfo.promptGenJetDr     , "promptGenJetDr/F" );
    promptFakeTree->Branch( "promptNumGenJets"   , &pfInfo.promptNumGenJets, "promptNumGenJets/I" );
    promptFakeTree->Branch( "fakeGenJetPt"      , &pfInfo.fakeGenJetPt    , "fakeGenJetPt/F" );
    promptFakeTree->Branch( "fakeGenJetEnergy"  , &pfInfo.fakeGenJetEnergy, "fakeGenJetEnergy/F" );
    promptFakeTree->Branch( "fakeGenJetEta"     , &pfInfo.fakeGenJetEta   , "fakeGenJetEta/F" );
    promptFakeTree->Branch( "fakeGenJetPhi"     , &pfInfo.fakeGenJetPhi   , "fakeGenJetPhi/F" );
    promptFakeTree->Branch( "fakeGenJetDr"      , &pfInfo.fakeGenJetDr     , "fakeGenJetDr/F" );
    promptFakeTree->Branch( "fakeNumGenJets"   , &pfInfo.fakeNumGenJets, "fakeNumGenJets/I" );

    promptFakeTree->Branch( "promptRecoJetPt"      , &pfInfo.promptRecoJetPt    , "promptRecoJetPt/F" );
    promptFakeTree->Branch( "promptRecoJetEnergy"  , &pfInfo.promptRecoJetEnergy, "promptRecoJetEnergy/F" );
    promptFakeTree->Branch( "promptRecoJetEta"     , &pfInfo.promptRecoJetEta   , "promptRecoJetEta/F" );
    promptFakeTree->Branch( "promptRecoJetPhi"     , &pfInfo.promptRecoJetPhi   , "promptRecoJetPhi/F" );
    promptFakeTree->Branch( "promptRecoJetDr"      , &pfInfo.promptRecoJetDr     , "promptRecoJetDr/F" );
    promptFakeTree->Branch( "promptNumRecoJets"   , &pfInfo.promptNumRecoJets, "promptNumRecoJets/I" );
    promptFakeTree->Branch( "fakeRecoJetPt"      , &pfInfo.fakeRecoJetPt    , "fakeRecoJetPt/F" );
    promptFakeTree->Branch( "fakeRecoJetEnergy"  , &pfInfo.fakeRecoJetEnergy, "fakeRecoJetEnergy/F" );
    promptFakeTree->Branch( "fakeRecoJetEta"     , &pfInfo.fakeRecoJetEta   , "fakeRecoJetEta/F" );
    promptFakeTree->Branch( "fakeRecoJetPhi"     , &pfInfo.fakeRecoJetPhi   , "fakeRecoJetPhi/F" );
    promptFakeTree->Branch( "fakeRecoJetDr"      , &pfInfo.fakeRecoJetDr     , "fakeRecoJetDr/F" );
    promptFakeTree->Branch( "fakeNumRecoJets"   , &pfInfo.fakeNumRecoJets, "fakeNumRecoJets/I" );

    promptFakeTree->Branch( "promptPartonPt"      , &pfInfo.promptPartonPt    , "promptPartonPt/F" );
    promptFakeTree->Branch( "promptPartonEnergy"  , &pfInfo.promptPartonEnergy, "promptPartonEnergy/F" );
    promptFakeTree->Branch( "promptPartonEta"     , &pfInfo.promptPartonEta   , "promptPartonEta/F" );
    promptFakeTree->Branch( "promptPartonPhi"     , &pfInfo.promptPartonPhi   , "promptPartonPhi/F" );
    promptFakeTree->Branch( "promptPartonDr"      , &pfInfo.promptPartonDr     , "promptPartonDr/F" );
    promptFakeTree->Branch( "promptPartonMatchType"   , &pfInfo.promptPartonMatchType, "promptPartonMatchType/I" );
    promptFakeTree->Branch( "fakePartonPt"      , &pfInfo.fakePartonPt    , "fakePartonPt/F" );
    promptFakeTree->Branch( "fakePartonEnergy"  , &pfInfo.fakePartonEnergy, "fakePartonEnergy/F" );
    promptFakeTree->Branch( "fakePartonEta"     , &pfInfo.fakePartonEta   , "fakePartonEta/F" );
    promptFakeTree->Branch( "fakePartonPhi"     , &pfInfo.fakePartonPhi   , "fakePartonPhi/F" );
    promptFakeTree->Branch( "fakePartonDr"      , &pfInfo.fakePartonDr     , "fakePartonDr/F" );
    promptFakeTree->Branch( "fakePartonMatchType"   , &pfInfo.fakePartonMatchType, "fakePartonMatchType/I" );

    /*promptFakeTree->Branch( "sigmarv", &pfInfo.sigmarv, "sigmarv/F" );
    promptFakeTree->Branch( "sigmawv", &pfInfo.sigmawv, "sigmawv/F" );
    promptFakeTree->Branch( "CosPhi", &pfInfo.CosPhi, "CosPhi/F" );
    promptFakeTree->Branch( "vtxprob", &pfInfo.vtxprob, "vtxprob/F" );*/

    promptFakeTree->Branch( "dijet_leadEta", &pfInfo.dijet_leadEta, "dijet_leadEta/F" );
    promptFakeTree->Branch( "dijet_subleadEta", &pfInfo.dijet_subleadEta, "dijet_subleadEta/F" );
    promptFakeTree->Branch( "dijet_abs_dEta", &pfInfo.dijet_abs_dEta, "dijet_abs_dEta/F" );
    promptFakeTree->Branch( "dijet_LeadJPt", &pfInfo.dijet_LeadJPt, "dijet_LeadJPt/F" );
    promptFakeTree->Branch( "dijet_SubJPt", &pfInfo.dijet_SubJPt, "dijet_SubJPt/F" );
    promptFakeTree->Branch( "dijet_Zep", &pfInfo.dijet_Zep, "dijet_Zep/F" );
    promptFakeTree->Branch( "dijet_dphi_trunc", &pfInfo.dijet_dphi_trunc, "dijet_dphi_trunc/F" );
    promptFakeTree->Branch( "dijet_dipho_dphi", &pfInfo.dijet_dipho_dphi, "dijet_dipho_dphi/F" );
    promptFakeTree->Branch( "dijet_Mjj", &pfInfo.dijet_Mjj, "dijet_Mjj/F" );
    promptFakeTree->Branch( "dijet_dy", &pfInfo.dijet_dy, "dijet_dy/F" );
    promptFakeTree->Branch( "dijet_leady", &pfInfo.dijet_leady, "dijet_leady/F" );
    promptFakeTree->Branch( "dijet_subleady", &pfInfo.dijet_subleady, "dijet_subleady/F" );
    promptFakeTree->Branch( "dijet_dipho_pt", &pfInfo.dijet_dipho_pt, "dijet_dipho_pt/F" );
    promptFakeTree->Branch( "dijet_minDRJetPho", &pfInfo.dijet_minDRJetPho, "dijet_minDRJetPho/F" );
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
