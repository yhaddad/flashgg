import FWCore.ParameterSet.Config as cms

from flashgg.Taggers.DiPhotonMVATrainingDumpConfPUPPI_cff import DiPhotonMVATrainingDumpConfPUPPI

DiPhotonMVADumperPUPPI = cms.EDAnalyzer('CutBasedDiPhotonMVAResultDumper',
                                        **DiPhotonMVATrainingDumpConfPUPPI.parameters_()
                                    )
