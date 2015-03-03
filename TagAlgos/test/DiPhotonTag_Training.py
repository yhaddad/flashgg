import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils

import FWCore.ParameterSet.VarParsing as VarParsing
from flashgg.MetaData.samples_utils import SamplesManager

process = cms.Process("TestDiPhotonMVATraining")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'POSTLS170_V5::All'
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
#process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring("file:test_vbfmvatraining/output_GJet_Pt40_doubleEMEnriched_TuneZ2star_13TeV-pythia6_numEvent100.root"))
process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring("file:myMicroAODOutputFile.root"))
process.load("flashgg/TagProducers/flashggTagSequence_cfi")
process.load("flashgg/TagProducers/flashggTagTester_cfi")
from flashgg.TagProducers.flashggTagOutputCommands_cff import tagDefaultOutputCommand
process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('myTagOutputFile.root'),
                               outputCommands = tagDefaultOutputCommand			       
                               )

import flashgg.TagAlgos.dumperConfigTools as cfgTools
process.load("flashgg/TagProducers/DiPhotonMVADumper_cff")
process.load("flashgg/TagProducers/flashggDiPhotonMVA_cfi")
process.TFileService = cms.Service("TFileService",
      fileName = cms.string("histo.root"),
			      closeFileFast = cms.untracked.bool(True)
						  )
process.DiPhotonMVADumper.dumpTrees = True
process.DiPhotonMVADumper.dumpWorkspace = False
process.DiPhotonMVADumper.quietRooFit = True

cfgTools.addCategories(process.DiPhotonMVADumper,
		[## cuts are applied in cascade
		("All","1",0),
		],
		variables=[
		"tes   :=  leadptom  ",
		],
		histograms=[
		"result>>DiPhotonMVAValue(100,-1,1)",
		]
		)
# split tree, histogram and datasets by process
process.DiPhotonMVADumper.nameTemplate ="$PROCESS_$SQRTS_$LABEL_$SUBCAT"

process.commissioning = cms.EDAnalyzer('test',
DiPhotonTag = cms.untracked.InputTag('flashggZeeDiPhotons','','FLASHggMicroAOD'),
)

# customization for job splitting, lumi weighting, etc.
from flashgg.MetaData.JobConfig import customize
customize.setDefault("maxEvents",-1)
customize.setDefault("targetLumi",1.e+4)
customize(process)
process.p = cms.Path(#process.flashggDiPhotonMVA*
			#process.DiPhotonMVADumper
			process.commissioning
			)

process.e = cms.EndPath(process.out)
