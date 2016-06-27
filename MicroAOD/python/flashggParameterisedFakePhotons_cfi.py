import FWCore.ParameterSet.Config as cms

flashggParameterisedFakePhotons = cms.EDProducer("FlashggParameterisedFakePhotonProducer",
                                    PhotonTag              = cms.InputTag('flashggRandomizedPhotons'),
                                    GenJetTag              = cms.InputTag('slimmedGenJets')
                                    )
