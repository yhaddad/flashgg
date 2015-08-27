import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils

process = cms.Process("FLASHggMicroAOD")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")

from Configuration.AlCa.GlobalTag import GlobalTag

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32( 5000 ) )
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 1000 )
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc')

debug = False

# Fix because auto:run2_mc points to MCRUN2_74_V9::All
current_gt = process.GlobalTag.globaltag.value()
if current_gt.count("::All"):
    new_gt = current_gt.replace("::All","")
    print 'Removing "::All" from GlobalTag by hand for condDBv2: was %s, now %s' % (current_gt,new_gt)
    process.GlobalTag.globaltag = new_gt
    
    

process.source = cms.Source("PoolSource",
                            fileNames=cms.untracked.vstring(
                                "/store/mc/RunIISpring15DR74/VBFHToGG_M-125_13TeV_powheg_pythia8/MINIAODSIM/Asympt50ns_MCRUN2_74_V9A-v1/50000/049AAFAA-CA2D-E511-93E8-02163E00F402.root"
                                #"/store/mc/RunIISpring15DR74/QCD_Pt-15to7000_TuneCUETP8M1_Flat_13TeV_pythia8/MINIAODSIM/AsymptFlat0to50bx50Reco_MCRUN2_74_V9A-v3/00000/023F427F-0E08-E511-A813-0025905A60EE.root"
                            ),
                            skipEvents=cms.untracked.uint32(0))

process.MessageLogger.cerr.threshold = 'ERROR' 
# process.MessageLogger.suppressWarning.extend(['SimpleMemoryCheck','MemoryCheck'])

# This is a lightweight tool to digg further
#process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck",
#                                        ignoreTotal = cms.untracked.int32(1),
#                                        monitorPssAndPrivate = cms.untracked.bool(True)
#                                       )
process.load("flashgg/MicroAOD/flashggMicroAODSequence_cff")

from flashgg.MicroAOD.flashggMicroAODOutputCommands_cff import microAODDefaultOutputCommand
process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('workspace/myMicroAOD_puppi_validation_VBFHtoGG.root'),
                               outputCommands = microAODDefaultOutputCommand
                           )

process.TFileService = cms.Service("TFileService",fileName  = cms.string("workspace/trees_puppi_validation_VBFHtoGG.root"))

# need to allow unscheduled processes otherwise reclustering function will fail
# this is because of the jet clustering tool, and we have to live with it for now.
process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True)
)
# import function which takes care of reclustering the jets using legacy vertex		
from flashgg.MicroAOD.flashggJets_cfi import addFlashggPFCHSJets 
from flashgg.MicroAOD.flashggJets_cfi import addFlashggPuppiJets
from flashgg.MicroAOD.flashggJets_cfi import maxJetCollections
from flashgg.MicroAOD.flashggJets_cfi import PuppiJetCollectionVInputTag, JetCollectionVInputTag
# call the function, it takes care of everything else.


for vtx in range(0,maxJetCollections):
    addFlashggPFCHSJets (process = process,
                         vertexIndex =vtx,
                         doQGTagging = False,
                         label = '' + str(vtx))    
    
    addFlashggPuppiJets (process     = process,
                         vertexIndex = vtx,
                         debug       = debug,
                         label = '' + str(vtx))
    
#------------------------------------------------------------------------------------------------    
# run a standard puppi with the default seeting

from flashgg.MicroAOD.flashggExtraJets_cfi import addStandardPuppiJets
addStandardPuppiJets( process,
                      label = '',
                      debug = debug)

from flashgg.Taggers.flashggTags_cff       import UnpackedJetCollectionVInputTag   
from flashgg.MicroAOD.flashggExtraJets_cfi import StandardPUPIJetVInputTag

process.flashggJetTreeMakerPFCHS = cms.EDAnalyzer('FlashggJetValidationTreeMaker',
                                                  GenParticleTag = cms.untracked.InputTag('prunedGenParticles'),
                                                  DiPhotonTag    = cms.InputTag('flashggDiPhotons'),
                                                  inputTagJets   = JetCollectionVInputTag,
                                                  debug          = cms.untracked.bool(debug),
                                                  ZeroVertexOnly = cms.untracked.bool(True),
                                                  StringTag      = cms.string("PFCHS"))

process.flashggJetTreeMakerPUPPI = cms.EDAnalyzer('FlashggJetValidationTreeMaker',
                                                  GenParticleTag = cms.untracked.InputTag('prunedGenParticles'),
                                                  DiPhotonTag    = cms.InputTag('flashggDiPhotons'),
                                                  inputTagJets   = PuppiJetCollectionVInputTag,
                                                  debug          = cms.untracked.bool(debug),
                                                  ZeroVertexOnly = cms.untracked.bool(True),
                                                  StringTag      = cms.string("PUPPI"))

process.flashggJetTreeMakerSTDPUPPI = cms.EDAnalyzer('FlashggJetValidationTreeMaker',
                                                     GenParticleTag = cms.untracked.InputTag('prunedGenParticles'),
                                                     DiPhotonTag    = cms.InputTag('flashggDiPhotons'),
                                                     inputTagJets   = StandardPUPIJetVInputTag,#TmpJetVInputTag,
                                                     debug          = cms.untracked.bool(debug),
                                                     ZeroVertexOnly = cms.untracked.bool(True),
                                                     StringTag      = cms.string("STDPUPPI"))

process.p = cms.Path(process.flashggMicroAODSequence )#+
                     #process.flashggJetTreeMakerPFCHS +
                     #process.flashggJetTreeMakerPUPPI  +
                     #process.flashggJetTreeMakerSTDPUPPI  )
process.e = cms.EndPath(process.out)


from flashgg.MicroAOD.MicroAODCustomize import customize
customize(process)

