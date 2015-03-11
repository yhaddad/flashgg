#!/usr/bin/env fwliteRun

import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
from flashgg.MetaData.samples_utils import SamplesManager
        
process = cms.Process("FWLitePlots")
process.fwliteInput = cms.PSet(
    fileNames = cms.vstring('file:myTagOutputFile.root'),
    maxEvents   = cms.int32(100),
    outputEvery = cms.uint32(1),
)

process.fwliteOutput = cms.PSet(
      fileName = cms.string("output.root")      ## mandatory
)

from flashgg.TagAlgos.VBFMVATrainingDumpConf_cff import VBFMVATrainingDumpConf
import flashgg.TagAlgos.dumperConfigTools as cfgTools
process.analyzer = VBFMVATrainingDumpConf
process.analyzer.dumpTrees = True
process.analyzer.dumpWorkspace = False
process.analyzer.quietRooFit = True
cfgTools.addCategories(process.analyzer,
                       [## cuts are applied in cascade
                           ("All","1",0),
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
                       ],
                       histograms=[
                           "mvaresult>>VBFMVAValue(100,-1,1)",
                       ]
                   )
# customization for job splitting, lumi weighting, etc.
from flashgg.MetaData.JobConfig import customize
customize.setDefault("maxEvents",500)
customize.setDefault("targetLumi",1.e+4)
customize(process)

