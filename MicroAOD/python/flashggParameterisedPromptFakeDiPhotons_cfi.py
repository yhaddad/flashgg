import FWCore.ParameterSet.Config as cms

flashggParameterisedPromptFakeDiPhotons = cms.EDProducer('FlashggParameterisedPromptFakeDiPhotonProducer',
                                  PromptPhotonTag        = cms.InputTag('flashggRandomizedPhotons'),
                                  FakePhotonTag          = cms.InputTag('flashggParameterisedFakePhotons'),
                                  VertexTag              = cms.InputTag('offlineSlimmedPrimaryVertices'),
                                  GenParticleTag         = cms.InputTag( "flashggPrunedGenParticles" ),
                                  )
