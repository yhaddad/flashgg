import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils

import FWCore.ParameterSet.VarParsing as VarParsing
from flashgg.MetaData.samples_utils import SamplesManager

process = cms.Process("TestVBFMVATraining")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'POSTLS170_V5::All'
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring())
process.load("flashgg/TagProducers/flashggTagSequence_cfi")
process.load("flashgg/TagProducers/flashggTagTester_cfi")
from flashgg.TagProducers.flashggTagOutputCommands_cff import tagDefaultOutputCommand
process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('myTagOutputFile.root'),
                               outputCommands = tagDefaultOutputCommand			       
                               )

import flashgg.TagAlgos.dumperConfigTools as cfgTools
process.load("flashgg/TagProducers/VBFMVADumper_cff")
process.TFileService = cms.Service("TFileService",
      fileName = cms.string("histo.root"),
			      closeFileFast = cms.untracked.bool(True)
						  )
process.VBFMVADumper.dumpTrees = True
process.VBFMVADumper.dumpWorkspace = False
process.VBFMVADumper.quietRooFit = True

cfgTools.addCategories(process.VBFMVADumper,
		[## cuts are applied in cascade
		("All","1",0),
		],
		variables=[
		"dijet_abs_dEta   :=  dijet_abs_dEta  ",
		"dijet_leadEta    :=  dijet_leadEta  ",
		"dijet_subleadEta :=  dijet_subleadEta  ",
		"dijet_LeadJPt    :=  dijet_LeadJPt    ",
		"dijet_SubJPt     :=  dijet_SubJPt     ",
		"dijet_Zep        :=  dijet_Zep        ",
		"dijet_Mjj        :=  dijet_Mjj        ",
		"dipho_PToM       :=  dipho_PToM     ",
		"leadPho_PToM     :=  leadPho_PToM     ",
		"sublPho_PToM     :=  sublPho_PToM     ",
		"dijet_dPhi_trunc :=  dijet_dPhi_trunc ",
		],
		histograms=[
		"mvaresult>>VBFMVAValue(100,-1,1)",
		]
		)
# split tree, histogram and datasets by process
process.VBFMVADumper.nameTemplate ="$PROCESS_$SQRTS_$LABEL_$SUBCAT"


# customization for job splitting, lumi weighting, etc.
from flashgg.MetaData.JobConfig import customize
customize.setDefault("maxEvents",-1)
customize.setDefault("targetLumi",1.e+4)
customize(process)
process.p = cms.Path(process.flashggTagSequence*
			process.VBFMVADumper
			)

process.e = cms.EndPath(process.out)
