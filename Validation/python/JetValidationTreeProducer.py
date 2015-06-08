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

# +++++ the source file
process.source = cms.Source("PoolSource", fileNames=cms.untracked.vstring(
        "/store/group/phys_higgs/cmshgg/yhaddad/flashgg/HggNewJetVal15/JetValMicroAOD/VBF_HToGG_M-125_13TeV-powheg-pythia6/HggNewJetVal15-JetValMicroAOD-v0-Phys14DR-PU20bx25_PHYS14_25_V1-v1/150606_103501/0000/myMicroAODOutputFile_1.root",
        "/store/group/phys_higgs/cmshgg/yhaddad/flashgg/HggNewJetVal15/JetValMicroAOD/VBF_HToGG_M-125_13TeV-powheg-pythia6/HggNewJetVal15-JetValMicroAOD-v0-Phys14DR-PU20bx25_PHYS14_25_V1-v1/150606_103501/0000/myMicroAODOutputFile_2.root",
        "/store/group/phys_higgs/cmshgg/yhaddad/flashgg/HggNewJetVal15/JetValMicroAOD/VBF_HToGG_M-125_13TeV-powheg-pythia6/HggNewJetVal15-JetValMicroAOD-v0-Phys14DR-PU20bx25_PHYS14_25_V1-v1/150606_103501/0000/myMicroAODOutputFile_3.root"))

process.MessageLogger.cerr.threshold = 'ERROR'

process.TFileService = cms.Service("TFileService",
                                   fileName  = cms.string("./workspace/VBF_HToGG_M-125_13TeV-powheg-pythia6-PU20bx25_PFLeg.root"))

jdebug=False
process.flashggJetValidationTreeMakerPF = cms.EDAnalyzer('FlashggJetValidationTreeMaker',
                                                         GenParticleTag        = cms.untracked.InputTag('prunedGenParticles'),
                                                         JetTagDz              = cms.InputTag("flashggJetsPF"),
                                                         StringTag	       = cms.string("PF"),
                                                         VertexCandidateMapTag = cms.InputTag("flashggVertexMapUnique"),
                                                         debug                 = cms.untracked.bool(jdebug),
                                                     )

process.flashggJetValidationTreeMakerPFCHS0 = cms.EDAnalyzer('FlashggJetValidationTreeMaker',
                                                             GenParticleTag     = cms.untracked.InputTag('prunedGenParticles'),
                                                             JetTagDz           = cms.InputTag("flashggJetsPFCHS0"),
                                                             StringTag		= cms.string("PFCHS0"),
                                                             VertexCandidateMapTag = cms.InputTag("flashggVertexMapUnique"),
                                                             debug                 = cms.untracked.bool(jdebug),
                                                         )

process.flashggJetValidationTreeMakerPFCHSLeg = cms.EDAnalyzer('FlashggJetValidationTreeMaker',
                                                               GenParticleTag = cms.untracked.InputTag('prunedGenParticles'),
                                                               JetTagDz       = cms.InputTag("flashggJets"),                  
                                                               StringTag	= cms.string("PFCHSLeg"),
                                                               VertexCandidateMapTag = cms.InputTag("flashggVertexMapUnique"),
                                                               debug                 = cms.untracked.bool(jdebug),
                                                           )

process.out = cms.OutputModule("PoolOutputModule", fileName = cms.untracked.string('./workspace/myMicroAODOutputFile.root'),
                               outputCommands = cms.untracked.vstring())

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True)
)

process.p = cms.Path(
    process.flashggJetValidationTreeMakerPF +
    process.flashggJetValidationTreeMakerPFCHS0 +
    process.flashggJetValidationTreeMakerPFCHSLeg 
)

process.e = cms.EndPath(process.out)
