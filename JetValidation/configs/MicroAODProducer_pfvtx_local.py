# MicroAODProducer with the jets collections

import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils

process = cms.Process("FLASHggMicroAOD")
process.load("FWCore.MessageService.MessageLogger_cfi")

# the number of processed events
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32 ( 10000 ) )
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 100 )

# the source file
process.source = cms.Source("PoolSource",
                            fileNames=cms.untracked.vstring("/store/mc/Phys14DR/GluGluToHToGG_M-125_13TeV-powheg-pythia6/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/3C2EFAB1-B16F-E411-AB34-7845C4FC39FB.root"))

# can't get suppressWarning to work: disable all warnings for now
process.MessageLogger.cerr.threshold = 'ERROR'

# Uncomment the following if you notice you have a memory leak
# This is a lightweight tool to digg further

process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck",
                                        ignoreTotal = cms.untracked.int32(1),
                                        monitorPssAndPrivate = cms.untracked.bool(True))

# the cofigurations
# process.load("flashgg/MicroAODProducers/flashggVertexMaps_cfi")
# flashggTkVtxMap_cfi.py
process.load("flashgg/MicroAODProducers/flashggTkVtxMap_cfi") 
process.load("flashgg/MicroAODProducers/flashggPhotons_cfi")
process.load("flashgg/MicroAODProducers/flashggDiPhotons_cfi")
process.load("flashgg/MicroAODProducers/flashggPreselectedDiPhotons_cfi")
process.load("flashgg/MicroAODProducers/flashggElectrons_cfi")

# ---------> END  PF selectors <-------------------
process.selectedMuons = cms.EDFilter("CandPtrSelector", src = cms.InputTag("slimmedMuons"), cut = cms.string('''abs(eta)<2.5 && pt>10. &&
                                      (pfIsolationR04().sumChargedHadronPt+ max(0.,pfIsolationR04().sumNeutralHadronEt+
                                      pfIsolationR04().sumPhotonEt-
					 0.50*pfIsolationR04().sumPUPt))/pt < 0.20 && 
				(isPFMuon && (isGlobalMuon || isTrackerMuon) )'''))
process.selectedElectrons = cms.EDFilter("CandPtrSelector", src = cms.InputTag("slimmedElectrons"), cut = cms.string('''abs(eta)<2.5 && pt>20. &&
				gsfTrack.isAvailable() &&
				gsfTrack.hitPattern().numberOfLostHits(\'MISSING_INNER_HITS\') < 2 &&
				(pfIsolationVariables().sumChargedHadronPt+
				 max(0.,pfIsolationVariables().sumNeutralHadronEt+
					 pfIsolationVariables().sumPhotonEt-
					 0.5*pfIsolationVariables().sumPUPt))/pt < 0.15'''))


# The following is make patJets, but EI is done with the above
process.load("PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff")
process.load("Configuration.EventContent.EventContent_cff")
process.load('Configuration.StandardSequences.Geometry_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'PLS170_V7AN1::All'

# --------->  PFCHS 0 Candidates inputs validation <-------------------

process.pfCHS0 = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedPFCandidates"), cut = cms.string("fromPV"))

# then remove the previously selected muons
process.pfNoMuonCHS0 =  cms.EDProducer("CandPtrProjector", src = cms.InputTag("pfCHS0"), veto = cms.InputTag("selectedMuons"))

# then remove the previously selected electrons
process.pfNoElectronsCHS0 = cms.EDProducer("CandPtrProjector", src = cms.InputTag("pfNoMuonCHS0"), veto =  cms.InputTag("selectedElectrons"))
#
#---------> PFCHS Legacy VERTEX <-------------------
process.flashggCHSLegacyVertexCandidates = cms.EDProducer('FlashggCHSLegacyVertexCandidateProducer',
                                                          PFCandidatesTag=cms.untracked.InputTag('packedPFCandidates'),
                                                          DiPhotonTag=cms.untracked.InputTag('flashggDiPhotons'),
                                                          VertexCandidateMapTag = cms.InputTag("flashggVertexMapUnique"),
                                                          VertexTag=cms.untracked.InputTag('offlineSlimmedPrimaryVertices')
)

process.pfCHSLeg = cms.EDFilter("CandPtrSelector", src = cms.InputTag("flashggCHSLegacyVertexCandidates"), cut = cms.string(""))

# then remove the previously selected muons
process.pfNoMuonCHSLeg =  cms.EDProducer("CandPtrProjector", src = cms.InputTag("pfCHSLeg"), veto = cms.InputTag("selectedMuons"))

# then remove the previously selected electrons
process.pfNoElectronsCHSLeg = cms.EDProducer("CandPtrProjector", src = cms.InputTag("pfNoMuonCHSLeg"), veto =  cms.InputTag("selectedElectrons"))


#---------> Analyzers and tree producers <-------------------
process.TFileService = cms.Service("TFileService",fileName  = cms.string("/afs/cern.ch/work/y/yhaddad/PFVertexValidationTrees_VBF_HToGG.root"))


#process.vtxPF = cms.EDAnalyzer('FlashggFlashggPFCollAnalyzer',
#                               CollTagPF         = cms.InputTag("packedPFCandidates"),
#                               CollTagPFPFCHS0   = cms.InputTag("pfNoElectronsCHS0"),
#                               CollTagPFPFCHSLeg = cms.InputTag("pfNoElectronsCHSLeg"),
#)

process.vtxPF    = cms.EDAnalyzer('VertexForJetValidation',
                                  packedPFToken=cms.InputTag("packedPFCandidates"),
                                  StringTag          = cms.string("PF"))
process.vtxCHS0  = cms.EDAnalyzer('VertexForJetValidation',
                                  packedPFToken=cms.InputTag("packedPFCandidates"),
                                  StringTag          = cms.string("PFCHS0"))
process.vtxCHSLeg= cms.EDAnalyzer('VertexForJetValidation',
                                  packedPFToken=cms.InputTag("packedPFCandidates"),
                                  StringTag          = cms.string("PFCHSLeg"))

process.load("flashgg/MicroAODProducers/flashggMicroAODSequence_cff")

process.out = cms.OutputModule("PoolOutputModule", 
                               #fileName = cms.untracked.string('myMicroAODOutputFile.root'),
                               fileName = cms.untracked.vstring(),
                               outputCommands = cms.untracked.vstring())
process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True)
)

process.p = cms.Path( process.flashggMicroAODSequence +
                      process.vtxPF + 
                      process.vtxCHS0 +
                      process.vtxCHSLeg
                  )
#process.e = cms.EndPath(process.out)
