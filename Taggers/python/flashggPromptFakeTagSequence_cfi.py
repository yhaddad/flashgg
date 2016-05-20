import FWCore.ParameterSet.Config as cms
from flashgg.Taggers.flashggDiPhotonMVA_cfi import flashggDiPhotonMVA
from flashgg.Taggers.flashggVBFMVA_cff import flashggVBFMVA,flashggVBFDiPhoDiJetMVA
from flashgg.Taggers.flashggPreselectOnePhotonOnly_cfi import flashggPreselectOnePhotonOnly
from flashgg.Taggers.flashggUpdatedIdMVADiPhotons_cfi import flashggUpdatedIdMVADiPhotons
from flashgg.Taggers.flashggTags_cff import *

flashggPromptFakeTagSequence = cms.Sequence(flashggUpdatedIdMVADiPhotons
                                  * flashggPreselectOnePhotonOnly
				  * flashggDiPhotonMVA
                                  * flashggUnpackedJets
                                  * flashggVBFMVA
                                  * flashggVBFDiPhoDiJetMVA
                                  )

