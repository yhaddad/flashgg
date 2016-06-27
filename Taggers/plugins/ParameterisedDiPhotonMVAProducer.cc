#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/EDMException.h"

#include "flashgg/DataFormats/interface/DiPhotonCandidate.h"
#include "flashgg/DataFormats/interface/DiPhotonMVAResult.h"

#include "flashgg/DataFormats/interface/SinglePhotonView.h"

#include "TMVA/Reader.h"
#include "TMath.h"
#include "TVector3.h"
#include "TLorentzVector.h"

#include "FWCore/Utilities/interface/RandomNumberGenerator.h"
#include "CLHEP/Random/RandomEngine.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CLHEP/Random/RandFlat.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

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

using namespace std;
using namespace edm;

namespace flashgg {

    class ParameterisedDiPhotonMVAProducer : public EDProducer
    {

    public:
        ParameterisedDiPhotonMVAProducer( const ParameterSet & );
    private:
        void produce( Event &, const EventSetup & ) override;

        EDGetTokenT<View<DiPhotonCandidate> > diPhotonToken_;
        EDGetTokenT<reco::BeamSpot > beamSpotToken_;
        EDGetTokenT<View<reco::GenJet> > genJetToken_;
        double BeamSig_fromConf_=-1.;

        unique_ptr<TMVA::Reader>DiphotonMva_;
        FileInPath diphotonMVAweightfile_;

        float sigmarv_;
        float sigmawv_;
        float vtxprob_;
        float leadptom_;
        float subleadptom_;
        float leadeta_;
        float subleadeta_;
        float CosPhi_;
        float leadmva_;
        float subleadmva_;
        
        float mass_;
        
        //float nConv_;
        float vtxProbMVA_;
        vector<double> vertex_prob_params_conv;
        vector<double> vertex_prob_params_noConv;

        std::string Version_;
        
        TH1F* hSigmarvChecksLowEB;
        TH1F* hSigmarvChecksHighEB;
        TH1F* hSigmarvChecksLowEE;
        TH1F* hSigmarvChecksHighEE;
    };

    ParameterisedDiPhotonMVAProducer::ParameterisedDiPhotonMVAProducer( const ParameterSet &iConfig ) :
        diPhotonToken_( consumes<View<flashgg::DiPhotonCandidate> >( iConfig.getParameter<InputTag> ( "DiPhotonTag" ) ) ),
        beamSpotToken_( consumes<reco::BeamSpot >( iConfig.getParameter<InputTag>( "BeamSpotTag" ) ) ),
        genJetToken_( consumes<View<reco::GenJet> >( iConfig.getParameter<InputTag> ( "GenJetTag" ) ) )
    {
        TFile *template_file = new TFile("file:/home/hep/es811/VBFStudies/CMSSW_7_6_3_patch2/src/flashgg/TemplateHists/templates_v2.root");

        hSigmarvChecksLowEB  = (TH1F*)template_file->Get("hSigmarvChecksLowEB");
        hSigmarvChecksHighEB = (TH1F*)template_file->Get("hSigmarvChecksHighEB");
        hSigmarvChecksLowEE  = (TH1F*)template_file->Get("hSigmarvChecksLowEE");
        hSigmarvChecksHighEE = (TH1F*)template_file->Get("hSigmarvChecksHighEE");

        vertex_prob_params_conv = iConfig.getParameter<vector<double>>( "VertexProbParamsConv" );
        vertex_prob_params_noConv = iConfig.getParameter<vector<double>>( "VertexProbParamsNoConv" );
        BeamSig_fromConf_ = iConfig.getParameter<double>( "BeamSpotSigma" );
        diphotonMVAweightfile_ = iConfig.getParameter<edm::FileInPath>( "diphotonMVAweightfile" );

        Version_ = iConfig.getParameter<string>( "Version" );

        //        std::cout << "Version" << Version_ << std::endl;

        sigmarv_ = 0.;
        sigmawv_ = 0.;
        vtxprob_ = 0.;
        leadptom_ = 0.;
        subleadptom_ = 0.;
        leadeta_ = 0.;
        subleadeta_ = 0.;
        CosPhi_ = 0.;
        leadmva_ = 0.;
        subleadmva_ = 0.;
        
        mass_=0;                

        std::string version_old = "old";
        std::string version_new = "new";

        if( version_old.compare( Version_ ) == 0 ) {
            DiphotonMva_.reset( new TMVA::Reader( "!Color:Silent" ) );
            DiphotonMva_->AddVariable( "masserrsmeared/mass", &sigmarv_ );
            DiphotonMva_->AddVariable( "masserrsmearedwrongvtx/mass", &sigmawv_ );
            DiphotonMva_->AddVariable( "vtxprob", &vtxprob_ );
            DiphotonMva_->AddVariable( "ph1.pt/mass", &leadptom_ );
            DiphotonMva_->AddVariable( "ph2.pt/mass", &subleadptom_ );
            DiphotonMva_->AddVariable( "ph1.eta", &leadeta_ );
            DiphotonMva_->AddVariable( "ph2.eta", &subleadeta_ );
            DiphotonMva_->AddVariable( "TMath::Cos(ph1.phi-ph2.phi)", &CosPhi_ );
            DiphotonMva_->AddVariable( "ph1.idmva", &leadmva_ );
            DiphotonMva_->AddVariable( "ph2.idmva", &subleadmva_ );
            DiphotonMva_->BookMVA( "BDT", diphotonMVAweightfile_.fullPath() );
            //            std::cout << "finished reading mva" << std::endl;
        }

        if( version_new.compare( Version_ ) == 0 ) {
            //            std::cout << "Reading MVA variables " << std::endl;
            DiphotonMva_.reset( new TMVA::Reader( "!Color:Silent" ) );
            DiphotonMva_->AddVariable( "leadptom", &leadptom_ );
            DiphotonMva_->AddVariable( "subleadptom", &subleadptom_ );
            DiphotonMva_->AddVariable( "leadmva", &leadmva_ );
            DiphotonMva_->AddVariable( "subleadmva", &subleadmva_ );
            DiphotonMva_->AddVariable( "leadeta", &leadeta_ );
            DiphotonMva_->AddVariable( "subleadeta", &subleadeta_ );
            DiphotonMva_->AddVariable( "sigmarv", &sigmarv_ );
            DiphotonMva_->AddVariable( "sigmawv", &sigmawv_ );
            DiphotonMva_->AddVariable( "CosPhi", &CosPhi_ );
            DiphotonMva_->AddVariable( "vtxprob", &vtxprob_ );

            //            DiphotonMva_->AddSpectator("Signal_wei", &weightSig_       );
            //            DiphotonMva_->AddSpectator("Background_wei", &weightBkg_           );            
            DiphotonMva_->BookMVA( "BDT", diphotonMVAweightfile_.fullPath() );
            //            std::cout << "finished reading mva" << std::endl;
        }
        produces<vector<DiPhotonMVAResult> >(); // one per diphoton, always in same order, vector is more efficient than map

        cout << "Inside constructor of parameterised diphoton MVA producer" << endl;
    }

    void ParameterisedDiPhotonMVAProducer::produce( Event &evt, const EventSetup & )
    {
        // setup random number generator
        edm::Service<edm::RandomNumberGenerator> rng;
        if( ! rng.isAvailable() ) {
            throw cms::Exception( "Configuration" ) << "ParameterisedFakePhotonProducer requires the RandomNumberGeneratorService  - please add to configuration";
        }

        CLHEP::HepRandomEngine & engine = rng->getEngine( evt.streamID() );

        Handle<View<flashgg::DiPhotonCandidate> > diPhotons;
        evt.getByToken( diPhotonToken_, diPhotons );
        // const PtrVector<flashgg::DiPhotonCandidate>& diPhotonPointers = diPhotons->ptrVector();

        Handle<reco::BeamSpot> recoBeamSpotHandle;
        evt.getByToken( beamSpotToken_, recoBeamSpotHandle );
        float beamsig;
        if(BeamSig_fromConf_ < 0){
            if( recoBeamSpotHandle.isValid() ) {
                beamsig = recoBeamSpotHandle->sigmaZ();
            } else {
                beamsig = -9999; // I hope this never happens! But it seems to in our default test, what's going wrong??
            }
        }
        else{
            beamsig = BeamSig_fromConf_;
        }


        //    std::auto_ptr<DiPhotonMVAResultMap> assoc(new DiPhotonMVAResultMap);
        std::auto_ptr<vector<DiPhotonMVAResult> > results( new vector<DiPhotonMVAResult> ); // one per diphoton, always in same order, vector is more efficient than map

        for( unsigned int candIndex = 0; candIndex < diPhotons->size() ; candIndex++ ) {
            flashgg::DiPhotonMVAResult mvares;
            edm::Ptr<reco::Vertex> vtx = diPhotons->ptrAt( candIndex )->vtx();

            const flashgg::Photon *g1 = diPhotons->ptrAt( candIndex )->leadingPhoton();
            const flashgg::Photon *g2 = diPhotons->ptrAt( candIndex )->subLeadingPhoton();

            //used for photon resolution wrt to correct vertex//
            TVector3 Photon1Dir;
            TVector3 Photon1Dir_uv;
            TVector3 Photon2Dir;
            TVector3 Photon2Dir_uv;
            TLorentzVector p14;
            TLorentzVector p24;

            // old version 
            /*Photon1Dir.SetXYZ( g1->superCluster()->position().x() - vtx->position().x(), g1->superCluster()->position().y() - vtx->position().y(),
                               g1->superCluster()->position().z() - vtx->position().z() );
            Photon2Dir.SetXYZ( g2->superCluster()->position().x() - vtx->position().x(), g2->superCluster()->position().y() - vtx->position().y(),
                               g2->superCluster()->position().z() - vtx->position().z() );
            Photon1Dir_uv = Photon1Dir.Unit() * g1->superCluster()->rawEnergy();
            Photon2Dir_uv = Photon2Dir.Unit() * g2->superCluster()->rawEnergy();
            p14.SetPxPyPzE( Photon1Dir_uv.x(), Photon1Dir_uv.y(), Photon1Dir_uv.z(), g1->superCluster()->rawEnergy() );
            p24.SetPxPyPzE( Photon2Dir_uv.x(), Photon2Dir_uv.y(), Photon2Dir_uv.z(), g2->superCluster()->rawEnergy() );
            //photon 4-vector with respect to correct vertex and superCluster hit// */
            
            // new version - no superclusters. No such thing as x, y, z for a photon - hmmmmm 
            // does px, py, pz work instead? I think so... 
            Photon1Dir.SetXYZ( g1->px() - vtx->position().x(), g1->py() - vtx->position().y(),
                               g1->pz() - vtx->position().z() );
            Photon2Dir.SetXYZ( g2->px() - vtx->position().x(), g2->py() - vtx->position().y(),
                               g2->pz() - vtx->position().z() );
            Photon1Dir_uv = Photon1Dir.Unit() * g1->energy();
            Photon2Dir_uv = Photon2Dir.Unit() * g2->energy();
            p14.SetPxPyPzE( Photon1Dir_uv.x(), Photon1Dir_uv.y(), Photon1Dir_uv.z(), g1->energy() );
            p24.SetPxPyPzE( Photon2Dir_uv.x(), Photon2Dir_uv.y(), Photon2Dir_uv.z(), g2->energy() );

            //

            //float angle = p14.Angle(p24.Vect());

            /*float x1 = g1->superCluster()->position().x() - vtx->position().x();
            float y1 = g1->superCluster()->position().y() - vtx->position().y();
            float z1 = g1->superCluster()->position().z() - vtx->position().z();

            float x2 = g2->superCluster()->position().x() - vtx->position().x();
            float y2 = g2->superCluster()->position().y() - vtx->position().y();
            float z2 = g2->superCluster()->position().z() - vtx->position().z();*/

            float x1 = g1->px() - vtx->position().x();
            //cout << "g1 px = " << g1->px() << endl;
            //cout << "vtx x = " << vtx->position().x() << endl;
            float y1 = g1->py() - vtx->position().y();
            //cout << "g1 py = " << g1->py() << endl;
            //cout << "vty y = " << vtx->position().y() << endl;
            float z1 = g1->pz() - vtx->position().z();
            //cout << "g1 pz = " << g1->pz() << endl;
            //cout << "vtz z = " << vtx->position().z() << endl;

            float x2 = g2->px() - vtx->position().x();
            float y2 = g2->py() - vtx->position().y();
            float z2 = g2->pz() - vtx->position().z();

            float r1 = TMath::Sqrt( x1 * x1 + y1 * y1 + z1 * z1 );
            float r2 = TMath::Sqrt( x2 * x2 + y2 * y2 + z2 * z2 );

            float cos_term = TMath::Cos( p14.Phi() - p24.Phi() );

            float sech1 = 1.0 / TMath::CosH( p14.Eta() );
            float sech2 = 1.0 / TMath::CosH( p24.Eta() );
            float tanh1 = TMath::TanH( p14.Eta() );
            float tanh2 = TMath::TanH( p24.Eta() );

            float numerator1 = sech1 * ( sech1 * tanh2 - tanh1 * sech2 * cos_term );
            float numerator2 = sech2 * ( sech2 * tanh1 - tanh2 * sech1 * cos_term );
            float denominator = 1. - tanh1 * tanh2 - sech1 * sech2 * cos_term;
            float angleResolutionWrgVtx = ( ( -1.*beamsig * TMath::Sqrt( 2. ) ) / denominator ) * ( numerator1 / r1 + numerator2 / r2 ); //dz = sigmabeamspot*sqrt(2)
            float alpha_sig_wrg = 0.5 * angleResolutionWrgVtx;
            //float alpha_sig_corr = angleResolutionCorrVtx;
            //float SigmaM = 0.5 * TMath::Sqrt( g1->sigEOverE() * g1->sigEOverE() + g2->sigEOverE() * g2->sigEOverE() );
            //float MassResolutionWrongVtx = TMath::Sqrt( ( SigmaM * SigmaM ) + ( alpha_sig_wrg * alpha_sig_wrg ) );
            
            const flashgg::Photon *fakePhoton   = g1;
            //const flashgg::Photon *promptPhoton = g2;
            if( g2->hasFakeIDMVA() )  {
                fakePhoton   = g2;
                //promptPhoton = g1;
            }
            else if( ! g1->hasFakeIDMVA() ) cout << "WARNING - NO FAKE PHOTON. SOMETHING DEFINITELY WRONG" << endl;
            float fakeEta = fakePhoton->eta();
            float fakePhi = fakePhoton->phi();
            // need to read in genJets and match to fake again - bit of a faff...
            Handle<View<reco::GenJet> > genJets;
            evt.getByToken( genJetToken_, genJets );
            float minDr = 10.;
            int fakeGenJetIndex = -1;
            for( uint genJetIndex = 0; genJetIndex < genJets->size(); genJetIndex++ ) {
                float tempEta = genJets->ptrAt( genJetIndex )->eta();
                float tempPhi = genJets->ptrAt( genJetIndex )->phi();
                float tempDeltaR = deltaR( tempEta, tempPhi, fakeEta, fakePhi );
                if( tempDeltaR < minDr ) {
                    minDr = tempDeltaR;
                    fakeGenJetIndex = genJetIndex;
                }
            }
            //cout << "minDr = " << minDr << endl;
            float fakeGenJetRatio = fakePhoton->energy() / genJets->ptrAt( fakeGenJetIndex )->energy();
            //cout << "fakeGenJetRatio = " << fakeGenJetRatio << endl;
            //cout << "fakeEta = " << fakeEta << endl;

            bool done = false;
            float max = 0; 
            if(      abs( fakeEta ) < 1.5 && fakeGenJetRatio < 0.8 ) max = hSigmarvChecksLowEB->GetMaximum();
            else if( abs( fakeEta ) < 1.5 && fakeGenJetRatio < 1.2 ) max = hSigmarvChecksHighEB->GetMaximum();
            else if( abs( fakeEta ) < 2.5 && fakeGenJetRatio < 0.8 ) max = hSigmarvChecksLowEE->GetMaximum();
            else if( abs( fakeEta ) < 2.5 && fakeGenJetRatio < 1.2 ) max = hSigmarvChecksHighEE->GetMaximum();
            //cout << "max = " << max << endl;
            float sigmarv = 0;
            //cout << "going into while loop" << endl;
            while( !done ) {
                sigmarv  = CLHEP::RandFlat::shoot( &engine, 0., 0.05 ); // to be parameterised
                //cout << "sigmarv = " << sigmarv << endl;
                int binNum = floor( sigmarv / 0.0025 ) + 1;
                //cout << "binNum = " << binNum << endl;
                float tempRand = CLHEP::RandFlat::shoot( &engine, 0., max );
                //cout << "tempRand = " << tempRand << endl;
                float tempHistVal = 0;

                if(      abs( fakeEta ) < 1.5 && fakeGenJetRatio < 0.8 ) tempHistVal = hSigmarvChecksLowEB->GetBinContent( binNum );
                else if( abs( fakeEta ) < 1.5 && fakeGenJetRatio < 1.2 ) tempHistVal = hSigmarvChecksHighEB->GetBinContent( binNum );
                else if( abs( fakeEta ) < 2.5 && fakeGenJetRatio < 0.8 ) tempHistVal = hSigmarvChecksLowEE->GetBinContent( binNum );
                else if( abs( fakeEta ) < 2.5 && fakeGenJetRatio < 1.2 ) tempHistVal = hSigmarvChecksHighEE->GetBinContent( binNum );
                else {
                    cout << "ERROR OF SORTS - EITHER ETA OR RATIO NO IN VALID RANGE" << endl;
                    cout << "fakeEta = " << fakeEta << endl;
                    cout << "fakeGenJetRatio = " << fakeGenJetRatio << endl;
                    cout << "minDr = " << minDr << endl;
                    tempHistVal = 1000000.;
                }

                //cout << "tempHistVal = " << tempHistVal << endl;
                if( tempRand < tempHistVal ) done = true; 
            }
            //cout << "end of while loop" << endl;
            float MassResolutionWrongVtx = TMath::Sqrt( ( sigmarv * sigmarv ) + ( alpha_sig_wrg * alpha_sig_wrg ) );
            if( abs(fakeEta) > 2.5 ) cout << MassResolutionWrongVtx << endl;


            leadptom_       = g1->pt() / ( diPhotons->ptrAt( candIndex )->mass() );
            subleadptom_    = g2->pt() / ( diPhotons->ptrAt( candIndex )->mass() );

            leadmva_        = g1->phoIdMvaDWrtVtx( vtx );
            subleadmva_     = g2->phoIdMvaDWrtVtx( vtx );

            leadeta_        = g1->eta();
            subleadeta_     = g2->eta();

            //sigmarv_        = .5 * sqrt( ( g1->sigEOverE() ) * ( g1->sigEOverE() ) + ( g2->sigEOverE() ) * ( g2->sigEOverE() ) );
            sigmarv_        = sigmarv;
            //sigmawv_        = MassResolutionWrongVtx;
            //sigmawv_        = sigmarv + 0.01;
            sigmawv_        = 1.36*sigmarv;
            CosPhi_         = TMath::Cos( deltaPhi( g1->phi(), g2->phi() ) );

            //vtxProbMVA_ = diPhotons->ptrAt( candIndex )->vtxProbMVA();
            //vtxProbMVA_ = 0.999;
            //vtxProbMVA_ = 0.99;
            vtxProbMVA_ = 0.96;
            vtxprob_ = vtxProbMVA_;
            //nConv_ = diPhotons->ptrAt( candIndex )->nConv();
            //nConv_ = promptPhoton->hasConversionTracks();

            /*if( nConv_ > 0 ) {
                vtxprob_        = ( 1 + vertex_prob_params_conv.at( 0 ) - vertex_prob_params_conv.at( 1 ) + vertex_prob_params_conv.at( 2 ) - vertex_prob_params_conv.at(
                                        3 ) ) + vertex_prob_params_conv.at( 0 ) * vtxProbMVA_ + vertex_prob_params_conv.at( 1 ) * pow( vtxProbMVA_,
                                                2 ) + vertex_prob_params_conv.at( 2 ) * pow( vtxProbMVA_, 3 ) + vertex_prob_params_conv.at( 3 ) * pow( vtxProbMVA_, 4 );
            }

            else {
                vtxprob_        = ( 1 + vertex_prob_params_noConv.at( 0 ) - vertex_prob_params_noConv.at( 1 ) + vertex_prob_params_noConv.at(
                                        2 ) - vertex_prob_params_noConv.at( 3 ) ) + vertex_prob_params_noConv.at( 0 ) * vtxProbMVA_ + vertex_prob_params_noConv.at( 1 ) * pow( vtxProbMVA_,
                                                2 ) + vertex_prob_params_noConv.at( 2 ) * pow( vtxProbMVA_, 3 ) + vertex_prob_params_noConv.at( 3 ) * pow( vtxProbMVA_, 4 );
            }*/

            mvares.result = DiphotonMva_->EvaluateMVA( "BDT" );

            mvares.leadptom = leadptom_;
            mvares.subleadptom = subleadptom_;
            mvares.leadmva = leadmva_;
            mvares.subleadmva = subleadmva_;
            mvares.leadeta = leadeta_;
            mvares.subleadeta = subleadeta_;
            mvares.sigmarv = sigmarv_;
            //cout << "sigmarv = " << sigmarv_ << endl;
            mvares.sigmawv = sigmawv_;
            //cout << "sigmawv = " << sigmawv_ << endl;
            mvares.CosPhi = CosPhi_;
            mvares.vtxprob = vtxprob_;

            results->push_back( mvares );
        }
        evt.put( results );
    }
}

typedef flashgg::ParameterisedDiPhotonMVAProducer FlashggParameterisedDiPhotonMVAProducer;
DEFINE_FWK_MODULE( FlashggParameterisedDiPhotonMVAProducer );
// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

