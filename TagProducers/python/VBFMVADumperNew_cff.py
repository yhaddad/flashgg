import FWCore.ParameterSet.Config as cms

from flashgg.TagAlgos.VBFMVATrainingDumpConfNew_cff import VBFMVATrainingDumpConfNew

VBFMVADumperNew = cms.EDAnalyzer('CutBasedVBFMVAResultDumper',
                                 **VBFMVATrainingDumpConfNew.parameters_()
                             )


