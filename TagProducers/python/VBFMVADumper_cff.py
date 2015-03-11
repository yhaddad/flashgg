import FWCore.ParameterSet.Config as cms

from flashgg.TagAlgos.VBFMVATrainingDumpConf_cff import VBFMVATrainingDumpConf

VBFMVADumper = cms.EDAnalyzer('CutBasedVBFMVAResultDumper',
                              **VBFMVATrainingDumpConf.parameters_()
                          )




