# ================================================
#   MicroAOD and Jet Tree Producer
#   Y. Haddad 01/2015
# ================================================

import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils

process = cms.Process("FLASHggJetValidation")
process.load("FWCore.MessageService.MessageLogger_cfi")

# +++++ the number of processed events
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32( -1 ) )
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 100 )

# +++++ the input source file
process.source = cms.Source("PoolSource",                fileNames=cms.untracked.vstring("file:/afs/cern.ch/work/y/yhaddad/JobSending/HggPUJIDValPhys14/crab_Phys14MicroAODV1_VBF_HToGG_M-125_13TeV-powheg-pythia6_00/results/JetValidationMicroAOD_1.root")) 
#fileNames=cms.untracked.vstring("file:/afs/cern.ch/work/y/yhaddad/JobSending/HggPUJIDValPhys14/crab_Phys14MicroAODV1_GluGluToHToGG_M-125_13TeV-powheg-pythia6_00/results/JetValidationMicroAOD_1.root")) 

process.MessageLogger.cerr.threshold = 'ERROR'


process.load("flashgg/MicroAODProducers/flashggTkVtxMap_cfi") 
process.load("flashgg/MicroAODProducers/flashggPhotons_cfi")
process.load("flashgg/MicroAODProducers/flashggDiPhotons_cfi")
process.load("flashgg/MicroAODProducers/flashggPreselectedDiPhotons_cfi")
process.load("flashgg/MicroAODProducers/flashggElectrons_cfi")

process.TFileService = cms.Service("TFileService",fileName = cms.string("/afs/cern.ch/work/y/yhaddad/VBF_HToGG_M-125_13TeV_JetValidationTree_v02.root"))
#cms.string("/afs/cern.ch/work/y/yhaddad/TEST_GluGluToHToGG_M-125_13TeV_JetValidationTree_v02.root"))
#process.flashggPFCollAnalyzer = cms.EDAnalyzer('FlashggFlashggPFCollAnalyzer',
#                                               CollTagPF         = cms.InputTag("packedPFCandidates"),
#                                               CollTagPFPFCHS0   = cms.InputTag("pfNoElectronsCHS0"),
#                                               CollTagPFPFCHSLeg = cms.InputTag("pfNoElectronsCHSLeg"),
#                                           )

process.out = cms.OutputModule("PoolOutputModule", 
                               #fileName = cms.untracked.string('myMicroAODOutputFile.root'),
                               fileName = cms.untracked.vstring(),
                               outputCommands = cms.untracked.vstring())

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True)
)

process.p = cms.Path(
    #process.flashggPFCollAnalyzer +
    process.flashggJetValidationTreeMaker +
    process.flashggJetValidationTreeMakerPFCHS0 +
    process.flashggJetValidationTreeMakerPFCHSLeg 
)

#process.e = cms.EndPath(process.out)
