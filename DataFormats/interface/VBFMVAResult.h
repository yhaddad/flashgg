#ifndef FLASHgg_VBFMVAResult_h
#define FLASHgg_VBFMVAResult_h

#include "DataFormats/Common/interface/Ptr.h"
#include "flashgg/DataFormats/interface/DiPhotonCandidate.h"
#include "flashgg/DataFormats/interface/Jet.h"


namespace flashgg {
    
    class VBFMVAResult
    {
        
    public:
        VBFMVAResult();
        VBFMVAResult( edm::Ptr<VBFMVAResult> );
        
        // diJet Info
        flashgg::Jet leadJet;
        flashgg::Jet subleadJet;
        flashgg::Jet subSubleadJet; // the third jet

        // di-photon info 
        flashgg::DiPhotonCandidate diphoton;

        // event based variables
        int  n_rec_jets;
        int  n_gen_jets;
        int  n_diphotons;
        
        // Input variables
        float dijet_leadEta ;
        float dijet_subleadEta;
        float dijet_abs_dEta;
        float dijet_LeadJPt ;
        float dijet_SubJPt;
        float dijet_Zep;
        float dijet_dphi_trunc;
        float dijet_dipho_dphi;
        float dijet_Mjj;
        float dijet_dy;
        float dijet_leady ;
        float dijet_subleady;
        float dijet_dipho_pt;
        float dipho_PToM;
        float leadPho_PToM;
        float sublPho_PToM;
        float minDRJetPho;
        
        // some 3-jet based variables 
        float VBFMVAValue() const {return vbfMvaResult_value;}
        
        // Output
        float vbfMvaResult_value;
        float vbfMvaResult_value_bdt;
        float vbfMvaResult_value_bdtg;
    };
    
    typedef std::map<edm::Ptr<DiPhotonCandidate>, VBFMVAResult> VBFMVAResultMap;

}

#endif
// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

