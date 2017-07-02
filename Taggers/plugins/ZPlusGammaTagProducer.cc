#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/EDMException.h"

#include "flashgg/DataFormats/interface/DiPhotonCandidate.h"
#include "flashgg/DataFormats/interface/ZPlusGammaTag.h"
//#include "flashgg/DataFormats/interface/ZPlusJetTagTruth.h"
#include "flashgg/DataFormats/interface/Photon.h"

#include "DataFormats/Common/interface/RefToPtr.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"


#include <vector>
#include <algorithm>

using namespace std;
using namespace edm;

namespace flashgg {

    class ZPlusGammaTagProducer : public EDProducer
    {

    public:
        typedef math::XYZPoint Point;

        ZPlusGammaTagProducer( const ParameterSet & );

    private:
        void produce( Event &, const EventSetup & ) override;

        EDGetTokenT<View<DiPhotonCandidate> >      diPhotonToken_;
        EDGetTokenT<View<DiPhotonMVAResult> >      mvaResultToken_;
        EDGetTokenT<View<reco::GenParticle> >      genPartToken_;
        EDGetTokenT<View<flashgg::Photon> > inputTagPhotons_;
        string systLabel_;

    };

    ZPlusGammaTagProducer::ZPlusGammaTagProducer( const ParameterSet &iConfig ) :
        diPhotonToken_( consumes<View<flashgg::DiPhotonCandidate> >( iConfig.getParameter<InputTag> ( "DiPhotonTag" ) ) ),
        mvaResultToken_( consumes<View<flashgg::DiPhotonMVAResult> >( iConfig.getParameter<InputTag> ( "MVAResultTag" ) ) ),
        genPartToken_( consumes<View<reco::GenParticle> >( iConfig.getParameter<InputTag> ( "GenParticleTag" ) ) ),
        inputTagPhotons_ ( consumes<View<flashgg::Photon> >( iConfig.getParameter<InputTag> ("inputTagPhotons" ) ) ),
        systLabel_   ( iConfig.getParameter<string> ( "SystLabel" ) )
    {

        produces<vector<ZPlusGammaTag> >();
        //        produces<vector<ZPlusJetTagTruth> >();
    }

    void ZPlusGammaTagProducer::produce( Event &evt, const EventSetup & )
    {

        Handle<View<flashgg::DiPhotonCandidate> > diPhotons;
        evt.getByToken( diPhotonToken_, diPhotons );
        
        Handle<View<flashgg::DiPhotonMVAResult> > mvaResults;
        evt.getByToken( mvaResultToken_, mvaResults );
        
        Handle<View<reco::GenParticle> > genParticles;

        Handle<View<flashgg::Photon> > photons;
         
        std::auto_ptr<vector<ZPlusGammaTag> >      tags  ( new vector<ZPlusGammaTag> );

        std::cout << "N photon  == " << photons->size() << std::endl;
        std::cout << "N MVA res == " << mvaResults->size() << std::endl;
        std::cout << "N dipho   == " << diPhotons->size() << std::endl;

        assert( diPhotons->size() == mvaResults->size() ); // We are relying on corresponding sets - update this to give an error/exception

        for( unsigned int candIndex = 0; candIndex < diPhotons->size() ; candIndex++ ) {
            edm::Ptr<flashgg::DiPhotonMVAResult>      mvares          = mvaResults->ptrAt( candIndex );
            edm::Ptr<flashgg::DiPhotonCandidate>      dipho           = diPhotons->ptrAt( candIndex );

            unsigned nphotons = 0;
            Ptr<flashgg::Photon> leadingPhoton;
            for ( unsigned int i = 0 ; i < photons->size() ; i++ ){
                Ptr<flashgg::Photon> photon = photons->ptrAt( i );
                if (photon->pt() < 20.) continue;

                // close to lead photon?
                float dPhi = deltaPhi( photon->phi(), dipho->leadingPhoton()->phi() );
                float dEta = photon->eta() - dipho->leadingPhoton()->eta();
                if( sqrt( dPhi * dPhi + dEta * dEta ) < 0.4 ) { continue; }

                // close to sublead photon?
                dPhi = deltaPhi( photon->phi(), dipho->subLeadingPhoton()->phi() );
                dEta = photon->eta() - dipho->subLeadingPhoton()->eta();
                if( sqrt( dPhi * dPhi + dEta * dEta ) < 0.4 ) { continue; }

                if ( nphotons == 0 ) {
                    leadingPhoton  = photon ;
                }
                nphotons++;
            }

            if (nphotons > 0) {
                    ZPlusGammaTag tag_obj( dipho, mvares, leadingPhoton );
                    tag_obj.setDiPhotonIndex( candIndex );
                    tag_obj.setSystLabel    ( systLabel_ );
                    tag_obj.includeWeights( *dipho );
                    tag_obj.includeWeights( *leadingPhoton );
                    
                    std::cout << "The jet's eta, HF hadronic energy fraction values are " << tag_obj.photon()->pt() << std::endl;
                    std::cout << "The Z mass, pt values are " << tag_obj.zMass() << ", " << tag_obj.zPt() << endl << endl;
                    std::cout << "The Z jet deltaPhi value is " << tag_obj.deltaPhiZPhoton() << endl << endl;
                    
                    // saving the collection
                    tags->push_back( tag_obj );
                    //                if( ! evt.isRealData() ) {
                    //                    truths->push_back( truth_obj );
                    //                    tags->back().setTagTruth( edm::refToPtr( edm::Ref<vector<ZPlusJetTagTruth> >( rTagTruth, idx++ ) ) );
                    //                }
            }
        }

        evt.put( tags );
        //        evt.put( truths );
    }
}

typedef flashgg::ZPlusGammaTagProducer FlashggZPlusGammaTagProducer;
DEFINE_FWK_MODULE( FlashggZPlusGammaTagProducer );
// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

