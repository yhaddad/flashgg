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

#include <map>

using namespace edm;
using namespace std;

namespace flashgg {

    class ParameterisedPromptFakeDiPhotonProducer : public EDProducer
    {

    public:
        ParameterisedPromptFakeDiPhotonProducer( const ParameterSet & );
    private:
        void produce( Event &, const EventSetup & ) override;
        EDGetTokenT<View<reco::Vertex> > vertexToken_;
        EDGetTokenT<View<flashgg::Photon> > promptPhotonToken_; // Ed
        EDGetTokenT<View<flashgg::Photon> > fakePhotonToken_; // Ed
        EDGetTokenT<View<reco::GenParticle> >      genPartToken_;
    };

    ParameterisedPromptFakeDiPhotonProducer::ParameterisedPromptFakeDiPhotonProducer( const ParameterSet &iConfig ) :
        vertexToken_( consumes<View<reco::Vertex> >( iConfig.getParameter<InputTag> ( "VertexTag" ) ) ),
        promptPhotonToken_( consumes<View<flashgg::Photon> >( iConfig.getParameter<InputTag> ( "PromptPhotonTag" ) ) ), // Ed
        fakePhotonToken_( consumes<View<flashgg::Photon> >( iConfig.getParameter<InputTag> ( "FakePhotonTag" ) ) ), // Ed
        genPartToken_( consumes<View<reco::GenParticle> >( iConfig.getParameter<InputTag> ( "GenParticleTag" ) ) )
    {
        produces<vector<flashgg::DiPhotonCandidate> >();
        cout << "Inside constructor of parameterised diphoton producer" << endl;
    }

    void ParameterisedPromptFakeDiPhotonProducer::produce( Event &evt, const EventSetup & )
    {
        //cout << "BEGIN EVENT--------------------------------------" << endl;
        //cout << "Inside parameterised diphoton produce method" << endl;
        Handle<View<reco::Vertex> > primaryVertices;
        evt.getByToken( vertexToken_, primaryVertices );

        Handle<View<flashgg::Photon> > promptPhotons;
        evt.getByToken( promptPhotonToken_, promptPhotons );
        
        Handle<View<flashgg::Photon> > fakePhotons;
        evt.getByToken( fakePhotonToken_, fakePhotons );

        math::XYZPoint higgsVtx;
        if( ! evt.isRealData() ) {
            Handle<View<reco::GenParticle> > genParticles;
            evt.getByToken( genPartToken_, genParticles );
            for( unsigned int genLoop = 0 ; genLoop < genParticles->size(); genLoop++ ) {
                int pdgid = genParticles->ptrAt( genLoop )->pdgId();
                if( pdgid == 25 || pdgid == 22 ) {
                    higgsVtx = genParticles->ptrAt( genLoop )->vertex();
                    break;
                }
            }
        }

        auto_ptr<vector<DiPhotonCandidate> > diPhotonColl( new vector<DiPhotonCandidate> );
        //cout << "DiPhoton collection initialised" << endl;
        //cout << "size of promptPhoton collection = " << promptPhotons->size() << endl;
        //cout << "size of fakePhoton collection   = " << fakePhotons->size()   << endl;

        // loop over potential normal, prompt photons, checking they are prompt on the way
        for( unsigned int promptIndex = 0 ; promptIndex < promptPhotons->size() ; promptIndex++ ) {

            //cout << "in prompt loop" << endl;
            Ptr<flashgg::Photon> promptPhoton = promptPhotons->ptrAt( promptIndex );
            flashgg::Photon::mcMatch_t promptMatchType = promptPhoton->genMatchType();
            if( promptMatchType != 1 ) continue;
            if( abs( promptPhoton->eta() > 2.5 ) ) continue;
            if( promptPhoton->pt() < 20 ) continue;
            //cout << "prompt accessed, is prompt" << endl;
            //cout << "prompt pt is = " << promptPhoton->pt() << endl;
            //auto tempPromptLV = promptPhoton->p4();
            //cout << "prompt pt is = " << tempPromptLV.pt() << endl;

            // loop over parameterised fake photons
            for( unsigned int fakeIndex = 0; fakeIndex < fakePhotons->size(); fakeIndex++ ) {
                //cout << "in fake loop" << endl;
                Ptr<flashgg::Photon> fakePhoton = fakePhotons->ptrAt( fakeIndex );
                //cout << "fake accessed" << endl;
                //cout << "fake pt is = " << fakePhoton->pt() << endl;
                //auto tempFakeLV = fakePhoton->p4();
                //cout << "fake pt is = " << tempFakeLV.pt() << endl;

                //cout << "number of primary vertices is " << primaryVertices->size() << endl;
                auto zerothVtx = primaryVertices->ptrAt( 0 );
                //DiPhotonCandidate dipho( promptPhoton, fakePhoton, primaryVertices->ptrAt( 0 ) );
                //cout << "attempting to make diphoton" << endl;
                DiPhotonCandidate dipho( promptPhoton, fakePhoton, zerothVtx );
                //cout << "dipho constructed" << endl;
                dipho.setVertexIndex( 0 );
                dipho.setGenPV( higgsVtx );

                /*if( dipho.leadingPhoton()->pt() > 30. && dipho.subLeadingPhoton()->pt() > 20. && abs( dipho.subLeadingPhoton()->eta() ) < 2.5 && abs( dipho.leadingPhoton()->eta() ) < 2.5 ) {
                    cout << "COULD HAVE PASSED PRESELECTION???" << endl;
                    cout << "lead pt " << dipho.leadingPhoton()->pt() << endl;
                    cout << "sublead pt " << dipho.subLeadingPhoton()->pt() << endl;
                    cout << "lead eta " << dipho.leadingPhoton()->eta() << endl;
                    cout << "sublead eta " << dipho.subLeadingPhoton()->eta() << endl;
                    cout << "lead full5x5_r9 " << dipho.leadingPhoton()->full5x5_r9() << endl;
                    cout << "sublead full5x5_r9 " << dipho.subLeadingPhoton()->full5x5_r9() << endl;
                    cout << "lead full5x5_sigmaIetaIeta " << dipho.leadingPhoton()->full5x5_sigmaIetaIeta() << endl;
                    cout << "sublead full5x5_sigmaIetaIeta " << dipho.subLeadingPhoton()->full5x5_sigmaIetaIeta() << endl;
                    cout << "lead hadronicOverEm " << dipho.leadingPhoton()->hadronicOverEm() << endl;
                    cout << "sublead hadronicOverEm " << dipho.subLeadingPhoton()->hadronicOverEm() << endl;
                    cout << "lead egChargedHadronIso " << dipho.leadingPhoton()->egChargedHadronIso() << endl;
                    cout << "sublead egChargedHadronIso " << dipho.subLeadingPhoton()->egChargedHadronIso() << endl;
                    cout << "lead pfPhoIso03 " << dipho.leadingPhoton()->pfPhoIso03() << endl;
                    cout << "sublead pfPhoIso03 " << dipho.subLeadingPhoton()->pfPhoIso03() << endl;
                    cout << "lead trkSumPtHollowConeDR03 " << dipho.leadingPhoton()->trkSumPtHollowConeDR03() << endl;
                    cout << "sublead trkSumPtHollowConeDR03 " << dipho.subLeadingPhoton()->trkSumPtHollowConeDR03() << endl;
                    cout << "lead passElectronVeto " << dipho.leadingPhoton()->passElectronVeto() << endl;
                    cout << "sublead passElectronVeto " << dipho.subLeadingPhoton()->passElectronVeto() << endl;
                    cout << "lead isEB " << dipho.leadingPhoton()->isEB() << endl;
                    cout << "sublead isEB " << dipho.subLeadingPhoton()->isEB() << endl;
                    cout << "lead isEE " << dipho.leadingPhoton()->isEE() << endl;
                    cout << "sublead isEE " << dipho.subLeadingPhoton()->isEE() << endl;
                }*/

                // line below necessary for diphoMVA, currently commented out so need to remove from treemaker and config as well
                //vertexSelector_->writeInfoFromLastSelectionTo( dipho );

                diPhotonColl->push_back( dipho );
                //cout << "dipho entered into collection" << endl;
            }
        }

        // Sort the final collection (descending) and put it in the event
        //cout << "exited prompt loop, now about to sort dipho collection" << endl;
        std::sort( diPhotonColl->begin(), diPhotonColl->end(), greater<DiPhotonCandidate>() );
        //cout << "dipho collection sorted, about to set jet collection indices" << endl;

        for( unsigned int i = 0 ; i < diPhotonColl->size() ; i++ ) {
            diPhotonColl->at( i ).setJetCollectionIndex( 0 );
        }
        //cout << "jet collection indices set, about to put dipho collection in the event" << endl;

        evt.put( diPhotonColl );
        //cout << "dipho collection is in the event" << endl;
        //cout << "END EVENT--------------------------------------" << endl << endl;
        //cout << "Exiting parameterised diphoton produce method" << endl;
    }
}

typedef flashgg::ParameterisedPromptFakeDiPhotonProducer FlashggParameterisedPromptFakeDiPhotonProducer;
DEFINE_FWK_MODULE( FlashggParameterisedPromptFakeDiPhotonProducer );
// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

