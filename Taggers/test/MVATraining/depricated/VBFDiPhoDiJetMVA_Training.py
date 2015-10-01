import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils
import FWCore.ParameterSet.VarParsing as VarParsing

from flashgg.MetaData.samples_utils import SamplesManager

process = cms.Process("VBFDiPhoDiJetMVATraining")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.GlobalTag.globaltag = 'POSTLS170_V5::All'

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.source    = cms.Source ("PoolSource",
                                fileNames = cms.untracked.vstring())


from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc')

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("histo.root"),
                                   closeFileFast = cms.untracked.bool(True)
)

process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1)

import flashgg.Taggers.dumperConfigTools as cfgTools


process.load("flashgg.Taggers.flashggTagSequence_cfi")
process.load("flashgg.Taggers.flashggTagTester_cfi")

process.flashggVBFMVANew.UseLegacyMVA = cms.untracked.bool(True)
process.flashggVBFMVA.UseLegacyMVA    = cms.untracked.bool(True)

from flashgg.Taggers.flashggTagOutputCommands_cff import tagDefaultOutputCommand

process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('myTagOutputFile.root'),
                               outputCommands = tagDefaultOutputCommand			       
                               )

process.load("flashgg.Taggers.VBFMVADumperNew_cff")
process.VBFMVADumperNew.dumpTrees     = True
process.VBFMVADumperNew.dumpWorkspace = False
process.VBFMVADumperNew.quietRooFit   = True
process.VBFMVADumperNew.nameTemplate  = "$PROCESS_$SQRTS_$LABEL_$SUBCAT"

preselection_cut = str("dijet_LeadJPt    > 30  && dijet_SubJPt  > 20"   +
                       "&& dijet_leadEta < 4.7 && dijet_leadEta > -4.7" + 
                       "&& dijet_leadEta < 4.7 && dijet_leadEta > -4.7" +
                       "&& dijet_Mjj     > 250 && leadPho_PToM  > 0.5")

cfgTools.addCategories(process.VBFMVADumperNew,
                       [
                           ("VBFDiJet"           ,"dijet_LeadJPt > 0",0),
                           ("PreselectedVBFDiJet",preselection_cut   ,0),
                           ("expluded","1",0) # really importent to avoid having an error
                       ],
                       variables=[
                           "dijet_abs_dEta   :=  dijet_abs_dEta   ",
                           "dijet_leadEta    :=  dijet_leadEta    ",
                           "dijet_subleadEta :=  dijet_subleadEta ",
                           "dijet_LeadJPt    :=  dijet_LeadJPt    ",
                           "dijet_SubJPt     :=  dijet_SubJPt     ",
                           "dijet_Zep        :=  dijet_Zep        ",
                           "dijet_Mjj        :=  dijet_Mjj        ",
                           "dipho_PToM       :=  dipho_PToM       ",
                           "leadPho_PToM     :=  leadPho_PToM     ",
                           "sublPho_PToM     :=  sublPho_PToM     ",
                           "dijet_dPhi_trunc :=  dijet_dPhi_trunc ",
                           "vbfMvaResult_value      := vbfMvaResult_value",
                           "vbfMvaResult_value_bdt  := vbfMvaResult_value_bdt",
                           "vbfMvaResult_value_bdtg := vbfMvaResult_value_bdtg",
                       ],
                       histograms=[
                           "vbfMvaResult_value>>outputBDT(400,-1,1)",
                           "vbfMvaResult_value_bdt>>output_bdt(400,-1,1)",
                           "vbfMvaResult_value_bdtg>>output_bdtg(400,-1,1)",
                       ]
)
# split tree, histogram and datasets by process
process.VBFMVADumperNew.nameTemplate ="$PROCESS_$SQRTS_$LABEL_$SUBCAT"

#process.load("flashgg/Taggers/VBFDiPhoDiJetMVADumperNew_cff")
#
#process.VBFDiPhoDiJetMVADumperNew.dumpTrees     = True
#process.VBFDiPhoDiJetMVADumperNew.dumpWorkspace = False
#process.VBFDiPhoDiJetMVADumperNew.quietRooFit   = True
#
#cfgTools.addCategories(process.VBFDiPhoDiJetMVADumperNew,
#                       [
#                           ("All","dipho_PToM>=0",0),
#                       ],
#                       variables=[
#                           "dijet_mva :=  dijet_mva",
#                           "dipho_mva :=  dipho_mva",
#                           "dipho_PToM :=  dipho_PToM",
#                           "vbfDiPhoDiJetMvaResult := vbfDiPhoDiJetMvaResult",
#                       ],
#                       histograms=[
#                           "VBFDiPhoDiJetMVAResult>>VBFDiPhoDiJetMVAResult(400,-1,1)",
#                       ]
#)
## split tree, histogram and datasets by process
#process.VBFDiPhoDiJetMVADumperNew.nameTemplate = "$PROCESS_$SQRTS_$LABEL_$SUBCAT"

# customization for job splitting, lumi weighting, etc.
from flashgg.MetaData.JobConfig import customize

customize.setDefault("maxEvents",-1)
customize.setDefault("targetLumi",1.e+4)
customize(process)

process.p = cms.Path( process.flashggTagSequence*
                      process.VBFMVADumperNew
)

#process.e = cms.EndPath(process.out)

