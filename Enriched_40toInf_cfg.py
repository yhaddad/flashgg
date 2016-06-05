# ================================================
#   Both jet tree and VBF tree at the same time
#   Y. Haddad 01/2015, S Zenz 04/2016
# ================================================

from sys import argv
print argv
myfilenum = str(argv[2])
outdir  = "/vols/cms/es811/PromptFake3Jun16/"
outname = "Enriched_40toInf_file"
#files are 1-484

import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils

process = cms.Process("FLASHggJetValidation")

# +++++ the number of processed events
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32( 1000 ) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32( -1 ) )
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 100 )
process.MessageLogger.cerr.threshold = 'ERROR'

# +++++ the source file
process.source = cms.Source("PoolSource",
                            fileNames=cms.untracked.vstring("root://eoscms.cern.ch//eos/cms//store/group/phys_higgs/cmshgg/ferriff/flashgg/RunIIFall15DR76-1_3_0-25ns_ext1/1_3_1/QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8/RunIIFall15DR76-1_3_0-25ns_ext1-1_3_1-v0-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/160127_023814/0000/myMicroAODOutputFile_"+myfilenum+".root"))

process.TFileService = cms.Service("TFileService", fileName = cms.string(outdir+outname+myfilenum+".root")) 

process.load("flashgg/Taggers/flashggPromptFakeTagSequence_cfi")
process.load("flashgg/MicroAOD/flashggParameterisedFakePhotons_cfi")
process.load("flashgg/MicroAOD/flashggParameterisedPromptFakeDiPhotons_cfi")

from PhysicsTools.PatAlgos.tools.helpers import massSearchReplaceAnyInputTag
#massSearchReplaceAnyInputTag( process.flashggPromptFakeTagSequence, cms.InputTag("flashggDiPhotons"), cms.InputTag("flashggParameterisedPromptFakeDiPhotons") )
massSearchReplaceAnyInputTag( process.flashggPromptFakeTagSequence, cms.InputTag("flashggUpdatedIdMVADiPhotons"), cms.InputTag("flashggParameterisedPromptFakeDiPhotons") )

from flashgg.Taggers.flashggTags_cff import UnpackedJetCollectionVInputTag
process.flashggJetValidationTreeMakerPFCHS = cms.EDAnalyzer('FlashggJetValidationTreeMaker',
                                                            GenParticleTag  = cms.untracked.InputTag('flashggPrunedGenParticles'),
                                                            #GenParticleTag  = cms.untracked.InputTag('prunedGenParticles'),
                                                            GenPhotonTag    = cms.untracked.InputTag('flashggGenPhotons'), # Ed
                                                            #GenPhotonTag    = cms.untracked.InputTag('packedGenParticles'), # Ed
                                                            DiPhotonTag     = cms.InputTag('flashggPreselectedDiPhotons'), #Ed
                                                            #DiPhotonTag     = cms.InputTag('flashggPreselectOnePhotonOnly'),
                                                            inputTagJets    = UnpackedJetCollectionVInputTag,
                                                            StringTag	    = cms.string("PFCHS"),
                                                            VBFMVAResultTag = cms.InputTag('flashggVBFMVA'),
                                                            #MVAResultTag    = cms.InputTag('flashggDiPhotonMVA'),
                                                            MVAResultTag    = cms.InputTag('flashggParameterisedDiPhotonMVA'),
                                                            VBFDiPhoDiJetMVAResultTag = cms.InputTag('flashggVBFDiPhoDiJetMVA'),
                                                            )

process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
                                                      flashggParameterisedFakePhotons = cms.PSet(
                                                          initialSeed = cms.untracked.uint32(178),
                                                          engineName  = cms.untracked.string('TRandom3')
                                                      ),
                                                      flashggParameterisedDiPhotonMVA = cms.PSet(
                                                          initialSeed = cms.untracked.uint32(31735),
                                                          engineName  = cms.untracked.string('TRandom3')
                                                      ),
                                                      flashggJetValidationTreeMakerPFCHS = cms.PSet(
                                                          initialSeed = cms.untracked.uint32(60267),
                                                          engineName  = cms.untracked.string('TRandom3')
                                                      ),
                                                  )

process.options = cms.untracked.PSet( allowUnscheduled = cms.untracked.bool(True) )

process.p = cms.Path( 
    process.flashggParameterisedFakePhotons *
    process.flashggParameterisedPromptFakeDiPhotons *
    process.flashggPromptFakeTagSequence *
    process.flashggJetValidationTreeMakerPFCHS
    )

