import FWCore.ParameterSet.Config as cms

from flashgg.TagAlgos.DiPhotonMVATrainingDumpConf_cff import DiPhotonMVATrainingDumpConf

DiPhotonMVADumper = cms.EDAnalyzer('CutBasedDiPhotonMVAResultDumper',
                                **DiPhotonMVATrainingDumpConf.parameters_()
                                )


