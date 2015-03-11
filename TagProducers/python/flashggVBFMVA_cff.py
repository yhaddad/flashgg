import FWCore.ParameterSet.Config as cms


# the legacy MVA 
flashggVBFMVA = cms.EDProducer('FlashggVBFMVAProducer',
                               DiPhotonTag      = cms.untracked.InputTag('flashggDiPhotons'),
                               JetTag           = cms.untracked.InputTag('flashggJets'),
                               UseLegacyMVA     = cms.untracked.bool(True),
                               MinDijetMinv     = cms.double(0.0),
                               vbfMVAweightfile = cms.FileInPath("flashgg/TagProducers/data/TMVA_dijet_sherpa_scalewt50_2evenb_powheg200_maxdPhi_oct9_Gradient.weights.xml"),
                           )

# the new MVA
flashggVBFMVANew = cms.EDProducer('FlashggVBFMVAProducer',
                                  DiPhotonTag      = cms.untracked.InputTag('flashggDiPhotons'),
                                  JetTag           = cms.untracked.InputTag('flashggJets'),
                                  UseLegacyMVA     = cms.untracked.bool(False),
                                  MinDijetMinv     = cms.double(0.0),
                                  vbfMVAweightfile = cms.FileInPath("flashgg/TagAlgos/test/weights/Yacine_phopt_BDTG.weights.xml"),
                              )

flashggVBFDiPhoDiJetMVA = cms.EDProducer('FlashggVBFDiPhoDiJetMVAProducer',
                                         DiPhotonTag=cms.untracked.InputTag('flashggDiPhotons'),
                                         VBFMVAResultTag=cms.untracked.InputTag('flashggVBFMVA'),
                                         MVAResultTag=cms.untracked.InputTag('flashggDiPhotonMVA'),
                                         vbfDiPhoDiJetMVAweightfile = cms.FileInPath("flashgg/TagProducers/data/TMVA_vbf_dijet_dipho_evenbkg_scaledwt50_maxdPhi_Gradient.weights.xml"),
                                     )
