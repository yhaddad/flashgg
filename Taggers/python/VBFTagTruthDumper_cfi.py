import FWCore.ParameterSet.Config as cms
from flashgg.Taggers.VBFTagTruthDumpConfig_cff import VBFTagTruthDumpConf

VBFTagTruthDumper = cms.EDAnalyzer('CutBasedVBFTagTruthDumper',
                                   **VBFTagTruthDumpConf.parameters_()
)
