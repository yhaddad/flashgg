import FWCore.ParameterSet.Config as cms
from flashgg.Taggers.VBFDiPhoDiJetMVATrainingDumpConfPUPPI_cff import VBFDiPhoDiJetMVATrainingDumpConfPUPPI

VBFDiPhoDiJetMVADumperPUPPI = cms.EDAnalyzer('CutBasedVBFDiPhoDiJetMVAResultDumper',
                                             **VBFDiPhoDiJetMVATrainingDumpConfPUPPI.parameters_()
                                         )
