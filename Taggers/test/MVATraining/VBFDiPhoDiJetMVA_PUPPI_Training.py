import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils
import FWCore.ParameterSet.VarParsing as VarParsing

from flashgg.MetaData.samples_utils import SamplesManager

process = cms.Process("VBFDiPhoDiJetMVATrainingPUPPI")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.GlobalTag.globaltag = 'POSTLS170_V5::All'

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring())


from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc')

import flashgg.Taggers.dumperConfigTools as cfgTools
process.load("flashgg.Taggers.VBFMVADumperPUPPI_cff")

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("histo.root"),
                                   closeFileFast = cms.untracked.bool(True)
                               )

process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1)



#process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring( "/store/group/phys_higgs/cmshgg/sethzenz/flashgg/HggPhys14/Phys14MicroAODV2/VBF_HToGG_M-125_13TeV-powheg-pythia6/HggPhys14-Phys14MicroAODV2-v0-Phys14DR-PU20bx25_PHYS14_25_V1-v1/150210_160130/0000/myMicroAODOutputFile_1.root"))

process.load("flashgg/Taggers/flashggTagSequence_cfi")
process.load("flashgg/Taggers/flashggTagTester_cfi")

from flashgg.Taggers.flashggTagOutputCommands_cff import tagDefaultOutputCommand

process.out = cms.OutputModule("PoolOutputModule",
			fileName = cms.untracked.string('myTagOutputFile.root'),
			outputCommands = tagDefaultOutputCommand			       
			)


process.VBFMVADumperPUPPI.dumpTrees     = True
process.VBFMVADumperPUPPI.dumpWorkspace = False
process.VBFMVADumperPUPPI.quietRooFit   = True

cfgTools.addCategories(process.VBFMVADumperPUPPI,
                       [## cuts are applied in cascade
                           ("VBFPFCHS",
                            "dijet_LeadJPt > 30 && dijet_SubJPt > 20 && dijet_leadEta < 4.7 && dijet_leadEta > -4.7 && dijet_leadEta < 4.7 && dijet_leadEta > -4.7 && dijet_Mjj > 250 && leadPho_PToM > 0.5",0),
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
                           "vbfMvaResult_value := vbfMvaResult_value",
                           "vbfMvaResult_value_bdt  := vbfMvaResult_value_bdt",
                           "vbfMvaResult_value_bdtg := vbfMvaResult_value_bdtg",
                       ],
                       histograms=[
                           "vbfMvaResult_value_bdt >> output_bdt(400,-1,1)",
                           "vbfMvaResult_value_bdtg>> output_bdtg(400,-1,1)",
                       ]
)
# split tree, histogram and datasets by process
process.VBFMVADumperPUPPI.nameTemplate ="$PROCESS_$SQRTS_$LABEL_$SUBCAT"

process.load("flashgg/Taggers/VBFDiPhoDiJetMVADumperPUPPI_cff")

process.VBFDiPhoDiJetMVADumperPUPPI.dumpTrees = True
process.VBFDiPhoDiJetMVADumperPUPPI.dumpWorkspace = False
process.VBFDiPhoDiJetMVADumperPUPPI.quietRooFit = True

cfgTools.addCategories(process.VBFDiPhoDiJetMVADumperPUPPI,
			[## cuts are applied in cascade
			("All","dipho_PToM>=0",0),
			],
			variables=[
                            "dijet_mva  :=  dijet_mva",
                            "dipho_mva  :=  dipho_mva",
                            "dipho_PToM :=  dipho_PToM",
                            "vbfDiPhoDiJetMvaResult := vbfDiPhoDiJetMvaResult",
			],
			histograms=[
                            "VBFDiPhoDiJetMVAResult>>VBFDiPhoDiJetMVAResult(400,-1,1)",
			]
                   )
# split tree, histogram and datasets by process
process.VBFDiPhoDiJetMVADumperPUPPI.nameTemplate ="$PROCESS_$SQRTS_$LABEL_$SUBCAT"

# customization for job splitting, lumi weighting, etc.
from flashgg.MetaData.JobConfig import customize
customize.setDefault("maxEvents",-1)
customize.setDefault("targetLumi",1.e+4)
customize(process)

process.p = cms.Path(process.flashggTagSequence*
                     process.VBFMVADumperPUPPI*
                     process.VBFDiPhoDiJetMVADumperPUPPI
                 )

process.e = cms.EndPath(process.out)

