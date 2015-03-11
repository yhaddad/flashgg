import FWCore.ParameterSet.Config as cms

flashggUntaggedCategory = cms.EDProducer("FlashggUntaggedCategoryProducer",
                                         #                                      DiPhotonTag=cms.untracked.InputTag('flashggPreselectedDiPhotons'), # why doesn't this work?
                                         DiPhotonTag=cms.untracked.InputTag('flashggDiPhotons'),
                                         MVAResultTag=cms.untracked.InputTag('flashggDiPhotonMVA'),
                                         Boundaries=cms.untracked.vdouble(0.07,0.31,0.62,0.86,0.98)
)

flashggTTHhadronicTag = cms.EDProducer("FlashggTTHhadronicTagProducer",
                                       TTHJetTag=cms.untracked.InputTag('flashggJets')
)

flashggVBFTag = cms.EDProducer("FlashggVBFTagProducer",
                               #                                         DiPhotonTag=cms.untracked.InputTag('flashggPreselectedDiPhotons'), # why doesn't this work?
                               DiPhotonTag=cms.untracked.InputTag('flashggDiPhotons'),
                               VBFDiPhoDiJetMVAResultTag=cms.untracked.InputTag('flashggVBFDiPhoDiJetMVA'),
                               VBFMVAResultTag=cms.untracked.InputTag('flashggVBFMVA'),
                               Boundaries=cms.untracked.vdouble(0.21,0.6,0.81)
)
flashggTTHleptonicTag = cms.EDProducer("FlashggTTHleptonicTagProducer",
                                       DiPhotonTag=cms.untracked.InputTag('flashggDiPhotons'),
                                       TTHJetTag=cms.untracked.InputTag('flashggJets'),
                                       ElectronTag=cms.untracked.InputTag('flashggElectrons'),
                                       MuonTag=cms.untracked.InputTag('slimmedMuon'),
                                       VertexTag=cms.untracked.InputTag('offlineSlimmedPrimaryVertices'),
                                       leptonPtThreshold = cms.untracked.double(20),
                                       leptonEtaThreshold = cms.untracked.double(2.4),
                                       leadPhoOverMassThreshold = cms.untracked.double(0.5),
                                       subleadPhoOverMassThreshold = cms.untracked.double(0.25),
                                       MVAThreshold = cms.untracked.double(-0.6),
                                       deltaRLepPhoThreshold = cms.untracked.double(0.5),
                                       deltaRJetLepThreshold = cms.untracked.double(0.5),
                                       jetsNumberThreshold = cms.untracked.double(2.),
                                       bjetsNumberThreshold = cms.untracked.double(1.),
                                       jetPtThreshold = cms.untracked.double(30.),
                                       jetEtaThreshold= cms.untracked.double(2.4),
                                       deltaRJetLeadPhoThreshold = cms.untracked.double(0.5),
                                       deltaRJetSubLeadPhoThreshold = cms.untracked.double(0.5),
                                       bDiscriminator=cms.untracked.vdouble(0.244,0.679),
                                       bTag = cms.untracked.string("combinedInclusiveSecondaryVertexV2BJetTags"),
                                       muPFIsoSumRelThreshold = cms.untracked.double(0.2),
                                       deltaRMuonJetcountThreshold = cms.untracked.double(2.),
                                       PuIDCutoffThreshold = cms.untracked.double(0.8),
                                       PhoMVAThreshold = cms.untracked.double(-0.2),
                                       ElectronPtThreshold = cms.untracked.double(20.),
                                       DeltaRTrkElec = cms.untracked.double(1.),
                                       TransverseImpactParam = cms.untracked.double(0.2),
                                       LongitudinalImpactParam = cms.untracked.double(0.02),
                                       LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
                                       MidPtEtaPhoThreshold = cms.untracked.double(1.566),
                                       HighEtaPhoThreshold = cms.untracked.double(2.5),
                                       deltaRPhoElectronThreshold = cms.untracked.double(1.),
                                       Zmass_ = cms.untracked.double(91.9),
                                       deltaMassElectronZThreshold_ = cms.untracked.double(10.),
                                       EtaCuts=cms.untracked.vdouble(1.442,1.566,2.5),
                                       nonTrigMVAThreshold = cms.untracked.double(0.9),
                                       electronIsoThreshold = cms.untracked.double(0.15),
                                       electronNumOfHitsThreshold = cms.untracked.double(1)
)
flashggVHlooseTag = cms.EDProducer("FlashggVHlooseTagProducer",
                                   DiPhotonTag=cms.untracked.InputTag('flashggDiPhotons'),
                                   VHlooseJetTag=cms.untracked.InputTag('flashggJets'),
                                   ElectronTag=cms.untracked.InputTag('flashggElectrons'),
                                   MuonTag=cms.untracked.InputTag('slimmedMuons'),
                                   VertexTag=cms.untracked.InputTag('offlineSlimmedPrimaryVertices'),
                                   MVAResultTag=cms.untracked.InputTag('flashggDiPhotonMVA'),
                                   METTag=cms.untracked.InputTag('slimmedMETs'),
                                   leptonPtThreshold = cms.untracked.double(20),
                                   leptonEtaThreshold = cms.untracked.double(2.4),
                                   leadPhoOverMassThreshold = cms.untracked.double(0.375),
                                   subleadPhoOverMassThreshold = cms.untracked.double(0.25),
                                   MVAThreshold = cms.untracked.double(-0.6),
                                   deltaRLepPhoThreshold = cms.untracked.double(1),
                                   jetsNumberThreshold = cms.untracked.double(3.),
                                   jetPtThreshold = cms.untracked.double(20.),
                                   jetEtaThreshold= cms.untracked.double(2.4),
                                   muPFIsoSumRelThreshold = cms.untracked.double(0.2),
                                   PuIDCutoffThreshold = cms.untracked.double(0.8),
                                   PhoMVAThreshold = cms.untracked.double(-0.2),
                                   METThreshold = cms.untracked.double(45.),
                                   LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
                                   MidPtEtaPhoThreshold = cms.untracked.double(1.566),
                                   HighEtaPhoThreshold = cms.untracked.double(2.5),
                                   ElectronPtThreshold = cms.untracked.double(20.),
                                   DeltaRTrkElec = cms.untracked.double(1.),
                                   TransverseImpactParam = cms.untracked.double(0.2),
                                   LongitudinalImpactParam = cms.untracked.double(0.02),
                                   deltaRPhoElectronThreshold = cms.untracked.double(1.),
                                   Zmass_ = cms.untracked.double(91.9),
                                   deltaMassElectronZThreshold_ = cms.untracked.double(10.),
                                   EtaCuts=cms.untracked.vdouble(1.442,1.566,2.5),
                                   nonTrigMVAThreshold = cms.untracked.double(0.9),
                                   electronIsoThreshold = cms.untracked.double(0.15),
                                   electronNumOfHitsThreshold = cms.untracked.double(1)

				    )
flashggVHtightTag = cms.EDProducer("FlashggVHtightTagProducer",
                                   DiPhotonTag=cms.untracked.InputTag('flashggDiPhotons'),
                                   VHtightJetTag=cms.untracked.InputTag('flashggJets'),
                                   ElectronTag=cms.untracked.InputTag('flashggElectrons'),
                                   MuonTag=cms.untracked.InputTag('slimmedMuons'),
                                   VertexTag=cms.untracked.InputTag('offlineSlimmedPrimaryVertices'),
                                   MVAResultTag=cms.untracked.InputTag('flashggDiPhotonMVA'),
                                   METTag=cms.untracked.InputTag('slimmedMETs'),
                                   leptonPtThreshold = cms.untracked.double(20),
                                   leptonEtaThreshold = cms.untracked.double(2.4),
                                   leadPhoOverMassThreshold = cms.untracked.double(0.375),
                                   subleadPhoOverMassThreshold = cms.untracked.double(0.25),
                                   MVAThreshold = cms.untracked.double(-0.6),
                                   deltaRLepPhoThreshold = cms.untracked.double(1),
                                   jetsNumberThreshold = cms.untracked.double(3.),
                                   jetPtThreshold = cms.untracked.double(20.),
                                   jetEtaThreshold= cms.untracked.double(2.4),
                                   muPFIsoSumRelThreshold = cms.untracked.double(0.2),
                                   PuIDCutoffThreshold = cms.untracked.double(0.8),
                                   PhoMVAThreshold = cms.untracked.double(-0.2),
                                   METThreshold = cms.untracked.double(45.),
                                   deltaRJetMuonThreshold = cms.untracked.double(0.5),
                                   invMassLepLowThreshold = cms.untracked.double(70.),
                                   invMassLepHighThreshold = cms.untracked.double(110.),
                                   numberOfLowPtMuonsThreshold = cms.untracked.double(2.),
                                   numberOfHighPtMuonsThreshold = cms.untracked.double(1.),
                                   leptonLowPtThreshold = cms.untracked.double(10.),
                                   deltaRLowPtMuonPhoThreshold = cms.untracked.double(0.5),
                                   deltaRPhoLeadJet = cms.untracked.double(0.5),
                                   deltaRPhoSubLeadJet = cms.untracked.double(0.5),
                                   LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
                                   MidPtEtaPhoThreshold = cms.untracked.double(1.566),
                                   HighEtaPhoThreshold = cms.untracked.double(2.5),
                                   ElectronPtThreshold = cms.untracked.double(20.),
                                   DeltaRTrkElec = cms.untracked.double(1.),
                                   TransverseImpactParam = cms.untracked.double(0.2),
                                   LongitudinalImpactParam = cms.untracked.double(0.02),
                                   deltaRPhoElectronThreshold = cms.untracked.double(1.),
                                   Zmass_ = cms.untracked.double(91.9),
                                   deltaMassElectronZThreshold_ = cms.untracked.double(10.),
                                   EtaCuts=cms.untracked.vdouble(1.442,1.566,2.5),
                                   nonTrigMVAThreshold = cms.untracked.double(0.9),
                                   electronIsoThreshold = cms.untracked.double(0.15),
                                   electronNumOfHitsThreshold = cms.untracked.double(1)
)


flashggVHhadronicTag = cms.EDProducer("FlashggVHhadronicTagProducer",
                                      DiPhotonTag = cms.untracked.InputTag('flashggDiPhotons'),
                                      JetTag = cms.untracked.InputTag('flashggJets'),
                                      leadPhoOverMassThreshold = cms.untracked.double(0.375),
                                      subleadPhoOverMassThreshold = cms.untracked.double(0.25),
                                      MVAThreshold = cms.untracked.double(-0.6),
                                      jetsNumberThreshold = cms.untracked.double(2.),
                                      jetPtThreshold = cms.untracked.double(40.),
                                      jetEtaThreshold= cms.untracked.double(2.4),
                                      dRJetToPhoLThreshold = cms.untracked.double(0.5),
                                      dRJetToPhoSThreshold = cms.untracked.double(0.5),
                                      dijetMassLowThreshold = cms.untracked.double(60.),
                                      dijetMassHighThreshold = cms.untracked.double(120.),
                                      cosThetaStarThreshold = cms.untracked.double(0.5),
                                      PhoMVAThreshold = cms.untracked.double(-0.2)
)



