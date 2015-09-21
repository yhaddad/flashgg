import FWCore.ParameterSet.Config as cms
from flashgg.Taggers.flashggDiPhotonMVA_cfi import flashggDiPhotonMVA,flashggDiPhotonMVANew,flashggDiPhotonMVAPUPPI
from flashgg.Taggers.flashggVBFMVA_cff import flashggVBFMVA,flashggVBFMVANew, flashggVBFMVAPUPPI,flashggVBFDiPhoDiJetMVA, flashggVBFDiPhoDiJetMVANew, flashggVBFDiPhoDiJetMVAPUPPI

from flashgg.Taggers.flashggTags_cff import *
from flashgg.Taggers.flashggTagSorter_cfi import flashggTagSorter

flashggTagSequence = cms.Sequence(flashggDiPhotonMVA
				  * flashggDiPhotonMVANew
                                  * flashggDiPhotonMVAPUPPI
                                  * flashggUnpackedJets
                                  * flashggUnpackedPuppiJets
                                  * flashggVBFMVA
                                  * flashggVBFMVANew
                                  * flashggVBFMVAPUPPI
                                  * flashggVBFDiPhoDiJetMVA
                                  * flashggVBFDiPhoDiJetMVANew
                                  * flashggVBFDiPhoDiJetMVAPUPPI
                                  * ( flashggUntagged
                                      + flashggVBFTag
                                     + flashggTTHLeptonicTag
                                     + flashggVHEtTag
                                     + flashggTTHHadronicTag
                                     + flashggVHLooseTag
                                     + flashggVHTightTag
                                     + flashggVHHadronicTag
					)
                                 * flashggTagSorter
                                  )

