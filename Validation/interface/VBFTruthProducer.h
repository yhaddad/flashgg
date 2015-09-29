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

#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Common/interface/Ptr.h"
#include "flashgg/DataFormats/interface/VBFTagTruth.h"

using namespace std;
using namespace edm;
using namespace flashgg;

struct MVAVarStruct {

    float leadingJetPt, subLeadingJetPt, subSubLeadingJetPt;
    float leadingJetEta, subLeadingJetEta, subSubLeadingJetEta;
    float leadingJetPhi, subLeadingJetPhi, subSubLeadingJetPhi;

    int   leadingJetHemisphere, subLeadingJetHemisphere, subSubLeadingJetHemisphere;   
    int   oppHemispheres_J1J2, oppHemispheres_J1J3, oppHemispheres_J2J3;
 
    float dR_12, dR_13, dR_23;
    float mjj_12, mjj_13, mjj_23, mjjj;
    float dEta_12, dEta_13, dEta_23;
    float zepjj_12, zepjj_13, zepjj_23, zepjjj;
    float dPhijj_12, dPhijj_13, dPhijj_23, dPhijjj;

    float dEta_J1J2J3, dEta_J2J3J1, dEta_J3J1J2;

    float mjj_d12_13plus23, mjj_d12_13, mjj_d12_23, mjj_d13_23;
    float dR_DP_12, dR_DP_13, dR_DP_23;
    float dR_Ph1_1,dR_Ph1_2,dR_Ph1_3,dR_Ph2_1,dR_Ph2_2,dR_Ph2_3;
    float dR_DP_123; 

    float missingP4_dPhi_jjj, missingP4_dPhi_jj, missingP4_Pt_jjj, missingP4_Pt_jj;
    float missingP4_dPhi_d3J2J, missingP4_Pt_d3J2J;
    float dPhi_12, dPhi_13, dPhi_23, dPhi_max, dPhi_min, dPhi_min_max;

    float leadingDR, subLeadingDR, subSubLeadingDR;
};

class VBFTruthProducer {

    private:
        VBFTagTruth truth_;

    public:
        VBFTruthProducer(){};

        ~VBFTruthProducer(){};

        void produce ( unsigned int diPhotonIndex,
                                Handle<View<reco::GenParticle> > genParticles,
                                Handle<View<reco::GenJet> > genJets,
                                Handle<View<flashgg::DiPhotonCandidate> > diPhotonCollection,
                                std::vector<edm::Handle<edm::View<flashgg::Jet> > > jetCollections );

        VBFTagTruth truthObject() {return truth_;}

        MVAVarStruct recoLevelMVAVars();
        MVAVarStruct genJetLevelMVAVars();
        MVAVarStruct genParticleLevelMVAVars();
        MVAVarStruct partonLevelMVAVars();

};

