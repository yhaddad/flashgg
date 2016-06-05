// Adapted from DiPhotonProducer by Ed Scott, 04/2016
// Takes in photons and gen jets and assigns E_pho / E_genJet and IDMVA,
// with weights according to templates from enriched prompt-fake events.
// Then instantiates them as "fake" photons and constructs diphoton candidates
// consisting of the prompt and each parametrised fake.
//
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/EDMException.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "flashgg/DataFormats/interface/DiPhotonCandidate.h"
#include "flashgg/MicroAOD/interface/PhotonIdUtils.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "flashgg/MicroAOD/interface/VertexSelectorBase.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "flashgg/DataFormats/interface/VertexCandidateMap.h"
#include "DataFormats/EgammaCandidates/interface/Conversion.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "DataFormats/Math/interface/deltaR.h"
//#include "TRandom3.h"
#include "FWCore/Utilities/interface/RandomNumberGenerator.h"
#include "CLHEP/Random/RandomEngine.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CLHEP/Random/RandFlat.h"

#include <map>

using namespace edm;
using namespace std;

namespace flashgg {

    class ParameterisedFakePhotonProducer : public EDProducer
    {

    public:
        ParameterisedFakePhotonProducer( const ParameterSet & );
    private:
        void produce( Event &, const EventSetup & ) override;
        EDGetTokenT<View<flashgg::Photon> > photonToken_;
        EDGetTokenT<View<reco::GenJet> > genJetToken_;

        // for parameterisation
        //TRandom3 *randomIDMVA;   
        //TRandom3 *randomEGAMEGEN;
        TH1F *hFakeGenJetRatio;
        TH1F *hBarrelLowTemplateIDMVA;
        //TH1F *hBarrelMedTemplateIDMVA;
        TH1F *hBarrelHighTemplateIDMVA;
        TH1F *hEndcapLowTemplateIDMVA;
        //TH1F *hEndcapMedTemplateIDMVA;
        TH1F *hEndcapHighTemplateIDMVA;
    };

    ParameterisedFakePhotonProducer::ParameterisedFakePhotonProducer( const ParameterSet &iConfig ) :
        photonToken_( consumes<View<flashgg::Photon> >( iConfig.getParameter<InputTag> ( "PhotonTag" ) ) ),
        //genJetToken_( consumes<View<reco::GenJet> >( iConfig.getUntrackedParameter<InputTag> ( "GenJetTag", InputTag( "slimmedGenJets" ) ) ) )
        genJetToken_( consumes<View<reco::GenJet> >( iConfig.getParameter<InputTag> ( "GenJetTag" ) ) )
    {
        produces<vector<flashgg::Photon> >();
        
        // random numbers for parameterisation
        //randomIDMVA    = new TRandom3(8157);
        //randomEGAMEGEN = new TRandom3(32935);

        // template histograms 
        //TFile *template_file = new TFile("file:/home/hep/es811/VBFStudies/CMSSW_7_6_3_patch2/src/flashgg/TemplateHists/templates.root");
        TFile *template_file = new TFile("file:/home/hep/es811/VBFStudies/CMSSW_7_6_3_patch2/src/flashgg/TemplateHists/templates_v1.root");

        hFakeGenJetRatio         = (TH1F*)template_file->Get("hFakeGenJetRatio");
        hBarrelLowTemplateIDMVA  = (TH1F*)template_file->Get("hBarrelLowTemplateIDMVA");
        //hBarrelMedTemplateIDMVA  = (TH1F*)template_file->Get("hBarrelMedTemplateIDMVA");
        hBarrelHighTemplateIDMVA = (TH1F*)template_file->Get("hBarrelHighTemplateIDMVA");
        hEndcapLowTemplateIDMVA  = (TH1F*)template_file->Get("hEndcapLowTemplateIDMVA");
        //hEndcapMedTemplateIDMVA  = (TH1F*)template_file->Get("hEndcapMedTemplateIDMVA");
        hEndcapHighTemplateIDMVA = (TH1F*)template_file->Get("hEndcapHighTemplateIDMVA");

        //delete template_file ?
        
        cout << "Inside constructor of the fakePhoton producer" << endl;
    }

    void ParameterisedFakePhotonProducer::produce( Event &evt, const EventSetup & )
    {
        // setup random number generator
        edm::Service<edm::RandomNumberGenerator> rng;
        if( ! rng.isAvailable() ) {
            throw cms::Exception( "Configuration" ) << "ParameterisedFakePhotonProducer requires the RandomNumberGeneratorService  - please add to configuration";
        }

        CLHEP::HepRandomEngine & engine = rng->getEngine( evt.streamID() );

        Handle<View<flashgg::Photon> > photons;
        evt.getByToken( photonToken_, photons );

        // Begin Prompt-Fake parameterisation----------------------------------------------------------------
        Handle<View<reco::GenJet> > genJets;
        auto_ptr<vector<flashgg::Photon> > fakePhotonCollection( new vector<flashgg::Photon> );
        evt.getByToken( genJetToken_, genJets );

        //cout << "size of photon collection is " << photons->size() << endl;

        // loop over photons, then loop over gen jets for each prompt photon
        for( uint photonIndex = 0; photonIndex < photons->size(); photonIndex++ ) {
            auto promptPhoton = photons->ptrAt( photonIndex );
            flashgg::Photon::mcMatch_t promptMatchType = promptPhoton->genMatchType();
            if( promptMatchType != 1 ) continue;
            float promptEta = promptPhoton->eta();
            float promptPhi = promptPhoton->phi();
            for( uint genJetIndex = 0; genJetIndex < genJets->size(); genJetIndex++ ) {
                auto fakeCandidate = genJets->ptrAt( genJetIndex );
                float fakeEta = fakeCandidate->eta();
                float fakePhi = fakeCandidate->phi();
                float promptFakeCandidateDeltaR = deltaR( promptEta, promptPhi, fakeEta, fakePhi );
                if( promptFakeCandidateDeltaR < 0.4 ) continue;
                flashgg::Photon fakePhoton = flashgg::Photon();

                // now do assignment and reweighting
                // formula for BinNum is 1 + (x-x_min)/binwidth
                // numbers currently hard-coded, should probably change
                float fakeWeight = 1.;
                //cout << "fakeWeight at step one = " << fakeWeight << endl;
                //float fakeGenJetEnergyRatio = randomEGAMEGEN->Uniform( 0., 1.2 );
                float fakeGenJetEnergyRatio = CLHEP::RandFlat::shoot( &engine, 0., 1.2 );
                //cout << "fakeGenJetEnergyRatio = " << fakeGenJetEnergyRatio << endl;
                int fakeRatioBinNum = floor( fakeGenJetEnergyRatio / 0.025  ) + 1;
                fakeWeight *= hFakeGenJetRatio->GetBinContent( fakeRatioBinNum ) / hFakeGenJetRatio->Integral("width");
                //cout << "fakeWeight at step two = " << fakeWeight << endl;

                //float fakeIDMVA = randomIDMVA->Uniform( -0.9, 1.0 );
                float fakeIDMVA = CLHEP::RandFlat::shoot( &engine, -0.9, 1.0 );
                //cout << "fakeIDMVA = " << fakeIDMVA << endl;
                fakePhoton.setFakeIDMVA( fakeIDMVA );
                fakePhoton.setHasFakeIDMVA( true );
                int fakeIDMVABinNum = floor( (fakeIDMVA + 1.) / 0.1 ) + 1;
                if( abs( fakeEta ) < 1.5 ) {
                    //if( fakeGenJetEnergyRatio < 0.4 )      fakeWeight *= hBarrelLowTemplateIDMVA->GetBinContent(  fakeIDMVABinNum ) / hBarrelLowTemplateIDMVA->Integral("width");
                    //else if( fakeGenJetEnergyRatio < 0.8 ) fakeWeight *= hBarrelMedTemplateIDMVA->GetBinContent(  fakeIDMVABinNum ) / hBarrelMedTemplateIDMVA->Integral("width");
                    if( fakeGenJetEnergyRatio < 0.8 )      fakeWeight *= hBarrelLowTemplateIDMVA->GetBinContent(  fakeIDMVABinNum ) / hBarrelLowTemplateIDMVA->Integral("width");
                    else if( fakeGenJetEnergyRatio < 1.2 ) fakeWeight *= hBarrelHighTemplateIDMVA->GetBinContent( fakeIDMVABinNum ) / hBarrelHighTemplateIDMVA->Integral("width");
                }
                else if( abs( fakeEta ) < 2.5 ) {
                    //if( fakeGenJetEnergyRatio < 0.4 )      fakeWeight *= hEndcapLowTemplateIDMVA->GetBinContent(  fakeIDMVABinNum ) / hEndcapLowTemplateIDMVA->Integral("width");
                    //else if( fakeGenJetEnergyRatio < 0.8 ) fakeWeight *= hEndcapMedTemplateIDMVA->GetBinContent(  fakeIDMVABinNum ) / hEndcapMedTemplateIDMVA->Integral("width");
                    if( fakeGenJetEnergyRatio < 0.8 )      fakeWeight *= hEndcapLowTemplateIDMVA->GetBinContent(  fakeIDMVABinNum ) / hEndcapLowTemplateIDMVA->Integral("width");
                    else if( fakeGenJetEnergyRatio < 1.2 ) fakeWeight *= hEndcapHighTemplateIDMVA->GetBinContent( fakeIDMVABinNum ) / hEndcapHighTemplateIDMVA->Integral("width");
                }
                else { fakeWeight = 0.; }
                //cout << "fakeWeight at step tre = " << fakeWeight << endl;
                //cout << "absolute value fakeEta = " << abs(fakeEta) << endl << endl;
                fakePhoton.setWeight( "fakeWeight", fakeWeight );
 
                float fakeEnergy = fakeGenJetEnergyRatio * fakeCandidate->energy();
                //cout << "fakeEnergy = "  << fakeEnergy << endl;
                float fakePt = fakeEnergy * sin( 2 * atan( exp( -fakeEta ) ) );
                //cout << "fakePt = "  << fakePt << endl;
                reco::Candidate::PolarLorentzVector fakeLV;
                fakeLV.SetEta( fakeEta );
                fakeLV.SetPhi( fakePhi );
                fakeLV.SetPt(  fakePt  );
                fakeLV.SetM( 0. );
                fakePhoton.setP4( fakeLV );

                fakePhoton.setPassElectronVeto( true );
                fakePhoton.setpfPhoIso03( 0. );

                fakePhotonCollection->push_back( fakePhoton );
            }
        }

        evt.put( fakePhotonCollection );
        // End Prompt-Fake parameterisation------------------------------------------------------------------

    }
}

typedef flashgg::ParameterisedFakePhotonProducer FlashggParameterisedFakePhotonProducer;
DEFINE_FWK_MODULE( FlashggParameterisedFakePhotonProducer );
// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

