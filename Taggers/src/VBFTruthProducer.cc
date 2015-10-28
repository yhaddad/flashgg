
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

#include "flashgg/DataFormats/interface/VBFTruthProducer.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Common/interface/Ptr.h"
#include "flashgg/DataFormats/interface/TagTruthBase.h"
#include "flashgg/DataFormats/interface/Jet.h"

using namespace std;
using namespace edm;
using namespace flashgg;

void VBFTruthProducer::produce(  unsigned int diPhotonIndex,
                                        Handle<View<reco::GenParticle> > genParticles,
                                        Handle<View<reco::GenJet> > GenJets,
                                        Handle<View<flashgg::DiPhotonCandidate> > diPhotonCollection,
                                        std::vector<edm::Handle<edm::View<flashgg::Jet> > > jetCollections ) {

    VBFTagTruth truthObject;
    //The diphoton
    edm::Ptr<flashgg::DiPhotonCandidate> diPhoton = diPhotonCollection->ptrAt(diPhotonIndex);
    truthObject.setDiPhoton(diPhoton);

//GenPartcle level
    //Find the ptOrderedPartons
    std::vector<edm::Ptr<reco::GenParticle>> ptOrderedPartons;
    for (unsigned int genLoop(0);genLoop < genParticles->size();genLoop++) {
        edm::Ptr<reco::GenParticle> gp = genParticles->ptrAt(genLoop);
        bool isGluon = abs( gp->pdgId() ) < 7 && gp->numberOfMothers() == 0;
        bool isQuark = gp->pdgId() == 21 && gp->numberOfMothers() == 0;
        if (isGluon || isQuark) {
            unsigned int insertionIndex(0);
            for (unsigned int parLoop(0);parLoop<ptOrderedPartons.size();parLoop++) {
                if (gp->pt() < ptOrderedPartons[parLoop]->pt()) { insertionIndex = parLoop + 1; }
            }
            ptOrderedPartons.insert( ptOrderedPartons.begin() + insertionIndex, gp);
        }
    }

    //Merge if close
/*
    Const issues need fixing  - leaving it as unmerged now
    std::pair<unsigned,unsigned> mergerIndices(0,0);
    for (unsigned i(0);i<ptOrderedPartons.size();i++) {
        for (unsigned j(0); j < ptOrderedPartons.size(); j++) {
            if (i <= j) continue;
            if (deltaR(ptOrderedPartons[i]->eta(),ptOrderedPartons[i]->phi(),ptOrderedPartons[j]->eta(),ptOrderedPartons[j]->phi()) < 0.4) {
                mergerIndices.first  = i;
                mergerIndices.second = j;
            }
        }
    }
    bool areDistinct = mergerIndices.first == 0 && mergerIndices.second == 0;
    if (!areDistinct) {
        ptOrderedPartons[mergerIndices.first]->setP4(ptOrderedPartons[mergerIndices.first]->p4() + ptOrderedPartons[mergerIndices.second]->p4());
        ptOrderedPartons[mergerIndices.first]->setPdgId(999);
        ptOrderedPartons.erase(ptOrderedPartons.begin()+mergerIndices.second);
        if (ptOrderedPartons[0]->pt() < ptOrderedPartons[1]->pt()) {std::swap(ptOrderedPartons[0],ptOrderedPartons[1]);}
    } 
*/

    //Add to truth object
    truthObject.setPtOrderedPartons(ptOrderedPartons);
    if (ptOrderedPartons.size() == 1) {truthObject.setLeadingParton(ptOrderedPartons[0]);}
    if (ptOrderedPartons.size() == 2) {truthObject.setLeadingParton(ptOrderedPartons[0]);truthObject.setSubLeadingParton(ptOrderedPartons[1]);}
    if (ptOrderedPartons.size() == 3) {truthObject.setLeadingParton(ptOrderedPartons[0]);truthObject.setSubLeadingParton(ptOrderedPartons[1]);truthObject.setSubSubLeadingParton(ptOrderedPartons[2]);}

//GenJet Level
    //Pt-ordered GenJets
    std::vector<edm::Ptr<reco::GenJet>> ptOrderedGenJets;
    for( unsigned int jetLoop( 0 ); jetLoop < GenJets->size(); jetLoop++ ) {
        edm::Ptr<reco::GenJet> gj = GenJets->ptrAt( jetLoop );
        unsigned insertionIndex( 0 );
        for( unsigned int i( 0 ); i < ptOrderedGenJets.size(); i++ ) {
            if( gj->pt() <= ptOrderedGenJets[i]->pt() && gj != ptOrderedGenJets[i] ) { insertionIndex = i + 1; }
        }
        //Remove photons        
        float dr_leadPhoton = deltaR( gj->eta(), gj->phi(),diPhoton->leadingPhoton()->eta(),diPhoton->leadingPhoton()->phi() ); 
        float dr_subLeadPhoton = deltaR( gj->eta(), gj->phi(),diPhoton->subLeadingPhoton()->eta(),diPhoton->subLeadingPhoton()->phi() ); 
        if( dr_leadPhoton > 0.1 && dr_subLeadPhoton > 0.1 ) {
            ptOrderedGenJets.insert( ptOrderedGenJets.begin() + insertionIndex, gj );
        }
    }

    //Add to truth object
    truthObject.setPtOrderedGenJets(ptOrderedGenJets);
    if (ptOrderedGenJets.size() == 1) {truthObject.setLeadingGenJet(ptOrderedGenJets[0]);}
    if (ptOrderedGenJets.size() == 2) {truthObject.setLeadingGenJet(ptOrderedGenJets[0]);truthObject.setSubLeadingGenJet(ptOrderedGenJets[1]);}
    if (ptOrderedGenJets.size() == 3) {
        truthObject.setLeadingGenJet(ptOrderedGenJets[0]);
        truthObject.setSubLeadingGenJet(ptOrderedGenJets[1]);
        truthObject.setSubSubLeadingGenJet(ptOrderedGenJets[2]);
    }

//FLASHgg Jet Level
    //Pt-ordered fggJets
    Handle<View<flashgg::Jet>> fggJets = jetCollections[diPhoton->jetCollectionIndex()]; 
    std::vector<edm::Ptr<flashgg::Jet>> ptOrderedFggJets;
    for (unsigned jetLoop(0);jetLoop<fggJets->size();jetLoop++) {
        edm::Ptr<flashgg::Jet> jet = fggJets->ptrAt(jetLoop);
        unsigned int insertionIndex( 0 );
        for ( unsigned int i(0);i<ptOrderedFggJets.size();i++) {
            if( jet->pt() <= ptOrderedFggJets[i]->pt() && jet != ptOrderedFggJets[i] ) { insertionIndex = i + 1; }
        }
        //Remove photons and pileup
        float dr_leadPhoton = deltaR( jet->eta(), jet->phi(),diPhoton->leadingPhoton()->eta(),diPhoton->leadingPhoton()->phi() ); 
        float dr_subLeadPhoton = deltaR( jet->eta(), jet->phi(),diPhoton->subLeadingPhoton()->eta(),diPhoton->subLeadingPhoton()->phi() ); 
        bool pileupRejection = true;
        if( dr_leadPhoton > 0.1 && dr_subLeadPhoton > 0.1 ) {
            if (pileupRejection && jet->passesPuJetId(diPhoton)) { 
                ptOrderedFggJets.insert( ptOrderedFggJets.begin() + insertionIndex, jet );
            } else if (!pileupRejection) {
                ptOrderedFggJets.insert( ptOrderedFggJets.begin() + insertionIndex, jet );
            }
        }
    } 
    //Add to truth object
    truthObject.setPtOrderedFggJets(ptOrderedFggJets);
    if (ptOrderedFggJets.size() > 0) {truthObject.setLeadingJet(ptOrderedFggJets[0]);}
    if (ptOrderedFggJets.size() > 1) {truthObject.setSubLeadingJet(ptOrderedFggJets[1]);}
    if (ptOrderedFggJets.size() > 2) {truthObject.setSubSubLeadingJet(ptOrderedFggJets[2]);}

//Closest matches to FLASHgg jets and the Diphoton
    //GenParticles
        //Lead
    if (ptOrderedFggJets.size() > 0 && genParticles->size() > 0) {
        float dr(999.0);
        unsigned gpIndex(0);
        for (unsigned partLoop(0);partLoop<genParticles->size();partLoop++) {
            edm::Ptr<reco::GenParticle> particle = genParticles->ptrAt(partLoop);
            float deltaR_temp = deltaR(ptOrderedFggJets[0]->eta(),ptOrderedFggJets[0]->phi(),particle->eta(),particle->phi());
            if (deltaR_temp < dr) {dr = deltaR_temp; gpIndex = partLoop;}
        }
        truthObject.setClosestParticleToLeadingJet(genParticles->ptrAt(gpIndex));
    } 
        //Sublead
    if (ptOrderedFggJets.size() > 1 && genParticles->size() > 0) {
        float dr(999.0);
        unsigned gpIndex(0);
        for (unsigned partLoop(0);partLoop<genParticles->size();partLoop++) {
            edm::Ptr<reco::GenParticle> particle = genParticles->ptrAt(partLoop);
            float deltaR_temp = deltaR(ptOrderedFggJets[1]->eta(),ptOrderedFggJets[1]->phi(),particle->eta(),particle->phi());
            if (deltaR_temp < dr) {dr = deltaR_temp; gpIndex = partLoop;}
        }
        truthObject.setClosestParticleToSubLeadingJet(genParticles->ptrAt(gpIndex));
    } 
        //Subsublead
    if (ptOrderedFggJets.size() > 2 && genParticles->size() > 0) {
        float dr(999.0);
        unsigned gpIndex(0);
        for (unsigned partLoop(0);partLoop<genParticles->size();partLoop++) {
            edm::Ptr<reco::GenParticle> particle = genParticles->ptrAt(partLoop);
            float deltaR_temp = deltaR(ptOrderedFggJets[2]->eta(),ptOrderedFggJets[2]->phi(),particle->eta(),particle->phi());
            if (deltaR_temp < dr) {dr = deltaR_temp; gpIndex = partLoop;}
        }
        truthObject.setClosestParticleToSubSubLeadingJet(genParticles->ptrAt(gpIndex));
    } 

    //GenJets
        //Lead
    if (ptOrderedFggJets.size() > 0 && ptOrderedGenJets.size() > 0) {
        float dr(999.0);
        unsigned gjIndex(0);
        for (unsigned jetLoop(0);jetLoop<ptOrderedGenJets.size();jetLoop++) {
            float deltaR_temp = deltaR(ptOrderedFggJets[0]->eta(),ptOrderedFggJets[0]->phi(),ptOrderedGenJets[jetLoop]->eta(),ptOrderedGenJets[jetLoop]->phi());
            if (deltaR_temp < dr) {dr = deltaR_temp; gjIndex = jetLoop;}
        }
        truthObject.setClosestGenJetToLeadingJet( ptOrderedGenJets[gjIndex] );
    }
        //Sublead
    if (ptOrderedFggJets.size() > 1 && ptOrderedGenJets.size() > 0) {
        float dr(999.0);
        unsigned gjIndex(0);
        for (unsigned jetLoop(0);jetLoop<ptOrderedGenJets.size();jetLoop++) {
            float deltaR_temp = deltaR(ptOrderedFggJets[1]->eta(),ptOrderedFggJets[1]->phi(),ptOrderedGenJets[jetLoop]->eta(),ptOrderedGenJets[jetLoop]->phi());
            if (deltaR_temp < dr) {dr = deltaR_temp; gjIndex = jetLoop;}
        }
        truthObject.setClosestGenJetToSubLeadingJet( ptOrderedGenJets[gjIndex] );
    }
        //Subsublead
    if (ptOrderedFggJets.size() > 2 && ptOrderedGenJets.size() > 0) {
        float dr(999.0);
        unsigned gjIndex(0);
        for (unsigned jetLoop(0);jetLoop<ptOrderedGenJets.size();jetLoop++) {
            float deltaR_temp = deltaR(ptOrderedFggJets[2]->eta(),ptOrderedFggJets[2]->phi(),ptOrderedGenJets[jetLoop]->eta(),ptOrderedGenJets[jetLoop]->phi());
            if (deltaR_temp < dr) {dr = deltaR_temp; gjIndex = jetLoop;}
        }
        truthObject.setClosestGenJetToSubSubLeadingJet( ptOrderedGenJets[gjIndex] );
    }
    //Partons
    //Lead
    if (ptOrderedFggJets.size() > 0 && ptOrderedPartons.size() > 0) {
        float dr(999.0);
        unsigned pIndex(0);
        for (unsigned partLoop(0);partLoop<ptOrderedPartons.size();partLoop++) {
            float deltaR_temp = deltaR(ptOrderedFggJets[0]->eta(),ptOrderedFggJets[0]->phi(),ptOrderedPartons[partLoop]->eta(),ptOrderedPartons[partLoop]->phi());
            if (deltaR_temp < dr) {dr = deltaR_temp; pIndex = partLoop;}
        }
        truthObject.setClosestPartonToLeadingJet( ptOrderedPartons[pIndex] );
    }
    //Sublead
    if (ptOrderedFggJets.size() > 1 && ptOrderedPartons.size() > 0) {
        float dr(999.0);
        unsigned pIndex(0);
        for (unsigned partLoop(0);partLoop<ptOrderedPartons.size();partLoop++) {
            float deltaR_temp = deltaR(ptOrderedFggJets[1]->eta(),ptOrderedFggJets[1]->phi(),ptOrderedPartons[partLoop]->eta(),ptOrderedPartons[partLoop]->phi());
            if (deltaR_temp < dr) {dr = deltaR_temp; pIndex = partLoop;}
        }
        truthObject.setClosestPartonToSubLeadingJet( ptOrderedPartons[pIndex] );
    }
    //Sublead
    if (ptOrderedFggJets.size() > 2 && ptOrderedPartons.size() > 0) {
        float dr(999.0);
        unsigned pIndex(0);
        for (unsigned partLoop(0);partLoop<ptOrderedPartons.size();partLoop++) {
            float deltaR_temp = deltaR(ptOrderedFggJets[2]->eta(),ptOrderedFggJets[2]->phi(),ptOrderedPartons[partLoop]->eta(),ptOrderedPartons[partLoop]->phi());
            if (deltaR_temp < dr) {dr = deltaR_temp; pIndex = partLoop;}
        }
        truthObject.setClosestPartonToSubSubLeadingJet( ptOrderedPartons[pIndex] );
    }


    //Diphoton-GenParticle Matching
    float dr_leadPhoton(999.),dr_subLeadPhoton(999.);
    unsigned gpIndex1(0),gpIndex2(0);
    for (unsigned partLoop(0);partLoop<genParticles->size();partLoop++) {
        edm::Ptr<reco::GenParticle> particle = genParticles->ptrAt(partLoop);
        float deltaR_temp = deltaR(diPhoton->leadingPhoton()->eta(),diPhoton->leadingPhoton()->phi(),particle->eta(),particle->phi());
        if (deltaR_temp < dr_leadPhoton) {dr_leadPhoton = deltaR_temp; gpIndex1 = partLoop;}
        deltaR_temp = deltaR(diPhoton->subLeadingPhoton()->eta(),diPhoton->subLeadingPhoton()->phi(),particle->eta(),particle->phi());
        if (deltaR_temp < dr_subLeadPhoton) {dr_subLeadPhoton = deltaR_temp; gpIndex2 = partLoop;}
    }
    truthObject.setClosestParticleToLeadingPhoton(genParticles->ptrAt(gpIndex1));
    truthObject.setClosestParticleToSubLeadingPhoton(genParticles->ptrAt(gpIndex2));

    truth_ = truthObject;
    
}
        




MVAVarStruct VBFTruthProducer::recoLevelMVAVars() {

    MVAVarStruct recoStruct;

    recoStruct.leadingJetPt = truth_.pt_J1();
    recoStruct.subLeadingJetPt = truth_.pt_J2();
    recoStruct.subSubLeadingJetPt = truth_.pt_J3();

    recoStruct.leadingJetEta = truth_.eta_J1();
    recoStruct.subLeadingJetEta = truth_.eta_J2();
    recoStruct.subSubLeadingJetEta = truth_.eta_J3();

    recoStruct.leadingJetPhi = truth_.phi_J1();
    recoStruct.subLeadingJetPhi = truth_.phi_J2();
    recoStruct.subSubLeadingJetPhi = truth_.phi_J3();

    recoStruct.dR_12 = truth_.dR_J1J2_FggJet();
    recoStruct.dR_13 = truth_.dR_J1J3_FggJet();
    recoStruct.dR_23 = truth_.dR_J2J3_FggJet();

    recoStruct.mjj_12 = truth_.mjj_J1J2_FggJet();
    recoStruct.mjj_13 = truth_.mjj_J1J3_FggJet();
    recoStruct.mjj_23 = truth_.mjj_J2J3_FggJet();
    recoStruct.mjjj = truth_.mjjj_FggJet();

    recoStruct.dEta_12 = truth_.dEta_J1J2_FggJet();
    recoStruct.dEta_13 = truth_.dEta_J1J3_FggJet();
    recoStruct.dEta_23 = truth_.dEta_J2J3_FggJet();

    recoStruct.zepjj_12 = truth_.zepjj_J1J2_FggJet();
    recoStruct.zepjj_13 = truth_.zepjj_J1J3_FggJet();
    recoStruct.zepjj_23 = truth_.zepjj_J2J3_FggJet();
    recoStruct.zepjjj = truth_.zepjjj_FggJet();

    recoStruct.dPhijj_12 = (truth_.dPhijj_J1J2_FggJet());
    recoStruct.dPhijj_13 = (truth_.dPhijj_J1J3_FggJet());
    recoStruct.dPhijj_23 = (truth_.dPhijj_J2J3_FggJet());
    recoStruct.dPhijjj = (truth_.dPhijjj_FggJet());

    recoStruct.leadingJetHemisphere = truth_.hemisphere_J1();
    recoStruct.subLeadingJetHemisphere = truth_.hemisphere_J2();
    recoStruct.subSubLeadingJetHemisphere = truth_.hemisphere_J3();

    recoStruct.oppHemispheres_J1J2 = truth_.oppHemispheres_J12();
    recoStruct.oppHemispheres_J1J3 = truth_.oppHemispheres_J13();
    recoStruct.oppHemispheres_J2J3 = truth_.oppHemispheres_J23();

    recoStruct.dEta_J1J2J3 = truth_.dEta_J1J2J3_FggJet();
    recoStruct.dEta_J2J3J1 = truth_.dEta_J2J3J1_FggJet();
    recoStruct.dEta_J3J1J2 = truth_.dEta_J3J1J2_FggJet();

    recoStruct.mjj_d12_13plus23 = truth_.mjj_d12_13plus23_FggJet();
    recoStruct.mjj_d12_13 = truth_.mjj_d12_13_FggJet();
    recoStruct.mjj_d12_23 = truth_.mjj_d12_23_FggJet();
    recoStruct.mjj_d13_23 = truth_.mjj_d13_23_FggJet();

    recoStruct.dR_DP_12   = truth_.dR_DP_12_FggJet();
    recoStruct.dR_DP_13   = truth_.dR_DP_13_FggJet();
    recoStruct.dR_DP_23   = truth_.dR_DP_23_FggJet();

    recoStruct.dR_Ph1_1 = truth_.dR_Ph1_1_FggJet();
    recoStruct.dR_Ph1_2 = truth_.dR_Ph1_2_FggJet();
    recoStruct.dR_Ph1_3 = truth_.dR_Ph1_3_FggJet();
    recoStruct.dR_Ph2_1 = truth_.dR_Ph2_1_FggJet();
    recoStruct.dR_Ph2_2 = truth_.dR_Ph2_2_FggJet();
    recoStruct.dR_Ph2_3 = truth_.dR_Ph2_3_FggJet();

    recoStruct.dR_DP_123 = truth_.dR_DP_123_FggJet();
    
    recoStruct.missingP4_dPhi_jjj = truth_.missingP4_dPhi_jjj_FggJet();
    recoStruct.missingP4_dPhi_jj = truth_.missingP4_dPhi_jj_FggJet();
    recoStruct.missingP4_Pt_jjj = truth_.missingP4_Pt_jjj_FggJet();
    recoStruct.missingP4_Pt_jj = truth_.missingP4_Pt_jj_FggJet();
    recoStruct.missingP4_dPhi_d3J2J = truth_.missingP4_dPhi_d3J2J_FggJet();
    recoStruct.missingP4_Pt_d3J2J = truth_.missingP4_Pt_d3J2J_FggJet();
    
    recoStruct.dPhi_12 = truth_.dPhi_12_FggJet();
    recoStruct.dPhi_13 = truth_.dPhi_13_FggJet();
    recoStruct.dPhi_23 = truth_.dPhi_23_FggJet();
    recoStruct.dPhi_max = truth_.dPhi_max_FggJet();
    recoStruct.dPhi_min = truth_.dPhi_min_FggJet();
    recoStruct.dPhi_min_max = truth_.dPhi_min_max_FggJet();

    recoStruct.leadingDR = 0;
    recoStruct.subLeadingDR = 0;
    recoStruct.subSubLeadingDR = 0;

    return recoStruct;
}


/*
    float mjj_d12_13plus23, mjj_d12_13, mjj_d12_23, mjj_d13_23;
    float dR_DP_12, dR_DP_13, dR_DP_23;
    float dR_Ph1_1,dR_Ph1_2,dR_Ph1_3,dR_Ph2_1,dR_Ph2_2,dR_Ph2_3;
    float dR_DP_123; 

    float missingP4_dPhi_jjj, missingP4_dPhi_jj, missingP4_Pt_jjj, missingP4_Pt_jj;
    float missingP4_dPhi_d3J2J, missingP4_Pt_d3J2J;
    float dPhi_12, dPhi_13, dPhi_23, dPhi_max, dPhi_min, dPhi_min_max;

    float leadingDR, subLeadingDR, subSubLeadingDR;
};
*/



MVAVarStruct VBFTruthProducer::genJetLevelMVAVars() {

    MVAVarStruct genJetStruct;
    genJetStruct.leadingJetPt = truth_.pt_genJetMatchingToJ1();
    genJetStruct.subLeadingJetPt = truth_.pt_genJetMatchingToJ2();
    genJetStruct.subSubLeadingJetPt = truth_.pt_genJetMatchingToJ2();

    genJetStruct.leadingJetEta = truth_.eta_genJetMatchingToJ1();
    genJetStruct.subLeadingJetEta = truth_.eta_genJetMatchingToJ2();
    genJetStruct.subSubLeadingJetEta = truth_.eta_genJetMatchingToJ2();

    genJetStruct.leadingJetPhi = truth_.phi_genJetMatchingToJ1();
    genJetStruct.subLeadingJetPhi = truth_.phi_genJetMatchingToJ2();
    genJetStruct.subSubLeadingJetPhi = truth_.phi_genJetMatchingToJ2();

    genJetStruct.dR_12 = truth_.dR_J1J2_GenJet();
    genJetStruct.dR_13 = truth_.dR_J1J3_GenJet();
    genJetStruct.dR_23 = truth_.dR_J2J3_GenJet();

    genJetStruct.mjj_12 = truth_.mjj_J1J2_GenJet();
    genJetStruct.mjj_13 = truth_.mjj_J1J3_GenJet();
    genJetStruct.mjj_23 = truth_.mjj_J2J3_GenJet();
    genJetStruct.mjjj = truth_.mjjj_GenJet();

    genJetStruct.dEta_12 = truth_.dEta_J1J2_GenJet();
    genJetStruct.dEta_13 = truth_.dEta_J1J3_GenJet();
    genJetStruct.dEta_23 = truth_.dEta_J2J3_GenJet();

    genJetStruct.zepjj_12 = truth_.zepjj_J1J2_GenJet();
    genJetStruct.zepjj_13 = truth_.zepjj_J1J3_GenJet();
    genJetStruct.zepjj_23 = truth_.zepjj_J2J3_GenJet();
    genJetStruct.zepjjj = truth_.zepjjj_GenJet();

    genJetStruct.dPhijj_12 = (truth_.dPhijj_J1J2_GenJet());
    genJetStruct.dPhijj_13 = (truth_.dPhijj_J1J3_GenJet());
    genJetStruct.dPhijj_23 = (truth_.dPhijj_J2J3_GenJet());
    genJetStruct.dPhijjj = (truth_.dPhijjj_GenJet());

    genJetStruct.leadingJetHemisphere = truth_.hemisphere_J1_GenJet();
    genJetStruct.subLeadingJetHemisphere = truth_.hemisphere_J2_GenJet();
    genJetStruct.subSubLeadingJetHemisphere = truth_.hemisphere_J3_GenJet();

    genJetStruct.oppHemispheres_J1J2 = truth_.oppHemispheres_J12_GenJet();
    genJetStruct.oppHemispheres_J1J3 = truth_.oppHemispheres_J13_GenJet();
    genJetStruct.oppHemispheres_J2J3 = truth_.oppHemispheres_J23_GenJet();

    genJetStruct.dEta_J1J2J3 = truth_.dEta_J1J2J3_GenJet();
    genJetStruct.dEta_J2J3J1 = truth_.dEta_J2J3J1_GenJet();
    genJetStruct.dEta_J3J1J2 = truth_.dEta_J3J1J2_GenJet();

    genJetStruct.mjj_d12_13plus23 = truth_.mjj_d12_13plus23_GenJet();
    genJetStruct.mjj_d12_13 = truth_.mjj_d12_13_GenJet();
    genJetStruct.mjj_d12_23 = truth_.mjj_d12_23_GenJet();
    genJetStruct.mjj_d13_23 = truth_.mjj_d13_23_GenJet();

    genJetStruct.dR_DP_12  = truth_.dR_DP_12_GenJet();
    genJetStruct.dR_DP_13  = truth_.dR_DP_13_GenJet();
    genJetStruct.dR_DP_23  = truth_.dR_DP_23_GenJet();

    genJetStruct.dR_Ph1_1 = truth_.dR_Ph1_1_GenJet();
    genJetStruct.dR_Ph1_2 = truth_.dR_Ph1_2_GenJet();
    genJetStruct.dR_Ph1_3 = truth_.dR_Ph1_3_GenJet();
    genJetStruct.dR_Ph2_1 = truth_.dR_Ph2_1_GenJet();
    genJetStruct.dR_Ph2_2 = truth_.dR_Ph2_2_GenJet();
    genJetStruct.dR_Ph2_3 = truth_.dR_Ph2_3_GenJet();

    genJetStruct.dR_DP_123 = truth_.dR_DP_123_GenJet();

    genJetStruct.missingP4_dPhi_jjj = truth_.missingP4_dPhi_jjj_GenJet();
    genJetStruct.missingP4_dPhi_jj = truth_.missingP4_dPhi_jj_GenJet();
    genJetStruct.missingP4_Pt_jjj = truth_.missingP4_Pt_jjj_GenJet();
    genJetStruct.missingP4_Pt_jj = truth_.missingP4_Pt_jj_GenJet();
    genJetStruct.missingP4_dPhi_d3J2J = truth_.missingP4_dPhi_d3J2J_GenJet();
    genJetStruct.missingP4_Pt_d3J2J = truth_.missingP4_Pt_d3J2J_GenJet();
    
    genJetStruct.dPhi_12 = truth_.dPhi_12_GenJet();
    genJetStruct.dPhi_13 = truth_.dPhi_13_GenJet();
    genJetStruct.dPhi_23 = truth_.dPhi_23_GenJet();
    genJetStruct.dPhi_max = truth_.dPhi_max_GenJet();
    genJetStruct.dPhi_min = truth_.dPhi_min_GenJet();
    genJetStruct.dPhi_min_max = truth_.dPhi_min_max_GenJet();

    genJetStruct.leadingDR = truth_.dR_genJetMatchingToJ1();
    genJetStruct.subLeadingDR = truth_.dR_genJetMatchingToJ2();
    genJetStruct.subSubLeadingDR = truth_.dR_genJetMatchingToJ3();

    return genJetStruct;

}

MVAVarStruct VBFTruthProducer::genParticleLevelMVAVars() {

    MVAVarStruct genParticleStruct;

    genParticleStruct.leadingJetPt = truth_.pt_genPartMatchingToJ1();
    genParticleStruct.subLeadingJetPt = truth_.pt_genPartMatchingToJ2();
    genParticleStruct.subSubLeadingJetPt = truth_.pt_genPartMatchingToJ2();

    genParticleStruct.leadingJetEta = truth_.eta_genPartMatchingToJ1();
    genParticleStruct.subLeadingJetEta = truth_.eta_genPartMatchingToJ2();
    genParticleStruct.subSubLeadingJetEta = truth_.eta_genPartMatchingToJ2();

    genParticleStruct.leadingJetPhi = truth_.phi_genPartMatchingToJ1();
    genParticleStruct.subLeadingJetPhi = truth_.phi_genPartMatchingToJ2();
    genParticleStruct.subSubLeadingJetPhi = truth_.phi_genPartMatchingToJ2();

    genParticleStruct.dR_12 = truth_.dR_J1J2_GenParticle();
    genParticleStruct.dR_13 = truth_.dR_J1J3_GenParticle();
    genParticleStruct.dR_23 = truth_.dR_J2J3_GenParticle();

    genParticleStruct.mjj_12 = truth_.mjj_J1J2_GenParticle();
    genParticleStruct.mjj_13 = truth_.mjj_J1J3_GenParticle();
    genParticleStruct.mjj_23 = truth_.mjj_J2J3_GenParticle();
    genParticleStruct.mjjj = truth_.mjjj_GenParticle();

    genParticleStruct.dEta_12 = truth_.dEta_J1J2_GenParticle();
    genParticleStruct.dEta_13 = truth_.dEta_J1J3_GenParticle();
    genParticleStruct.dEta_23 = truth_.dEta_J2J3_GenParticle();

    genParticleStruct.zepjj_12 = truth_.zepjj_J1J2_GenParticle();
    genParticleStruct.zepjj_13 = truth_.zepjj_J1J3_GenParticle();
    genParticleStruct.zepjj_23 = truth_.zepjj_J2J3_GenParticle();
    genParticleStruct.zepjjj = truth_.zepjjj_GenParticle();

    genParticleStruct.dPhijj_12 = (truth_.dPhijj_J1J2_GenParticle());
    genParticleStruct.dPhijj_13 = (truth_.dPhijj_J1J3_GenParticle());
    genParticleStruct.dPhijj_23 = (truth_.dPhijj_J2J3_GenParticle());
    genParticleStruct.dPhijjj = (truth_.dPhijjj_GenParticle());

    genParticleStruct.leadingJetHemisphere = truth_.hemisphere_J1_GenParticle();
    genParticleStruct.subLeadingJetHemisphere = truth_.hemisphere_J2_GenParticle();
    genParticleStruct.subSubLeadingJetHemisphere = truth_.hemisphere_J3_GenParticle();

    genParticleStruct.oppHemispheres_J1J2 = truth_.oppHemispheres_J12_GenParticle();
    genParticleStruct.oppHemispheres_J1J3 = truth_.oppHemispheres_J13_GenParticle();
    genParticleStruct.oppHemispheres_J2J3 = truth_.oppHemispheres_J23_GenParticle();

    genParticleStruct.dEta_J1J2J3 = truth_.dEta_J1J2J3_GenParticle();
    genParticleStruct.dEta_J2J3J1 = truth_.dEta_J2J3J1_GenParticle();
    genParticleStruct.dEta_J3J1J2 = truth_.dEta_J3J1J2_GenParticle();

    genParticleStruct.mjj_d12_13plus23 = truth_.mjj_d12_13plus23_GenParticle();
    genParticleStruct.mjj_d12_13 = truth_.mjj_d12_13_GenParticle();
    genParticleStruct.mjj_d12_23 = truth_.mjj_d12_23_GenParticle();
    genParticleStruct.mjj_d13_23 = truth_.mjj_d13_23_GenParticle();

    genParticleStruct.dR_DP_12   = truth_.dR_DP_12_GenParticle();
    genParticleStruct.dR_DP_13   = truth_.dR_DP_13_GenParticle();
    genParticleStruct.dR_DP_23   = truth_.dR_DP_23_GenParticle();

    genParticleStruct.dR_Ph1_1 = truth_.dR_Ph1_1_GenParticle();
    genParticleStruct.dR_Ph1_2 = truth_.dR_Ph1_2_GenParticle();
    genParticleStruct.dR_Ph1_3 = truth_.dR_Ph1_3_GenParticle();
    genParticleStruct.dR_Ph2_1 = truth_.dR_Ph2_1_GenParticle();
    genParticleStruct.dR_Ph2_2 = truth_.dR_Ph2_2_GenParticle();
    genParticleStruct.dR_Ph2_3 = truth_.dR_Ph2_3_GenParticle();

    genParticleStruct.dR_DP_123 = truth_.dR_DP_123_GenParticle();

    genParticleStruct.missingP4_dPhi_jjj = truth_.missingP4_dPhi_jjj_GenParticle();
    genParticleStruct.missingP4_dPhi_jj = truth_.missingP4_dPhi_jj_GenParticle();
    genParticleStruct.missingP4_Pt_jjj = truth_.missingP4_Pt_jjj_GenParticle();
    genParticleStruct.missingP4_Pt_jj = truth_.missingP4_Pt_jj_GenParticle();
    genParticleStruct.missingP4_dPhi_d3J2J = truth_.missingP4_dPhi_d3J2J_GenParticle();
    genParticleStruct.missingP4_Pt_d3J2J = truth_.missingP4_Pt_d3J2J_GenParticle();
    
    genParticleStruct.dPhi_12 = truth_.dPhi_12_GenParticle();
    genParticleStruct.dPhi_13 = truth_.dPhi_13_GenParticle();
    genParticleStruct.dPhi_23 = truth_.dPhi_23_GenParticle();
    genParticleStruct.dPhi_max = truth_.dPhi_max_GenParticle();
    genParticleStruct.dPhi_min = truth_.dPhi_min_GenParticle();
    genParticleStruct.dPhi_min_max = truth_.dPhi_min_max_GenParticle();

    genParticleStruct.leadingDR = truth_.dR_particleMatchingToJ1();
    genParticleStruct.subLeadingDR = truth_.dR_particleMatchingToJ2();
    genParticleStruct.subSubLeadingDR = truth_.dR_particleMatchingToJ3();

    return genParticleStruct;

}

MVAVarStruct VBFTruthProducer::partonLevelMVAVars() {

    MVAVarStruct partonStruct;

    partonStruct.leadingJetPt = truth_.pt_P1();
    partonStruct.subLeadingJetPt = truth_.pt_P2();
    partonStruct.subSubLeadingJetPt = truth_.pt_P3();

    partonStruct.leadingJetEta = truth_.eta_P1();
    partonStruct.subLeadingJetEta = truth_.eta_P2();
    partonStruct.subSubLeadingJetEta = truth_.eta_P3();

    partonStruct.leadingJetPhi = truth_.phi_P1();
    partonStruct.subLeadingJetPhi = truth_.phi_P2();
    partonStruct.subSubLeadingJetPhi = truth_.phi_P3();

    partonStruct.dR_12 = truth_.dR_P1P2_Partons();
    partonStruct.dR_13 = truth_.dR_P1P3_Partons();
    partonStruct.dR_23 = truth_.dR_P2P3_Partons();

    partonStruct.mjj_12 = truth_.mjj_P1P2_Partons();
    partonStruct.mjj_13 = truth_.mjj_P1P3_Partons();
    partonStruct.mjj_23 = truth_.mjj_P2P3_Partons();
    partonStruct.mjjj = truth_.mjjj_Partons();

    partonStruct.dEta_12 = truth_.dEta_P1P2_Partons();
    partonStruct.dEta_13 = truth_.dEta_P1P3_Partons();
    partonStruct.dEta_23 = truth_.dEta_P2P3_Partons();

    partonStruct.zepjj_12 = truth_.zepjj_P1P2_Partons();
    partonStruct.zepjj_13 = truth_.zepjj_P1P3_Partons();
    partonStruct.zepjj_23 = truth_.zepjj_P2P3_Partons();
    partonStruct.zepjjj = truth_.zepjjj_Partons();

    partonStruct.dPhijj_12 = (truth_.dPhijj_P1P2_Partons());
    partonStruct.dPhijj_13 = (truth_.dPhijj_P1P3_Partons());
    partonStruct.dPhijj_23 = (truth_.dPhijj_P2P3_Partons());
    partonStruct.dPhijjj = (truth_.dPhijjj_Partons());

    partonStruct.leadingJetHemisphere = truth_.hemisphere_P1();
    partonStruct.subLeadingJetHemisphere = truth_.hemisphere_P2();
    partonStruct.subSubLeadingJetHemisphere = truth_.hemisphere_P3();

    partonStruct.oppHemispheres_J1J2 = truth_.oppHemispheres_P12();
    partonStruct.oppHemispheres_J1J3 = truth_.oppHemispheres_P13();
    partonStruct.oppHemispheres_J2J3 = truth_.oppHemispheres_P23();

    partonStruct.dEta_J1J2J3 = truth_.dEta_P1P2P3_Partons();
    partonStruct.dEta_J2J3J1 = truth_.dEta_P2P3P1_Partons();
    partonStruct.dEta_J3J1J2 = truth_.dEta_P3P1P2_Partons();

    partonStruct.mjj_d12_13plus23 = truth_.mjj_d12_13plus23_Partons();
    partonStruct.mjj_d12_13 = truth_.mjj_d12_13_Partons();
    partonStruct.mjj_d12_23 = truth_.mjj_d12_23_Partons();
    partonStruct.mjj_d13_23 = truth_.mjj_d13_23_Partons();

    partonStruct.dR_DP_12   = truth_.dR_DP_12_Partons();
    partonStruct.dR_DP_13   = truth_.dR_DP_13_Partons();
    partonStruct.dR_DP_23   = truth_.dR_DP_23_Partons();

    partonStruct.dR_Ph1_1 = truth_.dR_Ph1_1_Partons();
    partonStruct.dR_Ph1_2 = truth_.dR_Ph1_2_Partons();
    partonStruct.dR_Ph1_3 = truth_.dR_Ph1_3_Partons();
    partonStruct.dR_Ph2_1 = truth_.dR_Ph2_1_Partons();
    partonStruct.dR_Ph2_2 = truth_.dR_Ph2_2_Partons();
    partonStruct.dR_Ph2_3 = truth_.dR_Ph2_3_Partons();

    partonStruct.dR_DP_123 = truth_.dR_DP_123_Partons();

    partonStruct.missingP4_dPhi_jjj = truth_.missingP4_dPhi_jjj_Partons();
    partonStruct.missingP4_dPhi_jj = truth_.missingP4_dPhi_jj_Partons();
    partonStruct.missingP4_Pt_jjj = truth_.missingP4_Pt_jjj_Partons();
    partonStruct.missingP4_Pt_jj = truth_.missingP4_Pt_jj_Partons();
    partonStruct.missingP4_dPhi_d3J2J = truth_.missingP4_dPhi_d3J2J_Partons();
    partonStruct.missingP4_Pt_d3J2J = truth_.missingP4_Pt_d3J2J_Partons();
    
    partonStruct.dPhi_12 = truth_.dPhi_12_Partons();
    partonStruct.dPhi_13 = truth_.dPhi_13_Partons();
    partonStruct.dPhi_23 = truth_.dPhi_23_Partons();
    partonStruct.dPhi_max = truth_.dPhi_max_Partons();
    partonStruct.dPhi_min = truth_.dPhi_min_Partons();
    partonStruct.dPhi_min_max = truth_.dPhi_min_max_Partons();

    partonStruct.leadingDR = truth_.dR_partonMatchingToJ1();
    partonStruct.subLeadingDR = truth_.dR_partonMatchingToJ2();
    partonStruct.subSubLeadingDR = truth_.dR_partonMatchingToJ3();

    return partonStruct;

}








