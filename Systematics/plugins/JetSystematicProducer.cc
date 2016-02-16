#ifndef FLASHgg_JetSystematicProducer_h
#define FLASHgg_JetSystematicProducer_h

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "flashgg/Systematics/interface/BaseSystMethod.h"
#include "flashgg/Systematics/interface/ObjectSystematicProducer.h"
#include "flashgg/DataFormats/interface/Jet.h"

#include "FWCore/Framework/interface/ESHandle.h"
//#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
//#include "JetMETCorrections/Objects/interface/JetCorrectionsRecord.h"
//#include "JetMETCorrections/Objects/interface/JetCorrector.h"
#include "JetMETCorrections/JetCorrector/interface/JetCorrector.h"

namespace flashgg {

    class JetSystematicProducer : public ObjectSystematicProducer<flashgg::Jet,int,std::vector>
    {
        
    public:
        JetSystematicProducer ( const edm::ParameterSet &iConfig );
        
    private:
        void produce( edm::Event &, const edm::EventSetup & ) override;
        bool   correctionsSet_;
        bool   doCentralJEC_;
        string JECLabel_;
        edm::EDGetTokenT<reco::JetCorrector> mJetCorrector;
    };
    
    JetSystematicProducer::JetSystematicProducer ( const edm::ParameterSet &iConfig ) : ObjectSystematicProducer<flashgg::Jet,int,std::vector>( iConfig ) {
        correctionsSet_ = false;
        doCentralJEC_  = iConfig.getParameter<bool>  ("DoCentralJEC");
        JECLabel_      = iConfig.getParameter<string>("JECLabel");
        mJetCorrector  = consumes<reco::JetCorrector>(iConfig.getParameter<InputTag>("JetCorrectorTag"));
    }
    
    void JetSystematicProducer::produce( edm::Event &iEvent, const edm::EventSetup & iSetup ) {
        if (doCentralJEC_) {
            // Sal: IIRC, you want "ak4PFCHSL1FastL2L3Residual" for data, "ak4PFCHSL1FastL2L3" for MC
            // The old way to retreive the correctors
            // const JetCorrector* corrector = JetCorrector::getJetCorrector (JECLabel_,iSetup); 
            // new recipe from :
            // https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookJetEnergyCorrections#CorrOnTheFly
            edm::Handle<reco::JetCorrector>  corrector  ;
            iEvent.getByToken(mJetCorrector, corrector );
            
            for( unsigned int ncorr = 0; ncorr < this->Corrections_.size(); ncorr++ ) {
                if( !this->Corrections_.at( ncorr )->makesWeight() ){
                    this->Corrections_.at( ncorr )->setJEC(corrector.product(),iEvent,iSetup);
                }
            }
            
            for( unsigned int ncorr = 0; ncorr < this->Corrections2D_.size(); ncorr++ ) {
                if( !this->Corrections2D_.at( ncorr )->makesWeight() ){
                    this->Corrections2D_.at( ncorr )->setJEC(corrector.product(),iEvent,iSetup);
                }
            }
        }
        //if (!correctionsSet_) {
        //    edm::ESHandle<JetCorrectorParametersCollection> JetCorParColl;
        //    iSetup.get<JetCorrectionsRecord>().get("AK4PFchs",JetCorParColl); 
        //    JetCorrectorParameters const & JetCorPar = (*JetCorParColl)["Uncertainty"];
        //    std::cout << "after the JetCorrectorParameters" << std::endl;
        //    for( unsigned int ncorr = 0; ncorr < this->Corrections_.size(); ncorr++ ) {
        //        if( !this->Corrections_.at( ncorr )->makesWeight() ){
        //            this->Corrections_.at( ncorr )->setJECUncertainty(JetCorPar);
        //        }
        //    }
        //    for( unsigned int ncorr = 0; ncorr < this->Corrections2D_.size(); ncorr++ ) {
        //        if( !this->Corrections2D_.at( ncorr )->makesWeight() ){
        //            this->Corrections2D_.at( ncorr )->setJECUncertainty(JetCorPar);
        //        }
        //    }
        //}
        ObjectSystematicProducer<flashgg::Jet,int,std::vector>::produce( iEvent, iSetup );
    }

}

#endif

typedef flashgg::JetSystematicProducer FlashggJetSystematicProducer;
DEFINE_FWK_MODULE( FlashggJetSystematicProducer );
// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
