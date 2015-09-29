import FWCore.ParameterSet.Config as cms
from flashgg.Taggers.VBFMVATrainingDumpConfPUPPI_cff import VBFMVATrainingDumpConfPUPPI

VBFMVADumperPUPPI = cms.EDAnalyzer('CutBasedVBFMVAResultDumper',
                                   **VBFMVATrainingDumpConfPUPPI.parameters_()
                               )
