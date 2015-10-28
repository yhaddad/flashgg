#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/EDMException.h"

#include "flashgg/DataFormats/interface/DiPhotonCandidate.h"
#include "flashgg/DataFormats/interface/Jet.h"
#include "flashgg/DataFormats/interface/VBFMVAResult.h"

#include "TMVA/Reader.h"
#include "TMath.h"
#include "DataFormats/Math/interface/deltaR.h"
#include <string>

using namespace std;
using namespace edm;

namespace flashgg {

    class VBFTruthProducer : public EDProducer
    {

    public:
        VBFTruthProducer( const ParameterSet & );
    private:
        void produce( Event &, const EventSetup & ) override;
        
        EDGetTokenT<View<DiPhotonCandidate> > diPhotonToken_;
        EDGetTokenT<View<reco::GenJet> >      GenJets_;
        EDGetTokenT<View<reco::GenParticle> > genParticles_;
        
        std::vector<edm::InputTag>            inputTagJets_;
        unique_ptr<TMVA::Reader>              VbfMva_;
        
        FileInPath vbfMVAweightfile_;
        string     _MVAMethod;
        bool       _usePuJetID;
        bool       _useJetID;
        string     _JetIDLevel;
        double     _minDijetMinv;
        
        typedef std::vector<edm::Handle<edm::View<flashgg::Jet> > > JetCollectionVector;
        
    };

    VBFTruthProducer::VBFTruthProducer( const ParameterSet &iConfig ) :
        diPhotonToken_( consumes<View<flashgg::DiPhotonCandidate> >( iConfig.getParameter<InputTag> ( "DiPhotonTag" ) ) ),
        inputTagJets_ ( iConfig.getParameter<std::vector<edm::InputTag> >( "inputTagJets" ) ),
        _MVAMethod    ( iConfig.getUntrackedParameter<string>( "MVAMethod" , "BDT") ),
        _usePuJetID   ( iConfig.getUntrackedParameter<bool>  ( "UsePuJetID"  , false ) ),
        _useJetID     ( iConfig.getUntrackedParameter<bool>  ( "UseJetID"    , false ) ),
        _JetIDLevel   ( iConfig.getUntrackedParameter<string>( "JetIDLevel", "Loose" ) ), // Loose == 0, Tight == 1
        _minDijetMinv ( iConfig.getParameter<double>         ( "MinDijetMinv" ) )
    {
        
        vbfMVAweightfile_ = iConfig.getParameter<edm::FileInPath>( "vbfMVAweightfile" );
        if ( false){
            VbfMva_.reset( new TMVA::Reader( "!Color:Silent" ) );
            VbfMva_->AddVariable( "dijet_LeadJPt"   , &dijet_LeadJPt_    );
            VbfMva_->AddVariable( "dijet_SubJPt"    , &dijet_SubJPt_     );
            VbfMva_->AddVariable( "dijet_abs_dEta"  , &dijet_abs_dEta_   );
            VbfMva_->AddVariable( "dijet_dy"        , &dijet_dy_         );
            VbfMva_->AddVariable( "dijet_Mjj"       , &dijet_Mjj_        );
            VbfMva_->AddVariable( "dijet_Zep"       , &dijet_Zep_        );
            VbfMva_->AddVariable( "minDRJetPho"     , &minDRJetPho_      );
            VbfMva_->AddVariable( "dijet_dipho_dphi", &dijet_dipho_dphi_ );
            VbfMva_->AddVariable( "dipho_PToM"      , &dipho_PToM_       );
            VbfMva_->BookMVA( _MVAMethod.c_str() , vbfMVAweightfile_.fullPath() );
        }
        produces<vector<VBFTagTruth> >();
        
    }

    void VBFTruthProducer::produce( Event &evt, const EventSetup & )
    {
        Handle<View<flashgg::DiPhotonCandidate> > diPhotonCollection;
        evt.getByToken( diPhotonToken_, diPhotonCollection );
        
        JetCollectionVector jetCollections( inputTagJets_.size() );
        for( size_t j = 0; j < inputTagJets_.size(); ++j ) {
            evt.getByLabel( inputTagJets_[j], Jets[j] );
        }
        
        std::auto_ptr<vector<VBFTagTruth> > VBFTagTruth_results( new vector<VBFTagTruth> );
        if (diPhotons->size()==0) std::cout << " --> no diphoton " << std::endl;
        
        for( unsigned int diPhotonIndex = 0; diPhotonIndex < diPhotonCollection->size() ; diPhotonIndex++ ) {
            flashgg::VBFTagTruth truthObject;
            // --> write your code here
            // the diphoton index is: candIndex (you can change it)
                        
            
            
            // save the tag object
            VBFTagTruth_results->push_back( truthObject );
        }
        // store in the event the tagObject
        evt.put( vbf_results );
    }
}

typedef flashgg::VBFTruthProducer FlashggVBFTruthProducer;
DEFINE_FWK_MODULE( FlashggVBFTruthProducer );
// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

