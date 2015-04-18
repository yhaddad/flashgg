#ifndef FLASHgg_VBFTag_h
#define FLASHgg_VBFTag_h


#include "flashgg/TagFormats/interface/DiPhotonTagBase.h"
#include "flashgg/TagFormats/interface/VBFDiPhoDiJetMVAResult.h"
#include "flashgg/MicroAODFormats/interface/Jet.h"

namespace flashgg {
  
  class VBFTag: public DiPhotonTagBase {
  public:
    VBFTag();
    ~VBFTag();
    
    VBFTag(edm::Ptr<DiPhotonCandidate>,edm::Ptr<DiPhotonMVAResult>,edm::Ptr<VBFDiPhoDiJetMVAResult>);
    VBFTag(edm::Ptr<DiPhotonCandidate>,DiPhotonMVAResult,VBFDiPhoDiJetMVAResult);
    VBFTag* clone() const;
    
    const VBFDiPhoDiJetMVAResult VBFDiPhoDiJetMVA() const;
    const VBFMVAResult           VBFMVA() const ;
    
    const Jet leadingJet() const; //needs to be validated
    const Jet subLeadingJet() const; //needs to be validated
    
    //!the MC truth or the VBF
    // const GenJet trueVbfJet_lead() const;    // 1
    // const GenJet trueVBFJet_subLead() const; // 2
    
    // mybe we can get the matched gen particle from
    // the previous two functions
    // const GenJet vbfParton_1() const; 
    // const GenJet vbfParton_2() const;
    
  private:
    VBFDiPhoDiJetMVAResult vbfDiPhoDiJet_mva_result_;
  };

}

#endif
