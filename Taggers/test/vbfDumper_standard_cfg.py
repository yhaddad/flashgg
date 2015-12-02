#!/usr/bin/env cmsRun

import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils
from FWCore.ParameterSet.VarParsing import VarParsing
from flashgg.MetaData.samples_utils import SamplesManager

process = cms.Process("VBFTagsDumper")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1))
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 1 )
process.source = cms.Source ("PoolSource",
                             fileNames = cms.untracked.vstring("/store/group/phys_higgs/cmshgg/sethzenz/flashgg/RunIISpring15-ReMiniAOD-BetaV7-25ns/Spring15BetaV7/VBFHToGG_M-125_13TeV_powheg_pythia8/RunIISpring15-ReMiniAOD-BetaV7-25ns-Spring15BetaV7-v0-RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/151021_152809/0000/myMicroAODOutputFile_1.root"))

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("VBFTagsDump.root"),
                                   closeFileFast = cms.untracked.bool(True))


from flashgg.Taggers.flashggTagOutputCommands_cff import tagDefaultOutputCommand
import flashgg.Taggers.dumperConfigTools as cfgTools
from  flashgg.Taggers.tagsDumpers_cfi import createTagDumper

process.load("flashgg.Taggers.flashggTagSequence_cfi")
process.load("flashgg.Taggers.flashggTagTester_cfi")

process.flashggVBFMVA.UseJetID      = cms.untracked.bool(True)
process.flashggVBFMVA.JetIDLevel    = cms.untracked.string("Loose")
process.flashggVBFMVA.vbfMVAweightfile = cms.FileInPath("flashgg/Taggers/test/VBFProduction/MVAWeights/Flashgg_VBF_CHS_BDTG.weights.xml")
process.flashggVBFMVA.MVAMethod        = cms.untracked.string("BDTG")

# the merging of the 3rd Jet
process.flashggVBFMVA.merge3rdJet   = cms.untracked.bool(False)
process.flashggVBFMVA.thirdJetDRCut = cms.untracked.double(1.5)

process.flashggVBFTag.Boundaries    = cms.untracked.vdouble(-2,0,2)
process.vbfTagDumper = createTagDumper("VBFTag")
process.vbfTagDumper.dumpTrees     = True
process.vbfTagDumper.dumpHistos    = True
process.vbfTagDumper.dumpWorkspace = False

from PhysicsTools.PatAlgos.tools.helpers import massSearchReplaceAnyInputTag
massSearchReplaceAnyInputTag(process.flashggTagSequence,cms.InputTag("flashggDiPhotons"),cms.InputTag("flashggPreselectedDiPhotons"))

dipho_variables=[
    "dipho_sumpt            := diPhoton.sumPt",
    "dipho_cosphi           := abs(cos(diPhoton.leadingPhoton.phi - diPhoton.subLeadingPhoton.phi))",
    "dipho_mass             := diPhoton.mass",
    "dipho_leadPt           := diPhoton.leadingPhoton.pt",
    "dipho_leadEt           := diPhoton.leadingPhoton.et",
    "dipho_leadEta          := diPhoton.leadingPhoton.eta",
    "dipho_leadPhi          := diPhoton.leadingPhoton.phi",
    "dipho_lead_sieie       := diPhoton.leadingPhoton.sigmaIetaIeta",
    "dipho_lead_hoe         := diPhoton.leadingPhoton.hadronicOverEm",
    "dipho_lead_sigmaEoE    := diPhoton.leadingPhoton.sigEOverE",
    "dipho_lead_ptoM        := diPhoton.leadingPhoton.pt/diPhoton.mass",
    "dipho_leadR9           := diPhoton.leadingPhoton.r9",
    "dipho_subleadPt        := diPhoton.subLeadingPhoton.pt",
    "dipho_subleadEt        := diPhoton.subLeadingPhoton.et",
    "dipho_subleadEta       := diPhoton.subLeadingPhoton.eta",
    "dipho_subleadPhi       := diPhoton.subLeadingPhoton.phi",
    "dipho_sublead_sieie    := diPhoton.subLeadingPhoton.sigmaIetaIeta",
    "dipho_sublead_hoe      := diPhoton.subLeadingPhoton.hadronicOverEm",
    "dipho_sublead_sigmaEoE := diPhoton.subLeadingPhoton.sigEOverE",
    "dipho_sublead_ptoM     := diPhoton.subLeadingPhoton.pt/diPhoton.mass",
    "dipho_subleadR9        := diPhoton.subLeadingPhoton.r9",
    "dipho_leadIDMVA        := diPhoton.leadingView.phoIdMvaWrtChosenVtx",
    "dipho_subleadIDMVA     := diPhoton.subLeadingView.phoIdMvaWrtChosenVtx",
    "dipho_lead_elveto      := diPhoton.leadingPhoton.passElectronVeto",
    "dipho_sublead_elveto   := diPhoton.subLeadingPhoton.passElectronVeto",
]

dijet_variables=[
    "dijet_abs_dEta         :=  abs(VBFMVA.dijet_leadEta - VBFMVA.dijet_subleadEta)",
    "dijet_leadEta          :=  VBFMVA.dijet_leadEta    ",
    "dijet_subleadEta       :=  VBFMVA.dijet_subleadEta ",
    "dijet_leady            :=  VBFMVA.dijet_leady      ",
    "dijet_subleady         :=  VBFMVA.dijet_subleady   ",
    "dijet_LeadJPt          :=  VBFMVA.dijet_LeadJPt    ",
    "dijet_SubJPt           :=  VBFMVA.dijet_SubJPt     ",
    "dijet_Zep              :=  VBFMVA.dijet_Zep        ",
    "dijet_Mjj              :=  VBFMVA.dijet_Mjj        ",
    "dipho_PToM             :=  VBFMVA.dipho_PToM       ",
    "leadPho_PToM           :=  VBFMVA.leadPho_PToM     ",
    "sublPho_PToM           :=  VBFMVA.sublPho_PToM     ",
    "dijet_dipho_dphi_trunc :=  VBFMVA.dijet_dphi_trunc ",
    "dijet_dipho_pt         :=  VBFMVA.dijet_dipho_pt   ",
    "dijet_dphi             :=  abs(deltaPhi(VBFMVA.leadJet.phi, VBFMVA.subleadJet.phi))",
    "dijet_dipho_dphi       :=  VBFMVA.dijet_dipho_dphi ",
    "dijet_dPhi_trunc       :=  VBFMVA.dijet_dphi_trunc ",
    "cos_dijet_dipho_dphi   :=  cos(VBFMVA.dijet_dipho_dphi)",
    "dijet_minDRJetPho      :=  VBFMVA.dijet_minDRJetPho",
    "has3Jet                :=  hasValidVBFTriJet",
    "dijet_mva              :=  VBFMVA.VBFMVAValue",
    "dipho_dijet_MVA        :=  VBFDiPhoDiJetMVA.VBFDiPhoDiJetMVAValue()",
    "dipho_mva              :=  diPhotonMVA.mvaValue()",
    "dijet_dipho_dphi_trunc :=  VBFMVA.dijet_dipho_dphi ",
    # new variables
    "jet1_pt             := leadingJet.pt",
    "jet2_pt             := subLeadingJet.pt",
    "jet3_pt             := subSubLeadingJet.pt",
    "jet1_eta            := leadingJet.eta",
    "jet2_eta            := subLeadingJet.eta",
    "jet3_eta            := subSubLeadingJet.eta",

    "jet1_pt_test        := tagTruth().pt_J1()",
 
    "J1J2_mjj            := tagTruth().mjj_J1J2_FggJet()",
    "J1J3_mjj            := tagTruth().mjj_J1J3_FggJet()",
    "J2J3_mjj            := tagTruth().mjj_J2J3_FggJet()",
    "Mjjj                := tagTruth().mjjj_FggJet()",
    
    "J1J2_dEta           := tagTruth().dEta_J1J2_FggJet()",
    "J1J3_dEta           := tagTruth().dEta_J1J3_FggJet()",
    "J2J3_dEta           := tagTruth().dEta_J2J3_FggJet()",

    "J1J2_Zep            := tagTruth().zepjj_J1J2_FggJet()",
    "J1J3_Zep            := tagTruth().zepjj_J1J3_FggJet()",
    "J2J3_Zep            := tagTruth().zepjj_J2J3_FggJet()",

    "J1J2J3_Zep          := tagTruth().zepjjj_FggJet()",

    "J1J2_dipho_dPhi     := tagTruth().dPhijj_J1J2_FggJet()",
    "J1J3_dipho_dPhi     := tagTruth().dPhijj_J1J3_FggJet()",
    "J2J3_dipho_dPhi     := tagTruth().dPhijj_J2J3_FggJet()",
    
    "J1J2J3_dipho_dPhi   := tagTruth().dPhijjj_FggJet()",
    
    "J1J2_dR             := tagTruth().dR_J1J2_FggJet()",
    "J1J3_dR             := tagTruth().dR_J1J3_FggJet()",
    "J2J3_dR             := tagTruth().dR_J2J3_FggJet()",
    
    "dEta_J1_J2J3        := tagTruth().dEta_J1J2J3_FggJet()",
    "dEta_J2_J3J1        := tagTruth().dEta_J2J3J1_FggJet()",
    "dEta_J3_J1J2        := tagTruth().dEta_J3J1J2_FggJet()",

    "dEta_dJ1_J2J3       := tagTruth().dEta_dJ1_J2J3_FggJet()",
    "dEta_dJ2_J3J1       := tagTruth().dEta_dJ2_J3J1_FggJet()",
    "dEta_dJ3_J1J2       := tagTruth().dEta_dJ3_J1J2_FggJet()",

    "dMjj_d12_13plus23   := tagTruth().mjj_d12_13plus23_FggJet()",
    "dMjj_d12_13         := tagTruth().mjj_d12_13_FggJet()",
    "dMjj_d12_23         := tagTruth().mjj_d12_23_FggJet()",
    "dMjj_d13_23         := tagTruth().mjj_d13_23_FggJet()",

    "dR_dipho_dijet12    := tagTruth().dR_DP_12_FggJet()",
    "dR_dipho_dijet13    := tagTruth().dR_DP_13_FggJet()",
    "dR_dipho_dijet23    := tagTruth().dR_DP_23_FggJet()",

    "dR_Photon1_J1       := tagTruth().dR_Ph1_1_FggJet()",
    "dR_Photon1_J2       := tagTruth().dR_Ph1_2_FggJet()",
    "dR_Photon1_J3       := tagTruth().dR_Ph1_3_FggJet()",
    "dR_Photon2_J1       := tagTruth().dR_Ph2_1_FggJet()",
    "dR_Photon2_J2       := tagTruth().dR_Ph2_2_FggJet()",
    "dR_Photon2_J3       := tagTruth().dR_Ph2_3_FggJet()",

    "dR_dipho_trijet     := tagTruth().dR_DP_123_FggJet()",

    "misPt_dPhi_3J       := tagTruth().missingP4_dPhi_jjj_FggJet()",
    "misPt_dPhi_2J       := tagTruth().missingP4_dPhi_jj_FggJet()",
    "misPt_mag_3J        := tagTruth().missingP4_Pt_jjj_FggJet()",
    "misPt_mag_2J        := tagTruth().missingP4_Pt_jj_FggJet()",

    "misPt_dPhi_d3J2J    := tagTruth().missingP4_dPhi_d3J2J_FggJet()",
    "misPt_mag_d3J2J     := tagTruth().missingP4_Pt_d3J2J_FggJet()",

    "dPhi_J1_J2          := tagTruth().dPhi_12_FggJet()",
    "dPhi_J1_J3          := tagTruth().dPhi_13_FggJet()",
    "dPhi_J2_J3          := tagTruth().dPhi_23_FggJet()",

    "dPhi_max_jets       := tagTruth().dPhi_max_FggJet()",
    "dPhi_min_jets       := tagTruth().dPhi_min_FggJet()",

    "momentum4Volume     := tagTruth().simplex_volume_DP_12_FggJet()",

    "dR_min_J12J23       := tagTruth().dR_min_J13J23_FggJet()",

    "dRToNearestPartonJ1 := tagTruth().dR_partonMatchingToJ1()",
    "dRToNearestPartonJ2 := tagTruth().dR_partonMatchingToJ2()",
    "dRToNearestPartonJ3 := tagTruth().dR_partonMatchingToJ3()",

    "numberOfMatches     := tagTruth().numberOfMatchesAfterDRCut(0.5)",

    # tag truth information
    "genZ                                 := tagTruth().genPV().z", # try that !!
    "pt_genJetMatchingToJ1                := tagTruth().pt_genJetMatchingToJ1",
    "pt_genJetMatchingToJ2                := tagTruth().pt_genJetMatchingToJ2",
    "pt_genJetMatchingToJ3                := tagTruth().pt_genJetMatchingToJ3",
    "eta_genJetMatchingToJ1               := tagTruth().eta_genJetMatchingToJ1",
    "eta_genJetMatchingToJ2               := tagTruth().eta_genJetMatchingToJ2",
    "eta_genJetMatchingToJ3               := tagTruth().eta_genJetMatchingToJ3",
    "hasClosestGenJetToLeadingJet         := tagTruth().hasClosestGenJetToLeadingJet",
    "hasClosestGenJetToSubLeadingJet      := tagTruth().hasClosestGenJetToSubLeadingJet",
    "hasClosestParticleToLeadingJet       := tagTruth().hasClosestParticleToLeadingJet",
    "hasClosestParticleToSubLeadingJet    := tagTruth().hasClosestParticleToSubLeadingJet",
    "hasClosestParticleToLeadingPhoton    := tagTruth().hasClosestParticleToLeadingPhoton",
    "hasClosestParticleToSubLeadingPhoton := tagTruth().hasClosestParticleToSubLeadingPhoton",
    "Mjj := sqrt((leadingJet.energy+subLeadingJet.energy)^2-(leadingJet.px+subLeadingJet.px)^2-(leadingJet.py+subLeadingJet.py)^2-(leadingJet.pz+subLeadingJet.pz)^2)"
    ]
cfgTools.addCategories(process.vbfTagDumper,
                       [
                           ("VBFDiJet","leadingJet.pt>0",0),
                           ("excluded","1",0)
                       ],
                       variables  = dipho_variables + dijet_variables,
                       histograms = []
)

#process.vbfTagDumper.nameTemplate ="$PROCESS_$SQRTS_$LABEL_$SUBCAT_$CLASSNAME"
process.vbfTagDumper.nameTemplate = "$PROCESS_$SQRTS_$CLASSNAME_$SUBCAT_$LABEL"

from flashgg.MetaData.JobConfig import customize
customize.setDefault("maxEvents",100)
customize.setDefault("targetLumi",2.11e+3)
customize(process)

process.p1 = cms.Path(
    process.flashggTagSequence*
#    process.flashggTagTester*
    process.vbfTagDumper
)

print process.p1
