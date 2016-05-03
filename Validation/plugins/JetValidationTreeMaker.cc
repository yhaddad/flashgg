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


#include "TTree.h"
#include "TH1.h"
#include "TH2.h"
#include "TMatrix.h"
#include "TVector.h"
#include "TLorentzVector.h"

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

    edm::InputTag 					qgVariablesInputTag;
    //edm::EDGetTokenT<edm::ValueMap<float>> 		qgToken;

    typedef std::vector<edm::Handle<edm::View<flashgg::Jet> > > JetCollectionVector;


    TTree     *eventTree;
    TTree     *jetTree;
    TTree     *genPartTree;
    TTree     *genJetTree;

    // initial plots // Ed
    TH1F      *hPromptFakeDeltaR;
    TH1F      *hPromptGenJetRatio; 
    TH1F      *hFakeGenJetRatio; 
    TH1F      *hPromptNumGenPhotons;
    TH1F      *hFakeNumGenPhotons;
    TH1F      *hPromptFakeDeltaRNoIso;
    TH1F      *hPromptGenJetRatioNoIso;
    TH1F      *hFakeGenJetRatioNoIso;
    TH1F      *hPromptNumGenPhotonsNoIso; 
    TH1F      *hFakeNumGenPhotonsNoIso; 
    // matrix element parton plots
    TH1F      *hPromptNearestPartonDeltaR;
    TH1F      *hFakeNearestPartonDeltaR;
    TH1F      *hPromptNearestPartonDeltaRNoIso;
    TH1F      *hFakeNearestPartonDeltaRNoIso;
    TH1F      *hPromptPartonRatio;
    TH1F      *hFakePartonRatio;
    TH1F      *hPromptPartonRatioNoIso;
    TH1F      *hFakePartonRatioNoIso;
    TH1F      *hPromptPartonMatching;
    TH1F      *hFakePartonMatching;
    TH1F      *hPromptPartonMatchingNoIso;
    TH1F      *hFakePartonMatchingNoIso;
    TH1F      *hPartonPdgId;
    TH1F      *hPartonPdgIdNoIso;
    // parton match only plots
    TH1F      *hIfMatchPromptGenJetDeltaR;
    TH1F      *hIfMatchPartonGenJetDeltaR;
    // 2D plots
    TH2F      *hFakeNumRatio;
    TH2F      *hFakeNumRatioNoIso; // Ed
    TH2F      *hPrPaDrRatio; // Ed
    TH2F      *hPrPaDrRatioNoIso; // Ed

    int  prompt_fake_count; // Ed
    int  promptIsoCount; // Ed

    eventInfo   eInfo;
    jetInfo     jInfo;
    GenPartInfo genInfo;
    GenJetInfo  genJetInfo;
    Int_t       event_number;
    std::string jetCollectionName;

    GenPartInfo jGenPhotonInfo;

    bool        usePUJetID;
    bool        photonJetVeto;
    bool        homeGenJetMatching_;
    bool        ZeroVertexOnly_;
    bool        debug_;
    bool        useVBFTagPhotonMatching_;

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

    //qgVariablesInputTag( iConfig.getParameter<edm::InputTag>( "qgVariablesInputTag" ) ),

    usePUJetID( iConfig.getUntrackedParameter<bool>( "UsePUJetID"   , false ) ),
    photonJetVeto( iConfig.getUntrackedParameter<bool>( "PhotonJetVeto", true ) ),
    homeGenJetMatching_( iConfig.getUntrackedParameter<bool>( "homeGenJetMatching", false ) ),
    ZeroVertexOnly_( iConfig.getUntrackedParameter<bool>( "ZeroVertexOnly", false ) ),
    debug_( iConfig.getUntrackedParameter<bool>( "debug", false ) ),
    useVBFTagPhotonMatching_( iConfig.getUntrackedParameter<bool>( "useVBFTagPhotonMatching", false ) )

{
    for( uint i = 0; i < inputTagJets_.size(); i++ ) {
        auto token = consumes<View<flashgg::Jet> >(inputTagJets_[i]);
        tokenJets_.push_back(token); 
    }

    event_number = 0;
    prompt_fake_count = 0; // Ed
    promptIsoCount = 0; // Ed
    jetCollectionName = iConfig.getParameter<string>( "StringTag" );
    //qgToken	= consumes<edm::ValueMap<float>>( edm::InputTag( qgVariablesInputTag.label(), "qgLikelihood" ) );

}

JetValidationTreeMaker::~JetValidationTreeMaker()
{
    event_number = 0;
}


void
JetValidationTreeMaker::analyze( const edm::Event &iEvent, const edm::EventSetup &iSetup )
{

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
        genInfo.pt     = gens->ptrAt( genLoop )->pt() ;
        genInfo.eta    = gens->ptrAt( genLoop )->eta();
        genInfo.phi    = gens->ptrAt( genLoop )->phi();
        genInfo.status = gens->ptrAt( genLoop )->status();
        genInfo.pdgid  = int( gens->ptrAt( genLoop )->pdgId() );

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
        genPartTree->Fill();
    }
    // find tag the jets close to the photons
    std::map<unsigned int, GenPhotonInfo> photonJet_id;
    std::map<unsigned int, bool>             _isPhoton;

    size_t diPhotonsSize = diPhotons->size();
    if( ZeroVertexOnly_ ) { diPhotonsSize = 1; }
 
    for( unsigned int diphoIndex = 0; diphoIndex < diPhotonsSize; diphoIndex++ ) {
        unsigned int jetCollectionIndex = 0;
        if( !ZeroVertexOnly_ ) { jetCollectionIndex = diPhotons->ptrAt( diphoIndex )->jetCollectionIndex(); }

        //--------------------------------------------------------------------------------------------------
        // Begin analysis of prompt-fake events // Ed
        
        auto printDipho = diPhotons->ptrAt(0);
        // select only diphoton candidate with highest IDMVA score
        if( diPhotonsSize > 1 ) {
            float max_phoIDMVA_sum = -3.0;
            for( uint secondDiphoIndex = 0; secondDiphoIndex < diPhotonsSize; secondDiphoIndex++ ) {
                float temp_phoIDMVA_sum =  diPhotons->ptrAt( secondDiphoIndex )->leadPhotonId() + diPhotons->ptrAt( secondDiphoIndex )->subLeadPhotonId();
                if( temp_phoIDMVA_sum > max_phoIDMVA_sum ) {
                    printDipho = diPhotons->ptrAt( secondDiphoIndex );
                    max_phoIDMVA_sum = temp_phoIDMVA_sum;
                }
            }
        }
        if( printDipho->mass() < 100 || printDipho->mass() > 180 ) continue;
        auto printLeadPho    = printDipho->leadingPhoton();
        auto printSubLeadPho = printDipho->subLeadingPhoton();
        flashgg::Photon::mcMatch_t leadMatchType    = printLeadPho->genMatchType();
        flashgg::Photon::mcMatch_t subleadMatchType = printSubLeadPho->genMatchType();
        bool prompt_fake = ( (!(leadMatchType==1 && subleadMatchType==1)) && (leadMatchType==1 || subleadMatchType==1) );
        auto promptPhoton   = printLeadPho;
        int photonsInPrompt = 0;
        auto fakePhoton     = printSubLeadPho;
        int photonsInFake   = 0;
        auto promptGenJet = genJets->ptrAt(0);
        auto fakeGenJet   = genJets->ptrAt(1);
        bool reversed     = false;
        bool promptIso    = false;
        auto promptNearestParton   = gens->ptrAt(0);
        int  promptPartonMatchType = 0;
        auto fakeNearestParton     = gens->ptrAt(1);
        int  fakePartonMatchType   = 0;
        int  partonPdgId0 = -999;
        int  partonPdgId1 = -999;

        if( prompt_fake ) {
            prompt_fake_count++;
            if( leadMatchType != 1 ) {
                promptPhoton = printSubLeadPho;
                fakePhoton   = printLeadPho;
                reversed     = true;
            }
            // check if promptPhoton is "isolated" and count matching genPhotons
            if( genPhotons->size() > 0 ) {
                for( uint genPhotonIndex = 0; genPhotonIndex < genPhotons->size(); genPhotonIndex++ ) {
                    bool nearLeadPhoton    = false;
                    bool nearSubLeadPhoton = false;
                    float genPhotonEta     = genPhotons->ptrAt( genPhotonIndex )->eta();
                    float genPhotonPhi     = genPhotons->ptrAt( genPhotonIndex )->phi();
                    float drGenPhoLead     = sqrt( (genPhotonEta-printLeadPho->eta())*(genPhotonEta-printLeadPho->eta()) 
                                                 + (genPhotonPhi-printLeadPho->phi())*(genPhotonPhi-printLeadPho->phi()) );
                    float drGenPhoSubLead  = sqrt( (genPhotonEta-printSubLeadPho->eta())*(genPhotonEta-printSubLeadPho->eta()) 
                                                 + (genPhotonPhi-printSubLeadPho->phi())*(genPhotonPhi-printSubLeadPho->phi()) );
                    if( drGenPhoLead    < 0.4 ) nearLeadPhoton    = true;
                    if( drGenPhoSubLead < 0.4 ) nearSubLeadPhoton = true;
                    if( nearLeadPhoton && !nearSubLeadPhoton ) {
                        if(     !reversed && (abs(printLeadPho->energy() - genPhotons->ptrAt( genPhotonIndex )->energy()) / genPhotons->ptrAt( genPhotonIndex )->energy() < 0.1) ) { 
                            promptIso    = true; 
                            photonsInPrompt++;
                        }
                        else if( !reversed ) { 
                            photonsInPrompt++;
                        }
                        else if( reversed ) { 
                            photonsInFake++;
                        }
                    }
                    else if ( !nearLeadPhoton && nearSubLeadPhoton ) {
                        if(      reversed && (abs(printSubLeadPho->energy() - genPhotons->ptrAt( genPhotonIndex )->energy()) / genPhotons->ptrAt( genPhotonIndex )->energy() < 0.1) ) { 
                            promptIso = true;
                            photonsInPrompt++;
                        }
                        else if( reversed ) { 
                            photonsInPrompt++;
                        }
                        else if( !reversed ) { 
                            photonsInFake++;
                        }
                    }
                }
            } // end of iso checking and genPhoton counting

            // only print for "unusual" events
            cout << "------------------------------------------------------------------- " << endl;
            cout << "NEW EVENT" << endl;
            cout << "-------------------------------------------------------------------" << endl << endl;
            if( !promptIso ) {
                cout << "number of diphotons = " << diPhotonsSize << endl << endl;
                cout << "leadMatchType    = " << leadMatchType << endl;
                cout << "lead IDMVA       = " << printDipho->leadPhotonId() << endl;
                cout << "lead pt          = " << printLeadPho->pt() << endl;
                cout << "lead energy      = " << printLeadPho->energy() << endl;
                cout << "lead eta         = " << printLeadPho->eta() << endl;
                cout << "lead phi         = " << printLeadPho->phi() << endl << endl;
                cout << "subleadMatchType = " << subleadMatchType << endl;
                cout << "sublead IDMVA    = " << printDipho->subLeadPhotonId() << endl;
                cout << "sublead pt       = " << printSubLeadPho->pt() << endl;
                cout << "sublead energy   = " << printSubLeadPho->energy() << endl;
                cout << "sublead eta      = " << printSubLeadPho->eta() << endl;
                cout << "sublead phi      = " << printSubLeadPho->phi() << endl << endl;
                cout << "photon deltaR    = " << sqrt( (printLeadPho->phi()-printSubLeadPho->phi())*(printLeadPho->phi()-printSubLeadPho->phi())
                                                     + (printLeadPho->eta()-printSubLeadPho->eta())*(printLeadPho->eta()-printSubLeadPho->eta()) ) << endl;
                cout << "photon deltaPhi  = " << printLeadPho->phi()-printSubLeadPho->phi() << endl << endl << endl;

                // print out gen photon info
                if( genPhotons->size() > 0 ) {
                    for( uint genPhotonIndex = 0; genPhotonIndex < genPhotons->size(); genPhotonIndex++ ) {
                        bool nearLeadPhoton    = false;
                        bool nearSubLeadPhoton = false;
                        float genPhotonEta = genPhotons->ptrAt( genPhotonIndex )->eta();
                        float genPhotonPhi = genPhotons->ptrAt( genPhotonIndex )->phi();
                        float drGenPhoLead    = sqrt( (genPhotonEta-printLeadPho->eta())*(genPhotonEta-printLeadPho->eta()) 
                                                    + (genPhotonPhi-printLeadPho->phi())*(genPhotonPhi-printLeadPho->phi()) );
                        float drGenPhoSubLead = sqrt( (genPhotonEta-printSubLeadPho->eta())*(genPhotonEta-printSubLeadPho->eta()) 
                                                    + (genPhotonPhi-printSubLeadPho->phi())*(genPhotonPhi-printSubLeadPho->phi()) );
                        if( drGenPhoLead    < 0.4 ) nearLeadPhoton    = true;
                        if( drGenPhoSubLead < 0.4 ) nearSubLeadPhoton = true;
                        if( !nearLeadPhoton && !nearSubLeadPhoton ) {
                            cout << "gen photon " << genPhotonIndex << " is near neither photon" << endl << endl;
                        }
                        else if ( nearLeadPhoton && !nearSubLeadPhoton ) {
                            cout << "gen photon " << genPhotonIndex << " is near leading photon" << endl;
                            cout << "gen photon " << genPhotonIndex << " pt     = " << genPhotons->ptrAt( genPhotonIndex )->pt() << endl;
                            cout << "gen photon " << genPhotonIndex << " energy = " << genPhotons->ptrAt( genPhotonIndex )->energy() << endl;
                            cout << "gen photon " << genPhotonIndex << " eta    = " << genPhotons->ptrAt( genPhotonIndex )->eta() << endl;
                            cout << "gen photon " << genPhotonIndex << " phi    = " << genPhotons->ptrAt( genPhotonIndex )->phi() << endl;
                            cout << "gen photon " << genPhotonIndex << " deltaR = " << drGenPhoLead << endl << endl;
                        }
                        else if ( !nearLeadPhoton && nearSubLeadPhoton ) {
                            cout << "gen photon " << genPhotonIndex << " is near subleading photon" << endl;
                            cout << "gen photon " << genPhotonIndex << " pt     = " << genPhotons->ptrAt( genPhotonIndex )->pt() << endl;
                            cout << "gen photon " << genPhotonIndex << " energy = " << genPhotons->ptrAt( genPhotonIndex )->energy() << endl;
                            cout << "gen photon " << genPhotonIndex << " eta    = " << genPhotons->ptrAt( genPhotonIndex )->eta() << endl;
                            cout << "gen photon " << genPhotonIndex << " phi    = " << genPhotons->ptrAt( genPhotonIndex )->phi() << endl;
                            cout << "gen photon " << genPhotonIndex << " deltaR = " << drGenPhoSubLead << endl << endl;
                        }
                        else {
                            cout << "gen photon " << genPhotonIndex << " is near both photons!!!" << endl << endl;
                        }
                    }
                } // end of gen photon info
                cout << "" << endl;
            }

            // Print out gen jet info
            if( genJets->size() > 0 ) {
                for( uint genJetIndex = 0; genJetIndex < genJets->size(); genJetIndex++ ) {
                    bool nearLeadPhoton    = false;
                    bool nearSubLeadPhoton = false;
                    float genJetEta = genJets->ptrAt( genJetIndex )->eta();
                    float genJetPhi = genJets->ptrAt( genJetIndex )->phi();
                    float drGenLead    = sqrt( (genJetEta-printLeadPho->eta())*(genJetEta-printLeadPho->eta()) + (genJetPhi-printLeadPho->phi())*(genJetPhi-printLeadPho->phi()) );
                    float drGenSubLead = sqrt( (genJetEta-printSubLeadPho->eta())*(genJetEta-printSubLeadPho->eta()) + (genJetPhi-printSubLeadPho->phi())*(genJetPhi-printSubLeadPho->phi()) );
                    if( drGenLead    < 0.4 ) nearLeadPhoton    = true;
                    if( drGenSubLead < 0.4 ) nearSubLeadPhoton = true;
                    if( !nearLeadPhoton && !nearSubLeadPhoton && !promptIso ) {
                        cout << "Gen Jet " << genJetIndex << " is near neither photon" << endl << endl;
                    }
                    else if ( nearLeadPhoton && !nearSubLeadPhoton ) {
                        if( !promptIso ) {
                            cout << "Gen Jet " << genJetIndex << " is near leading photon" << endl;
                            cout << "Gen Jet " << genJetIndex << " pt     = " << genJets->ptrAt( genJetIndex )->pt() << endl;
                            cout << "Gen Jet " << genJetIndex << " energy = " << genJets->ptrAt( genJetIndex )->energy() << endl;
                            cout << "Gen Jet " << genJetIndex << " eta    = " << genJetEta << endl;
                            cout << "Gen Jet " << genJetIndex << " phi    = " << genJetPhi << endl;
                            cout << "Gen Jet " << genJetIndex << " deltaR = " << drGenLead << endl;
                            cout << "Gen Jet " << genJetIndex << " has      " << genJets->ptrAt(genJetIndex)->numberOfDaughters() << " daughters" << endl << endl;
                        }
                        if(     !reversed ) { 
                            promptGenJet = genJets->ptrAt( genJetIndex );
                        }
                        else if( reversed ) { 
                            fakeGenJet   = genJets->ptrAt( genJetIndex );
                        }
                    }
                    else if ( !nearLeadPhoton && nearSubLeadPhoton ) {
                        if( !promptIso ) {
                            cout << "Gen Jet " << genJetIndex << " is near subleading photon" << endl;
                            cout << "Gen Jet " << genJetIndex << " pt     = " << genJets->ptrAt( genJetIndex )->pt() << endl;
                            cout << "Gen Jet " << genJetIndex << " energy = " << genJets->ptrAt( genJetIndex )->energy() << endl;
                            cout << "Gen Jet " << genJetIndex << " eta    = " << genJetEta << endl;
                            cout << "Gen Jet " << genJetIndex << " phi    = " << genJetPhi << endl;
                            cout << "Gen Jet " << genJetIndex << " deltaR = " << drGenSubLead << endl;
                            cout << "Gen Jet " << genJetIndex << " has      " << genJets->ptrAt(genJetIndex)->numberOfDaughters() << " daughters" << endl << endl;
                        }
                        if(       reversed ) { 
                            promptGenJet = genJets->ptrAt( genJetIndex );
                        }
                        else if( !reversed ) { 
                            fakeGenJet   = genJets->ptrAt( genJetIndex );
                        }
                    }
                    else if( !promptIso ) {
                        cout << "Gen Jet " << genJetIndex << " is near both photons!!!" << endl << endl;
                    }
                    /*if( !promptIso ) {
                        for( uint genDaughterIndex = 0; genDaughterIndex < genJets->ptrAt( genJetIndex )->numberOfDaughters(); genDaughterIndex++ ) {
                            cout << "daughter " << genDaughterIndex << " has pdgID, energy = "
                                 << genJets->ptrAt( genJetIndex )->daughter( genDaughterIndex )->pdgId() << ", " 
                                 << genJets->ptrAt( genJetIndex )->daughter( genDaughterIndex )->energy() << endl;
                        }
                        cout << "" << endl << endl;
                    }*/
                }
            } // end of gen jet info

            // print out the reco jet info
            if( !promptIso ) {
                auto recoJets = Jets[jetCollectionIndex];
                if( recoJets->size() > 0 ) {
                    for( unsigned int recoJetIndex = 0; recoJetIndex < recoJets->size(); recoJetIndex++ ) {
                        /*float recoJetEta = recoJets->ptrAt( recoJetIndex )->eta();
                        float recoJetPhi = recoJets->ptrAt( recoJetIndex )->phi();
                        cout << "Reco Jet " << recoJetIndex << " pt     = " << recoJets->ptrAt( recoJetIndex )->pt() << endl;
                        cout << "Reco Jet " << recoJetIndex << " energy = " << recoJets->ptrAt( recoJetIndex )->energy() << endl;
                        cout << "Reco Jet " << recoJetIndex << " eta    = " << recoJetEta << endl;
                        cout << "Reco Jet " << recoJetIndex << " phi    = " << recoJetPhi << endl << endl;*/

                        bool nearLeadPhoton    = false;
                        bool nearSubLeadPhoton = false;
                        float recoJetEta = recoJets->ptrAt( recoJetIndex )->eta();
                        float recoJetPhi = recoJets->ptrAt( recoJetIndex )->phi();
                        float drRecoLead    = sqrt( (recoJetEta-printLeadPho->eta())*(recoJetEta-printLeadPho->eta()) + (recoJetPhi-printLeadPho->phi())*(recoJetPhi-printLeadPho->phi()) );
                        float drRecoSubLead = sqrt( (recoJetEta-printSubLeadPho->eta())*(recoJetEta-printSubLeadPho->eta()) + (recoJetPhi-printSubLeadPho->phi())*(recoJetPhi-printSubLeadPho->phi()) );
                        if( drRecoLead    < 0.4 ) nearLeadPhoton    = true;
                        if( drRecoSubLead < 0.4 ) nearSubLeadPhoton = true;
                        if( !nearLeadPhoton && !nearSubLeadPhoton ) {
                            cout << "Reco Jet " << recoJetIndex << " is near neither photon" << endl << endl;
                        }
                        else if ( nearLeadPhoton && !nearSubLeadPhoton ) {
                            cout << "Reco Jet " << recoJetIndex << " is near leading photon" << endl;
                            cout << "Reco Jet " << recoJetIndex << " pt     = " << recoJets->ptrAt( recoJetIndex )->pt() << endl;
                            cout << "Reco Jet " << recoJetIndex << " energy = " << recoJets->ptrAt( recoJetIndex )->energy() << endl;
                            cout << "Reco Jet " << recoJetIndex << " eta    = " << recoJetEta << endl;
                            cout << "Reco Jet " << recoJetIndex << " phi    = " << recoJetPhi << endl;
                            cout << "Reco Jet " << recoJetIndex << " deltaR = " << drRecoLead << endl << endl;
                        }
                        else if ( !nearLeadPhoton && nearSubLeadPhoton ) {
                            cout << "Reco Jet " << recoJetIndex << " is near subleading photon" << endl;
                            cout << "Reco Jet " << recoJetIndex << " pt     = " << recoJets->ptrAt( recoJetIndex )->pt() << endl;
                            cout << "Reco Jet " << recoJetIndex << " energy = " << recoJets->ptrAt( recoJetIndex )->energy() << endl;
                            cout << "Reco Jet " << recoJetIndex << " eta    = " << recoJetEta << endl;
                            cout << "Reco Jet " << recoJetIndex << " phi    = " << recoJetPhi << endl;
                            cout << "Reco Jet " << recoJetIndex << " deltaR = " << drRecoSubLead << endl << endl;
                        }
                        else {
                            cout << "Reco Jet " << recoJetIndex << " is near both photons !!!" << endl << endl;
                        }
                    }
                } // end of reco jet info
            }

            // loop over partons from matrix element
            if( gens->size() > 0 ) {
                cout << "number of partons = " << gens->size() << endl << endl;
                float mindrPromptPho = 10.;
                float mindrFakePho   = 10.;
                for( uint genParticleIndex = 0; genParticleIndex < gens->size(); genParticleIndex++ ) {
                    bool nearPromptPho    = false;
                    bool nearFakePho      = false;
                    bool nearPromptGenJet = false;
                    bool nearFakeGenJet   = false;
                    auto gen              = gens->ptrAt( genParticleIndex );
                    string pdg_type       = "";
                    if( gen->pdgId() == 21 )                    pdg_type = "gluon";
                    if( gen->pdgId() < 7 && gen->pdgId() > -7 ) pdg_type = "quark";
                    if ( genParticleIndex == 0 ) partonPdgId0 = gen->pdgId();
                    if ( genParticleIndex == 1 ) partonPdgId1 = gen->pdgId();

                    float drPromptPho               = sqrt( (gen->eta()-promptPhoton->eta())*(gen->eta()-promptPhoton->eta()) + 
                                                      (gen->phi()-promptPhoton->phi())*(gen->phi()-promptPhoton->phi()) );
                    if( drPromptPho < mindrPromptPho ) {
                        mindrPromptPho        = drPromptPho;
                        promptNearestParton   = gen;
                        if( mindrPromptPho < 0.4 ) {
                            nearPromptPho     = true;
                            if( pdg_type == "quark" ) promptPartonMatchType = 1;
                            if( pdg_type == "gluon" ) promptPartonMatchType = 2;
                        }
                    }

                    float drFakePho               = sqrt( (gen->eta()-fakePhoton->eta())*(gen->eta()-fakePhoton->eta()) + 
                                                    (gen->phi()-fakePhoton->phi())*(gen->phi()-fakePhoton->phi()) );
                    if( drFakePho < mindrFakePho ) {
                        mindrFakePho        = drFakePho;
                        fakeNearestParton   = gen;
                        if( mindrFakePho < 0.4 ) {
                            nearFakePho     = true;
                            if( pdg_type == "quark" ) fakePartonMatchType = 1;
                            if( pdg_type == "gluon" ) fakePartonMatchType = 2;
                        }
                    }

                    float drPromptGenJet = sqrt( (gen->eta()-promptGenJet->eta())*(gen->eta()-promptGenJet->eta()) + 
                                                 (gen->phi()-promptGenJet->phi())*(gen->phi()-promptGenJet->phi()) );
                    if( drPromptGenJet < 0.4 ) {
                        nearPromptGenJet = true;
                    }
                    float drFakeGenJet = sqrt( (gen->eta()-fakeGenJet->eta())*(gen->eta()-fakeGenJet->eta()) + 
                                               (gen->phi()-fakeGenJet->phi())*(gen->phi()-fakeGenJet->phi()) );
                    if( drFakeGenJet < 0.4 ) {
                        nearFakeGenJet = true;
                    }
                    if( nearPromptPho && nearPromptGenJet ) {
                        cout << "a gen "+pdg_type+" matches both the promptPhoton and its genJet" << endl;
                        cout << "energies of parton , photon are " << gen->energy() << " , " << promptPhoton->energy() << endl;
                        cout << "pts of parton , photon are      " << gen->pt() << " , " << promptPhoton->pt() << endl;
                        cout << "etas of parton , photon are     " << gen->eta() << " , " << promptPhoton->eta() << endl;
                        cout << "phis of parton , photon are     " << gen->phi() << " , " << promptPhoton->phi() << endl << endl;
                        cout << "drPromptPho          = " << drPromptPho << endl;
                        cout << "drPromptGenJet       = " << drPromptGenJet << endl;
                        float drPromptPhoItsGenJet = sqrt( (promptPhoton->eta()-promptGenJet->eta())*(promptPhoton->eta()-promptGenJet->eta()) + 
                                                           (promptPhoton->phi()-promptGenJet->phi())*(promptPhoton->phi()-promptGenJet->phi()) );
                        cout << "drPromptPhoItsGenJet = " << drPromptPhoItsGenJet << endl << endl;
                    }
                    else if( nearFakePho && nearFakeGenJet ) {
                        cout << "a gen "+pdg_type+" matches both the fakePhoton and its genJet" << endl;
                        cout << "energies of parton , photon are " << gen->energy() << " , " << fakePhoton->energy() << endl;
                        cout << "pts of parton , photon are      " << gen->pt() << " , " << fakePhoton->pt() << endl;
                        cout << "etas of parton , photon are     " << gen->eta() << " , " << fakePhoton->eta() << endl;
                        cout << "phis of parton , photon are     " << gen->phi() << " , " << fakePhoton->phi() << endl << endl;
                    }
                    else { 
                        cout << "this parton does not have a perfect match... " << endl << endl;
                    }
                }
                cout << "" << endl;
            }

            float promptEta          = promptPhoton->eta();
            float promptPhi          = promptPhoton->phi();
            float promptPartonEta    = promptNearestParton->eta();
            float promptPartonPhi    = promptNearestParton->phi();
            float promptGenJetEta    = promptGenJet->eta();
            float promptGenJetPhi    = promptGenJet->phi();
            float fakeEta            = fakePhoton->eta();
            float fakePhi            = fakePhoton->phi();
            float fakePartonEta      = fakeNearestParton->eta();
            float fakePartonPhi      = fakeNearestParton->phi();
            float drPromptFake       = sqrt( (promptEta-fakeEta)*(promptEta-fakeEta) + (promptPhi-fakePhi)*(promptPhi-fakePhi) );
            float drPromptParton     = sqrt( (promptEta-promptPartonEta)*(promptEta-promptPartonEta) + (promptPhi-promptPartonPhi)*(promptPhi-promptPartonPhi) );
            float drPromptGenJet     = sqrt( (promptEta-promptGenJetEta)*(promptEta-promptGenJetEta) + (promptPhi-promptGenJetPhi)*(promptPhi-promptGenJetPhi) );
            float drPartonGenJet     = sqrt( (promptGenJetEta-promptPartonEta)*(promptGenJetEta-promptPartonEta) + (promptGenJetPhi-promptPartonPhi)*(promptGenJetPhi-promptPartonPhi) );
            float drFakeParton       = sqrt( (fakeEta-fakePartonEta)*(fakeEta-fakePartonEta) + (fakePhi-fakePartonPhi)*(fakePhi-fakePartonPhi) );
            float promptPhotonEnergy = promptPhoton->energy();
            float promptGenJetEnergy = promptGenJet->energy();
            float promptPartonEnergy = promptNearestParton->energy();
            float fakePhotonEnergy   = fakePhoton->energy();
            float fakeGenJetEnergy   = fakeGenJet->energy();
            float fakePartonEnergy   = fakeNearestParton->energy();
            if( promptIso ) {
                promptIsoCount++;
                /*cout << "EVENT HAD ISOLATED PROMPT PHOTON" << endl;
                cout << "with energy    = " << promptPhoton->energy() << endl;
                cout << "gen jet energy = " << promptGenJet->energy() << endl;
                cout << "fake energy    = " << fakePhoton->energy() << endl;
                cout << "gen jet energy = " << fakeGenJet->energy() << endl;*/
                hPromptFakeDeltaR->Fill( drPromptFake );
                hPromptGenJetRatio->Fill( promptPhotonEnergy / promptGenJetEnergy );
                hFakeGenJetRatio->Fill( fakePhotonEnergy / fakeGenJetEnergy );
                hPromptNumGenPhotons->Fill( photonsInPrompt );
                hFakeNumGenPhotons->Fill( photonsInFake );
                hPromptPartonMatching->Fill( promptPartonMatchType );
                hFakePartonMatching->Fill( fakePartonMatchType );
                hPromptNearestPartonDeltaR->Fill( drPromptParton );
                hFakeNearestPartonDeltaR->Fill( drFakeParton );
                if( promptPartonMatchType != 0) hPromptPartonRatio->Fill( promptPhotonEnergy / promptPartonEnergy );
                if( fakePartonMatchType   != 0) hFakePartonRatio->Fill( fakePhotonEnergy / fakePartonEnergy );
                hPartonPdgId->Fill( partonPdgId0 );
                hPartonPdgId->Fill( partonPdgId1 );
                hFakeNumRatio->Fill( photonsInFake, fakePhotonEnergy / fakeGenJetEnergy );
                hPrPaDrRatio->Fill( drPromptParton, promptPhotonEnergy / promptPartonEnergy );
                if( promptPartonMatchType != 0) hIfMatchPartonGenJetDeltaR->Fill( drPartonGenJet );
                if( promptPartonMatchType != 0) hIfMatchPromptGenJetDeltaR->Fill( drPromptGenJet );
            }
            else {
                cout << "EVENT DID NOT HAVE ISOLATED PROMPT PHOTON" << endl << endl << endl << endl;
                hPromptFakeDeltaRNoIso->Fill( drPromptFake );
                hPromptGenJetRatioNoIso->Fill( promptPhotonEnergy / promptGenJetEnergy );
                hFakeGenJetRatioNoIso->Fill( fakePhotonEnergy / fakeGenJetEnergy );
                hPromptNumGenPhotonsNoIso->Fill( photonsInPrompt );
                hFakeNumGenPhotonsNoIso->Fill( photonsInFake );
                hPromptPartonMatchingNoIso->Fill( promptPartonMatchType );
                hFakePartonMatchingNoIso->Fill( fakePartonMatchType );
                hPromptNearestPartonDeltaRNoIso->Fill( drPromptParton );
                hFakeNearestPartonDeltaRNoIso->Fill( drFakeParton );
                if( promptPartonMatchType != 0) hPromptPartonRatioNoIso->Fill( promptPhotonEnergy / promptPartonEnergy );
                if( fakePartonMatchType   != 0) hFakePartonRatioNoIso->Fill( fakePhotonEnergy / fakePartonEnergy );
                hPartonPdgIdNoIso->Fill( partonPdgId0 );
                hPartonPdgIdNoIso->Fill( partonPdgId1 );
                hFakeNumRatioNoIso->Fill( photonsInFake, fakePhotonEnergy / fakeGenJetEnergy );
                hPrPaDrRatioNoIso->Fill( drPromptParton, promptPhotonEnergy / promptPartonEnergy );
            }

        } // End printouts of prompt-fake events */ // Ed
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

    genPartTree = fs_->make<TTree>( "genPartTree", "Check per-jet tree" );
    genPartTree->Branch( "pt"     , &genInfo.pt      , "pt/F" );
    genPartTree->Branch( "eta"    , &genInfo.eta     , "eta/F" );
    genPartTree->Branch( "phi"    , &genInfo.phi     , "phi/F" );
    genPartTree->Branch( "status" , &genInfo.status  , "status/I" );
    genPartTree->Branch( "pdgid"  , &genInfo.pdgid   , "pdgid/I" );
    genPartTree->Branch( "y"      , &genInfo.y       , "y/F" );

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

    // First set of plots
    hPromptFakeDeltaR = fs_->make<TH1F>("hPromptFakeDeltaR","DeltaR between Prompt and Fake photons",60,0.,6.); // Ed
    hPromptFakeDeltaR->GetXaxis()->SetTitle("#DeltaR");

    hPromptGenJetRatio = fs_->make<TH1F>("hPromptGenJetRatio","promptPhoton energy / genJet energy",60,0.,1.2);
    hPromptGenJetRatio->GetXaxis()->SetTitle("E_{#gamma} / E_{genJet}");

    hFakeGenJetRatio = fs_->make<TH1F>("hFakeGenJetRatio","fakePhoton energy / genJet energy",60,0.,1.2);
    hFakeGenJetRatio->GetXaxis()->SetTitle("E_{#gamma} / E_{genJet}");

    hPromptNumGenPhotons = fs_->make<TH1F>("hPromptNumGenPhotons","number of genPhotons matching promptPhoton",9,-0.5,8.5);
    hPromptNumGenPhotons->GetXaxis()->SetTitle("n_{#gamma}");

    hFakeNumGenPhotons = fs_->make<TH1F>("hFakeNumGenPhotons","number of genPhotons matching fakePhoton",9,-0.5,8.5);
    hFakeNumGenPhotons->GetXaxis()->SetTitle("n_{#gamma}");

    hPromptFakeDeltaRNoIso = fs_->make<TH1F>("hPromptFakeDeltaRNoIso","DeltaR between Prompt and Fake photons",60,0.,6.);
    hPromptFakeDeltaRNoIso->GetXaxis()->SetTitle("deltaR");

    hPromptGenJetRatioNoIso = fs_->make<TH1F>("hPromptGenJetRatioNoIso","promptPhoton energy / genJet energy",60,0.,1.2);
    hPromptGenJetRatioNoIso->GetXaxis()->SetTitle("E_{#gamma} / E_{genJet}");

    hFakeGenJetRatioNoIso = fs_->make<TH1F>("hFakeGenJetRatioNoIso","fakePhoton energy / genJet energy",60,0.,1.2);
    hFakeGenJetRatioNoIso->GetXaxis()->SetTitle("E_{#gamma} / E_{genJet}");

    hPromptNumGenPhotonsNoIso = fs_->make<TH1F>("hPromptNumGenPhotonsNoIso","number of genPhotons matching promptPhoton",9,-0.5,8.5);
    hPromptNumGenPhotonsNoIso->GetXaxis()->SetTitle("n_{#gamma}");

    hFakeNumGenPhotonsNoIso = fs_->make<TH1F>("hFakeNumGenPhotonsNoIso","number of genPhotons matching fakePhoton",9,-0.5,8.5);
    hFakeNumGenPhotonsNoIso->GetXaxis()->SetTitle("n_{#gamma}");

    // Matrix element parton plots
    hPromptNearestPartonDeltaR = fs_->make<TH1F>("hPromptNearestPartonDeltaR","DeltaR between promptPhoton and nearest parton",60,0.,6.); 
    hPromptNearestPartonDeltaR->GetXaxis()->SetTitle("#DeltaR");

    hFakeNearestPartonDeltaR = fs_->make<TH1F>("hFakeNearestPartonDeltaR","DeltaR between fakePhoton and nearest parton",60,0.,6.); 
    hFakeNearestPartonDeltaR->GetXaxis()->SetTitle("#DeltaR");

    hPromptNearestPartonDeltaRNoIso = fs_->make<TH1F>("hPromptNearestPartonDeltaRNoIso","DeltaR between promptPhoton and nearest parton",60,0.,6.); 
    hPromptNearestPartonDeltaRNoIso->GetXaxis()->SetTitle("#DeltaR");

    hFakeNearestPartonDeltaRNoIso = fs_->make<TH1F>("hFakeNearestPartonDeltaRNoIso","DeltaR between fakePhoton and nearest parton",60,0.,6.); 
    hFakeNearestPartonDeltaRNoIso->GetXaxis()->SetTitle("#DeltaR");

    hPromptPartonRatio = fs_->make<TH1F>("hPromptPartonRatio","Energy promptPhoton / energy matching parton",75,0.,1.5); 
    hPromptPartonRatio->GetXaxis()->SetTitle("E_{#gamma} / E_{parton}");

    hFakePartonRatio = fs_->make<TH1F>("hFakePartonRatio","Energy fakePhoton / energy matching parton",75,0.,1.5); 
    hFakePartonRatio->GetXaxis()->SetTitle("E_{#gamma} / E_{parton}");

    hPromptPartonRatioNoIso = fs_->make<TH1F>("hPromptPartonRatioNoIso","Energy promptPhoton / energy matching parton",75,0.,1.5); 
    hPromptPartonRatioNoIso->GetXaxis()->SetTitle("E_{#gamma} / E_{parton}");

    hFakePartonRatioNoIso = fs_->make<TH1F>("hFakePartonRatioNoIso","Energy fakePhoton / energy matching parton",75,0.,1.5); 
    hFakePartonRatioNoIso->GetXaxis()->SetTitle("E_{#gamma} / E_{parton}");

    hPromptPartonMatching = fs_->make<TH1F>("hPromptPartonMatching","Whether matching is none, quark or gluon",3,-0.5,2.5); 
    hPromptPartonMatching->GetXaxis()->SetTitle("Match Type");

    hFakePartonMatching = fs_->make<TH1F>("hFakePartonMatching","Whether matching is none, quark or gluon",3,-0.5,2.5); 
    hFakePartonMatching->GetXaxis()->SetTitle("Match Type");

    hPromptPartonMatchingNoIso = fs_->make<TH1F>("hPromptPartonMatchingNoIso","Whether matching is none, quark or gluon",3,-0.5,2.5); 
    hPromptPartonMatchingNoIso->GetXaxis()->SetTitle("Match Type");

    hFakePartonMatchingNoIso = fs_->make<TH1F>("hFakePartonMatchingNoIso","Whether matching is none, quark or gluon",3,-0.5,2.5); 
    hFakePartonMatchingNoIso->GetXaxis()->SetTitle("Match Type");

    hPartonPdgId = fs_->make<TH1F>("hPartonPdgId","Pdg of parton",30,-5.5,24.5);
    hPartonPdgId->GetXaxis()->SetTitle("PdgId");

    hPartonPdgIdNoIso = fs_->make<TH1F>("hPartonPdgIdNoIso","Pdg of parton",30,-5.5,24.5);
    hPartonPdgIdNoIso->GetXaxis()->SetTitle("PdgId");

    // plots only if parton matches
    hIfMatchPromptGenJetDeltaR = fs_->make<TH1F>("hIfMatchPromptGenJetDeltaR","DeltaR between Prompt and genJet (parton match only)",60,0.,6.);
    hIfMatchPromptGenJetDeltaR->GetXaxis()->SetTitle("deltaR");

    hIfMatchPartonGenJetDeltaR = fs_->make<TH1F>("hIfMatchPartonGenJetDeltaR","DeltaR between parton and genJet (parton match only)",60,0.,6.);
    hIfMatchPartonGenJetDeltaR->GetXaxis()->SetTitle("deltaR");

    // 2D plots
    hFakeNumRatio = fs_->make<TH2F>("hFakeNumRatio","Number of genPhotons matching fakePhoton vs fakePhoton energy / fake genJet energy",10,-0.5,9.5,12,0.,1.2);
    hFakeNumRatio->GetXaxis()->SetTitle("n_{gen#gamma}");
    hFakeNumRatio->GetYaxis()->SetTitle("E_{reco#gamma} / E_{genJet}");

    hFakeNumRatioNoIso = fs_->make<TH2F>("hFakeNumRatioNoIso","Number of genPhotons matching fakePhoton vs fakePhoton energy / fake genJet energy",10,-0.5,9.5,12,0.,1.2);
    hFakeNumRatioNoIso->GetXaxis()->SetTitle("n_{gen#gamma}");
    hFakeNumRatioNoIso->GetYaxis()->SetTitle("E_{reco#gamma} / E_{genJet}"); // Ed

    hPrPaDrRatio = fs_->make<TH2F>("hPrPaDrRatio","#DeltaR(Parton,Prompt) vs prompt energy / parton energy",24,0.,6.,12,0.,1.2);
    hPrPaDrRatio->GetXaxis()->SetTitle("#DeltaR");
    hPrPaDrRatio->GetYaxis()->SetTitle("E_{#gamma} / E_{parton}");

    hPrPaDrRatioNoIso = fs_->make<TH2F>("hPrPaDrRatioNoIso","#DeltaR(Parton,Prompt) vs prompt energy / parton energy",24,0.,6.,12,0.,1.2);
    hPrPaDrRatioNoIso->GetXaxis()->SetTitle("#DeltaR");
    hPrPaDrRatioNoIso->GetYaxis()->SetTitle("E_{#gamma} / E_{parton}");

}

void JetValidationTreeMaker::endJob()
{
    /*cout << "" << endl << endl << endl; // Ed
    cout << "promptIsoCount  = " << promptIsoCount << endl; 
    cout << "promptFakeCount = " << prompt_fake_count << endl << endl << endl << endl;*/ // Ed
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
