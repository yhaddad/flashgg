import FWCore.ParameterSet.Config as cms

process = cms.Process("FLASHggSyst")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:myMicroAODOutputFile.root')
)
process.flashggDiPhotonMVA = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics"),
    Version = cms.string('old'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/HggBambu_SMDipho_Oct29_rwgtptallsigevenbkg7TeV_BDTG.weights.xml')
)


process.flashggDiPhotonMVAMCScaleHighR9EBDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBDown01sigma"),
    Version = cms.string('old'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/HggBambu_SMDipho_Oct29_rwgtptallsigevenbkg7TeV_BDTG.weights.xml')
)


process.flashggDiPhotonMVAMCScaleHighR9EBUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBUp01sigma"),
    Version = cms.string('old'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/HggBambu_SMDipho_Oct29_rwgtptallsigevenbkg7TeV_BDTG.weights.xml')
)


process.flashggDiPhotonMVAMCScaleHighR9EEDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEDown01sigma"),
    Version = cms.string('old'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/HggBambu_SMDipho_Oct29_rwgtptallsigevenbkg7TeV_BDTG.weights.xml')
)


process.flashggDiPhotonMVAMCScaleHighR9EEUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEUp01sigma"),
    Version = cms.string('old'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/HggBambu_SMDipho_Oct29_rwgtptallsigevenbkg7TeV_BDTG.weights.xml')
)


process.flashggDiPhotonMVAMCScaleLowR9EBDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBDown01sigma"),
    Version = cms.string('old'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/HggBambu_SMDipho_Oct29_rwgtptallsigevenbkg7TeV_BDTG.weights.xml')
)


process.flashggDiPhotonMVAMCScaleLowR9EBUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBUp01sigma"),
    Version = cms.string('old'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/HggBambu_SMDipho_Oct29_rwgtptallsigevenbkg7TeV_BDTG.weights.xml')
)


process.flashggDiPhotonMVAMCScaleLowR9EEDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEDown01sigma"),
    Version = cms.string('old'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/HggBambu_SMDipho_Oct29_rwgtptallsigevenbkg7TeV_BDTG.weights.xml')
)


process.flashggDiPhotonMVAMCScaleLowR9EEUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEUp01sigma"),
    Version = cms.string('old'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/HggBambu_SMDipho_Oct29_rwgtptallsigevenbkg7TeV_BDTG.weights.xml')
)


process.flashggDiPhotonMVAMCSmearHighR9EBPhiDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiDown01sigma"),
    Version = cms.string('old'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/HggBambu_SMDipho_Oct29_rwgtptallsigevenbkg7TeV_BDTG.weights.xml')
)


process.flashggDiPhotonMVAMCSmearHighR9EBPhiUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiUp01sigma"),
    Version = cms.string('old'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/HggBambu_SMDipho_Oct29_rwgtptallsigevenbkg7TeV_BDTG.weights.xml')
)


process.flashggDiPhotonMVAMCSmearHighR9EBRhoDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoDown01sigma"),
    Version = cms.string('old'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/HggBambu_SMDipho_Oct29_rwgtptallsigevenbkg7TeV_BDTG.weights.xml')
)


process.flashggDiPhotonMVAMCSmearHighR9EBRhoUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoUp01sigma"),
    Version = cms.string('old'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/HggBambu_SMDipho_Oct29_rwgtptallsigevenbkg7TeV_BDTG.weights.xml')
)


process.flashggDiPhotonMVAMCSmearHighR9EEDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEDown01sigma"),
    Version = cms.string('old'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/HggBambu_SMDipho_Oct29_rwgtptallsigevenbkg7TeV_BDTG.weights.xml')
)


process.flashggDiPhotonMVAMCSmearHighR9EEUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEUp01sigma"),
    Version = cms.string('old'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/HggBambu_SMDipho_Oct29_rwgtptallsigevenbkg7TeV_BDTG.weights.xml')
)


process.flashggDiPhotonMVAMCSmearLowR9EBPhiDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiDown01sigma"),
    Version = cms.string('old'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/HggBambu_SMDipho_Oct29_rwgtptallsigevenbkg7TeV_BDTG.weights.xml')
)


process.flashggDiPhotonMVAMCSmearLowR9EBPhiUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiUp01sigma"),
    Version = cms.string('old'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/HggBambu_SMDipho_Oct29_rwgtptallsigevenbkg7TeV_BDTG.weights.xml')
)


process.flashggDiPhotonMVAMCSmearLowR9EBRhoDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoDown01sigma"),
    Version = cms.string('old'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/HggBambu_SMDipho_Oct29_rwgtptallsigevenbkg7TeV_BDTG.weights.xml')
)


process.flashggDiPhotonMVAMCSmearLowR9EBRhoUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoUp01sigma"),
    Version = cms.string('old'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/HggBambu_SMDipho_Oct29_rwgtptallsigevenbkg7TeV_BDTG.weights.xml')
)


process.flashggDiPhotonMVAMCSmearLowR9EEDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEDown01sigma"),
    Version = cms.string('old'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/HggBambu_SMDipho_Oct29_rwgtptallsigevenbkg7TeV_BDTG.weights.xml')
)


process.flashggDiPhotonMVAMCSmearLowR9EEUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEUp01sigma"),
    Version = cms.string('old'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/HggBambu_SMDipho_Oct29_rwgtptallsigevenbkg7TeV_BDTG.weights.xml')
)


process.flashggDiPhotonMVANew = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVANewMCScaleHighR9EBDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBDown01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVANewMCScaleHighR9EBUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBUp01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVANewMCScaleHighR9EEDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEDown01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVANewMCScaleHighR9EEUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEUp01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVANewMCScaleLowR9EBDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBDown01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVANewMCScaleLowR9EBUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBUp01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVANewMCScaleLowR9EEDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEDown01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVANewMCScaleLowR9EEUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEUp01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVANewMCSmearHighR9EBPhiDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiDown01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVANewMCSmearHighR9EBPhiUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiUp01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVANewMCSmearHighR9EBRhoDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoDown01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVANewMCSmearHighR9EBRhoUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoUp01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVANewMCSmearHighR9EEDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEDown01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVANewMCSmearHighR9EEUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEUp01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVANewMCSmearLowR9EBPhiDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiDown01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVANewMCSmearLowR9EBPhiUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiUp01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVANewMCSmearLowR9EBRhoDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoDown01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVANewMCSmearLowR9EBRhoUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoUp01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVANewMCSmearLowR9EEDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEDown01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVANewMCSmearLowR9EEUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEUp01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVAPUPPI = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVAPUPPIMCScaleHighR9EBDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBDown01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVAPUPPIMCScaleHighR9EBUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBUp01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVAPUPPIMCScaleHighR9EEDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEDown01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVAPUPPIMCScaleHighR9EEUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEUp01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVAPUPPIMCScaleLowR9EBDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBDown01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVAPUPPIMCScaleLowR9EBUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBUp01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVAPUPPIMCScaleLowR9EEDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEDown01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVAPUPPIMCScaleLowR9EEUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEUp01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVAPUPPIMCSmearHighR9EBPhiDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiDown01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVAPUPPIMCSmearHighR9EBPhiUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiUp01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVAPUPPIMCSmearHighR9EBRhoDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoDown01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVAPUPPIMCSmearHighR9EBRhoUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoUp01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVAPUPPIMCSmearHighR9EEDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEDown01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVAPUPPIMCSmearHighR9EEUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEUp01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVAPUPPIMCSmearLowR9EBPhiDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiDown01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVAPUPPIMCSmearLowR9EBPhiUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiUp01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVAPUPPIMCSmearLowR9EBRhoDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoDown01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVAPUPPIMCSmearLowR9EBRhoUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoUp01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVAPUPPIMCSmearLowR9EEDown01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEDown01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonMVAPUPPIMCSmearLowR9EEUp01sigma = cms.EDProducer("FlashggDiPhotonMVAProducer",
    BeamSpotTag = cms.InputTag("offlineBeamSpot"),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEUp01sigma"),
    Version = cms.string('new'),
    VertexProbParamsConv = cms.vdouble(-0.049, -0.241, -0.505, -0.27),
    VertexProbParamsNoConv = cms.vdouble(-0.344, -0.091, -0.234, -0.186),
    diphotonMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoton_BDTG.weights.xml')
)


process.flashggDiPhotonSystematics = cms.EDProducer("FlashggDiPhotonSystematicProducer",
    SystMethods = cms.VPSet(cms.PSet(
        BinList = cms.PSet(
            bins = cms.VPSet(cms.PSet(
                lowBounds = cms.vdouble(0.0, 0.94),
                uncertainties = cms.vdouble(0.0005),
                upBounds = cms.vdouble(1.0, 999.0),
                values = cms.vdouble(0.0)
            ), 
                cms.PSet(
                    lowBounds = cms.vdouble(0.0, -999.0),
                    uncertainties = cms.vdouble(0.0005),
                    upBounds = cms.vdouble(1.0, 0.94),
                    values = cms.vdouble(0.0)
                ), 
                cms.PSet(
                    lowBounds = cms.vdouble(1.0, 0.94),
                    uncertainties = cms.vdouble(0.0006),
                    upBounds = cms.vdouble(1.5, 999.0),
                    values = cms.vdouble(0.0)
                ), 
                cms.PSet(
                    lowBounds = cms.vdouble(1.0, -999.0),
                    uncertainties = cms.vdouble(0.0012),
                    upBounds = cms.vdouble(1.5, 0.94),
                    values = cms.vdouble(0.0)
                ), 
                cms.PSet(
                    lowBounds = cms.vdouble(1.5, -999.0),
                    uncertainties = cms.vdouble(0.002),
                    upBounds = cms.vdouble(2.0, 0.94),
                    values = cms.vdouble(0.0)
                ), 
                cms.PSet(
                    lowBounds = cms.vdouble(1.5, 0.94),
                    uncertainties = cms.vdouble(0.003),
                    upBounds = cms.vdouble(2.0, 999.0),
                    values = cms.vdouble(0.0)
                ), 
                cms.PSet(
                    lowBounds = cms.vdouble(2.0, -999.0),
                    uncertainties = cms.vdouble(0.002),
                    upBounds = cms.vdouble(3.0, 0.94),
                    values = cms.vdouble(0.0)
                ), 
                cms.PSet(
                    lowBounds = cms.vdouble(2.0, 0.94),
                    uncertainties = cms.vdouble(0.003),
                    upBounds = cms.vdouble(3.0, 999.0),
                    values = cms.vdouble(0.0)
                )),
            variables = cms.vstring('abs(superCluster.eta)', 
                'r9')
        ),
        Debug = cms.untracked.bool(False),
        Label = cms.string('MCScaleHighR9EB'),
        MethodName = cms.string('FlashggDiPhotonFromPhoton'),
        NSigmas = cms.vint32(-1, 1),
        OverallRange = cms.string('r9>0.94&&abs(eta)<1.5'),
        PhotonMethodName = cms.string('FlashggPhotonScale')
    ), 
        cms.PSet(
            BinList = cms.PSet(
                bins = cms.VPSet(cms.PSet(
                    lowBounds = cms.vdouble(0.0, 0.94),
                    uncertainties = cms.vdouble(0.0005),
                    upBounds = cms.vdouble(1.0, 999.0),
                    values = cms.vdouble(0.0)
                ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(0.0, -999.0),
                        uncertainties = cms.vdouble(0.0005),
                        upBounds = cms.vdouble(1.0, 0.94),
                        values = cms.vdouble(0.0)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.0, 0.94),
                        uncertainties = cms.vdouble(0.0006),
                        upBounds = cms.vdouble(1.5, 999.0),
                        values = cms.vdouble(0.0)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.0, -999.0),
                        uncertainties = cms.vdouble(0.0012),
                        upBounds = cms.vdouble(1.5, 0.94),
                        values = cms.vdouble(0.0)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.5, -999.0),
                        uncertainties = cms.vdouble(0.002),
                        upBounds = cms.vdouble(2.0, 0.94),
                        values = cms.vdouble(0.0)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.5, 0.94),
                        uncertainties = cms.vdouble(0.003),
                        upBounds = cms.vdouble(2.0, 999.0),
                        values = cms.vdouble(0.0)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(2.0, -999.0),
                        uncertainties = cms.vdouble(0.002),
                        upBounds = cms.vdouble(3.0, 0.94),
                        values = cms.vdouble(0.0)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(2.0, 0.94),
                        uncertainties = cms.vdouble(0.003),
                        upBounds = cms.vdouble(3.0, 999.0),
                        values = cms.vdouble(0.0)
                    )),
                variables = cms.vstring('abs(superCluster.eta)', 
                    'r9')
            ),
            Debug = cms.untracked.bool(False),
            Label = cms.string('MCScaleLowR9EB'),
            MethodName = cms.string('FlashggDiPhotonFromPhoton'),
            NSigmas = cms.vint32(-1, 1),
            OverallRange = cms.string('r9<0.94&&abs(eta)<1.5'),
            PhotonMethodName = cms.string('FlashggPhotonScale')
        ), 
        cms.PSet(
            BinList = cms.PSet(
                bins = cms.VPSet(cms.PSet(
                    lowBounds = cms.vdouble(0.0, 0.94),
                    uncertainties = cms.vdouble(0.0005),
                    upBounds = cms.vdouble(1.0, 999.0),
                    values = cms.vdouble(0.0)
                ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(0.0, -999.0),
                        uncertainties = cms.vdouble(0.0005),
                        upBounds = cms.vdouble(1.0, 0.94),
                        values = cms.vdouble(0.0)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.0, 0.94),
                        uncertainties = cms.vdouble(0.0006),
                        upBounds = cms.vdouble(1.5, 999.0),
                        values = cms.vdouble(0.0)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.0, -999.0),
                        uncertainties = cms.vdouble(0.0012),
                        upBounds = cms.vdouble(1.5, 0.94),
                        values = cms.vdouble(0.0)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.5, -999.0),
                        uncertainties = cms.vdouble(0.002),
                        upBounds = cms.vdouble(2.0, 0.94),
                        values = cms.vdouble(0.0)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.5, 0.94),
                        uncertainties = cms.vdouble(0.003),
                        upBounds = cms.vdouble(2.0, 999.0),
                        values = cms.vdouble(0.0)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(2.0, -999.0),
                        uncertainties = cms.vdouble(0.002),
                        upBounds = cms.vdouble(3.0, 0.94),
                        values = cms.vdouble(0.0)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(2.0, 0.94),
                        uncertainties = cms.vdouble(0.003),
                        upBounds = cms.vdouble(3.0, 999.0),
                        values = cms.vdouble(0.0)
                    )),
                variables = cms.vstring('abs(superCluster.eta)', 
                    'r9')
            ),
            Debug = cms.untracked.bool(False),
            Label = cms.string('MCScaleHighR9EE'),
            MethodName = cms.string('FlashggDiPhotonFromPhoton'),
            NSigmas = cms.vint32(-1, 1),
            OverallRange = cms.string('r9>0.94&&abs(eta)>=1.5'),
            PhotonMethodName = cms.string('FlashggPhotonScale')
        ), 
        cms.PSet(
            BinList = cms.PSet(
                bins = cms.VPSet(cms.PSet(
                    lowBounds = cms.vdouble(0.0, 0.94),
                    uncertainties = cms.vdouble(0.0005),
                    upBounds = cms.vdouble(1.0, 999.0),
                    values = cms.vdouble(0.0)
                ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(0.0, -999.0),
                        uncertainties = cms.vdouble(0.0005),
                        upBounds = cms.vdouble(1.0, 0.94),
                        values = cms.vdouble(0.0)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.0, 0.94),
                        uncertainties = cms.vdouble(0.0006),
                        upBounds = cms.vdouble(1.5, 999.0),
                        values = cms.vdouble(0.0)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.0, -999.0),
                        uncertainties = cms.vdouble(0.0012),
                        upBounds = cms.vdouble(1.5, 0.94),
                        values = cms.vdouble(0.0)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.5, -999.0),
                        uncertainties = cms.vdouble(0.002),
                        upBounds = cms.vdouble(2.0, 0.94),
                        values = cms.vdouble(0.0)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.5, 0.94),
                        uncertainties = cms.vdouble(0.003),
                        upBounds = cms.vdouble(2.0, 999.0),
                        values = cms.vdouble(0.0)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(2.0, -999.0),
                        uncertainties = cms.vdouble(0.002),
                        upBounds = cms.vdouble(3.0, 0.94),
                        values = cms.vdouble(0.0)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(2.0, 0.94),
                        uncertainties = cms.vdouble(0.003),
                        upBounds = cms.vdouble(3.0, 999.0),
                        values = cms.vdouble(0.0)
                    )),
                variables = cms.vstring('abs(superCluster.eta)', 
                    'r9')
            ),
            Debug = cms.untracked.bool(False),
            Label = cms.string('MCScaleLowR9EE'),
            MethodName = cms.string('FlashggDiPhotonFromPhoton'),
            NSigmas = cms.vint32(-1, 1),
            OverallRange = cms.string('r9<0.94&&abs(eta)>=1.5'),
            PhotonMethodName = cms.string('FlashggPhotonScale')
        ), 
        cms.PSet(
            BinList = cms.PSet(
                bins = cms.VPSet(cms.PSet(
                    lowBounds = cms.vdouble(0.0, -999.0),
                    uncertainties = cms.vdouble(0.00063, 0.16),
                    upBounds = cms.vdouble(1.0, 0.94),
                    values = cms.vdouble(0.0077, 0.0, 6.73)
                ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(0.0, 0.94),
                        uncertainties = cms.vdouble(0.00065, 0.16),
                        upBounds = cms.vdouble(1.0, 999.0),
                        values = cms.vdouble(0.0074, 0.0, 6.6)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.0, -999.0),
                        uncertainties = cms.vdouble(0.00103, 0.07),
                        upBounds = cms.vdouble(1.5, 0.94),
                        values = cms.vdouble(0.0126, 0.0, 6.73)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.0, 0.94),
                        uncertainties = cms.vdouble(0.00132, 0.22),
                        upBounds = cms.vdouble(1.5, 999.0),
                        values = cms.vdouble(0.0112, 0.0, 6.52)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.5, -999.0),
                        uncertainties = cms.vdouble(0.00303),
                        upBounds = cms.vdouble(2.0, 0.94),
                        values = cms.vdouble(0.0198)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.5, 0.94),
                        uncertainties = cms.vdouble(0.00122),
                        upBounds = cms.vdouble(2.0, 999.0),
                        values = cms.vdouble(0.0163)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(2.0, -999.0),
                        uncertainties = cms.vdouble(0.00092),
                        upBounds = cms.vdouble(3.0, 0.94),
                        values = cms.vdouble(0.0192)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(2.0, 0.94),
                        uncertainties = cms.vdouble(0.00078),
                        upBounds = cms.vdouble(3.0, 999.0),
                        values = cms.vdouble(0.0186)
                    )),
                variables = cms.vstring('abs(superCluster.eta)', 
                    'r9')
            ),
            Debug = cms.untracked.bool(False),
            ExaggerateShiftUp = cms.untracked.bool(True),
            Label = cms.string('MCSmearHighR9EE'),
            MethodName = cms.string('FlashggDiPhotonFromPhoton'),
            NSigmas = cms.vint32(-1, 1),
            OverallRange = cms.string('r9>0.94&&abs(eta)>=1.5'),
            PhotonMethodName = cms.string('FlashggPhotonSmearConstant')
        ), 
        cms.PSet(
            BinList = cms.PSet(
                bins = cms.VPSet(cms.PSet(
                    lowBounds = cms.vdouble(0.0, -999.0),
                    uncertainties = cms.vdouble(0.00063, 0.16),
                    upBounds = cms.vdouble(1.0, 0.94),
                    values = cms.vdouble(0.0077, 0.0, 6.73)
                ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(0.0, 0.94),
                        uncertainties = cms.vdouble(0.00065, 0.16),
                        upBounds = cms.vdouble(1.0, 999.0),
                        values = cms.vdouble(0.0074, 0.0, 6.6)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.0, -999.0),
                        uncertainties = cms.vdouble(0.00103, 0.07),
                        upBounds = cms.vdouble(1.5, 0.94),
                        values = cms.vdouble(0.0126, 0.0, 6.73)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.0, 0.94),
                        uncertainties = cms.vdouble(0.00132, 0.22),
                        upBounds = cms.vdouble(1.5, 999.0),
                        values = cms.vdouble(0.0112, 0.0, 6.52)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.5, -999.0),
                        uncertainties = cms.vdouble(0.00303),
                        upBounds = cms.vdouble(2.0, 0.94),
                        values = cms.vdouble(0.0198)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.5, 0.94),
                        uncertainties = cms.vdouble(0.00122),
                        upBounds = cms.vdouble(2.0, 999.0),
                        values = cms.vdouble(0.0163)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(2.0, -999.0),
                        uncertainties = cms.vdouble(0.00092),
                        upBounds = cms.vdouble(3.0, 0.94),
                        values = cms.vdouble(0.0192)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(2.0, 0.94),
                        uncertainties = cms.vdouble(0.00078),
                        upBounds = cms.vdouble(3.0, 999.0),
                        values = cms.vdouble(0.0186)
                    )),
                variables = cms.vstring('abs(superCluster.eta)', 
                    'r9')
            ),
            Debug = cms.untracked.bool(False),
            ExaggerateShiftUp = cms.untracked.bool(True),
            Label = cms.string('MCSmearLowR9EE'),
            MethodName = cms.string('FlashggDiPhotonFromPhoton'),
            NSigmas = cms.vint32(-1, 1),
            OverallRange = cms.string('r9<0.94&&abs(eta)>=1.5'),
            PhotonMethodName = cms.string('FlashggPhotonSmearConstant')
        )),
    SystMethods2D = cms.VPSet(cms.PSet(
        BinList = cms.PSet(
            bins = cms.VPSet(cms.PSet(
                lowBounds = cms.vdouble(0.0, -999.0),
                uncertainties = cms.vdouble(0.00063, 0.16),
                upBounds = cms.vdouble(1.0, 0.94),
                values = cms.vdouble(0.0077, 0.0, 6.73)
            ), 
                cms.PSet(
                    lowBounds = cms.vdouble(0.0, 0.94),
                    uncertainties = cms.vdouble(0.00065, 0.16),
                    upBounds = cms.vdouble(1.0, 999.0),
                    values = cms.vdouble(0.0074, 0.0, 6.6)
                ), 
                cms.PSet(
                    lowBounds = cms.vdouble(1.0, -999.0),
                    uncertainties = cms.vdouble(0.00103, 0.07),
                    upBounds = cms.vdouble(1.5, 0.94),
                    values = cms.vdouble(0.0126, 0.0, 6.73)
                ), 
                cms.PSet(
                    lowBounds = cms.vdouble(1.0, 0.94),
                    uncertainties = cms.vdouble(0.00132, 0.22),
                    upBounds = cms.vdouble(1.5, 999.0),
                    values = cms.vdouble(0.0112, 0.0, 6.52)
                ), 
                cms.PSet(
                    lowBounds = cms.vdouble(1.5, -999.0),
                    uncertainties = cms.vdouble(0.00303),
                    upBounds = cms.vdouble(2.0, 0.94),
                    values = cms.vdouble(0.0198)
                ), 
                cms.PSet(
                    lowBounds = cms.vdouble(1.5, 0.94),
                    uncertainties = cms.vdouble(0.00122),
                    upBounds = cms.vdouble(2.0, 999.0),
                    values = cms.vdouble(0.0163)
                ), 
                cms.PSet(
                    lowBounds = cms.vdouble(2.0, -999.0),
                    uncertainties = cms.vdouble(0.00092),
                    upBounds = cms.vdouble(3.0, 0.94),
                    values = cms.vdouble(0.0192)
                ), 
                cms.PSet(
                    lowBounds = cms.vdouble(2.0, 0.94),
                    uncertainties = cms.vdouble(0.00078),
                    upBounds = cms.vdouble(3.0, 999.0),
                    values = cms.vdouble(0.0186)
                )),
            variables = cms.vstring('abs(superCluster.eta)', 
                'r9')
        ),
        Debug = cms.untracked.bool(False),
        ExaggerateShiftUp = cms.untracked.bool(True),
        Label = cms.string('MCSmearHighR9EB'),
        MethodName = cms.string('FlashggDiPhotonFromPhoton2D'),
        NSigmas = cms.PSet(
            firstVar = cms.vint32(1, -1, 0, 0),
            secondVar = cms.vint32(0, 0, 1, -1)
        ),
        OverallRange = cms.string('r9>0.94&&abs(eta)<1.5'),
        PhotonMethodName = cms.string('FlashggPhotonSmearStochastic')
    ), 
        cms.PSet(
            BinList = cms.PSet(
                bins = cms.VPSet(cms.PSet(
                    lowBounds = cms.vdouble(0.0, -999.0),
                    uncertainties = cms.vdouble(0.00063, 0.16),
                    upBounds = cms.vdouble(1.0, 0.94),
                    values = cms.vdouble(0.0077, 0.0, 6.73)
                ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(0.0, 0.94),
                        uncertainties = cms.vdouble(0.00065, 0.16),
                        upBounds = cms.vdouble(1.0, 999.0),
                        values = cms.vdouble(0.0074, 0.0, 6.6)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.0, -999.0),
                        uncertainties = cms.vdouble(0.00103, 0.07),
                        upBounds = cms.vdouble(1.5, 0.94),
                        values = cms.vdouble(0.0126, 0.0, 6.73)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.0, 0.94),
                        uncertainties = cms.vdouble(0.00132, 0.22),
                        upBounds = cms.vdouble(1.5, 999.0),
                        values = cms.vdouble(0.0112, 0.0, 6.52)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.5, -999.0),
                        uncertainties = cms.vdouble(0.00303),
                        upBounds = cms.vdouble(2.0, 0.94),
                        values = cms.vdouble(0.0198)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(1.5, 0.94),
                        uncertainties = cms.vdouble(0.00122),
                        upBounds = cms.vdouble(2.0, 999.0),
                        values = cms.vdouble(0.0163)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(2.0, -999.0),
                        uncertainties = cms.vdouble(0.00092),
                        upBounds = cms.vdouble(3.0, 0.94),
                        values = cms.vdouble(0.0192)
                    ), 
                    cms.PSet(
                        lowBounds = cms.vdouble(2.0, 0.94),
                        uncertainties = cms.vdouble(0.00078),
                        upBounds = cms.vdouble(3.0, 999.0),
                        values = cms.vdouble(0.0186)
                    )),
                variables = cms.vstring('abs(superCluster.eta)', 
                    'r9')
            ),
            Debug = cms.untracked.bool(False),
            ExaggerateShiftUp = cms.untracked.bool(True),
            Label = cms.string('MCSmearLowR9EB'),
            MethodName = cms.string('FlashggDiPhotonFromPhoton2D'),
            NSigmas = cms.PSet(
                firstVar = cms.vint32(1, -1, 0, 0),
                secondVar = cms.vint32(0, 0, 1, -1)
            ),
            OverallRange = cms.string('r9<0.94&&abs(eta)<1.5'),
            PhotonMethodName = cms.string('FlashggPhotonSmearStochastic')
        )),
    src = cms.InputTag("flashggFinalEGamma","finalDiPhotons")
)


process.flashggElectronSystematics = cms.EDProducer("FlashggElectronEffSystematicProducer",
    SystMethods = cms.VPSet(cms.PSet(
        BinList = cms.PSet(
            bins = cms.VPSet(cms.PSet(
                lowBounds = cms.vdouble(1.0),
                uncertainties = cms.vdouble(0.05, 0.3),
                upBounds = cms.vdouble(25.0),
                values = cms.vdouble(0.8)
            ), 
                cms.PSet(
                    lowBounds = cms.vdouble(25.0),
                    uncertainties = cms.vdouble(0.05, 0.3),
                    upBounds = cms.vdouble(100.0),
                    values = cms.vdouble(0.9)
                ), 
                cms.PSet(
                    lowBounds = cms.vdouble(100.0),
                    uncertainties = cms.vdouble(0.05, 0.3),
                    upBounds = cms.vdouble(300.0),
                    values = cms.vdouble(0.95)
                )),
            variables = cms.vstring('pt')
        ),
        Debug = cms.untracked.bool(False),
        Label = cms.string('ElectronWeight'),
        MethodName = cms.string('FlashggElectronEffScale'),
        NSigmas = cms.vint32(-1, 1),
        OverallRange = cms.string('abs(eta)<1.5')
    )),
    SystMethods2D = cms.VPSet(),
    src = cms.InputTag("flashggFinalEGamma","finalElectrons")
)


process.flashggMuonSystematics = cms.EDProducer("FlashggMuonEffSystematicProducer",
    SystMethods = cms.VPSet(cms.PSet(
        BinList = cms.PSet(
            bins = cms.VPSet(cms.PSet(
                lowBounds = cms.vdouble(1.0),
                uncertainties = cms.vdouble(0.05, 0.3),
                upBounds = cms.vdouble(25.0),
                values = cms.vdouble(0.8)
            ), 
                cms.PSet(
                    lowBounds = cms.vdouble(25.0),
                    uncertainties = cms.vdouble(0.05, 0.3),
                    upBounds = cms.vdouble(100.0),
                    values = cms.vdouble(0.9)
                ), 
                cms.PSet(
                    lowBounds = cms.vdouble(100.0),
                    uncertainties = cms.vdouble(0.05, 0.3),
                    upBounds = cms.vdouble(300.0),
                    values = cms.vdouble(0.95)
                )),
            variables = cms.vstring('pt')
        ),
        Debug = cms.untracked.bool(False),
        Label = cms.string('MuonWeight'),
        MethodName = cms.string('FlashggMuonEffScale'),
        NSigmas = cms.vint32(-1, 1),
        OverallRange = cms.string('abs(eta)<1.5')
    )),
    SystMethods2D = cms.VPSet(),
    src = cms.InputTag("flashggSelectedMuons")
)


process.flashggSystTagMerger = cms.EDProducer("TagMerger",
    src = cms.VInputTag("flashggTagSorter", cms.InputTag("flashggTagSorterMCSmearHighR9EEUp01sigma"), cms.InputTag("flashggTagSorterMCSmearHighR9EBRhoUp01sigma"), cms.InputTag("flashggTagSorterMCSmearHighR9EBPhiUp01sigma"), cms.InputTag("flashggTagSorterMCScaleHighR9EBUp01sigma"), 
        cms.InputTag("flashggTagSorterMCScaleHighR9EEUp01sigma"), cms.InputTag("flashggTagSorterMCSmearHighR9EEDown01sigma"), cms.InputTag("flashggTagSorterMCSmearHighR9EBRhoDown01sigma"), cms.InputTag("flashggTagSorterMCSmearHighR9EBPhiDown01sigma"), cms.InputTag("flashggTagSorterMCScaleHighR9EBDown01sigma"), 
        cms.InputTag("flashggTagSorterMCScaleHighR9EEDown01sigma"), cms.InputTag("flashggTagSorterMCSmearLowR9EEUp01sigma"), cms.InputTag("flashggTagSorterMCSmearLowR9EBRhoUp01sigma"), cms.InputTag("flashggTagSorterMCSmearLowR9EBPhiUp01sigma"), cms.InputTag("flashggTagSorterMCScaleLowR9EBUp01sigma"), 
        cms.InputTag("flashggTagSorterMCScaleLowR9EEUp01sigma"), cms.InputTag("flashggTagSorterMCSmearLowR9EEDown01sigma"), cms.InputTag("flashggTagSorterMCSmearLowR9EBRhoDown01sigma"), cms.InputTag("flashggTagSorterMCSmearLowR9EBPhiDown01sigma"), cms.InputTag("flashggTagSorterMCScaleLowR9EBDown01sigma"), 
        cms.InputTag("flashggTagSorterMCScaleLowR9EEDown01sigma"))
)


process.flashggTTHHadronicTag = cms.EDProducer("FlashggTTHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVA"),
    SystLabel = cms.string(''),
    bDiscriminatorLoose = cms.untracked.double(0.275),
    bDiscriminatorMedium = cms.untracked.double(0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.int32(0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJets","0"), cms.InputTag("flashggUnpackedJets","1"), cms.InputTag("flashggUnpackedJets","2"), cms.InputTag("flashggUnpackedJets","3"), cms.InputTag("flashggUnpackedJets","4"), 
        cms.InputTag("flashggUnpackedJets","5"), cms.InputTag("flashggUnpackedJets","6"), cms.InputTag("flashggUnpackedJets","7")),
    jetsNumberThreshold = cms.untracked.int32(4)
)


process.flashggTTHHadronicTagMCScaleHighR9EBDown01sigma = cms.EDProducer("FlashggTTHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EBDown01sigma"),
    SystLabel = cms.string('MCScaleHighR9EBDown01sigma'),
    bDiscriminatorLoose = cms.untracked.double(0.275),
    bDiscriminatorMedium = cms.untracked.double(0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.int32(0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","7")),
    jetsNumberThreshold = cms.untracked.int32(4)
)


process.flashggTTHHadronicTagMCScaleHighR9EBUp01sigma = cms.EDProducer("FlashggTTHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EBUp01sigma"),
    SystLabel = cms.string('MCScaleHighR9EBUp01sigma'),
    bDiscriminatorLoose = cms.untracked.double(0.275),
    bDiscriminatorMedium = cms.untracked.double(0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.int32(0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","7")),
    jetsNumberThreshold = cms.untracked.int32(4)
)


process.flashggTTHHadronicTagMCScaleHighR9EEDown01sigma = cms.EDProducer("FlashggTTHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EEDown01sigma"),
    SystLabel = cms.string('MCScaleHighR9EEDown01sigma'),
    bDiscriminatorLoose = cms.untracked.double(0.275),
    bDiscriminatorMedium = cms.untracked.double(0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.int32(0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","7")),
    jetsNumberThreshold = cms.untracked.int32(4)
)


process.flashggTTHHadronicTagMCScaleHighR9EEUp01sigma = cms.EDProducer("FlashggTTHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EEUp01sigma"),
    SystLabel = cms.string('MCScaleHighR9EEUp01sigma'),
    bDiscriminatorLoose = cms.untracked.double(0.275),
    bDiscriminatorMedium = cms.untracked.double(0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.int32(0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","7")),
    jetsNumberThreshold = cms.untracked.int32(4)
)


process.flashggTTHHadronicTagMCScaleLowR9EBDown01sigma = cms.EDProducer("FlashggTTHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EBDown01sigma"),
    SystLabel = cms.string('MCScaleLowR9EBDown01sigma'),
    bDiscriminatorLoose = cms.untracked.double(0.275),
    bDiscriminatorMedium = cms.untracked.double(0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.int32(0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","7")),
    jetsNumberThreshold = cms.untracked.int32(4)
)


process.flashggTTHHadronicTagMCScaleLowR9EBUp01sigma = cms.EDProducer("FlashggTTHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EBUp01sigma"),
    SystLabel = cms.string('MCScaleLowR9EBUp01sigma'),
    bDiscriminatorLoose = cms.untracked.double(0.275),
    bDiscriminatorMedium = cms.untracked.double(0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.int32(0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","7")),
    jetsNumberThreshold = cms.untracked.int32(4)
)


process.flashggTTHHadronicTagMCScaleLowR9EEDown01sigma = cms.EDProducer("FlashggTTHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EEDown01sigma"),
    SystLabel = cms.string('MCScaleLowR9EEDown01sigma'),
    bDiscriminatorLoose = cms.untracked.double(0.275),
    bDiscriminatorMedium = cms.untracked.double(0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.int32(0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","7")),
    jetsNumberThreshold = cms.untracked.int32(4)
)


process.flashggTTHHadronicTagMCScaleLowR9EEUp01sigma = cms.EDProducer("FlashggTTHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EEUp01sigma"),
    SystLabel = cms.string('MCScaleLowR9EEUp01sigma'),
    bDiscriminatorLoose = cms.untracked.double(0.275),
    bDiscriminatorMedium = cms.untracked.double(0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.int32(0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","7")),
    jetsNumberThreshold = cms.untracked.int32(4)
)


process.flashggTTHHadronicTagMCSmearHighR9EBPhiDown01sigma = cms.EDProducer("FlashggTTHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBPhiDown01sigma"),
    SystLabel = cms.string('MCSmearHighR9EBPhiDown01sigma'),
    bDiscriminatorLoose = cms.untracked.double(0.275),
    bDiscriminatorMedium = cms.untracked.double(0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.int32(0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","7")),
    jetsNumberThreshold = cms.untracked.int32(4)
)


process.flashggTTHHadronicTagMCSmearHighR9EBPhiUp01sigma = cms.EDProducer("FlashggTTHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBPhiUp01sigma"),
    SystLabel = cms.string('MCSmearHighR9EBPhiUp01sigma'),
    bDiscriminatorLoose = cms.untracked.double(0.275),
    bDiscriminatorMedium = cms.untracked.double(0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.int32(0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","7")),
    jetsNumberThreshold = cms.untracked.int32(4)
)


process.flashggTTHHadronicTagMCSmearHighR9EBRhoDown01sigma = cms.EDProducer("FlashggTTHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBRhoDown01sigma"),
    SystLabel = cms.string('MCSmearHighR9EBRhoDown01sigma'),
    bDiscriminatorLoose = cms.untracked.double(0.275),
    bDiscriminatorMedium = cms.untracked.double(0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.int32(0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","7")),
    jetsNumberThreshold = cms.untracked.int32(4)
)


process.flashggTTHHadronicTagMCSmearHighR9EBRhoUp01sigma = cms.EDProducer("FlashggTTHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBRhoUp01sigma"),
    SystLabel = cms.string('MCSmearHighR9EBRhoUp01sigma'),
    bDiscriminatorLoose = cms.untracked.double(0.275),
    bDiscriminatorMedium = cms.untracked.double(0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.int32(0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","7")),
    jetsNumberThreshold = cms.untracked.int32(4)
)


process.flashggTTHHadronicTagMCSmearHighR9EEDown01sigma = cms.EDProducer("FlashggTTHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EEDown01sigma"),
    SystLabel = cms.string('MCSmearHighR9EEDown01sigma'),
    bDiscriminatorLoose = cms.untracked.double(0.275),
    bDiscriminatorMedium = cms.untracked.double(0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.int32(0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","7")),
    jetsNumberThreshold = cms.untracked.int32(4)
)


process.flashggTTHHadronicTagMCSmearHighR9EEUp01sigma = cms.EDProducer("FlashggTTHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EEUp01sigma"),
    SystLabel = cms.string('MCSmearHighR9EEUp01sigma'),
    bDiscriminatorLoose = cms.untracked.double(0.275),
    bDiscriminatorMedium = cms.untracked.double(0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.int32(0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","7")),
    jetsNumberThreshold = cms.untracked.int32(4)
)


process.flashggTTHHadronicTagMCSmearLowR9EBPhiDown01sigma = cms.EDProducer("FlashggTTHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBPhiDown01sigma"),
    SystLabel = cms.string('MCSmearLowR9EBPhiDown01sigma'),
    bDiscriminatorLoose = cms.untracked.double(0.275),
    bDiscriminatorMedium = cms.untracked.double(0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.int32(0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","7")),
    jetsNumberThreshold = cms.untracked.int32(4)
)


process.flashggTTHHadronicTagMCSmearLowR9EBPhiUp01sigma = cms.EDProducer("FlashggTTHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBPhiUp01sigma"),
    SystLabel = cms.string('MCSmearLowR9EBPhiUp01sigma'),
    bDiscriminatorLoose = cms.untracked.double(0.275),
    bDiscriminatorMedium = cms.untracked.double(0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.int32(0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","7")),
    jetsNumberThreshold = cms.untracked.int32(4)
)


process.flashggTTHHadronicTagMCSmearLowR9EBRhoDown01sigma = cms.EDProducer("FlashggTTHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBRhoDown01sigma"),
    SystLabel = cms.string('MCSmearLowR9EBRhoDown01sigma'),
    bDiscriminatorLoose = cms.untracked.double(0.275),
    bDiscriminatorMedium = cms.untracked.double(0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.int32(0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","7")),
    jetsNumberThreshold = cms.untracked.int32(4)
)


process.flashggTTHHadronicTagMCSmearLowR9EBRhoUp01sigma = cms.EDProducer("FlashggTTHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBRhoUp01sigma"),
    SystLabel = cms.string('MCSmearLowR9EBRhoUp01sigma'),
    bDiscriminatorLoose = cms.untracked.double(0.275),
    bDiscriminatorMedium = cms.untracked.double(0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.int32(0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","7")),
    jetsNumberThreshold = cms.untracked.int32(4)
)


process.flashggTTHHadronicTagMCSmearLowR9EEDown01sigma = cms.EDProducer("FlashggTTHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EEDown01sigma"),
    SystLabel = cms.string('MCSmearLowR9EEDown01sigma'),
    bDiscriminatorLoose = cms.untracked.double(0.275),
    bDiscriminatorMedium = cms.untracked.double(0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.int32(0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","7")),
    jetsNumberThreshold = cms.untracked.int32(4)
)


process.flashggTTHHadronicTagMCSmearLowR9EEUp01sigma = cms.EDProducer("FlashggTTHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EEUp01sigma"),
    SystLabel = cms.string('MCSmearLowR9EEUp01sigma'),
    bDiscriminatorLoose = cms.untracked.double(0.275),
    bDiscriminatorMedium = cms.untracked.double(0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.int32(0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","7")),
    jetsNumberThreshold = cms.untracked.int32(4)
)


process.flashggTTHLeptonicTag = cms.EDProducer("FlashggTTHLeptonicTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVA"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string(''),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    bDiscriminator = cms.untracked.vdouble(0.275, 0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.double(1.0),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRJetLepThreshold = cms.untracked.double(0.5),
    deltaRJetSubLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(0.5),
    deltaRMuonJetcountThreshold = cms.untracked.double(2.0),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJets","0"), cms.InputTag("flashggUnpackedJets","1"), cms.InputTag("flashggUnpackedJets","2"), cms.InputTag("flashggUnpackedJets","3"), cms.InputTag("flashggUnpackedJets","4"), 
        cms.InputTag("flashggUnpackedJets","5"), cms.InputTag("flashggUnpackedJets","6"), cms.InputTag("flashggUnpackedJets","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(30.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.5),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggTTHLeptonicTagMCScaleHighR9EBDown01sigma = cms.EDProducer("FlashggTTHLeptonicTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EBDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleHighR9EBDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    bDiscriminator = cms.untracked.vdouble(0.275, 0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.double(1.0),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRJetLepThreshold = cms.untracked.double(0.5),
    deltaRJetSubLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(0.5),
    deltaRMuonJetcountThreshold = cms.untracked.double(2.0),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(30.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.5),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggTTHLeptonicTagMCScaleHighR9EBUp01sigma = cms.EDProducer("FlashggTTHLeptonicTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EBUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleHighR9EBUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    bDiscriminator = cms.untracked.vdouble(0.275, 0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.double(1.0),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRJetLepThreshold = cms.untracked.double(0.5),
    deltaRJetSubLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(0.5),
    deltaRMuonJetcountThreshold = cms.untracked.double(2.0),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(30.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.5),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggTTHLeptonicTagMCScaleHighR9EEDown01sigma = cms.EDProducer("FlashggTTHLeptonicTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EEDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleHighR9EEDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    bDiscriminator = cms.untracked.vdouble(0.275, 0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.double(1.0),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRJetLepThreshold = cms.untracked.double(0.5),
    deltaRJetSubLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(0.5),
    deltaRMuonJetcountThreshold = cms.untracked.double(2.0),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(30.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.5),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggTTHLeptonicTagMCScaleHighR9EEUp01sigma = cms.EDProducer("FlashggTTHLeptonicTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EEUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleHighR9EEUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    bDiscriminator = cms.untracked.vdouble(0.275, 0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.double(1.0),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRJetLepThreshold = cms.untracked.double(0.5),
    deltaRJetSubLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(0.5),
    deltaRMuonJetcountThreshold = cms.untracked.double(2.0),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(30.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.5),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggTTHLeptonicTagMCScaleLowR9EBDown01sigma = cms.EDProducer("FlashggTTHLeptonicTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EBDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleLowR9EBDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    bDiscriminator = cms.untracked.vdouble(0.275, 0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.double(1.0),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRJetLepThreshold = cms.untracked.double(0.5),
    deltaRJetSubLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(0.5),
    deltaRMuonJetcountThreshold = cms.untracked.double(2.0),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(30.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.5),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggTTHLeptonicTagMCScaleLowR9EBUp01sigma = cms.EDProducer("FlashggTTHLeptonicTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EBUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleLowR9EBUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    bDiscriminator = cms.untracked.vdouble(0.275, 0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.double(1.0),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRJetLepThreshold = cms.untracked.double(0.5),
    deltaRJetSubLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(0.5),
    deltaRMuonJetcountThreshold = cms.untracked.double(2.0),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(30.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.5),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggTTHLeptonicTagMCScaleLowR9EEDown01sigma = cms.EDProducer("FlashggTTHLeptonicTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EEDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleLowR9EEDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    bDiscriminator = cms.untracked.vdouble(0.275, 0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.double(1.0),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRJetLepThreshold = cms.untracked.double(0.5),
    deltaRJetSubLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(0.5),
    deltaRMuonJetcountThreshold = cms.untracked.double(2.0),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(30.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.5),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggTTHLeptonicTagMCScaleLowR9EEUp01sigma = cms.EDProducer("FlashggTTHLeptonicTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EEUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleLowR9EEUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    bDiscriminator = cms.untracked.vdouble(0.275, 0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.double(1.0),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRJetLepThreshold = cms.untracked.double(0.5),
    deltaRJetSubLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(0.5),
    deltaRMuonJetcountThreshold = cms.untracked.double(2.0),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(30.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.5),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggTTHLeptonicTagMCSmearHighR9EBPhiDown01sigma = cms.EDProducer("FlashggTTHLeptonicTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBPhiDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearHighR9EBPhiDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    bDiscriminator = cms.untracked.vdouble(0.275, 0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.double(1.0),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRJetLepThreshold = cms.untracked.double(0.5),
    deltaRJetSubLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(0.5),
    deltaRMuonJetcountThreshold = cms.untracked.double(2.0),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(30.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.5),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggTTHLeptonicTagMCSmearHighR9EBPhiUp01sigma = cms.EDProducer("FlashggTTHLeptonicTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBPhiUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearHighR9EBPhiUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    bDiscriminator = cms.untracked.vdouble(0.275, 0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.double(1.0),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRJetLepThreshold = cms.untracked.double(0.5),
    deltaRJetSubLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(0.5),
    deltaRMuonJetcountThreshold = cms.untracked.double(2.0),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(30.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.5),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggTTHLeptonicTagMCSmearHighR9EBRhoDown01sigma = cms.EDProducer("FlashggTTHLeptonicTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBRhoDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearHighR9EBRhoDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    bDiscriminator = cms.untracked.vdouble(0.275, 0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.double(1.0),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRJetLepThreshold = cms.untracked.double(0.5),
    deltaRJetSubLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(0.5),
    deltaRMuonJetcountThreshold = cms.untracked.double(2.0),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(30.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.5),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggTTHLeptonicTagMCSmearHighR9EBRhoUp01sigma = cms.EDProducer("FlashggTTHLeptonicTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBRhoUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearHighR9EBRhoUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    bDiscriminator = cms.untracked.vdouble(0.275, 0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.double(1.0),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRJetLepThreshold = cms.untracked.double(0.5),
    deltaRJetSubLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(0.5),
    deltaRMuonJetcountThreshold = cms.untracked.double(2.0),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(30.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.5),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggTTHLeptonicTagMCSmearHighR9EEDown01sigma = cms.EDProducer("FlashggTTHLeptonicTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EEDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearHighR9EEDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    bDiscriminator = cms.untracked.vdouble(0.275, 0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.double(1.0),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRJetLepThreshold = cms.untracked.double(0.5),
    deltaRJetSubLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(0.5),
    deltaRMuonJetcountThreshold = cms.untracked.double(2.0),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(30.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.5),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggTTHLeptonicTagMCSmearHighR9EEUp01sigma = cms.EDProducer("FlashggTTHLeptonicTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EEUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearHighR9EEUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    bDiscriminator = cms.untracked.vdouble(0.275, 0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.double(1.0),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRJetLepThreshold = cms.untracked.double(0.5),
    deltaRJetSubLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(0.5),
    deltaRMuonJetcountThreshold = cms.untracked.double(2.0),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(30.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.5),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggTTHLeptonicTagMCSmearLowR9EBPhiDown01sigma = cms.EDProducer("FlashggTTHLeptonicTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBPhiDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearLowR9EBPhiDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    bDiscriminator = cms.untracked.vdouble(0.275, 0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.double(1.0),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRJetLepThreshold = cms.untracked.double(0.5),
    deltaRJetSubLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(0.5),
    deltaRMuonJetcountThreshold = cms.untracked.double(2.0),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(30.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.5),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggTTHLeptonicTagMCSmearLowR9EBPhiUp01sigma = cms.EDProducer("FlashggTTHLeptonicTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBPhiUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearLowR9EBPhiUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    bDiscriminator = cms.untracked.vdouble(0.275, 0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.double(1.0),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRJetLepThreshold = cms.untracked.double(0.5),
    deltaRJetSubLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(0.5),
    deltaRMuonJetcountThreshold = cms.untracked.double(2.0),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(30.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.5),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggTTHLeptonicTagMCSmearLowR9EBRhoDown01sigma = cms.EDProducer("FlashggTTHLeptonicTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBRhoDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearLowR9EBRhoDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    bDiscriminator = cms.untracked.vdouble(0.275, 0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.double(1.0),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRJetLepThreshold = cms.untracked.double(0.5),
    deltaRJetSubLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(0.5),
    deltaRMuonJetcountThreshold = cms.untracked.double(2.0),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(30.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.5),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggTTHLeptonicTagMCSmearLowR9EBRhoUp01sigma = cms.EDProducer("FlashggTTHLeptonicTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBRhoUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearLowR9EBRhoUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    bDiscriminator = cms.untracked.vdouble(0.275, 0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.double(1.0),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRJetLepThreshold = cms.untracked.double(0.5),
    deltaRJetSubLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(0.5),
    deltaRMuonJetcountThreshold = cms.untracked.double(2.0),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(30.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.5),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggTTHLeptonicTagMCSmearLowR9EEDown01sigma = cms.EDProducer("FlashggTTHLeptonicTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EEDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearLowR9EEDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    bDiscriminator = cms.untracked.vdouble(0.275, 0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.double(1.0),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRJetLepThreshold = cms.untracked.double(0.5),
    deltaRJetSubLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(0.5),
    deltaRMuonJetcountThreshold = cms.untracked.double(2.0),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(30.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.5),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggTTHLeptonicTagMCSmearLowR9EEUp01sigma = cms.EDProducer("FlashggTTHLeptonicTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EEUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearLowR9EEUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    bDiscriminator = cms.untracked.vdouble(0.275, 0.545),
    bTag = cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bjetsNumberThreshold = cms.untracked.double(1.0),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRJetLepThreshold = cms.untracked.double(0.5),
    deltaRJetSubLeadPhoThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(0.5),
    deltaRMuonJetcountThreshold = cms.untracked.double(2.0),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(30.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.5),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggTagSorter = cms.EDProducer("FlashggTagSorter",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics"),
    TagPriorityRanges = cms.VPSet(cms.PSet(
        TagName = cms.InputTag("flashggVHTightTag")
    ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHLooseTag")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHHadronicTag")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHEtTag")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHLeptonicTag")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHHadronicTag")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(0),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggVBFTag")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(1),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggUntagged")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(2),
            MinCategory = cms.untracked.int32(1),
            TagName = cms.InputTag("flashggVBFTag")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(4),
            MinCategory = cms.untracked.int32(2),
            TagName = cms.InputTag("flashggUntagged")
        )),
    massCutLower = cms.untracked.double(100),
    massCutUpper = cms.untracked.double(180.0)
)


process.flashggTagSorterMCScaleHighR9EBDown01sigma = cms.EDProducer("FlashggTagSorter",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBDown01sigma"),
    TagPriorityRanges = cms.VPSet(cms.PSet(
        TagName = cms.InputTag("flashggVHTightTagMCScaleHighR9EBDown01sigma")
    ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHLooseTagMCScaleHighR9EBDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHHadronicTagMCScaleHighR9EBDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHEtTagMCScaleHighR9EBDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHLeptonicTagMCScaleHighR9EBDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHHadronicTagMCScaleHighR9EBDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(0),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggVBFTagMCScaleHighR9EBDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(1),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggUntaggedMCScaleHighR9EBDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(2),
            MinCategory = cms.untracked.int32(1),
            TagName = cms.InputTag("flashggVBFTagMCScaleHighR9EBDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(4),
            MinCategory = cms.untracked.int32(2),
            TagName = cms.InputTag("flashggUntaggedMCScaleHighR9EBDown01sigma")
        )),
    massCutLower = cms.untracked.double(100),
    massCutUpper = cms.untracked.double(180.0)
)


process.flashggTagSorterMCScaleHighR9EBUp01sigma = cms.EDProducer("FlashggTagSorter",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBUp01sigma"),
    TagPriorityRanges = cms.VPSet(cms.PSet(
        TagName = cms.InputTag("flashggVHTightTagMCScaleHighR9EBUp01sigma")
    ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHLooseTagMCScaleHighR9EBUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHHadronicTagMCScaleHighR9EBUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHEtTagMCScaleHighR9EBUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHLeptonicTagMCScaleHighR9EBUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHHadronicTagMCScaleHighR9EBUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(0),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggVBFTagMCScaleHighR9EBUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(1),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggUntaggedMCScaleHighR9EBUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(2),
            MinCategory = cms.untracked.int32(1),
            TagName = cms.InputTag("flashggVBFTagMCScaleHighR9EBUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(4),
            MinCategory = cms.untracked.int32(2),
            TagName = cms.InputTag("flashggUntaggedMCScaleHighR9EBUp01sigma")
        )),
    massCutLower = cms.untracked.double(100),
    massCutUpper = cms.untracked.double(180.0)
)


process.flashggTagSorterMCScaleHighR9EEDown01sigma = cms.EDProducer("FlashggTagSorter",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEDown01sigma"),
    TagPriorityRanges = cms.VPSet(cms.PSet(
        TagName = cms.InputTag("flashggVHTightTagMCScaleHighR9EEDown01sigma")
    ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHLooseTagMCScaleHighR9EEDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHHadronicTagMCScaleHighR9EEDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHEtTagMCScaleHighR9EEDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHLeptonicTagMCScaleHighR9EEDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHHadronicTagMCScaleHighR9EEDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(0),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggVBFTagMCScaleHighR9EEDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(1),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggUntaggedMCScaleHighR9EEDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(2),
            MinCategory = cms.untracked.int32(1),
            TagName = cms.InputTag("flashggVBFTagMCScaleHighR9EEDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(4),
            MinCategory = cms.untracked.int32(2),
            TagName = cms.InputTag("flashggUntaggedMCScaleHighR9EEDown01sigma")
        )),
    massCutLower = cms.untracked.double(100),
    massCutUpper = cms.untracked.double(180.0)
)


process.flashggTagSorterMCScaleHighR9EEUp01sigma = cms.EDProducer("FlashggTagSorter",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEUp01sigma"),
    TagPriorityRanges = cms.VPSet(cms.PSet(
        TagName = cms.InputTag("flashggVHTightTagMCScaleHighR9EEUp01sigma")
    ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHLooseTagMCScaleHighR9EEUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHHadronicTagMCScaleHighR9EEUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHEtTagMCScaleHighR9EEUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHLeptonicTagMCScaleHighR9EEUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHHadronicTagMCScaleHighR9EEUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(0),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggVBFTagMCScaleHighR9EEUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(1),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggUntaggedMCScaleHighR9EEUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(2),
            MinCategory = cms.untracked.int32(1),
            TagName = cms.InputTag("flashggVBFTagMCScaleHighR9EEUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(4),
            MinCategory = cms.untracked.int32(2),
            TagName = cms.InputTag("flashggUntaggedMCScaleHighR9EEUp01sigma")
        )),
    massCutLower = cms.untracked.double(100),
    massCutUpper = cms.untracked.double(180.0)
)


process.flashggTagSorterMCScaleLowR9EBDown01sigma = cms.EDProducer("FlashggTagSorter",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBDown01sigma"),
    TagPriorityRanges = cms.VPSet(cms.PSet(
        TagName = cms.InputTag("flashggVHTightTagMCScaleLowR9EBDown01sigma")
    ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHLooseTagMCScaleLowR9EBDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHHadronicTagMCScaleLowR9EBDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHEtTagMCScaleLowR9EBDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHLeptonicTagMCScaleLowR9EBDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHHadronicTagMCScaleLowR9EBDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(0),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggVBFTagMCScaleLowR9EBDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(1),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggUntaggedMCScaleLowR9EBDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(2),
            MinCategory = cms.untracked.int32(1),
            TagName = cms.InputTag("flashggVBFTagMCScaleLowR9EBDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(4),
            MinCategory = cms.untracked.int32(2),
            TagName = cms.InputTag("flashggUntaggedMCScaleLowR9EBDown01sigma")
        )),
    massCutLower = cms.untracked.double(100),
    massCutUpper = cms.untracked.double(180.0)
)


process.flashggTagSorterMCScaleLowR9EBUp01sigma = cms.EDProducer("FlashggTagSorter",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBUp01sigma"),
    TagPriorityRanges = cms.VPSet(cms.PSet(
        TagName = cms.InputTag("flashggVHTightTagMCScaleLowR9EBUp01sigma")
    ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHLooseTagMCScaleLowR9EBUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHHadronicTagMCScaleLowR9EBUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHEtTagMCScaleLowR9EBUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHLeptonicTagMCScaleLowR9EBUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHHadronicTagMCScaleLowR9EBUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(0),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggVBFTagMCScaleLowR9EBUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(1),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggUntaggedMCScaleLowR9EBUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(2),
            MinCategory = cms.untracked.int32(1),
            TagName = cms.InputTag("flashggVBFTagMCScaleLowR9EBUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(4),
            MinCategory = cms.untracked.int32(2),
            TagName = cms.InputTag("flashggUntaggedMCScaleLowR9EBUp01sigma")
        )),
    massCutLower = cms.untracked.double(100),
    massCutUpper = cms.untracked.double(180.0)
)


process.flashggTagSorterMCScaleLowR9EEDown01sigma = cms.EDProducer("FlashggTagSorter",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEDown01sigma"),
    TagPriorityRanges = cms.VPSet(cms.PSet(
        TagName = cms.InputTag("flashggVHTightTagMCScaleLowR9EEDown01sigma")
    ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHLooseTagMCScaleLowR9EEDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHHadronicTagMCScaleLowR9EEDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHEtTagMCScaleLowR9EEDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHLeptonicTagMCScaleLowR9EEDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHHadronicTagMCScaleLowR9EEDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(0),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggVBFTagMCScaleLowR9EEDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(1),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggUntaggedMCScaleLowR9EEDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(2),
            MinCategory = cms.untracked.int32(1),
            TagName = cms.InputTag("flashggVBFTagMCScaleLowR9EEDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(4),
            MinCategory = cms.untracked.int32(2),
            TagName = cms.InputTag("flashggUntaggedMCScaleLowR9EEDown01sigma")
        )),
    massCutLower = cms.untracked.double(100),
    massCutUpper = cms.untracked.double(180.0)
)


process.flashggTagSorterMCScaleLowR9EEUp01sigma = cms.EDProducer("FlashggTagSorter",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEUp01sigma"),
    TagPriorityRanges = cms.VPSet(cms.PSet(
        TagName = cms.InputTag("flashggVHTightTagMCScaleLowR9EEUp01sigma")
    ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHLooseTagMCScaleLowR9EEUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHHadronicTagMCScaleLowR9EEUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHEtTagMCScaleLowR9EEUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHLeptonicTagMCScaleLowR9EEUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHHadronicTagMCScaleLowR9EEUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(0),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggVBFTagMCScaleLowR9EEUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(1),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggUntaggedMCScaleLowR9EEUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(2),
            MinCategory = cms.untracked.int32(1),
            TagName = cms.InputTag("flashggVBFTagMCScaleLowR9EEUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(4),
            MinCategory = cms.untracked.int32(2),
            TagName = cms.InputTag("flashggUntaggedMCScaleLowR9EEUp01sigma")
        )),
    massCutLower = cms.untracked.double(100),
    massCutUpper = cms.untracked.double(180.0)
)


process.flashggTagSorterMCSmearHighR9EBPhiDown01sigma = cms.EDProducer("FlashggTagSorter",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiDown01sigma"),
    TagPriorityRanges = cms.VPSet(cms.PSet(
        TagName = cms.InputTag("flashggVHTightTagMCSmearHighR9EBPhiDown01sigma")
    ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHLooseTagMCSmearHighR9EBPhiDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHHadronicTagMCSmearHighR9EBPhiDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHEtTagMCSmearHighR9EBPhiDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHLeptonicTagMCSmearHighR9EBPhiDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHHadronicTagMCSmearHighR9EBPhiDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(0),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggVBFTagMCSmearHighR9EBPhiDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(1),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggUntaggedMCSmearHighR9EBPhiDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(2),
            MinCategory = cms.untracked.int32(1),
            TagName = cms.InputTag("flashggVBFTagMCSmearHighR9EBPhiDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(4),
            MinCategory = cms.untracked.int32(2),
            TagName = cms.InputTag("flashggUntaggedMCSmearHighR9EBPhiDown01sigma")
        )),
    massCutLower = cms.untracked.double(100),
    massCutUpper = cms.untracked.double(180.0)
)


process.flashggTagSorterMCSmearHighR9EBPhiUp01sigma = cms.EDProducer("FlashggTagSorter",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiUp01sigma"),
    TagPriorityRanges = cms.VPSet(cms.PSet(
        TagName = cms.InputTag("flashggVHTightTagMCSmearHighR9EBPhiUp01sigma")
    ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHLooseTagMCSmearHighR9EBPhiUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHHadronicTagMCSmearHighR9EBPhiUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHEtTagMCSmearHighR9EBPhiUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHLeptonicTagMCSmearHighR9EBPhiUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHHadronicTagMCSmearHighR9EBPhiUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(0),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggVBFTagMCSmearHighR9EBPhiUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(1),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggUntaggedMCSmearHighR9EBPhiUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(2),
            MinCategory = cms.untracked.int32(1),
            TagName = cms.InputTag("flashggVBFTagMCSmearHighR9EBPhiUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(4),
            MinCategory = cms.untracked.int32(2),
            TagName = cms.InputTag("flashggUntaggedMCSmearHighR9EBPhiUp01sigma")
        )),
    massCutLower = cms.untracked.double(100),
    massCutUpper = cms.untracked.double(180.0)
)


process.flashggTagSorterMCSmearHighR9EBRhoDown01sigma = cms.EDProducer("FlashggTagSorter",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoDown01sigma"),
    TagPriorityRanges = cms.VPSet(cms.PSet(
        TagName = cms.InputTag("flashggVHTightTagMCSmearHighR9EBRhoDown01sigma")
    ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHLooseTagMCSmearHighR9EBRhoDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHHadronicTagMCSmearHighR9EBRhoDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHEtTagMCSmearHighR9EBRhoDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHLeptonicTagMCSmearHighR9EBRhoDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHHadronicTagMCSmearHighR9EBRhoDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(0),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggVBFTagMCSmearHighR9EBRhoDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(1),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggUntaggedMCSmearHighR9EBRhoDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(2),
            MinCategory = cms.untracked.int32(1),
            TagName = cms.InputTag("flashggVBFTagMCSmearHighR9EBRhoDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(4),
            MinCategory = cms.untracked.int32(2),
            TagName = cms.InputTag("flashggUntaggedMCSmearHighR9EBRhoDown01sigma")
        )),
    massCutLower = cms.untracked.double(100),
    massCutUpper = cms.untracked.double(180.0)
)


process.flashggTagSorterMCSmearHighR9EBRhoUp01sigma = cms.EDProducer("FlashggTagSorter",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoUp01sigma"),
    TagPriorityRanges = cms.VPSet(cms.PSet(
        TagName = cms.InputTag("flashggVHTightTagMCSmearHighR9EBRhoUp01sigma")
    ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHLooseTagMCSmearHighR9EBRhoUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHHadronicTagMCSmearHighR9EBRhoUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHEtTagMCSmearHighR9EBRhoUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHLeptonicTagMCSmearHighR9EBRhoUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHHadronicTagMCSmearHighR9EBRhoUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(0),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggVBFTagMCSmearHighR9EBRhoUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(1),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggUntaggedMCSmearHighR9EBRhoUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(2),
            MinCategory = cms.untracked.int32(1),
            TagName = cms.InputTag("flashggVBFTagMCSmearHighR9EBRhoUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(4),
            MinCategory = cms.untracked.int32(2),
            TagName = cms.InputTag("flashggUntaggedMCSmearHighR9EBRhoUp01sigma")
        )),
    massCutLower = cms.untracked.double(100),
    massCutUpper = cms.untracked.double(180.0)
)


process.flashggTagSorterMCSmearHighR9EEDown01sigma = cms.EDProducer("FlashggTagSorter",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEDown01sigma"),
    TagPriorityRanges = cms.VPSet(cms.PSet(
        TagName = cms.InputTag("flashggVHTightTagMCSmearHighR9EEDown01sigma")
    ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHLooseTagMCSmearHighR9EEDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHHadronicTagMCSmearHighR9EEDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHEtTagMCSmearHighR9EEDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHLeptonicTagMCSmearHighR9EEDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHHadronicTagMCSmearHighR9EEDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(0),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggVBFTagMCSmearHighR9EEDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(1),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggUntaggedMCSmearHighR9EEDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(2),
            MinCategory = cms.untracked.int32(1),
            TagName = cms.InputTag("flashggVBFTagMCSmearHighR9EEDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(4),
            MinCategory = cms.untracked.int32(2),
            TagName = cms.InputTag("flashggUntaggedMCSmearHighR9EEDown01sigma")
        )),
    massCutLower = cms.untracked.double(100),
    massCutUpper = cms.untracked.double(180.0)
)


process.flashggTagSorterMCSmearHighR9EEUp01sigma = cms.EDProducer("FlashggTagSorter",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEUp01sigma"),
    TagPriorityRanges = cms.VPSet(cms.PSet(
        TagName = cms.InputTag("flashggVHTightTagMCSmearHighR9EEUp01sigma")
    ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHLooseTagMCSmearHighR9EEUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHHadronicTagMCSmearHighR9EEUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHEtTagMCSmearHighR9EEUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHLeptonicTagMCSmearHighR9EEUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHHadronicTagMCSmearHighR9EEUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(0),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggVBFTagMCSmearHighR9EEUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(1),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggUntaggedMCSmearHighR9EEUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(2),
            MinCategory = cms.untracked.int32(1),
            TagName = cms.InputTag("flashggVBFTagMCSmearHighR9EEUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(4),
            MinCategory = cms.untracked.int32(2),
            TagName = cms.InputTag("flashggUntaggedMCSmearHighR9EEUp01sigma")
        )),
    massCutLower = cms.untracked.double(100),
    massCutUpper = cms.untracked.double(180.0)
)


process.flashggTagSorterMCSmearLowR9EBPhiDown01sigma = cms.EDProducer("FlashggTagSorter",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiDown01sigma"),
    TagPriorityRanges = cms.VPSet(cms.PSet(
        TagName = cms.InputTag("flashggVHTightTagMCSmearLowR9EBPhiDown01sigma")
    ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHLooseTagMCSmearLowR9EBPhiDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHHadronicTagMCSmearLowR9EBPhiDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHEtTagMCSmearLowR9EBPhiDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHLeptonicTagMCSmearLowR9EBPhiDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHHadronicTagMCSmearLowR9EBPhiDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(0),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggVBFTagMCSmearLowR9EBPhiDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(1),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggUntaggedMCSmearLowR9EBPhiDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(2),
            MinCategory = cms.untracked.int32(1),
            TagName = cms.InputTag("flashggVBFTagMCSmearLowR9EBPhiDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(4),
            MinCategory = cms.untracked.int32(2),
            TagName = cms.InputTag("flashggUntaggedMCSmearLowR9EBPhiDown01sigma")
        )),
    massCutLower = cms.untracked.double(100),
    massCutUpper = cms.untracked.double(180.0)
)


process.flashggTagSorterMCSmearLowR9EBPhiUp01sigma = cms.EDProducer("FlashggTagSorter",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiUp01sigma"),
    TagPriorityRanges = cms.VPSet(cms.PSet(
        TagName = cms.InputTag("flashggVHTightTagMCSmearLowR9EBPhiUp01sigma")
    ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHLooseTagMCSmearLowR9EBPhiUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHHadronicTagMCSmearLowR9EBPhiUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHEtTagMCSmearLowR9EBPhiUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHLeptonicTagMCSmearLowR9EBPhiUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHHadronicTagMCSmearLowR9EBPhiUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(0),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggVBFTagMCSmearLowR9EBPhiUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(1),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggUntaggedMCSmearLowR9EBPhiUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(2),
            MinCategory = cms.untracked.int32(1),
            TagName = cms.InputTag("flashggVBFTagMCSmearLowR9EBPhiUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(4),
            MinCategory = cms.untracked.int32(2),
            TagName = cms.InputTag("flashggUntaggedMCSmearLowR9EBPhiUp01sigma")
        )),
    massCutLower = cms.untracked.double(100),
    massCutUpper = cms.untracked.double(180.0)
)


process.flashggTagSorterMCSmearLowR9EBRhoDown01sigma = cms.EDProducer("FlashggTagSorter",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoDown01sigma"),
    TagPriorityRanges = cms.VPSet(cms.PSet(
        TagName = cms.InputTag("flashggVHTightTagMCSmearLowR9EBRhoDown01sigma")
    ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHLooseTagMCSmearLowR9EBRhoDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHHadronicTagMCSmearLowR9EBRhoDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHEtTagMCSmearLowR9EBRhoDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHLeptonicTagMCSmearLowR9EBRhoDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHHadronicTagMCSmearLowR9EBRhoDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(0),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggVBFTagMCSmearLowR9EBRhoDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(1),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggUntaggedMCSmearLowR9EBRhoDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(2),
            MinCategory = cms.untracked.int32(1),
            TagName = cms.InputTag("flashggVBFTagMCSmearLowR9EBRhoDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(4),
            MinCategory = cms.untracked.int32(2),
            TagName = cms.InputTag("flashggUntaggedMCSmearLowR9EBRhoDown01sigma")
        )),
    massCutLower = cms.untracked.double(100),
    massCutUpper = cms.untracked.double(180.0)
)


process.flashggTagSorterMCSmearLowR9EBRhoUp01sigma = cms.EDProducer("FlashggTagSorter",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoUp01sigma"),
    TagPriorityRanges = cms.VPSet(cms.PSet(
        TagName = cms.InputTag("flashggVHTightTagMCSmearLowR9EBRhoUp01sigma")
    ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHLooseTagMCSmearLowR9EBRhoUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHHadronicTagMCSmearLowR9EBRhoUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHEtTagMCSmearLowR9EBRhoUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHLeptonicTagMCSmearLowR9EBRhoUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHHadronicTagMCSmearLowR9EBRhoUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(0),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggVBFTagMCSmearLowR9EBRhoUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(1),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggUntaggedMCSmearLowR9EBRhoUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(2),
            MinCategory = cms.untracked.int32(1),
            TagName = cms.InputTag("flashggVBFTagMCSmearLowR9EBRhoUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(4),
            MinCategory = cms.untracked.int32(2),
            TagName = cms.InputTag("flashggUntaggedMCSmearLowR9EBRhoUp01sigma")
        )),
    massCutLower = cms.untracked.double(100),
    massCutUpper = cms.untracked.double(180.0)
)


process.flashggTagSorterMCSmearLowR9EEDown01sigma = cms.EDProducer("FlashggTagSorter",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEDown01sigma"),
    TagPriorityRanges = cms.VPSet(cms.PSet(
        TagName = cms.InputTag("flashggVHTightTagMCSmearLowR9EEDown01sigma")
    ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHLooseTagMCSmearLowR9EEDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHHadronicTagMCSmearLowR9EEDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHEtTagMCSmearLowR9EEDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHLeptonicTagMCSmearLowR9EEDown01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHHadronicTagMCSmearLowR9EEDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(0),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggVBFTagMCSmearLowR9EEDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(1),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggUntaggedMCSmearLowR9EEDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(2),
            MinCategory = cms.untracked.int32(1),
            TagName = cms.InputTag("flashggVBFTagMCSmearLowR9EEDown01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(4),
            MinCategory = cms.untracked.int32(2),
            TagName = cms.InputTag("flashggUntaggedMCSmearLowR9EEDown01sigma")
        )),
    massCutLower = cms.untracked.double(100),
    massCutUpper = cms.untracked.double(180.0)
)


process.flashggTagSorterMCSmearLowR9EEUp01sigma = cms.EDProducer("FlashggTagSorter",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEUp01sigma"),
    TagPriorityRanges = cms.VPSet(cms.PSet(
        TagName = cms.InputTag("flashggVHTightTagMCSmearLowR9EEUp01sigma")
    ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHLooseTagMCSmearLowR9EEUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHHadronicTagMCSmearLowR9EEUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggVHEtTagMCSmearLowR9EEUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHLeptonicTagMCSmearLowR9EEUp01sigma")
        ), 
        cms.PSet(
            TagName = cms.InputTag("flashggTTHHadronicTagMCSmearLowR9EEUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(0),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggVBFTagMCSmearLowR9EEUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(1),
            MinCategory = cms.untracked.int32(0),
            TagName = cms.InputTag("flashggUntaggedMCSmearLowR9EEUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(2),
            MinCategory = cms.untracked.int32(1),
            TagName = cms.InputTag("flashggVBFTagMCSmearLowR9EEUp01sigma")
        ), 
        cms.PSet(
            MaxCategory = cms.untracked.int32(4),
            MinCategory = cms.untracked.int32(2),
            TagName = cms.InputTag("flashggUntaggedMCSmearLowR9EEUp01sigma")
        )),
    massCutLower = cms.untracked.double(100),
    massCutUpper = cms.untracked.double(180.0)
)


process.flashggUnpackedJets = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedJetsMCScaleHighR9EBDown01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedJetsMCScaleHighR9EBUp01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedJetsMCScaleHighR9EEDown01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedJetsMCScaleHighR9EEUp01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedJetsMCScaleLowR9EBDown01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedJetsMCScaleLowR9EBUp01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedJetsMCScaleLowR9EEDown01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedJetsMCScaleLowR9EEUp01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedJetsMCSmearHighR9EEDown01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedJetsMCSmearHighR9EEUp01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedJetsMCSmearLowR9EEDown01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedJetsMCSmearLowR9EEUp01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedPuppiJets = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalPuppiJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedPuppiJetsMCScaleHighR9EBDown01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalPuppiJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedPuppiJetsMCScaleHighR9EBUp01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalPuppiJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedPuppiJetsMCScaleHighR9EEDown01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalPuppiJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedPuppiJetsMCScaleHighR9EEUp01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalPuppiJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedPuppiJetsMCScaleLowR9EBDown01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalPuppiJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedPuppiJetsMCScaleLowR9EBUp01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalPuppiJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedPuppiJetsMCScaleLowR9EEDown01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalPuppiJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedPuppiJetsMCScaleLowR9EEUp01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalPuppiJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedPuppiJetsMCSmearHighR9EBPhiDown01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalPuppiJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedPuppiJetsMCSmearHighR9EBPhiUp01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalPuppiJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedPuppiJetsMCSmearHighR9EBRhoDown01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalPuppiJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedPuppiJetsMCSmearHighR9EBRhoUp01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalPuppiJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedPuppiJetsMCSmearHighR9EEDown01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalPuppiJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedPuppiJetsMCSmearHighR9EEUp01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalPuppiJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedPuppiJetsMCSmearLowR9EBPhiDown01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalPuppiJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedPuppiJetsMCSmearLowR9EBPhiUp01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalPuppiJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedPuppiJetsMCSmearLowR9EBRhoDown01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalPuppiJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedPuppiJetsMCSmearLowR9EBRhoUp01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalPuppiJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedPuppiJetsMCSmearLowR9EEDown01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalPuppiJets"),
    NCollections = cms.uint32(8)
)


process.flashggUnpackedPuppiJetsMCSmearLowR9EEUp01sigma = cms.EDProducer("FlashggVectorVectorJetUnpacker",
    JetsTag = cms.InputTag("flashggFinalPuppiJets"),
    NCollections = cms.uint32(8)
)


process.flashggUntagged = cms.EDProducer("FlashggUntaggedTagProducer",
    Boundaries = cms.untracked.vdouble(0.07, 0.31, 0.62, 0.86, 0.98),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVA"),
    SystLabel = cms.string('')
)


process.flashggUntaggedMCScaleHighR9EBDown01sigma = cms.EDProducer("FlashggUntaggedTagProducer",
    Boundaries = cms.untracked.vdouble(0.07, 0.31, 0.62, 0.86, 0.98),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EBDown01sigma"),
    SystLabel = cms.string('MCScaleHighR9EBDown01sigma')
)


process.flashggUntaggedMCScaleHighR9EBUp01sigma = cms.EDProducer("FlashggUntaggedTagProducer",
    Boundaries = cms.untracked.vdouble(0.07, 0.31, 0.62, 0.86, 0.98),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EBUp01sigma"),
    SystLabel = cms.string('MCScaleHighR9EBUp01sigma')
)


process.flashggUntaggedMCScaleHighR9EEDown01sigma = cms.EDProducer("FlashggUntaggedTagProducer",
    Boundaries = cms.untracked.vdouble(0.07, 0.31, 0.62, 0.86, 0.98),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EEDown01sigma"),
    SystLabel = cms.string('MCScaleHighR9EEDown01sigma')
)


process.flashggUntaggedMCScaleHighR9EEUp01sigma = cms.EDProducer("FlashggUntaggedTagProducer",
    Boundaries = cms.untracked.vdouble(0.07, 0.31, 0.62, 0.86, 0.98),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EEUp01sigma"),
    SystLabel = cms.string('MCScaleHighR9EEUp01sigma')
)


process.flashggUntaggedMCScaleLowR9EBDown01sigma = cms.EDProducer("FlashggUntaggedTagProducer",
    Boundaries = cms.untracked.vdouble(0.07, 0.31, 0.62, 0.86, 0.98),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EBDown01sigma"),
    SystLabel = cms.string('MCScaleLowR9EBDown01sigma')
)


process.flashggUntaggedMCScaleLowR9EBUp01sigma = cms.EDProducer("FlashggUntaggedTagProducer",
    Boundaries = cms.untracked.vdouble(0.07, 0.31, 0.62, 0.86, 0.98),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EBUp01sigma"),
    SystLabel = cms.string('MCScaleLowR9EBUp01sigma')
)


process.flashggUntaggedMCScaleLowR9EEDown01sigma = cms.EDProducer("FlashggUntaggedTagProducer",
    Boundaries = cms.untracked.vdouble(0.07, 0.31, 0.62, 0.86, 0.98),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EEDown01sigma"),
    SystLabel = cms.string('MCScaleLowR9EEDown01sigma')
)


process.flashggUntaggedMCScaleLowR9EEUp01sigma = cms.EDProducer("FlashggUntaggedTagProducer",
    Boundaries = cms.untracked.vdouble(0.07, 0.31, 0.62, 0.86, 0.98),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EEUp01sigma"),
    SystLabel = cms.string('MCScaleLowR9EEUp01sigma')
)


process.flashggUntaggedMCSmearHighR9EBPhiDown01sigma = cms.EDProducer("FlashggUntaggedTagProducer",
    Boundaries = cms.untracked.vdouble(0.07, 0.31, 0.62, 0.86, 0.98),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBPhiDown01sigma"),
    SystLabel = cms.string('MCSmearHighR9EBPhiDown01sigma')
)


process.flashggUntaggedMCSmearHighR9EBPhiUp01sigma = cms.EDProducer("FlashggUntaggedTagProducer",
    Boundaries = cms.untracked.vdouble(0.07, 0.31, 0.62, 0.86, 0.98),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBPhiUp01sigma"),
    SystLabel = cms.string('MCSmearHighR9EBPhiUp01sigma')
)


process.flashggUntaggedMCSmearHighR9EBRhoDown01sigma = cms.EDProducer("FlashggUntaggedTagProducer",
    Boundaries = cms.untracked.vdouble(0.07, 0.31, 0.62, 0.86, 0.98),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBRhoDown01sigma"),
    SystLabel = cms.string('MCSmearHighR9EBRhoDown01sigma')
)


process.flashggUntaggedMCSmearHighR9EBRhoUp01sigma = cms.EDProducer("FlashggUntaggedTagProducer",
    Boundaries = cms.untracked.vdouble(0.07, 0.31, 0.62, 0.86, 0.98),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBRhoUp01sigma"),
    SystLabel = cms.string('MCSmearHighR9EBRhoUp01sigma')
)


process.flashggUntaggedMCSmearHighR9EEDown01sigma = cms.EDProducer("FlashggUntaggedTagProducer",
    Boundaries = cms.untracked.vdouble(0.07, 0.31, 0.62, 0.86, 0.98),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EEDown01sigma"),
    SystLabel = cms.string('MCSmearHighR9EEDown01sigma')
)


process.flashggUntaggedMCSmearHighR9EEUp01sigma = cms.EDProducer("FlashggUntaggedTagProducer",
    Boundaries = cms.untracked.vdouble(0.07, 0.31, 0.62, 0.86, 0.98),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EEUp01sigma"),
    SystLabel = cms.string('MCSmearHighR9EEUp01sigma')
)


process.flashggUntaggedMCSmearLowR9EBPhiDown01sigma = cms.EDProducer("FlashggUntaggedTagProducer",
    Boundaries = cms.untracked.vdouble(0.07, 0.31, 0.62, 0.86, 0.98),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBPhiDown01sigma"),
    SystLabel = cms.string('MCSmearLowR9EBPhiDown01sigma')
)


process.flashggUntaggedMCSmearLowR9EBPhiUp01sigma = cms.EDProducer("FlashggUntaggedTagProducer",
    Boundaries = cms.untracked.vdouble(0.07, 0.31, 0.62, 0.86, 0.98),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBPhiUp01sigma"),
    SystLabel = cms.string('MCSmearLowR9EBPhiUp01sigma')
)


process.flashggUntaggedMCSmearLowR9EBRhoDown01sigma = cms.EDProducer("FlashggUntaggedTagProducer",
    Boundaries = cms.untracked.vdouble(0.07, 0.31, 0.62, 0.86, 0.98),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBRhoDown01sigma"),
    SystLabel = cms.string('MCSmearLowR9EBRhoDown01sigma')
)


process.flashggUntaggedMCSmearLowR9EBRhoUp01sigma = cms.EDProducer("FlashggUntaggedTagProducer",
    Boundaries = cms.untracked.vdouble(0.07, 0.31, 0.62, 0.86, 0.98),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBRhoUp01sigma"),
    SystLabel = cms.string('MCSmearLowR9EBRhoUp01sigma')
)


process.flashggUntaggedMCSmearLowR9EEDown01sigma = cms.EDProducer("FlashggUntaggedTagProducer",
    Boundaries = cms.untracked.vdouble(0.07, 0.31, 0.62, 0.86, 0.98),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EEDown01sigma"),
    SystLabel = cms.string('MCSmearLowR9EEDown01sigma')
)


process.flashggUntaggedMCSmearLowR9EEUp01sigma = cms.EDProducer("FlashggUntaggedTagProducer",
    Boundaries = cms.untracked.vdouble(0.07, 0.31, 0.62, 0.86, 0.98),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EEUp01sigma"),
    SystLabel = cms.string('MCSmearLowR9EEUp01sigma')
)


process.flashggVBFDiPhoDiJetMVA = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVA"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVA"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVALegacy = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVA"),
    UseLegacyMVA = cms.untracked.bool(True),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVALegacy"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_vbf_dijet_dipho_evenbkg_scaledwt50_maxdPhi_Gradient.weights.xml')
)


process.flashggVBFDiPhoDiJetMVALegacyMCScaleHighR9EBDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EBDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(True),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVALegacyMCScaleHighR9EBDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_vbf_dijet_dipho_evenbkg_scaledwt50_maxdPhi_Gradient.weights.xml')
)


process.flashggVBFDiPhoDiJetMVALegacyMCScaleHighR9EBUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EBUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(True),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVALegacyMCScaleHighR9EBUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_vbf_dijet_dipho_evenbkg_scaledwt50_maxdPhi_Gradient.weights.xml')
)


process.flashggVBFDiPhoDiJetMVALegacyMCScaleHighR9EEDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EEDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(True),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVALegacyMCScaleHighR9EEDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_vbf_dijet_dipho_evenbkg_scaledwt50_maxdPhi_Gradient.weights.xml')
)


process.flashggVBFDiPhoDiJetMVALegacyMCScaleHighR9EEUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EEUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(True),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVALegacyMCScaleHighR9EEUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_vbf_dijet_dipho_evenbkg_scaledwt50_maxdPhi_Gradient.weights.xml')
)


process.flashggVBFDiPhoDiJetMVALegacyMCScaleLowR9EBDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EBDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(True),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVALegacyMCScaleLowR9EBDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_vbf_dijet_dipho_evenbkg_scaledwt50_maxdPhi_Gradient.weights.xml')
)


process.flashggVBFDiPhoDiJetMVALegacyMCScaleLowR9EBUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EBUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(True),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVALegacyMCScaleLowR9EBUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_vbf_dijet_dipho_evenbkg_scaledwt50_maxdPhi_Gradient.weights.xml')
)


process.flashggVBFDiPhoDiJetMVALegacyMCScaleLowR9EEDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EEDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(True),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVALegacyMCScaleLowR9EEDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_vbf_dijet_dipho_evenbkg_scaledwt50_maxdPhi_Gradient.weights.xml')
)


process.flashggVBFDiPhoDiJetMVALegacyMCScaleLowR9EEUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EEUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(True),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVALegacyMCScaleLowR9EEUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_vbf_dijet_dipho_evenbkg_scaledwt50_maxdPhi_Gradient.weights.xml')
)


process.flashggVBFDiPhoDiJetMVALegacyMCSmearHighR9EBPhiDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBPhiDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(True),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVALegacyMCSmearHighR9EBPhiDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_vbf_dijet_dipho_evenbkg_scaledwt50_maxdPhi_Gradient.weights.xml')
)


process.flashggVBFDiPhoDiJetMVALegacyMCSmearHighR9EBPhiUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBPhiUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(True),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVALegacyMCSmearHighR9EBPhiUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_vbf_dijet_dipho_evenbkg_scaledwt50_maxdPhi_Gradient.weights.xml')
)


process.flashggVBFDiPhoDiJetMVALegacyMCSmearHighR9EBRhoDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBRhoDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(True),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVALegacyMCSmearHighR9EBRhoDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_vbf_dijet_dipho_evenbkg_scaledwt50_maxdPhi_Gradient.weights.xml')
)


process.flashggVBFDiPhoDiJetMVALegacyMCSmearHighR9EBRhoUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBRhoUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(True),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVALegacyMCSmearHighR9EBRhoUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_vbf_dijet_dipho_evenbkg_scaledwt50_maxdPhi_Gradient.weights.xml')
)


process.flashggVBFDiPhoDiJetMVALegacyMCSmearHighR9EEDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EEDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(True),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVALegacyMCSmearHighR9EEDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_vbf_dijet_dipho_evenbkg_scaledwt50_maxdPhi_Gradient.weights.xml')
)


process.flashggVBFDiPhoDiJetMVALegacyMCSmearHighR9EEUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EEUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(True),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVALegacyMCSmearHighR9EEUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_vbf_dijet_dipho_evenbkg_scaledwt50_maxdPhi_Gradient.weights.xml')
)


process.flashggVBFDiPhoDiJetMVALegacyMCSmearLowR9EBPhiDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBPhiDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(True),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVALegacyMCSmearLowR9EBPhiDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_vbf_dijet_dipho_evenbkg_scaledwt50_maxdPhi_Gradient.weights.xml')
)


process.flashggVBFDiPhoDiJetMVALegacyMCSmearLowR9EBPhiUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBPhiUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(True),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVALegacyMCSmearLowR9EBPhiUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_vbf_dijet_dipho_evenbkg_scaledwt50_maxdPhi_Gradient.weights.xml')
)


process.flashggVBFDiPhoDiJetMVALegacyMCSmearLowR9EBRhoDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBRhoDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(True),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVALegacyMCSmearLowR9EBRhoDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_vbf_dijet_dipho_evenbkg_scaledwt50_maxdPhi_Gradient.weights.xml')
)


process.flashggVBFDiPhoDiJetMVALegacyMCSmearLowR9EBRhoUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBRhoUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(True),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVALegacyMCSmearLowR9EBRhoUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_vbf_dijet_dipho_evenbkg_scaledwt50_maxdPhi_Gradient.weights.xml')
)


process.flashggVBFDiPhoDiJetMVALegacyMCSmearLowR9EEDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EEDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(True),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVALegacyMCSmearLowR9EEDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_vbf_dijet_dipho_evenbkg_scaledwt50_maxdPhi_Gradient.weights.xml')
)


process.flashggVBFDiPhoDiJetMVALegacyMCSmearLowR9EEUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EEUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(True),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVALegacyMCSmearLowR9EEUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_vbf_dijet_dipho_evenbkg_scaledwt50_maxdPhi_Gradient.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAMCScaleHighR9EBDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EBDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCScaleHighR9EBDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAMCScaleHighR9EBUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EBUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCScaleHighR9EBUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAMCScaleHighR9EEDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EEDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCScaleHighR9EEDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAMCScaleHighR9EEUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EEUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCScaleHighR9EEUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAMCScaleLowR9EBDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EBDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCScaleLowR9EBDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAMCScaleLowR9EBUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EBUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCScaleLowR9EBUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAMCScaleLowR9EEDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EEDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCScaleLowR9EEDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAMCScaleLowR9EEUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EEUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCScaleLowR9EEUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAMCSmearHighR9EBPhiDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBPhiDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearHighR9EBPhiDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAMCSmearHighR9EBPhiUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBPhiUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearHighR9EBPhiUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAMCSmearHighR9EBRhoDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBRhoDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearHighR9EBRhoDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAMCSmearHighR9EBRhoUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBRhoUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearHighR9EBRhoUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAMCSmearHighR9EEDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EEDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearHighR9EEDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAMCSmearHighR9EEUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EEUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearHighR9EEUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAMCSmearLowR9EBPhiDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBPhiDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearLowR9EBPhiDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAMCSmearLowR9EBPhiUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBPhiUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearLowR9EBPhiUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAMCSmearLowR9EBRhoDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBRhoDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearLowR9EBRhoDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAMCSmearLowR9EBRhoUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBRhoUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearLowR9EBRhoUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAMCSmearLowR9EEDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EEDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearLowR9EEDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAMCSmearLowR9EEUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EEUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearLowR9EEUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAPUPPI = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVA"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAPUPPI"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAPUPPIMCScaleHighR9EBDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EBDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAPUPPIMCScaleHighR9EBDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAPUPPIMCScaleHighR9EBUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EBUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAPUPPIMCScaleHighR9EBUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAPUPPIMCScaleHighR9EEDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EEDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAPUPPIMCScaleHighR9EEDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAPUPPIMCScaleHighR9EEUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EEUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAPUPPIMCScaleHighR9EEUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAPUPPIMCScaleLowR9EBDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EBDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAPUPPIMCScaleLowR9EBDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAPUPPIMCScaleLowR9EBUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EBUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAPUPPIMCScaleLowR9EBUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAPUPPIMCScaleLowR9EEDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EEDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAPUPPIMCScaleLowR9EEDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAPUPPIMCScaleLowR9EEUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EEUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAPUPPIMCScaleLowR9EEUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearHighR9EBPhiDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBPhiDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAPUPPIMCSmearHighR9EBPhiDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearHighR9EBPhiUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBPhiUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAPUPPIMCSmearHighR9EBPhiUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearHighR9EBRhoDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBRhoDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAPUPPIMCSmearHighR9EBRhoDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearHighR9EBRhoUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBRhoUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAPUPPIMCSmearHighR9EBRhoUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearHighR9EEDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EEDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAPUPPIMCSmearHighR9EEDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearHighR9EEUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EEUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAPUPPIMCSmearHighR9EEUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearLowR9EBPhiDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBPhiDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAPUPPIMCSmearLowR9EBPhiDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearLowR9EBPhiUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBPhiUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAPUPPIMCSmearLowR9EBPhiUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearLowR9EBRhoDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBRhoDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAPUPPIMCSmearLowR9EBRhoDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearLowR9EBRhoUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBRhoUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAPUPPIMCSmearLowR9EBRhoUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearLowR9EEDown01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEDown01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EEDown01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAPUPPIMCSmearLowR9EEDown01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearLowR9EEUp01sigma = cms.EDProducer("FlashggVBFDiPhoDiJetMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEUp01sigma"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EEUp01sigma"),
    UseLegacyMVA = cms.untracked.bool(False),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAPUPPIMCSmearLowR9EEUp01sigma"),
    vbfDiPhoDiJetMVAweightfile = cms.FileInPath('flashgg/Taggers/data/Flashgg_DiPhoDiJet_BDT.weights.xml')
)


process.flashggVBFMVA = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJets","0"), cms.InputTag("flashggUnpackedJets","1"), cms.InputTag("flashggUnpackedJets","2"), cms.InputTag("flashggUnpackedJets","3"), cms.InputTag("flashggUnpackedJets","4"), 
        cms.InputTag("flashggUnpackedJets","5"), cms.InputTag("flashggUnpackedJets","6"), cms.InputTag("flashggUnpackedJets","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_CHS_BDTG.weights.xml')
)


process.flashggVBFMVALegacy = cms.EDProducer("FlashggVBFMVALegacyProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics"),
    MinDijetMinv = cms.double(0.0),
    UseLegacyMVA = cms.untracked.bool(True),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJets","0"), cms.InputTag("flashggUnpackedJets","1"), cms.InputTag("flashggUnpackedJets","2"), cms.InputTag("flashggUnpackedJets","3"), cms.InputTag("flashggUnpackedJets","4"), 
        cms.InputTag("flashggUnpackedJets","5"), cms.InputTag("flashggUnpackedJets","6"), cms.InputTag("flashggUnpackedJets","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_dijet_sherpa_scalewt50_2evenb_powheg200_maxdPhi_oct9_Gradient.weights.xml')
)


process.flashggVBFMVALegacyMCScaleHighR9EBDown01sigma = cms.EDProducer("FlashggVBFMVALegacyProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBDown01sigma"),
    MinDijetMinv = cms.double(0.0),
    UseLegacyMVA = cms.untracked.bool(True),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_dijet_sherpa_scalewt50_2evenb_powheg200_maxdPhi_oct9_Gradient.weights.xml')
)


process.flashggVBFMVALegacyMCScaleHighR9EBUp01sigma = cms.EDProducer("FlashggVBFMVALegacyProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBUp01sigma"),
    MinDijetMinv = cms.double(0.0),
    UseLegacyMVA = cms.untracked.bool(True),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_dijet_sherpa_scalewt50_2evenb_powheg200_maxdPhi_oct9_Gradient.weights.xml')
)


process.flashggVBFMVALegacyMCScaleHighR9EEDown01sigma = cms.EDProducer("FlashggVBFMVALegacyProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEDown01sigma"),
    MinDijetMinv = cms.double(0.0),
    UseLegacyMVA = cms.untracked.bool(True),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_dijet_sherpa_scalewt50_2evenb_powheg200_maxdPhi_oct9_Gradient.weights.xml')
)


process.flashggVBFMVALegacyMCScaleHighR9EEUp01sigma = cms.EDProducer("FlashggVBFMVALegacyProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEUp01sigma"),
    MinDijetMinv = cms.double(0.0),
    UseLegacyMVA = cms.untracked.bool(True),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_dijet_sherpa_scalewt50_2evenb_powheg200_maxdPhi_oct9_Gradient.weights.xml')
)


process.flashggVBFMVALegacyMCScaleLowR9EBDown01sigma = cms.EDProducer("FlashggVBFMVALegacyProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBDown01sigma"),
    MinDijetMinv = cms.double(0.0),
    UseLegacyMVA = cms.untracked.bool(True),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_dijet_sherpa_scalewt50_2evenb_powheg200_maxdPhi_oct9_Gradient.weights.xml')
)


process.flashggVBFMVALegacyMCScaleLowR9EBUp01sigma = cms.EDProducer("FlashggVBFMVALegacyProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBUp01sigma"),
    MinDijetMinv = cms.double(0.0),
    UseLegacyMVA = cms.untracked.bool(True),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_dijet_sherpa_scalewt50_2evenb_powheg200_maxdPhi_oct9_Gradient.weights.xml')
)


process.flashggVBFMVALegacyMCScaleLowR9EEDown01sigma = cms.EDProducer("FlashggVBFMVALegacyProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEDown01sigma"),
    MinDijetMinv = cms.double(0.0),
    UseLegacyMVA = cms.untracked.bool(True),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_dijet_sherpa_scalewt50_2evenb_powheg200_maxdPhi_oct9_Gradient.weights.xml')
)


process.flashggVBFMVALegacyMCScaleLowR9EEUp01sigma = cms.EDProducer("FlashggVBFMVALegacyProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEUp01sigma"),
    MinDijetMinv = cms.double(0.0),
    UseLegacyMVA = cms.untracked.bool(True),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_dijet_sherpa_scalewt50_2evenb_powheg200_maxdPhi_oct9_Gradient.weights.xml')
)


process.flashggVBFMVALegacyMCSmearHighR9EBPhiDown01sigma = cms.EDProducer("FlashggVBFMVALegacyProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiDown01sigma"),
    MinDijetMinv = cms.double(0.0),
    UseLegacyMVA = cms.untracked.bool(True),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_dijet_sherpa_scalewt50_2evenb_powheg200_maxdPhi_oct9_Gradient.weights.xml')
)


process.flashggVBFMVALegacyMCSmearHighR9EBPhiUp01sigma = cms.EDProducer("FlashggVBFMVALegacyProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiUp01sigma"),
    MinDijetMinv = cms.double(0.0),
    UseLegacyMVA = cms.untracked.bool(True),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_dijet_sherpa_scalewt50_2evenb_powheg200_maxdPhi_oct9_Gradient.weights.xml')
)


process.flashggVBFMVALegacyMCSmearHighR9EBRhoDown01sigma = cms.EDProducer("FlashggVBFMVALegacyProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoDown01sigma"),
    MinDijetMinv = cms.double(0.0),
    UseLegacyMVA = cms.untracked.bool(True),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_dijet_sherpa_scalewt50_2evenb_powheg200_maxdPhi_oct9_Gradient.weights.xml')
)


process.flashggVBFMVALegacyMCSmearHighR9EBRhoUp01sigma = cms.EDProducer("FlashggVBFMVALegacyProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoUp01sigma"),
    MinDijetMinv = cms.double(0.0),
    UseLegacyMVA = cms.untracked.bool(True),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_dijet_sherpa_scalewt50_2evenb_powheg200_maxdPhi_oct9_Gradient.weights.xml')
)


process.flashggVBFMVALegacyMCSmearHighR9EEDown01sigma = cms.EDProducer("FlashggVBFMVALegacyProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEDown01sigma"),
    MinDijetMinv = cms.double(0.0),
    UseLegacyMVA = cms.untracked.bool(True),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_dijet_sherpa_scalewt50_2evenb_powheg200_maxdPhi_oct9_Gradient.weights.xml')
)


process.flashggVBFMVALegacyMCSmearHighR9EEUp01sigma = cms.EDProducer("FlashggVBFMVALegacyProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEUp01sigma"),
    MinDijetMinv = cms.double(0.0),
    UseLegacyMVA = cms.untracked.bool(True),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_dijet_sherpa_scalewt50_2evenb_powheg200_maxdPhi_oct9_Gradient.weights.xml')
)


process.flashggVBFMVALegacyMCSmearLowR9EBPhiDown01sigma = cms.EDProducer("FlashggVBFMVALegacyProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiDown01sigma"),
    MinDijetMinv = cms.double(0.0),
    UseLegacyMVA = cms.untracked.bool(True),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_dijet_sherpa_scalewt50_2evenb_powheg200_maxdPhi_oct9_Gradient.weights.xml')
)


process.flashggVBFMVALegacyMCSmearLowR9EBPhiUp01sigma = cms.EDProducer("FlashggVBFMVALegacyProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiUp01sigma"),
    MinDijetMinv = cms.double(0.0),
    UseLegacyMVA = cms.untracked.bool(True),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_dijet_sherpa_scalewt50_2evenb_powheg200_maxdPhi_oct9_Gradient.weights.xml')
)


process.flashggVBFMVALegacyMCSmearLowR9EBRhoDown01sigma = cms.EDProducer("FlashggVBFMVALegacyProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoDown01sigma"),
    MinDijetMinv = cms.double(0.0),
    UseLegacyMVA = cms.untracked.bool(True),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_dijet_sherpa_scalewt50_2evenb_powheg200_maxdPhi_oct9_Gradient.weights.xml')
)


process.flashggVBFMVALegacyMCSmearLowR9EBRhoUp01sigma = cms.EDProducer("FlashggVBFMVALegacyProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoUp01sigma"),
    MinDijetMinv = cms.double(0.0),
    UseLegacyMVA = cms.untracked.bool(True),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_dijet_sherpa_scalewt50_2evenb_powheg200_maxdPhi_oct9_Gradient.weights.xml')
)


process.flashggVBFMVALegacyMCSmearLowR9EEDown01sigma = cms.EDProducer("FlashggVBFMVALegacyProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEDown01sigma"),
    MinDijetMinv = cms.double(0.0),
    UseLegacyMVA = cms.untracked.bool(True),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_dijet_sherpa_scalewt50_2evenb_powheg200_maxdPhi_oct9_Gradient.weights.xml')
)


process.flashggVBFMVALegacyMCSmearLowR9EEUp01sigma = cms.EDProducer("FlashggVBFMVALegacyProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEUp01sigma"),
    MinDijetMinv = cms.double(0.0),
    UseLegacyMVA = cms.untracked.bool(True),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/data/TMVA_dijet_sherpa_scalewt50_2evenb_powheg200_maxdPhi_oct9_Gradient.weights.xml')
)


process.flashggVBFMVAMCScaleHighR9EBDown01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBDown01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_CHS_BDTG.weights.xml')
)


process.flashggVBFMVAMCScaleHighR9EBUp01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBUp01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_CHS_BDTG.weights.xml')
)


process.flashggVBFMVAMCScaleHighR9EEDown01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEDown01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_CHS_BDTG.weights.xml')
)


process.flashggVBFMVAMCScaleHighR9EEUp01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEUp01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_CHS_BDTG.weights.xml')
)


process.flashggVBFMVAMCScaleLowR9EBDown01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBDown01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_CHS_BDTG.weights.xml')
)


process.flashggVBFMVAMCScaleLowR9EBUp01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBUp01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_CHS_BDTG.weights.xml')
)


process.flashggVBFMVAMCScaleLowR9EEDown01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEDown01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_CHS_BDTG.weights.xml')
)


process.flashggVBFMVAMCScaleLowR9EEUp01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEUp01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_CHS_BDTG.weights.xml')
)


process.flashggVBFMVAMCSmearHighR9EBPhiDown01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiDown01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_CHS_BDTG.weights.xml')
)


process.flashggVBFMVAMCSmearHighR9EBPhiUp01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiUp01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_CHS_BDTG.weights.xml')
)


process.flashggVBFMVAMCSmearHighR9EBRhoDown01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoDown01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_CHS_BDTG.weights.xml')
)


process.flashggVBFMVAMCSmearHighR9EBRhoUp01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoUp01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_CHS_BDTG.weights.xml')
)


process.flashggVBFMVAMCSmearHighR9EEDown01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEDown01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_CHS_BDTG.weights.xml')
)


process.flashggVBFMVAMCSmearHighR9EEUp01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEUp01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_CHS_BDTG.weights.xml')
)


process.flashggVBFMVAMCSmearLowR9EBPhiDown01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiDown01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_CHS_BDTG.weights.xml')
)


process.flashggVBFMVAMCSmearLowR9EBPhiUp01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiUp01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_CHS_BDTG.weights.xml')
)


process.flashggVBFMVAMCSmearLowR9EBRhoDown01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoDown01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_CHS_BDTG.weights.xml')
)


process.flashggVBFMVAMCSmearLowR9EBRhoUp01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoUp01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_CHS_BDTG.weights.xml')
)


process.flashggVBFMVAMCSmearLowR9EEDown01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEDown01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_CHS_BDTG.weights.xml')
)


process.flashggVBFMVAMCSmearLowR9EEUp01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEUp01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_CHS_BDTG.weights.xml')
)


process.flashggVBFMVAPUPPI = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedPuppiJets","0"), cms.InputTag("flashggUnpackedPuppiJets","1"), cms.InputTag("flashggUnpackedPuppiJets","2"), cms.InputTag("flashggUnpackedPuppiJets","3"), cms.InputTag("flashggUnpackedPuppiJets","4"), 
        cms.InputTag("flashggUnpackedPuppiJets","5"), cms.InputTag("flashggUnpackedPuppiJets","6"), cms.InputTag("flashggUnpackedPuppiJets","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_PUPPI_BDTG.weights.xml')
)


process.flashggVBFMVAPUPPIMCScaleHighR9EBDown01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBDown01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EBDown01sigma","0"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EBDown01sigma","1"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EBDown01sigma","2"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EBDown01sigma","3"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EBDown01sigma","4"), 
        cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EBDown01sigma","5"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EBDown01sigma","6"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EBDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_PUPPI_BDTG.weights.xml')
)


process.flashggVBFMVAPUPPIMCScaleHighR9EBUp01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBUp01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EBUp01sigma","0"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EBUp01sigma","1"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EBUp01sigma","2"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EBUp01sigma","3"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EBUp01sigma","4"), 
        cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EBUp01sigma","5"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EBUp01sigma","6"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EBUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_PUPPI_BDTG.weights.xml')
)


process.flashggVBFMVAPUPPIMCScaleHighR9EEDown01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEDown01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EEDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_PUPPI_BDTG.weights.xml')
)


process.flashggVBFMVAPUPPIMCScaleHighR9EEUp01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEUp01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleHighR9EEUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_PUPPI_BDTG.weights.xml')
)


process.flashggVBFMVAPUPPIMCScaleLowR9EBDown01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBDown01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EBDown01sigma","0"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EBDown01sigma","1"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EBDown01sigma","2"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EBDown01sigma","3"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EBDown01sigma","4"), 
        cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EBDown01sigma","5"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EBDown01sigma","6"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EBDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_PUPPI_BDTG.weights.xml')
)


process.flashggVBFMVAPUPPIMCScaleLowR9EBUp01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBUp01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EBUp01sigma","0"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EBUp01sigma","1"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EBUp01sigma","2"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EBUp01sigma","3"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EBUp01sigma","4"), 
        cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EBUp01sigma","5"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EBUp01sigma","6"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EBUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_PUPPI_BDTG.weights.xml')
)


process.flashggVBFMVAPUPPIMCScaleLowR9EEDown01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEDown01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EEDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_PUPPI_BDTG.weights.xml')
)


process.flashggVBFMVAPUPPIMCScaleLowR9EEUp01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEUp01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedPuppiJetsMCScaleLowR9EEUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_PUPPI_BDTG.weights.xml')
)


process.flashggVBFMVAPUPPIMCSmearHighR9EBPhiDown01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiDown01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBPhiDown01sigma","0"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBPhiDown01sigma","1"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBPhiDown01sigma","2"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBPhiDown01sigma","3"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBPhiDown01sigma","4"), 
        cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBPhiDown01sigma","5"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBPhiDown01sigma","6"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBPhiDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_PUPPI_BDTG.weights.xml')
)


process.flashggVBFMVAPUPPIMCSmearHighR9EBPhiUp01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiUp01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBPhiUp01sigma","0"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBPhiUp01sigma","1"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBPhiUp01sigma","2"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBPhiUp01sigma","3"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBPhiUp01sigma","4"), 
        cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBPhiUp01sigma","5"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBPhiUp01sigma","6"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBPhiUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_PUPPI_BDTG.weights.xml')
)


process.flashggVBFMVAPUPPIMCSmearHighR9EBRhoDown01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoDown01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBRhoDown01sigma","0"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBRhoDown01sigma","1"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBRhoDown01sigma","2"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBRhoDown01sigma","3"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBRhoDown01sigma","4"), 
        cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBRhoDown01sigma","5"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBRhoDown01sigma","6"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBRhoDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_PUPPI_BDTG.weights.xml')
)


process.flashggVBFMVAPUPPIMCSmearHighR9EBRhoUp01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoUp01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBRhoUp01sigma","0"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBRhoUp01sigma","1"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBRhoUp01sigma","2"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBRhoUp01sigma","3"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBRhoUp01sigma","4"), 
        cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBRhoUp01sigma","5"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBRhoUp01sigma","6"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EBRhoUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_PUPPI_BDTG.weights.xml')
)


process.flashggVBFMVAPUPPIMCSmearHighR9EEDown01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEDown01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EEDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_PUPPI_BDTG.weights.xml')
)


process.flashggVBFMVAPUPPIMCSmearHighR9EEUp01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEUp01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearHighR9EEUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_PUPPI_BDTG.weights.xml')
)


process.flashggVBFMVAPUPPIMCSmearLowR9EBPhiDown01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiDown01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBPhiDown01sigma","0"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBPhiDown01sigma","1"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBPhiDown01sigma","2"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBPhiDown01sigma","3"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBPhiDown01sigma","4"), 
        cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBPhiDown01sigma","5"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBPhiDown01sigma","6"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBPhiDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_PUPPI_BDTG.weights.xml')
)


process.flashggVBFMVAPUPPIMCSmearLowR9EBPhiUp01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiUp01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBPhiUp01sigma","0"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBPhiUp01sigma","1"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBPhiUp01sigma","2"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBPhiUp01sigma","3"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBPhiUp01sigma","4"), 
        cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBPhiUp01sigma","5"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBPhiUp01sigma","6"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBPhiUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_PUPPI_BDTG.weights.xml')
)


process.flashggVBFMVAPUPPIMCSmearLowR9EBRhoDown01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoDown01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBRhoDown01sigma","0"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBRhoDown01sigma","1"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBRhoDown01sigma","2"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBRhoDown01sigma","3"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBRhoDown01sigma","4"), 
        cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBRhoDown01sigma","5"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBRhoDown01sigma","6"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBRhoDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_PUPPI_BDTG.weights.xml')
)


process.flashggVBFMVAPUPPIMCSmearLowR9EBRhoUp01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoUp01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBRhoUp01sigma","0"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBRhoUp01sigma","1"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBRhoUp01sigma","2"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBRhoUp01sigma","3"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBRhoUp01sigma","4"), 
        cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBRhoUp01sigma","5"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBRhoUp01sigma","6"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EBRhoUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_PUPPI_BDTG.weights.xml')
)


process.flashggVBFMVAPUPPIMCSmearLowR9EEDown01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEDown01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EEDown01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_PUPPI_BDTG.weights.xml')
)


process.flashggVBFMVAPUPPIMCSmearLowR9EEUp01sigma = cms.EDProducer("FlashggVBFMVAProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEUp01sigma"),
    MVAMethod = cms.untracked.string('BDTG'),
    MinDijetMinv = cms.double(0.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedPuppiJetsMCSmearLowR9EEUp01sigma","7")),
    vbfMVAweightfile = cms.FileInPath('flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_PUPPI_BDTG.weights.xml')
)


process.flashggVBFTag = cms.EDProducer("FlashggVBFTagProducer",
    Boundaries = cms.untracked.vdouble(0.21, 0.6, 0.81),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics"),
    GenJetTag = cms.InputTag("slimmedGenJets"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVA"),
    SystLabel = cms.string(''),
    VBFDiPhoDiJetMVAResultTag = cms.InputTag("flashggVBFDiPhoDiJetMVA"),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVA")
)


process.flashggVBFTagMCScaleHighR9EBDown01sigma = cms.EDProducer("FlashggVBFTagProducer",
    Boundaries = cms.untracked.vdouble(0.21, 0.6, 0.81),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBDown01sigma"),
    GenJetTag = cms.InputTag("slimmedGenJets"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EBDown01sigma"),
    SystLabel = cms.string('MCScaleHighR9EBDown01sigma'),
    VBFDiPhoDiJetMVAResultTag = cms.InputTag("flashggVBFDiPhoDiJetMVAMCScaleHighR9EBDown01sigma"),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCScaleHighR9EBDown01sigma")
)


process.flashggVBFTagMCScaleHighR9EBUp01sigma = cms.EDProducer("FlashggVBFTagProducer",
    Boundaries = cms.untracked.vdouble(0.21, 0.6, 0.81),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBUp01sigma"),
    GenJetTag = cms.InputTag("slimmedGenJets"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EBUp01sigma"),
    SystLabel = cms.string('MCScaleHighR9EBUp01sigma'),
    VBFDiPhoDiJetMVAResultTag = cms.InputTag("flashggVBFDiPhoDiJetMVAMCScaleHighR9EBUp01sigma"),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCScaleHighR9EBUp01sigma")
)


process.flashggVBFTagMCScaleHighR9EEDown01sigma = cms.EDProducer("FlashggVBFTagProducer",
    Boundaries = cms.untracked.vdouble(0.21, 0.6, 0.81),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEDown01sigma"),
    GenJetTag = cms.InputTag("slimmedGenJets"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EEDown01sigma"),
    SystLabel = cms.string('MCScaleHighR9EEDown01sigma'),
    VBFDiPhoDiJetMVAResultTag = cms.InputTag("flashggVBFDiPhoDiJetMVAMCScaleHighR9EEDown01sigma"),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCScaleHighR9EEDown01sigma")
)


process.flashggVBFTagMCScaleHighR9EEUp01sigma = cms.EDProducer("FlashggVBFTagProducer",
    Boundaries = cms.untracked.vdouble(0.21, 0.6, 0.81),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEUp01sigma"),
    GenJetTag = cms.InputTag("slimmedGenJets"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EEUp01sigma"),
    SystLabel = cms.string('MCScaleHighR9EEUp01sigma'),
    VBFDiPhoDiJetMVAResultTag = cms.InputTag("flashggVBFDiPhoDiJetMVAMCScaleHighR9EEUp01sigma"),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCScaleHighR9EEUp01sigma")
)


process.flashggVBFTagMCScaleLowR9EBDown01sigma = cms.EDProducer("FlashggVBFTagProducer",
    Boundaries = cms.untracked.vdouble(0.21, 0.6, 0.81),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBDown01sigma"),
    GenJetTag = cms.InputTag("slimmedGenJets"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EBDown01sigma"),
    SystLabel = cms.string('MCScaleLowR9EBDown01sigma'),
    VBFDiPhoDiJetMVAResultTag = cms.InputTag("flashggVBFDiPhoDiJetMVAMCScaleLowR9EBDown01sigma"),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCScaleLowR9EBDown01sigma")
)


process.flashggVBFTagMCScaleLowR9EBUp01sigma = cms.EDProducer("FlashggVBFTagProducer",
    Boundaries = cms.untracked.vdouble(0.21, 0.6, 0.81),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBUp01sigma"),
    GenJetTag = cms.InputTag("slimmedGenJets"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EBUp01sigma"),
    SystLabel = cms.string('MCScaleLowR9EBUp01sigma'),
    VBFDiPhoDiJetMVAResultTag = cms.InputTag("flashggVBFDiPhoDiJetMVAMCScaleLowR9EBUp01sigma"),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCScaleLowR9EBUp01sigma")
)


process.flashggVBFTagMCScaleLowR9EEDown01sigma = cms.EDProducer("FlashggVBFTagProducer",
    Boundaries = cms.untracked.vdouble(0.21, 0.6, 0.81),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEDown01sigma"),
    GenJetTag = cms.InputTag("slimmedGenJets"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EEDown01sigma"),
    SystLabel = cms.string('MCScaleLowR9EEDown01sigma'),
    VBFDiPhoDiJetMVAResultTag = cms.InputTag("flashggVBFDiPhoDiJetMVAMCScaleLowR9EEDown01sigma"),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCScaleLowR9EEDown01sigma")
)


process.flashggVBFTagMCScaleLowR9EEUp01sigma = cms.EDProducer("FlashggVBFTagProducer",
    Boundaries = cms.untracked.vdouble(0.21, 0.6, 0.81),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEUp01sigma"),
    GenJetTag = cms.InputTag("slimmedGenJets"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EEUp01sigma"),
    SystLabel = cms.string('MCScaleLowR9EEUp01sigma'),
    VBFDiPhoDiJetMVAResultTag = cms.InputTag("flashggVBFDiPhoDiJetMVAMCScaleLowR9EEUp01sigma"),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCScaleLowR9EEUp01sigma")
)


process.flashggVBFTagMCSmearHighR9EBPhiDown01sigma = cms.EDProducer("FlashggVBFTagProducer",
    Boundaries = cms.untracked.vdouble(0.21, 0.6, 0.81),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiDown01sigma"),
    GenJetTag = cms.InputTag("slimmedGenJets"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBPhiDown01sigma"),
    SystLabel = cms.string('MCSmearHighR9EBPhiDown01sigma'),
    VBFDiPhoDiJetMVAResultTag = cms.InputTag("flashggVBFDiPhoDiJetMVAMCSmearHighR9EBPhiDown01sigma"),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearHighR9EBPhiDown01sigma")
)


process.flashggVBFTagMCSmearHighR9EBPhiUp01sigma = cms.EDProducer("FlashggVBFTagProducer",
    Boundaries = cms.untracked.vdouble(0.21, 0.6, 0.81),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiUp01sigma"),
    GenJetTag = cms.InputTag("slimmedGenJets"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBPhiUp01sigma"),
    SystLabel = cms.string('MCSmearHighR9EBPhiUp01sigma'),
    VBFDiPhoDiJetMVAResultTag = cms.InputTag("flashggVBFDiPhoDiJetMVAMCSmearHighR9EBPhiUp01sigma"),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearHighR9EBPhiUp01sigma")
)


process.flashggVBFTagMCSmearHighR9EBRhoDown01sigma = cms.EDProducer("FlashggVBFTagProducer",
    Boundaries = cms.untracked.vdouble(0.21, 0.6, 0.81),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoDown01sigma"),
    GenJetTag = cms.InputTag("slimmedGenJets"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBRhoDown01sigma"),
    SystLabel = cms.string('MCSmearHighR9EBRhoDown01sigma'),
    VBFDiPhoDiJetMVAResultTag = cms.InputTag("flashggVBFDiPhoDiJetMVAMCSmearHighR9EBRhoDown01sigma"),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearHighR9EBRhoDown01sigma")
)


process.flashggVBFTagMCSmearHighR9EBRhoUp01sigma = cms.EDProducer("FlashggVBFTagProducer",
    Boundaries = cms.untracked.vdouble(0.21, 0.6, 0.81),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoUp01sigma"),
    GenJetTag = cms.InputTag("slimmedGenJets"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBRhoUp01sigma"),
    SystLabel = cms.string('MCSmearHighR9EBRhoUp01sigma'),
    VBFDiPhoDiJetMVAResultTag = cms.InputTag("flashggVBFDiPhoDiJetMVAMCSmearHighR9EBRhoUp01sigma"),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearHighR9EBRhoUp01sigma")
)


process.flashggVBFTagMCSmearHighR9EEDown01sigma = cms.EDProducer("FlashggVBFTagProducer",
    Boundaries = cms.untracked.vdouble(0.21, 0.6, 0.81),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEDown01sigma"),
    GenJetTag = cms.InputTag("slimmedGenJets"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EEDown01sigma"),
    SystLabel = cms.string('MCSmearHighR9EEDown01sigma'),
    VBFDiPhoDiJetMVAResultTag = cms.InputTag("flashggVBFDiPhoDiJetMVAMCSmearHighR9EEDown01sigma"),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearHighR9EEDown01sigma")
)


process.flashggVBFTagMCSmearHighR9EEUp01sigma = cms.EDProducer("FlashggVBFTagProducer",
    Boundaries = cms.untracked.vdouble(0.21, 0.6, 0.81),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEUp01sigma"),
    GenJetTag = cms.InputTag("slimmedGenJets"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EEUp01sigma"),
    SystLabel = cms.string('MCSmearHighR9EEUp01sigma'),
    VBFDiPhoDiJetMVAResultTag = cms.InputTag("flashggVBFDiPhoDiJetMVAMCSmearHighR9EEUp01sigma"),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearHighR9EEUp01sigma")
)


process.flashggVBFTagMCSmearLowR9EBPhiDown01sigma = cms.EDProducer("FlashggVBFTagProducer",
    Boundaries = cms.untracked.vdouble(0.21, 0.6, 0.81),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiDown01sigma"),
    GenJetTag = cms.InputTag("slimmedGenJets"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBPhiDown01sigma"),
    SystLabel = cms.string('MCSmearLowR9EBPhiDown01sigma'),
    VBFDiPhoDiJetMVAResultTag = cms.InputTag("flashggVBFDiPhoDiJetMVAMCSmearLowR9EBPhiDown01sigma"),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearLowR9EBPhiDown01sigma")
)


process.flashggVBFTagMCSmearLowR9EBPhiUp01sigma = cms.EDProducer("FlashggVBFTagProducer",
    Boundaries = cms.untracked.vdouble(0.21, 0.6, 0.81),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiUp01sigma"),
    GenJetTag = cms.InputTag("slimmedGenJets"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBPhiUp01sigma"),
    SystLabel = cms.string('MCSmearLowR9EBPhiUp01sigma'),
    VBFDiPhoDiJetMVAResultTag = cms.InputTag("flashggVBFDiPhoDiJetMVAMCSmearLowR9EBPhiUp01sigma"),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearLowR9EBPhiUp01sigma")
)


process.flashggVBFTagMCSmearLowR9EBRhoDown01sigma = cms.EDProducer("FlashggVBFTagProducer",
    Boundaries = cms.untracked.vdouble(0.21, 0.6, 0.81),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoDown01sigma"),
    GenJetTag = cms.InputTag("slimmedGenJets"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBRhoDown01sigma"),
    SystLabel = cms.string('MCSmearLowR9EBRhoDown01sigma'),
    VBFDiPhoDiJetMVAResultTag = cms.InputTag("flashggVBFDiPhoDiJetMVAMCSmearLowR9EBRhoDown01sigma"),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearLowR9EBRhoDown01sigma")
)


process.flashggVBFTagMCSmearLowR9EBRhoUp01sigma = cms.EDProducer("FlashggVBFTagProducer",
    Boundaries = cms.untracked.vdouble(0.21, 0.6, 0.81),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoUp01sigma"),
    GenJetTag = cms.InputTag("slimmedGenJets"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBRhoUp01sigma"),
    SystLabel = cms.string('MCSmearLowR9EBRhoUp01sigma'),
    VBFDiPhoDiJetMVAResultTag = cms.InputTag("flashggVBFDiPhoDiJetMVAMCSmearLowR9EBRhoUp01sigma"),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearLowR9EBRhoUp01sigma")
)


process.flashggVBFTagMCSmearLowR9EEDown01sigma = cms.EDProducer("FlashggVBFTagProducer",
    Boundaries = cms.untracked.vdouble(0.21, 0.6, 0.81),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEDown01sigma"),
    GenJetTag = cms.InputTag("slimmedGenJets"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EEDown01sigma"),
    SystLabel = cms.string('MCSmearLowR9EEDown01sigma'),
    VBFDiPhoDiJetMVAResultTag = cms.InputTag("flashggVBFDiPhoDiJetMVAMCSmearLowR9EEDown01sigma"),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearLowR9EEDown01sigma")
)


process.flashggVBFTagMCSmearLowR9EEUp01sigma = cms.EDProducer("FlashggVBFTagProducer",
    Boundaries = cms.untracked.vdouble(0.21, 0.6, 0.81),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEUp01sigma"),
    GenJetTag = cms.InputTag("slimmedGenJets"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EEUp01sigma"),
    SystLabel = cms.string('MCSmearLowR9EEUp01sigma'),
    VBFDiPhoDiJetMVAResultTag = cms.InputTag("flashggVBFDiPhoDiJetMVAMCSmearLowR9EEUp01sigma"),
    VBFMVAResultTag = cms.InputTag("flashggVBFMVAMCSmearLowR9EEUp01sigma")
)


process.flashggVHEtTag = cms.EDProducer("FlashggVHEtTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    METTag = cms.InputTag("slimmedMETs"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVA"),
    SystLabel = cms.string('')
)


process.flashggVHEtTagMCScaleHighR9EBDown01sigma = cms.EDProducer("FlashggVHEtTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    METTag = cms.InputTag("slimmedMETs"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EBDown01sigma"),
    SystLabel = cms.string('MCScaleHighR9EBDown01sigma')
)


process.flashggVHEtTagMCScaleHighR9EBUp01sigma = cms.EDProducer("FlashggVHEtTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    METTag = cms.InputTag("slimmedMETs"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EBUp01sigma"),
    SystLabel = cms.string('MCScaleHighR9EBUp01sigma')
)


process.flashggVHEtTagMCScaleHighR9EEDown01sigma = cms.EDProducer("FlashggVHEtTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    METTag = cms.InputTag("slimmedMETs"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EEDown01sigma"),
    SystLabel = cms.string('MCScaleHighR9EEDown01sigma')
)


process.flashggVHEtTagMCScaleHighR9EEUp01sigma = cms.EDProducer("FlashggVHEtTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    METTag = cms.InputTag("slimmedMETs"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EEUp01sigma"),
    SystLabel = cms.string('MCScaleHighR9EEUp01sigma')
)


process.flashggVHEtTagMCScaleLowR9EBDown01sigma = cms.EDProducer("FlashggVHEtTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    METTag = cms.InputTag("slimmedMETs"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EBDown01sigma"),
    SystLabel = cms.string('MCScaleLowR9EBDown01sigma')
)


process.flashggVHEtTagMCScaleLowR9EBUp01sigma = cms.EDProducer("FlashggVHEtTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    METTag = cms.InputTag("slimmedMETs"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EBUp01sigma"),
    SystLabel = cms.string('MCScaleLowR9EBUp01sigma')
)


process.flashggVHEtTagMCScaleLowR9EEDown01sigma = cms.EDProducer("FlashggVHEtTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    METTag = cms.InputTag("slimmedMETs"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EEDown01sigma"),
    SystLabel = cms.string('MCScaleLowR9EEDown01sigma')
)


process.flashggVHEtTagMCScaleLowR9EEUp01sigma = cms.EDProducer("FlashggVHEtTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    METTag = cms.InputTag("slimmedMETs"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EEUp01sigma"),
    SystLabel = cms.string('MCScaleLowR9EEUp01sigma')
)


process.flashggVHEtTagMCSmearHighR9EBPhiDown01sigma = cms.EDProducer("FlashggVHEtTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    METTag = cms.InputTag("slimmedMETs"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBPhiDown01sigma"),
    SystLabel = cms.string('MCSmearHighR9EBPhiDown01sigma')
)


process.flashggVHEtTagMCSmearHighR9EBPhiUp01sigma = cms.EDProducer("FlashggVHEtTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    METTag = cms.InputTag("slimmedMETs"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBPhiUp01sigma"),
    SystLabel = cms.string('MCSmearHighR9EBPhiUp01sigma')
)


process.flashggVHEtTagMCSmearHighR9EBRhoDown01sigma = cms.EDProducer("FlashggVHEtTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    METTag = cms.InputTag("slimmedMETs"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBRhoDown01sigma"),
    SystLabel = cms.string('MCSmearHighR9EBRhoDown01sigma')
)


process.flashggVHEtTagMCSmearHighR9EBRhoUp01sigma = cms.EDProducer("FlashggVHEtTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    METTag = cms.InputTag("slimmedMETs"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBRhoUp01sigma"),
    SystLabel = cms.string('MCSmearHighR9EBRhoUp01sigma')
)


process.flashggVHEtTagMCSmearHighR9EEDown01sigma = cms.EDProducer("FlashggVHEtTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    METTag = cms.InputTag("slimmedMETs"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EEDown01sigma"),
    SystLabel = cms.string('MCSmearHighR9EEDown01sigma')
)


process.flashggVHEtTagMCSmearHighR9EEUp01sigma = cms.EDProducer("FlashggVHEtTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    METTag = cms.InputTag("slimmedMETs"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EEUp01sigma"),
    SystLabel = cms.string('MCSmearHighR9EEUp01sigma')
)


process.flashggVHEtTagMCSmearLowR9EBPhiDown01sigma = cms.EDProducer("FlashggVHEtTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    METTag = cms.InputTag("slimmedMETs"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBPhiDown01sigma"),
    SystLabel = cms.string('MCSmearLowR9EBPhiDown01sigma')
)


process.flashggVHEtTagMCSmearLowR9EBPhiUp01sigma = cms.EDProducer("FlashggVHEtTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    METTag = cms.InputTag("slimmedMETs"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBPhiUp01sigma"),
    SystLabel = cms.string('MCSmearLowR9EBPhiUp01sigma')
)


process.flashggVHEtTagMCSmearLowR9EBRhoDown01sigma = cms.EDProducer("FlashggVHEtTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    METTag = cms.InputTag("slimmedMETs"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBRhoDown01sigma"),
    SystLabel = cms.string('MCSmearLowR9EBRhoDown01sigma')
)


process.flashggVHEtTagMCSmearLowR9EBRhoUp01sigma = cms.EDProducer("FlashggVHEtTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    METTag = cms.InputTag("slimmedMETs"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBRhoUp01sigma"),
    SystLabel = cms.string('MCSmearLowR9EBRhoUp01sigma')
)


process.flashggVHEtTagMCSmearLowR9EEDown01sigma = cms.EDProducer("FlashggVHEtTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    METTag = cms.InputTag("slimmedMETs"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EEDown01sigma"),
    SystLabel = cms.string('MCSmearLowR9EEDown01sigma')
)


process.flashggVHEtTagMCSmearLowR9EEUp01sigma = cms.EDProducer("FlashggVHEtTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    METTag = cms.InputTag("slimmedMETs"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EEUp01sigma"),
    SystLabel = cms.string('MCSmearLowR9EEUp01sigma')
)


process.flashggVHHadronicTag = cms.EDProducer("FlashggVHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVA"),
    MVAThreshold = cms.untracked.double(-0.6),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    SystLabel = cms.string(''),
    cosThetaStarThreshold = cms.untracked.double(0.5),
    dRJetToPhoLThreshold = cms.untracked.double(0.5),
    dRJetToPhoSThreshold = cms.untracked.double(0.5),
    dijetMassHighThreshold = cms.untracked.double(120.0),
    dijetMassLowThreshold = cms.untracked.double(60.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJets","0"), cms.InputTag("flashggUnpackedJets","1"), cms.InputTag("flashggUnpackedJets","2"), cms.InputTag("flashggUnpackedJets","3"), cms.InputTag("flashggUnpackedJets","4"), 
        cms.InputTag("flashggUnpackedJets","5"), cms.InputTag("flashggUnpackedJets","6"), cms.InputTag("flashggUnpackedJets","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(40.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHHadronicTagMCScaleHighR9EBDown01sigma = cms.EDProducer("FlashggVHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EBDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    SystLabel = cms.string('MCScaleHighR9EBDown01sigma'),
    cosThetaStarThreshold = cms.untracked.double(0.5),
    dRJetToPhoLThreshold = cms.untracked.double(0.5),
    dRJetToPhoSThreshold = cms.untracked.double(0.5),
    dijetMassHighThreshold = cms.untracked.double(120.0),
    dijetMassLowThreshold = cms.untracked.double(60.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(40.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHHadronicTagMCScaleHighR9EBUp01sigma = cms.EDProducer("FlashggVHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EBUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    SystLabel = cms.string('MCScaleHighR9EBUp01sigma'),
    cosThetaStarThreshold = cms.untracked.double(0.5),
    dRJetToPhoLThreshold = cms.untracked.double(0.5),
    dRJetToPhoSThreshold = cms.untracked.double(0.5),
    dijetMassHighThreshold = cms.untracked.double(120.0),
    dijetMassLowThreshold = cms.untracked.double(60.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(40.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHHadronicTagMCScaleHighR9EEDown01sigma = cms.EDProducer("FlashggVHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EEDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    SystLabel = cms.string('MCScaleHighR9EEDown01sigma'),
    cosThetaStarThreshold = cms.untracked.double(0.5),
    dRJetToPhoLThreshold = cms.untracked.double(0.5),
    dRJetToPhoSThreshold = cms.untracked.double(0.5),
    dijetMassHighThreshold = cms.untracked.double(120.0),
    dijetMassLowThreshold = cms.untracked.double(60.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(40.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHHadronicTagMCScaleHighR9EEUp01sigma = cms.EDProducer("FlashggVHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EEUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    SystLabel = cms.string('MCScaleHighR9EEUp01sigma'),
    cosThetaStarThreshold = cms.untracked.double(0.5),
    dRJetToPhoLThreshold = cms.untracked.double(0.5),
    dRJetToPhoSThreshold = cms.untracked.double(0.5),
    dijetMassHighThreshold = cms.untracked.double(120.0),
    dijetMassLowThreshold = cms.untracked.double(60.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(40.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHHadronicTagMCScaleLowR9EBDown01sigma = cms.EDProducer("FlashggVHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EBDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    SystLabel = cms.string('MCScaleLowR9EBDown01sigma'),
    cosThetaStarThreshold = cms.untracked.double(0.5),
    dRJetToPhoLThreshold = cms.untracked.double(0.5),
    dRJetToPhoSThreshold = cms.untracked.double(0.5),
    dijetMassHighThreshold = cms.untracked.double(120.0),
    dijetMassLowThreshold = cms.untracked.double(60.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(40.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHHadronicTagMCScaleLowR9EBUp01sigma = cms.EDProducer("FlashggVHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EBUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    SystLabel = cms.string('MCScaleLowR9EBUp01sigma'),
    cosThetaStarThreshold = cms.untracked.double(0.5),
    dRJetToPhoLThreshold = cms.untracked.double(0.5),
    dRJetToPhoSThreshold = cms.untracked.double(0.5),
    dijetMassHighThreshold = cms.untracked.double(120.0),
    dijetMassLowThreshold = cms.untracked.double(60.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(40.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHHadronicTagMCScaleLowR9EEDown01sigma = cms.EDProducer("FlashggVHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EEDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    SystLabel = cms.string('MCScaleLowR9EEDown01sigma'),
    cosThetaStarThreshold = cms.untracked.double(0.5),
    dRJetToPhoLThreshold = cms.untracked.double(0.5),
    dRJetToPhoSThreshold = cms.untracked.double(0.5),
    dijetMassHighThreshold = cms.untracked.double(120.0),
    dijetMassLowThreshold = cms.untracked.double(60.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(40.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHHadronicTagMCScaleLowR9EEUp01sigma = cms.EDProducer("FlashggVHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EEUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    SystLabel = cms.string('MCScaleLowR9EEUp01sigma'),
    cosThetaStarThreshold = cms.untracked.double(0.5),
    dRJetToPhoLThreshold = cms.untracked.double(0.5),
    dRJetToPhoSThreshold = cms.untracked.double(0.5),
    dijetMassHighThreshold = cms.untracked.double(120.0),
    dijetMassLowThreshold = cms.untracked.double(60.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(40.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHHadronicTagMCSmearHighR9EBPhiDown01sigma = cms.EDProducer("FlashggVHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBPhiDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    SystLabel = cms.string('MCSmearHighR9EBPhiDown01sigma'),
    cosThetaStarThreshold = cms.untracked.double(0.5),
    dRJetToPhoLThreshold = cms.untracked.double(0.5),
    dRJetToPhoSThreshold = cms.untracked.double(0.5),
    dijetMassHighThreshold = cms.untracked.double(120.0),
    dijetMassLowThreshold = cms.untracked.double(60.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(40.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHHadronicTagMCSmearHighR9EBPhiUp01sigma = cms.EDProducer("FlashggVHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBPhiUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    SystLabel = cms.string('MCSmearHighR9EBPhiUp01sigma'),
    cosThetaStarThreshold = cms.untracked.double(0.5),
    dRJetToPhoLThreshold = cms.untracked.double(0.5),
    dRJetToPhoSThreshold = cms.untracked.double(0.5),
    dijetMassHighThreshold = cms.untracked.double(120.0),
    dijetMassLowThreshold = cms.untracked.double(60.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(40.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHHadronicTagMCSmearHighR9EBRhoDown01sigma = cms.EDProducer("FlashggVHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBRhoDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    SystLabel = cms.string('MCSmearHighR9EBRhoDown01sigma'),
    cosThetaStarThreshold = cms.untracked.double(0.5),
    dRJetToPhoLThreshold = cms.untracked.double(0.5),
    dRJetToPhoSThreshold = cms.untracked.double(0.5),
    dijetMassHighThreshold = cms.untracked.double(120.0),
    dijetMassLowThreshold = cms.untracked.double(60.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(40.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHHadronicTagMCSmearHighR9EBRhoUp01sigma = cms.EDProducer("FlashggVHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBRhoUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    SystLabel = cms.string('MCSmearHighR9EBRhoUp01sigma'),
    cosThetaStarThreshold = cms.untracked.double(0.5),
    dRJetToPhoLThreshold = cms.untracked.double(0.5),
    dRJetToPhoSThreshold = cms.untracked.double(0.5),
    dijetMassHighThreshold = cms.untracked.double(120.0),
    dijetMassLowThreshold = cms.untracked.double(60.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(40.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHHadronicTagMCSmearHighR9EEDown01sigma = cms.EDProducer("FlashggVHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EEDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    SystLabel = cms.string('MCSmearHighR9EEDown01sigma'),
    cosThetaStarThreshold = cms.untracked.double(0.5),
    dRJetToPhoLThreshold = cms.untracked.double(0.5),
    dRJetToPhoSThreshold = cms.untracked.double(0.5),
    dijetMassHighThreshold = cms.untracked.double(120.0),
    dijetMassLowThreshold = cms.untracked.double(60.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(40.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHHadronicTagMCSmearHighR9EEUp01sigma = cms.EDProducer("FlashggVHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EEUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    SystLabel = cms.string('MCSmearHighR9EEUp01sigma'),
    cosThetaStarThreshold = cms.untracked.double(0.5),
    dRJetToPhoLThreshold = cms.untracked.double(0.5),
    dRJetToPhoSThreshold = cms.untracked.double(0.5),
    dijetMassHighThreshold = cms.untracked.double(120.0),
    dijetMassLowThreshold = cms.untracked.double(60.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(40.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHHadronicTagMCSmearLowR9EBPhiDown01sigma = cms.EDProducer("FlashggVHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBPhiDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    SystLabel = cms.string('MCSmearLowR9EBPhiDown01sigma'),
    cosThetaStarThreshold = cms.untracked.double(0.5),
    dRJetToPhoLThreshold = cms.untracked.double(0.5),
    dRJetToPhoSThreshold = cms.untracked.double(0.5),
    dijetMassHighThreshold = cms.untracked.double(120.0),
    dijetMassLowThreshold = cms.untracked.double(60.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(40.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHHadronicTagMCSmearLowR9EBPhiUp01sigma = cms.EDProducer("FlashggVHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBPhiUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    SystLabel = cms.string('MCSmearLowR9EBPhiUp01sigma'),
    cosThetaStarThreshold = cms.untracked.double(0.5),
    dRJetToPhoLThreshold = cms.untracked.double(0.5),
    dRJetToPhoSThreshold = cms.untracked.double(0.5),
    dijetMassHighThreshold = cms.untracked.double(120.0),
    dijetMassLowThreshold = cms.untracked.double(60.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(40.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHHadronicTagMCSmearLowR9EBRhoDown01sigma = cms.EDProducer("FlashggVHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBRhoDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    SystLabel = cms.string('MCSmearLowR9EBRhoDown01sigma'),
    cosThetaStarThreshold = cms.untracked.double(0.5),
    dRJetToPhoLThreshold = cms.untracked.double(0.5),
    dRJetToPhoSThreshold = cms.untracked.double(0.5),
    dijetMassHighThreshold = cms.untracked.double(120.0),
    dijetMassLowThreshold = cms.untracked.double(60.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(40.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHHadronicTagMCSmearLowR9EBRhoUp01sigma = cms.EDProducer("FlashggVHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBRhoUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    SystLabel = cms.string('MCSmearLowR9EBRhoUp01sigma'),
    cosThetaStarThreshold = cms.untracked.double(0.5),
    dRJetToPhoLThreshold = cms.untracked.double(0.5),
    dRJetToPhoSThreshold = cms.untracked.double(0.5),
    dijetMassHighThreshold = cms.untracked.double(120.0),
    dijetMassLowThreshold = cms.untracked.double(60.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(40.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHHadronicTagMCSmearLowR9EEDown01sigma = cms.EDProducer("FlashggVHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEDown01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EEDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    SystLabel = cms.string('MCSmearLowR9EEDown01sigma'),
    cosThetaStarThreshold = cms.untracked.double(0.5),
    dRJetToPhoLThreshold = cms.untracked.double(0.5),
    dRJetToPhoSThreshold = cms.untracked.double(0.5),
    dijetMassHighThreshold = cms.untracked.double(120.0),
    dijetMassLowThreshold = cms.untracked.double(60.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(40.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHHadronicTagMCSmearLowR9EEUp01sigma = cms.EDProducer("FlashggVHHadronicTagProducer",
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEUp01sigma"),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EEUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    SystLabel = cms.string('MCSmearLowR9EEUp01sigma'),
    cosThetaStarThreshold = cms.untracked.double(0.5),
    dRJetToPhoLThreshold = cms.untracked.double(0.5),
    dRJetToPhoSThreshold = cms.untracked.double(0.5),
    dijetMassHighThreshold = cms.untracked.double(120.0),
    dijetMassLowThreshold = cms.untracked.double(60.0),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(40.0),
    jetsNumberThreshold = cms.untracked.double(2.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHLooseTag = cms.EDProducer("FlashggVHLooseTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVA"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string(''),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJets","0"), cms.InputTag("flashggUnpackedJets","1"), cms.InputTag("flashggUnpackedJets","2"), cms.InputTag("flashggUnpackedJets","3"), cms.InputTag("flashggUnpackedJets","4"), 
        cms.InputTag("flashggUnpackedJets","5"), cms.InputTag("flashggUnpackedJets","6"), cms.InputTag("flashggUnpackedJets","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHLooseTagMCScaleHighR9EBDown01sigma = cms.EDProducer("FlashggVHLooseTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EBDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleHighR9EBDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHLooseTagMCScaleHighR9EBUp01sigma = cms.EDProducer("FlashggVHLooseTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EBUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleHighR9EBUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHLooseTagMCScaleHighR9EEDown01sigma = cms.EDProducer("FlashggVHLooseTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EEDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleHighR9EEDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHLooseTagMCScaleHighR9EEUp01sigma = cms.EDProducer("FlashggVHLooseTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EEUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleHighR9EEUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHLooseTagMCScaleLowR9EBDown01sigma = cms.EDProducer("FlashggVHLooseTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EBDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleLowR9EBDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHLooseTagMCScaleLowR9EBUp01sigma = cms.EDProducer("FlashggVHLooseTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EBUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleLowR9EBUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHLooseTagMCScaleLowR9EEDown01sigma = cms.EDProducer("FlashggVHLooseTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EEDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleLowR9EEDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHLooseTagMCScaleLowR9EEUp01sigma = cms.EDProducer("FlashggVHLooseTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EEUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleLowR9EEUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHLooseTagMCSmearHighR9EBPhiDown01sigma = cms.EDProducer("FlashggVHLooseTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBPhiDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearHighR9EBPhiDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHLooseTagMCSmearHighR9EBPhiUp01sigma = cms.EDProducer("FlashggVHLooseTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBPhiUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearHighR9EBPhiUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHLooseTagMCSmearHighR9EBRhoDown01sigma = cms.EDProducer("FlashggVHLooseTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBRhoDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearHighR9EBRhoDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHLooseTagMCSmearHighR9EBRhoUp01sigma = cms.EDProducer("FlashggVHLooseTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBRhoUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearHighR9EBRhoUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHLooseTagMCSmearHighR9EEDown01sigma = cms.EDProducer("FlashggVHLooseTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EEDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearHighR9EEDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHLooseTagMCSmearHighR9EEUp01sigma = cms.EDProducer("FlashggVHLooseTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EEUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearHighR9EEUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHLooseTagMCSmearLowR9EBPhiDown01sigma = cms.EDProducer("FlashggVHLooseTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBPhiDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearLowR9EBPhiDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHLooseTagMCSmearLowR9EBPhiUp01sigma = cms.EDProducer("FlashggVHLooseTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBPhiUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearLowR9EBPhiUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHLooseTagMCSmearLowR9EBRhoDown01sigma = cms.EDProducer("FlashggVHLooseTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBRhoDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearLowR9EBRhoDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHLooseTagMCSmearLowR9EBRhoUp01sigma = cms.EDProducer("FlashggVHLooseTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBRhoUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearLowR9EBRhoUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHLooseTagMCSmearLowR9EEDown01sigma = cms.EDProducer("FlashggVHLooseTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EEDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearLowR9EEDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHLooseTagMCSmearLowR9EEUp01sigma = cms.EDProducer("FlashggVHLooseTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EEUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearLowR9EEUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","7")),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHTightTag = cms.EDProducer("FlashggVHTightTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVA"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string(''),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetMuonThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRLowPtMuonPhoThreshold = cms.untracked.double(0.5),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    deltaRPhoLeadJet = cms.untracked.double(0.5),
    deltaRPhoSubLeadJet = cms.untracked.double(0.5),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJets","0"), cms.InputTag("flashggUnpackedJets","1"), cms.InputTag("flashggUnpackedJets","2"), cms.InputTag("flashggUnpackedJets","3"), cms.InputTag("flashggUnpackedJets","4"), 
        cms.InputTag("flashggUnpackedJets","5"), cms.InputTag("flashggUnpackedJets","6"), cms.InputTag("flashggUnpackedJets","7")),
    invMassLepHighThreshold = cms.untracked.double(110.0),
    invMassLepLowThreshold = cms.untracked.double(70.0),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonLowPtThreshold = cms.untracked.double(10.0),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    numberOfHighPtMuonsThreshold = cms.untracked.double(1.0),
    numberOfLowPtMuonsThreshold = cms.untracked.double(2.0),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHTightTagMCScaleHighR9EBDown01sigma = cms.EDProducer("FlashggVHTightTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EBDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleHighR9EBDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetMuonThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRLowPtMuonPhoThreshold = cms.untracked.double(0.5),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    deltaRPhoLeadJet = cms.untracked.double(0.5),
    deltaRPhoSubLeadJet = cms.untracked.double(0.5),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBDown01sigma","7")),
    invMassLepHighThreshold = cms.untracked.double(110.0),
    invMassLepLowThreshold = cms.untracked.double(70.0),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonLowPtThreshold = cms.untracked.double(10.0),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    numberOfHighPtMuonsThreshold = cms.untracked.double(1.0),
    numberOfLowPtMuonsThreshold = cms.untracked.double(2.0),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHTightTagMCScaleHighR9EBUp01sigma = cms.EDProducer("FlashggVHTightTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EBUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EBUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleHighR9EBUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetMuonThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRLowPtMuonPhoThreshold = cms.untracked.double(0.5),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    deltaRPhoLeadJet = cms.untracked.double(0.5),
    deltaRPhoSubLeadJet = cms.untracked.double(0.5),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EBUp01sigma","7")),
    invMassLepHighThreshold = cms.untracked.double(110.0),
    invMassLepLowThreshold = cms.untracked.double(70.0),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonLowPtThreshold = cms.untracked.double(10.0),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    numberOfHighPtMuonsThreshold = cms.untracked.double(1.0),
    numberOfLowPtMuonsThreshold = cms.untracked.double(2.0),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHTightTagMCScaleHighR9EEDown01sigma = cms.EDProducer("FlashggVHTightTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EEDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleHighR9EEDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetMuonThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRLowPtMuonPhoThreshold = cms.untracked.double(0.5),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    deltaRPhoLeadJet = cms.untracked.double(0.5),
    deltaRPhoSubLeadJet = cms.untracked.double(0.5),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEDown01sigma","7")),
    invMassLepHighThreshold = cms.untracked.double(110.0),
    invMassLepLowThreshold = cms.untracked.double(70.0),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonLowPtThreshold = cms.untracked.double(10.0),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    numberOfHighPtMuonsThreshold = cms.untracked.double(1.0),
    numberOfLowPtMuonsThreshold = cms.untracked.double(2.0),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHTightTagMCScaleHighR9EEUp01sigma = cms.EDProducer("FlashggVHTightTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleHighR9EEUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleHighR9EEUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleHighR9EEUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetMuonThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRLowPtMuonPhoThreshold = cms.untracked.double(0.5),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    deltaRPhoLeadJet = cms.untracked.double(0.5),
    deltaRPhoSubLeadJet = cms.untracked.double(0.5),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleHighR9EEUp01sigma","7")),
    invMassLepHighThreshold = cms.untracked.double(110.0),
    invMassLepLowThreshold = cms.untracked.double(70.0),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonLowPtThreshold = cms.untracked.double(10.0),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    numberOfHighPtMuonsThreshold = cms.untracked.double(1.0),
    numberOfLowPtMuonsThreshold = cms.untracked.double(2.0),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHTightTagMCScaleLowR9EBDown01sigma = cms.EDProducer("FlashggVHTightTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EBDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleLowR9EBDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetMuonThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRLowPtMuonPhoThreshold = cms.untracked.double(0.5),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    deltaRPhoLeadJet = cms.untracked.double(0.5),
    deltaRPhoSubLeadJet = cms.untracked.double(0.5),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBDown01sigma","7")),
    invMassLepHighThreshold = cms.untracked.double(110.0),
    invMassLepLowThreshold = cms.untracked.double(70.0),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonLowPtThreshold = cms.untracked.double(10.0),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    numberOfHighPtMuonsThreshold = cms.untracked.double(1.0),
    numberOfLowPtMuonsThreshold = cms.untracked.double(2.0),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHTightTagMCScaleLowR9EBUp01sigma = cms.EDProducer("FlashggVHTightTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EBUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EBUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleLowR9EBUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetMuonThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRLowPtMuonPhoThreshold = cms.untracked.double(0.5),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    deltaRPhoLeadJet = cms.untracked.double(0.5),
    deltaRPhoSubLeadJet = cms.untracked.double(0.5),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EBUp01sigma","7")),
    invMassLepHighThreshold = cms.untracked.double(110.0),
    invMassLepLowThreshold = cms.untracked.double(70.0),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonLowPtThreshold = cms.untracked.double(10.0),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    numberOfHighPtMuonsThreshold = cms.untracked.double(1.0),
    numberOfLowPtMuonsThreshold = cms.untracked.double(2.0),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHTightTagMCScaleLowR9EEDown01sigma = cms.EDProducer("FlashggVHTightTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EEDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleLowR9EEDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetMuonThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRLowPtMuonPhoThreshold = cms.untracked.double(0.5),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    deltaRPhoLeadJet = cms.untracked.double(0.5),
    deltaRPhoSubLeadJet = cms.untracked.double(0.5),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEDown01sigma","7")),
    invMassLepHighThreshold = cms.untracked.double(110.0),
    invMassLepLowThreshold = cms.untracked.double(70.0),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonLowPtThreshold = cms.untracked.double(10.0),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    numberOfHighPtMuonsThreshold = cms.untracked.double(1.0),
    numberOfLowPtMuonsThreshold = cms.untracked.double(2.0),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHTightTagMCScaleLowR9EEUp01sigma = cms.EDProducer("FlashggVHTightTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCScaleLowR9EEUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCScaleLowR9EEUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCScaleLowR9EEUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetMuonThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRLowPtMuonPhoThreshold = cms.untracked.double(0.5),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    deltaRPhoLeadJet = cms.untracked.double(0.5),
    deltaRPhoSubLeadJet = cms.untracked.double(0.5),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCScaleLowR9EEUp01sigma","7")),
    invMassLepHighThreshold = cms.untracked.double(110.0),
    invMassLepLowThreshold = cms.untracked.double(70.0),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonLowPtThreshold = cms.untracked.double(10.0),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    numberOfHighPtMuonsThreshold = cms.untracked.double(1.0),
    numberOfLowPtMuonsThreshold = cms.untracked.double(2.0),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHTightTagMCSmearHighR9EBPhiDown01sigma = cms.EDProducer("FlashggVHTightTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBPhiDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearHighR9EBPhiDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetMuonThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRLowPtMuonPhoThreshold = cms.untracked.double(0.5),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    deltaRPhoLeadJet = cms.untracked.double(0.5),
    deltaRPhoSubLeadJet = cms.untracked.double(0.5),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma","7")),
    invMassLepHighThreshold = cms.untracked.double(110.0),
    invMassLepLowThreshold = cms.untracked.double(70.0),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonLowPtThreshold = cms.untracked.double(10.0),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    numberOfHighPtMuonsThreshold = cms.untracked.double(1.0),
    numberOfLowPtMuonsThreshold = cms.untracked.double(2.0),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHTightTagMCSmearHighR9EBPhiUp01sigma = cms.EDProducer("FlashggVHTightTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBPhiUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBPhiUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearHighR9EBPhiUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetMuonThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRLowPtMuonPhoThreshold = cms.untracked.double(0.5),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    deltaRPhoLeadJet = cms.untracked.double(0.5),
    deltaRPhoSubLeadJet = cms.untracked.double(0.5),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma","7")),
    invMassLepHighThreshold = cms.untracked.double(110.0),
    invMassLepLowThreshold = cms.untracked.double(70.0),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonLowPtThreshold = cms.untracked.double(10.0),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    numberOfHighPtMuonsThreshold = cms.untracked.double(1.0),
    numberOfLowPtMuonsThreshold = cms.untracked.double(2.0),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHTightTagMCSmearHighR9EBRhoDown01sigma = cms.EDProducer("FlashggVHTightTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBRhoDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearHighR9EBRhoDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetMuonThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRLowPtMuonPhoThreshold = cms.untracked.double(0.5),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    deltaRPhoLeadJet = cms.untracked.double(0.5),
    deltaRPhoSubLeadJet = cms.untracked.double(0.5),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma","7")),
    invMassLepHighThreshold = cms.untracked.double(110.0),
    invMassLepLowThreshold = cms.untracked.double(70.0),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonLowPtThreshold = cms.untracked.double(10.0),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    numberOfHighPtMuonsThreshold = cms.untracked.double(1.0),
    numberOfLowPtMuonsThreshold = cms.untracked.double(2.0),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHTightTagMCSmearHighR9EBRhoUp01sigma = cms.EDProducer("FlashggVHTightTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EBRhoUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EBRhoUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearHighR9EBRhoUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetMuonThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRLowPtMuonPhoThreshold = cms.untracked.double(0.5),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    deltaRPhoLeadJet = cms.untracked.double(0.5),
    deltaRPhoSubLeadJet = cms.untracked.double(0.5),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma","7")),
    invMassLepHighThreshold = cms.untracked.double(110.0),
    invMassLepLowThreshold = cms.untracked.double(70.0),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonLowPtThreshold = cms.untracked.double(10.0),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    numberOfHighPtMuonsThreshold = cms.untracked.double(1.0),
    numberOfLowPtMuonsThreshold = cms.untracked.double(2.0),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHTightTagMCSmearHighR9EEDown01sigma = cms.EDProducer("FlashggVHTightTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EEDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearHighR9EEDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetMuonThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRLowPtMuonPhoThreshold = cms.untracked.double(0.5),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    deltaRPhoLeadJet = cms.untracked.double(0.5),
    deltaRPhoSubLeadJet = cms.untracked.double(0.5),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEDown01sigma","7")),
    invMassLepHighThreshold = cms.untracked.double(110.0),
    invMassLepLowThreshold = cms.untracked.double(70.0),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonLowPtThreshold = cms.untracked.double(10.0),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    numberOfHighPtMuonsThreshold = cms.untracked.double(1.0),
    numberOfLowPtMuonsThreshold = cms.untracked.double(2.0),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHTightTagMCSmearHighR9EEUp01sigma = cms.EDProducer("FlashggVHTightTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearHighR9EEUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearHighR9EEUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearHighR9EEUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetMuonThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRLowPtMuonPhoThreshold = cms.untracked.double(0.5),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    deltaRPhoLeadJet = cms.untracked.double(0.5),
    deltaRPhoSubLeadJet = cms.untracked.double(0.5),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearHighR9EEUp01sigma","7")),
    invMassLepHighThreshold = cms.untracked.double(110.0),
    invMassLepLowThreshold = cms.untracked.double(70.0),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonLowPtThreshold = cms.untracked.double(10.0),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    numberOfHighPtMuonsThreshold = cms.untracked.double(1.0),
    numberOfLowPtMuonsThreshold = cms.untracked.double(2.0),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHTightTagMCSmearLowR9EBPhiDown01sigma = cms.EDProducer("FlashggVHTightTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBPhiDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearLowR9EBPhiDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetMuonThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRLowPtMuonPhoThreshold = cms.untracked.double(0.5),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    deltaRPhoLeadJet = cms.untracked.double(0.5),
    deltaRPhoSubLeadJet = cms.untracked.double(0.5),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma","7")),
    invMassLepHighThreshold = cms.untracked.double(110.0),
    invMassLepLowThreshold = cms.untracked.double(70.0),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonLowPtThreshold = cms.untracked.double(10.0),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    numberOfHighPtMuonsThreshold = cms.untracked.double(1.0),
    numberOfLowPtMuonsThreshold = cms.untracked.double(2.0),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHTightTagMCSmearLowR9EBPhiUp01sigma = cms.EDProducer("FlashggVHTightTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBPhiUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBPhiUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearLowR9EBPhiUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetMuonThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRLowPtMuonPhoThreshold = cms.untracked.double(0.5),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    deltaRPhoLeadJet = cms.untracked.double(0.5),
    deltaRPhoSubLeadJet = cms.untracked.double(0.5),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma","7")),
    invMassLepHighThreshold = cms.untracked.double(110.0),
    invMassLepLowThreshold = cms.untracked.double(70.0),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonLowPtThreshold = cms.untracked.double(10.0),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    numberOfHighPtMuonsThreshold = cms.untracked.double(1.0),
    numberOfLowPtMuonsThreshold = cms.untracked.double(2.0),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHTightTagMCSmearLowR9EBRhoDown01sigma = cms.EDProducer("FlashggVHTightTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBRhoDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearLowR9EBRhoDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetMuonThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRLowPtMuonPhoThreshold = cms.untracked.double(0.5),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    deltaRPhoLeadJet = cms.untracked.double(0.5),
    deltaRPhoSubLeadJet = cms.untracked.double(0.5),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma","7")),
    invMassLepHighThreshold = cms.untracked.double(110.0),
    invMassLepLowThreshold = cms.untracked.double(70.0),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonLowPtThreshold = cms.untracked.double(10.0),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    numberOfHighPtMuonsThreshold = cms.untracked.double(1.0),
    numberOfLowPtMuonsThreshold = cms.untracked.double(2.0),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHTightTagMCSmearLowR9EBRhoUp01sigma = cms.EDProducer("FlashggVHTightTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EBRhoUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EBRhoUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearLowR9EBRhoUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetMuonThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRLowPtMuonPhoThreshold = cms.untracked.double(0.5),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    deltaRPhoLeadJet = cms.untracked.double(0.5),
    deltaRPhoSubLeadJet = cms.untracked.double(0.5),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma","7")),
    invMassLepHighThreshold = cms.untracked.double(110.0),
    invMassLepLowThreshold = cms.untracked.double(70.0),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonLowPtThreshold = cms.untracked.double(10.0),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    numberOfHighPtMuonsThreshold = cms.untracked.double(1.0),
    numberOfLowPtMuonsThreshold = cms.untracked.double(2.0),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHTightTagMCSmearLowR9EEDown01sigma = cms.EDProducer("FlashggVHTightTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEDown01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EEDown01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearLowR9EEDown01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetMuonThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRLowPtMuonPhoThreshold = cms.untracked.double(0.5),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    deltaRPhoLeadJet = cms.untracked.double(0.5),
    deltaRPhoSubLeadJet = cms.untracked.double(0.5),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEDown01sigma","7")),
    invMassLepHighThreshold = cms.untracked.double(110.0),
    invMassLepLowThreshold = cms.untracked.double(70.0),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonLowPtThreshold = cms.untracked.double(10.0),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    numberOfHighPtMuonsThreshold = cms.untracked.double(1.0),
    numberOfLowPtMuonsThreshold = cms.untracked.double(2.0),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggVHTightTagMCSmearLowR9EEUp01sigma = cms.EDProducer("FlashggVHTightTagProducer",
    DeltaRTrkElec = cms.untracked.double(1.0),
    DiPhotonTag = cms.InputTag("flashggDiPhotonSystematics","MCSmearLowR9EEUp01sigma"),
    ElectronPtThreshold = cms.untracked.double(20.0),
    ElectronTag = cms.InputTag("flashggElectronSystematics"),
    EtaCuts = cms.untracked.vdouble(1.442, 1.566, 2.5),
    GenParticleTag = cms.InputTag("flashggPrunedGenParticles"),
    HighEtaPhoThreshold = cms.untracked.double(2.5),
    LongitudinalImpactParam = cms.untracked.double(0.02),
    LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
    METTag = cms.InputTag("slimmedMETs"),
    METThreshold = cms.untracked.double(45.0),
    MVAResultTag = cms.InputTag("flashggDiPhotonMVAMCSmearLowR9EEUp01sigma"),
    MVAThreshold = cms.untracked.double(-0.6),
    MidPtEtaPhoThreshold = cms.untracked.double(1.566),
    MuonTag = cms.InputTag("flashggMuonSystematics"),
    PhoMVAThreshold = cms.untracked.double(-0.2),
    PuIDCutoffThreshold = cms.untracked.double(0.8),
    SystLabel = cms.string('MCSmearLowR9EEUp01sigma'),
    TransverseImpactParam = cms.untracked.double(0.2),
    VertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Zmass_ = cms.untracked.double(91.9),
    deltaMassElectronZThreshold_ = cms.untracked.double(10.0),
    deltaRJetMuonThreshold = cms.untracked.double(0.5),
    deltaRLepPhoThreshold = cms.untracked.double(1),
    deltaRLowPtMuonPhoThreshold = cms.untracked.double(0.5),
    deltaRPhoElectronThreshold = cms.untracked.double(1.0),
    deltaRPhoLeadJet = cms.untracked.double(0.5),
    deltaRPhoSubLeadJet = cms.untracked.double(0.5),
    electronIsoThreshold = cms.untracked.double(0.15),
    electronNumOfHitsThreshold = cms.untracked.double(1),
    inputTagJets = cms.VInputTag(cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","0"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","1"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","2"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","3"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","4"), 
        cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","5"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","6"), cms.InputTag("flashggUnpackedJetsMCSmearLowR9EEUp01sigma","7")),
    invMassLepHighThreshold = cms.untracked.double(110.0),
    invMassLepLowThreshold = cms.untracked.double(70.0),
    jetEtaThreshold = cms.untracked.double(2.4),
    jetPtThreshold = cms.untracked.double(20.0),
    jetsNumberThreshold = cms.untracked.double(3.0),
    leadPhoOverMassThreshold = cms.untracked.double(0.375),
    leptonEtaThreshold = cms.untracked.double(2.4),
    leptonLowPtThreshold = cms.untracked.double(10.0),
    leptonPtThreshold = cms.untracked.double(20),
    muPFIsoSumRelThreshold = cms.untracked.double(0.2),
    nonTrigMVAThreshold = cms.untracked.double(0.9),
    numberOfHighPtMuonsThreshold = cms.untracked.double(1.0),
    numberOfLowPtMuonsThreshold = cms.untracked.double(2.0),
    subleadPhoOverMassThreshold = cms.untracked.double(0.25)
)


process.flashggTagTester = cms.EDAnalyzer("FlashggTagTestAnalyzer",
    TagSorter = cms.InputTag("flashggTagSorter")
)


process.tagsDumper = cms.EDAnalyzer("DiPhotonTagDumper",
    categories = cms.VPSet(cms.PSet(
        className = cms.string('UntaggedTag'),
        histograms = cms.VPSet(),
        label = cms.string(''),
        subcats = cms.int32(5),
        variables = cms.VPSet(cms.PSet(
            expr = cms.string('diPhoton().mass'),
            name = cms.untracked.string('CMS_hgg_mass'),
            nbins = cms.untracked.int32(160),
            vmax = cms.untracked.double(180.0),
            vmin = cms.untracked.double(100.0)
        ), 
            cms.PSet(
                expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                name = cms.untracked.string('dZ')
            ))
    ), 
        cms.PSet(
            className = cms.string('UntaggedTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EEUp01sigma'),
            subcats = cms.int32(5),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('UntaggedTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBRhoUp01sigma'),
            subcats = cms.int32(5),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('UntaggedTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBPhiUp01sigma'),
            subcats = cms.int32(5),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('UntaggedTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EBUp01sigma'),
            subcats = cms.int32(5),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('UntaggedTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EEUp01sigma'),
            subcats = cms.int32(5),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('UntaggedTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EEDown01sigma'),
            subcats = cms.int32(5),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('UntaggedTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBRhoDown01sigma'),
            subcats = cms.int32(5),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('UntaggedTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBPhiDown01sigma'),
            subcats = cms.int32(5),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('UntaggedTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EBDown01sigma'),
            subcats = cms.int32(5),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('UntaggedTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EEDown01sigma'),
            subcats = cms.int32(5),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('UntaggedTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EEUp01sigma'),
            subcats = cms.int32(5),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('UntaggedTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBRhoUp01sigma'),
            subcats = cms.int32(5),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('UntaggedTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBPhiUp01sigma'),
            subcats = cms.int32(5),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('UntaggedTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EBUp01sigma'),
            subcats = cms.int32(5),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('UntaggedTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EEUp01sigma'),
            subcats = cms.int32(5),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('UntaggedTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EEDown01sigma'),
            subcats = cms.int32(5),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('UntaggedTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBRhoDown01sigma'),
            subcats = cms.int32(5),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('UntaggedTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBPhiDown01sigma'),
            subcats = cms.int32(5),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('UntaggedTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EBDown01sigma'),
            subcats = cms.int32(5),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('UntaggedTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EEDown01sigma'),
            subcats = cms.int32(5),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VBFTag'),
            histograms = cms.VPSet(),
            label = cms.string(''),
            subcats = cms.int32(3),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VBFTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EEUp01sigma'),
            subcats = cms.int32(3),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VBFTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBRhoUp01sigma'),
            subcats = cms.int32(3),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VBFTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBPhiUp01sigma'),
            subcats = cms.int32(3),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VBFTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EBUp01sigma'),
            subcats = cms.int32(3),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VBFTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EEUp01sigma'),
            subcats = cms.int32(3),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VBFTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EEDown01sigma'),
            subcats = cms.int32(3),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VBFTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBRhoDown01sigma'),
            subcats = cms.int32(3),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VBFTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBPhiDown01sigma'),
            subcats = cms.int32(3),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VBFTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EBDown01sigma'),
            subcats = cms.int32(3),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VBFTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EEDown01sigma'),
            subcats = cms.int32(3),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VBFTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EEUp01sigma'),
            subcats = cms.int32(3),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VBFTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBRhoUp01sigma'),
            subcats = cms.int32(3),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VBFTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBPhiUp01sigma'),
            subcats = cms.int32(3),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VBFTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EBUp01sigma'),
            subcats = cms.int32(3),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VBFTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EEUp01sigma'),
            subcats = cms.int32(3),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VBFTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EEDown01sigma'),
            subcats = cms.int32(3),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VBFTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBRhoDown01sigma'),
            subcats = cms.int32(3),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VBFTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBPhiDown01sigma'),
            subcats = cms.int32(3),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VBFTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EBDown01sigma'),
            subcats = cms.int32(3),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VBFTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EEDown01sigma'),
            subcats = cms.int32(3),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHTightTag'),
            histograms = cms.VPSet(),
            label = cms.string(''),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHTightTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHTightTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBRhoUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHTightTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBPhiUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHTightTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EBUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHTightTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHTightTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHTightTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBRhoDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHTightTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBPhiDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHTightTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EBDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHTightTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHTightTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHTightTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBRhoUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHTightTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBPhiUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHTightTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EBUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHTightTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHTightTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHTightTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBRhoDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHTightTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBPhiDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHTightTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EBDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHTightTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHLooseTag'),
            histograms = cms.VPSet(),
            label = cms.string(''),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHLooseTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHLooseTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBRhoUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHLooseTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBPhiUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHLooseTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EBUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHLooseTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHLooseTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHLooseTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBRhoDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHLooseTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBPhiDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHLooseTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EBDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHLooseTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHLooseTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHLooseTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBRhoUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHLooseTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBPhiUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHLooseTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EBUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHLooseTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHLooseTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHLooseTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBRhoDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHLooseTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBPhiDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHLooseTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EBDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHLooseTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHEtTag'),
            histograms = cms.VPSet(),
            label = cms.string(''),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHEtTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHEtTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBRhoUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHEtTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBPhiUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHEtTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EBUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHEtTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHEtTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHEtTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBRhoDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHEtTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBPhiDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHEtTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EBDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHEtTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHEtTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHEtTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBRhoUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHEtTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBPhiUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHEtTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EBUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHEtTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHEtTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHEtTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBRhoDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHEtTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBPhiDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHEtTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EBDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHEtTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string(''),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBRhoUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBPhiUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EBUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBRhoDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBPhiDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EBDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBRhoUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBPhiUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EBUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBRhoDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBPhiDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EBDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('VHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string(''),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBRhoUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBPhiUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EBUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBRhoDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBPhiDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EBDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBRhoUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBPhiUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EBUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBRhoDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBPhiDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EBDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHHadronicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHLeptonicTag'),
            histograms = cms.VPSet(),
            label = cms.string(''),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHLeptonicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHLeptonicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBRhoUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHLeptonicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBPhiUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHLeptonicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EBUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHLeptonicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHLeptonicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHLeptonicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBRhoDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHLeptonicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearHighR9EBPhiDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHLeptonicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EBDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHLeptonicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleHighR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHLeptonicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHLeptonicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBRhoUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHLeptonicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBPhiUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHLeptonicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EBUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHLeptonicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EEUp01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHLeptonicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHLeptonicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBRhoDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHLeptonicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCSmearLowR9EBPhiDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHLeptonicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EBDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        ), 
        cms.PSet(
            className = cms.string('TTHLeptonicTag'),
            histograms = cms.VPSet(),
            label = cms.string('MCScaleLowR9EEDown01sigma'),
            subcats = cms.int32(0),
            variables = cms.VPSet(cms.PSet(
                expr = cms.string('diPhoton().mass'),
                name = cms.untracked.string('CMS_hgg_mass'),
                nbins = cms.untracked.int32(160),
                vmax = cms.untracked.double(180.0),
                vmin = cms.untracked.double(100.0)
            ), 
                cms.PSet(
                    expr = cms.string('abs(tagTruth().genPV().z-diPhoton().vtx().z)'),
                    name = cms.untracked.string('dZ')
                ))
        )),
    className = cms.untracked.string('DiPhotonTagDumper'),
    classifierCfg = cms.PSet(
        categories = cms.VPSet(cms.PSet(
            cut = cms.string('hasSyst("") '),
            name = cms.untracked.string('')
        ), 
            cms.PSet(
                cut = cms.string('hasSyst("MCSmearHighR9EEUp01sigma") '),
                name = cms.untracked.string('MCSmearHighR9EEUp01sigma')
            ), 
            cms.PSet(
                cut = cms.string('hasSyst("MCSmearHighR9EBRhoUp01sigma") '),
                name = cms.untracked.string('MCSmearHighR9EBRhoUp01sigma')
            ), 
            cms.PSet(
                cut = cms.string('hasSyst("MCSmearHighR9EBPhiUp01sigma") '),
                name = cms.untracked.string('MCSmearHighR9EBPhiUp01sigma')
            ), 
            cms.PSet(
                cut = cms.string('hasSyst("MCScaleHighR9EBUp01sigma") '),
                name = cms.untracked.string('MCScaleHighR9EBUp01sigma')
            ), 
            cms.PSet(
                cut = cms.string('hasSyst("MCScaleHighR9EEUp01sigma") '),
                name = cms.untracked.string('MCScaleHighR9EEUp01sigma')
            ), 
            cms.PSet(
                cut = cms.string('hasSyst("MCSmearHighR9EEDown01sigma") '),
                name = cms.untracked.string('MCSmearHighR9EEDown01sigma')
            ), 
            cms.PSet(
                cut = cms.string('hasSyst("MCSmearHighR9EBRhoDown01sigma") '),
                name = cms.untracked.string('MCSmearHighR9EBRhoDown01sigma')
            ), 
            cms.PSet(
                cut = cms.string('hasSyst("MCSmearHighR9EBPhiDown01sigma") '),
                name = cms.untracked.string('MCSmearHighR9EBPhiDown01sigma')
            ), 
            cms.PSet(
                cut = cms.string('hasSyst("MCScaleHighR9EBDown01sigma") '),
                name = cms.untracked.string('MCScaleHighR9EBDown01sigma')
            ), 
            cms.PSet(
                cut = cms.string('hasSyst("MCScaleHighR9EEDown01sigma") '),
                name = cms.untracked.string('MCScaleHighR9EEDown01sigma')
            ), 
            cms.PSet(
                cut = cms.string('hasSyst("MCSmearLowR9EEUp01sigma") '),
                name = cms.untracked.string('MCSmearLowR9EEUp01sigma')
            ), 
            cms.PSet(
                cut = cms.string('hasSyst("MCSmearLowR9EBRhoUp01sigma") '),
                name = cms.untracked.string('MCSmearLowR9EBRhoUp01sigma')
            ), 
            cms.PSet(
                cut = cms.string('hasSyst("MCSmearLowR9EBPhiUp01sigma") '),
                name = cms.untracked.string('MCSmearLowR9EBPhiUp01sigma')
            ), 
            cms.PSet(
                cut = cms.string('hasSyst("MCScaleLowR9EBUp01sigma") '),
                name = cms.untracked.string('MCScaleLowR9EBUp01sigma')
            ), 
            cms.PSet(
                cut = cms.string('hasSyst("MCScaleLowR9EEUp01sigma") '),
                name = cms.untracked.string('MCScaleLowR9EEUp01sigma')
            ), 
            cms.PSet(
                cut = cms.string('hasSyst("MCSmearLowR9EEDown01sigma") '),
                name = cms.untracked.string('MCSmearLowR9EEDown01sigma')
            ), 
            cms.PSet(
                cut = cms.string('hasSyst("MCSmearLowR9EBRhoDown01sigma") '),
                name = cms.untracked.string('MCSmearLowR9EBRhoDown01sigma')
            ), 
            cms.PSet(
                cut = cms.string('hasSyst("MCSmearLowR9EBPhiDown01sigma") '),
                name = cms.untracked.string('MCSmearLowR9EBPhiDown01sigma')
            ), 
            cms.PSet(
                cut = cms.string('hasSyst("MCScaleLowR9EBDown01sigma") '),
                name = cms.untracked.string('MCScaleLowR9EBDown01sigma')
            ), 
            cms.PSet(
                cut = cms.string('hasSyst("MCScaleLowR9EEDown01sigma") '),
                name = cms.untracked.string('MCScaleLowR9EEDown01sigma')
            )),
        remap = cms.untracked.VPSet(cms.untracked.PSet(
            dst = cms.untracked.string('UntaggedTag'),
            src = cms.untracked.string('flashggUntaggedTag')
        ), 
            cms.untracked.PSet(
                dst = cms.untracked.string('VBFTag'),
                src = cms.untracked.string('flashggVBFTag')
            ), 
            cms.untracked.PSet(
                dst = cms.untracked.string('VHTightTag'),
                src = cms.untracked.string('flashggVHTightTag')
            ), 
            cms.untracked.PSet(
                dst = cms.untracked.string('VHLooseTag'),
                src = cms.untracked.string('flashggVHLooseTag')
            ), 
            cms.untracked.PSet(
                dst = cms.untracked.string('VHEtTag'),
                src = cms.untracked.string('flashggVHEtTag')
            ), 
            cms.untracked.PSet(
                dst = cms.untracked.string('VHHadronicTag'),
                src = cms.untracked.string('flashggVHHadronicTag')
            ), 
            cms.untracked.PSet(
                dst = cms.untracked.string('TTHHadronicTag'),
                src = cms.untracked.string('flashggTTHHadronicTag')
            ), 
            cms.untracked.PSet(
                dst = cms.untracked.string('TTHLeptonicTag'),
                src = cms.untracked.string('flashggTTHLeptonicTag')
            ))
    ),
    dumpGlobalVariables = cms.untracked.bool(True),
    dumpHistos = cms.untracked.bool(False),
    dumpTrees = cms.untracked.bool(True),
    dumpWorkspace = cms.untracked.bool(True),
    generatorInfo = cms.InputTag("generator"),
    globalVariables = cms.PSet(
        rho = cms.InputTag("fixedGridRhoAll"),
        vertexes = cms.InputTag("offlineSlimmedPrimaryVertices")
    ),
    lumiWeight = cms.double(1.0),
    maxCandPerEvent = cms.int32(-1),
    nameTemplate = cms.untracked.string('$PROCESS_$SQRTS_$CLASSNAME_$SUBCAT_$LABEL'),
    processId = cms.string('test'),
    quietRooFit = cms.untracked.bool(True),
    src = cms.InputTag("flashggSystTagMerger"),
    workspaceName = cms.untracked.string('cms_hgg_$SQRTS')
)


process.flashggTagSequenceMCSmearLowR9EBPhiUp01sigma = cms.Sequence(process.flashggDiPhotonMVAMCSmearLowR9EBPhiUp01sigma+process.flashggDiPhotonMVANewMCSmearLowR9EBPhiUp01sigma+process.flashggDiPhotonMVAPUPPIMCSmearLowR9EBPhiUp01sigma+process.flashggUnpackedJetsMCSmearLowR9EBPhiUp01sigma+process.flashggUnpackedPuppiJetsMCSmearLowR9EBPhiUp01sigma+process.flashggVBFMVAMCSmearLowR9EBPhiUp01sigma+process.flashggVBFMVALegacyMCSmearLowR9EBPhiUp01sigma+process.flashggVBFMVAPUPPIMCSmearLowR9EBPhiUp01sigma+process.flashggVBFDiPhoDiJetMVAMCSmearLowR9EBPhiUp01sigma+process.flashggVBFDiPhoDiJetMVALegacyMCSmearLowR9EBPhiUp01sigma+process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearLowR9EBPhiUp01sigma+process.flashggUntaggedMCSmearLowR9EBPhiUp01sigma+process.flashggVBFTagMCSmearLowR9EBPhiUp01sigma+process.flashggTTHLeptonicTagMCSmearLowR9EBPhiUp01sigma+process.flashggVHEtTagMCSmearLowR9EBPhiUp01sigma+process.flashggTTHHadronicTagMCSmearLowR9EBPhiUp01sigma+process.flashggVHLooseTagMCSmearLowR9EBPhiUp01sigma+process.flashggVHTightTagMCSmearLowR9EBPhiUp01sigma+process.flashggVHHadronicTagMCSmearLowR9EBPhiUp01sigma+process.flashggTagSorterMCSmearLowR9EBPhiUp01sigma)


process.flashggTagSequenceMCSmearHighR9EBRhoDown01sigma = cms.Sequence(process.flashggDiPhotonMVAMCSmearHighR9EBRhoDown01sigma+process.flashggDiPhotonMVANewMCSmearHighR9EBRhoDown01sigma+process.flashggDiPhotonMVAPUPPIMCSmearHighR9EBRhoDown01sigma+process.flashggUnpackedJetsMCSmearHighR9EBRhoDown01sigma+process.flashggUnpackedPuppiJetsMCSmearHighR9EBRhoDown01sigma+process.flashggVBFMVAMCSmearHighR9EBRhoDown01sigma+process.flashggVBFMVALegacyMCSmearHighR9EBRhoDown01sigma+process.flashggVBFMVAPUPPIMCSmearHighR9EBRhoDown01sigma+process.flashggVBFDiPhoDiJetMVAMCSmearHighR9EBRhoDown01sigma+process.flashggVBFDiPhoDiJetMVALegacyMCSmearHighR9EBRhoDown01sigma+process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearHighR9EBRhoDown01sigma+process.flashggUntaggedMCSmearHighR9EBRhoDown01sigma+process.flashggVBFTagMCSmearHighR9EBRhoDown01sigma+process.flashggTTHLeptonicTagMCSmearHighR9EBRhoDown01sigma+process.flashggVHEtTagMCSmearHighR9EBRhoDown01sigma+process.flashggTTHHadronicTagMCSmearHighR9EBRhoDown01sigma+process.flashggVHLooseTagMCSmearHighR9EBRhoDown01sigma+process.flashggVHTightTagMCSmearHighR9EBRhoDown01sigma+process.flashggVHHadronicTagMCSmearHighR9EBRhoDown01sigma+process.flashggTagSorterMCSmearHighR9EBRhoDown01sigma)


process.flashggTagSequenceMCSmearLowR9EBRhoUp01sigma = cms.Sequence(process.flashggDiPhotonMVAMCSmearLowR9EBRhoUp01sigma+process.flashggDiPhotonMVANewMCSmearLowR9EBRhoUp01sigma+process.flashggDiPhotonMVAPUPPIMCSmearLowR9EBRhoUp01sigma+process.flashggUnpackedJetsMCSmearLowR9EBRhoUp01sigma+process.flashggUnpackedPuppiJetsMCSmearLowR9EBRhoUp01sigma+process.flashggVBFMVAMCSmearLowR9EBRhoUp01sigma+process.flashggVBFMVALegacyMCSmearLowR9EBRhoUp01sigma+process.flashggVBFMVAPUPPIMCSmearLowR9EBRhoUp01sigma+process.flashggVBFDiPhoDiJetMVAMCSmearLowR9EBRhoUp01sigma+process.flashggVBFDiPhoDiJetMVALegacyMCSmearLowR9EBRhoUp01sigma+process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearLowR9EBRhoUp01sigma+process.flashggUntaggedMCSmearLowR9EBRhoUp01sigma+process.flashggVBFTagMCSmearLowR9EBRhoUp01sigma+process.flashggTTHLeptonicTagMCSmearLowR9EBRhoUp01sigma+process.flashggVHEtTagMCSmearLowR9EBRhoUp01sigma+process.flashggTTHHadronicTagMCSmearLowR9EBRhoUp01sigma+process.flashggVHLooseTagMCSmearLowR9EBRhoUp01sigma+process.flashggVHTightTagMCSmearLowR9EBRhoUp01sigma+process.flashggVHHadronicTagMCSmearLowR9EBRhoUp01sigma+process.flashggTagSorterMCSmearLowR9EBRhoUp01sigma)


process.flashggTagSequenceMCScaleHighR9EBUp01sigma = cms.Sequence(process.flashggDiPhotonMVAMCScaleHighR9EBUp01sigma+process.flashggDiPhotonMVANewMCScaleHighR9EBUp01sigma+process.flashggDiPhotonMVAPUPPIMCScaleHighR9EBUp01sigma+process.flashggUnpackedJetsMCScaleHighR9EBUp01sigma+process.flashggUnpackedPuppiJetsMCScaleHighR9EBUp01sigma+process.flashggVBFMVAMCScaleHighR9EBUp01sigma+process.flashggVBFMVALegacyMCScaleHighR9EBUp01sigma+process.flashggVBFMVAPUPPIMCScaleHighR9EBUp01sigma+process.flashggVBFDiPhoDiJetMVAMCScaleHighR9EBUp01sigma+process.flashggVBFDiPhoDiJetMVALegacyMCScaleHighR9EBUp01sigma+process.flashggVBFDiPhoDiJetMVAPUPPIMCScaleHighR9EBUp01sigma+process.flashggUntaggedMCScaleHighR9EBUp01sigma+process.flashggVBFTagMCScaleHighR9EBUp01sigma+process.flashggTTHLeptonicTagMCScaleHighR9EBUp01sigma+process.flashggVHEtTagMCScaleHighR9EBUp01sigma+process.flashggTTHHadronicTagMCScaleHighR9EBUp01sigma+process.flashggVHLooseTagMCScaleHighR9EBUp01sigma+process.flashggVHTightTagMCScaleHighR9EBUp01sigma+process.flashggVHHadronicTagMCScaleHighR9EBUp01sigma+process.flashggTagSorterMCScaleHighR9EBUp01sigma)


process.extraDumpers = cms.Sequence()


process.flashggTagSequence = cms.Sequence(process.flashggDiPhotonMVA+process.flashggDiPhotonMVANew+process.flashggDiPhotonMVAPUPPI+process.flashggUnpackedJets+process.flashggUnpackedPuppiJets+process.flashggVBFMVA+process.flashggVBFMVALegacy+process.flashggVBFMVAPUPPI+process.flashggVBFDiPhoDiJetMVA+process.flashggVBFDiPhoDiJetMVALegacy+process.flashggVBFDiPhoDiJetMVAPUPPI+process.flashggUntagged+process.flashggVBFTag+process.flashggTTHLeptonicTag+process.flashggVHEtTag+process.flashggTTHHadronicTag+process.flashggVHLooseTag+process.flashggVHTightTag+process.flashggVHHadronicTag+process.flashggTagSorter)


process.flashggTagSequenceMCScaleLowR9EBUp01sigma = cms.Sequence(process.flashggDiPhotonMVAMCScaleLowR9EBUp01sigma+process.flashggDiPhotonMVANewMCScaleLowR9EBUp01sigma+process.flashggDiPhotonMVAPUPPIMCScaleLowR9EBUp01sigma+process.flashggUnpackedJetsMCScaleLowR9EBUp01sigma+process.flashggUnpackedPuppiJetsMCScaleLowR9EBUp01sigma+process.flashggVBFMVAMCScaleLowR9EBUp01sigma+process.flashggVBFMVALegacyMCScaleLowR9EBUp01sigma+process.flashggVBFMVAPUPPIMCScaleLowR9EBUp01sigma+process.flashggVBFDiPhoDiJetMVAMCScaleLowR9EBUp01sigma+process.flashggVBFDiPhoDiJetMVALegacyMCScaleLowR9EBUp01sigma+process.flashggVBFDiPhoDiJetMVAPUPPIMCScaleLowR9EBUp01sigma+process.flashggUntaggedMCScaleLowR9EBUp01sigma+process.flashggVBFTagMCScaleLowR9EBUp01sigma+process.flashggTTHLeptonicTagMCScaleLowR9EBUp01sigma+process.flashggVHEtTagMCScaleLowR9EBUp01sigma+process.flashggTTHHadronicTagMCScaleLowR9EBUp01sigma+process.flashggVHLooseTagMCScaleLowR9EBUp01sigma+process.flashggVHTightTagMCScaleLowR9EBUp01sigma+process.flashggVHHadronicTagMCScaleLowR9EBUp01sigma+process.flashggTagSorterMCScaleLowR9EBUp01sigma)


process.flashggTagSequenceMCScaleHighR9EBDown01sigma = cms.Sequence(process.flashggDiPhotonMVAMCScaleHighR9EBDown01sigma+process.flashggDiPhotonMVANewMCScaleHighR9EBDown01sigma+process.flashggDiPhotonMVAPUPPIMCScaleHighR9EBDown01sigma+process.flashggUnpackedJetsMCScaleHighR9EBDown01sigma+process.flashggUnpackedPuppiJetsMCScaleHighR9EBDown01sigma+process.flashggVBFMVAMCScaleHighR9EBDown01sigma+process.flashggVBFMVALegacyMCScaleHighR9EBDown01sigma+process.flashggVBFMVAPUPPIMCScaleHighR9EBDown01sigma+process.flashggVBFDiPhoDiJetMVAMCScaleHighR9EBDown01sigma+process.flashggVBFDiPhoDiJetMVALegacyMCScaleHighR9EBDown01sigma+process.flashggVBFDiPhoDiJetMVAPUPPIMCScaleHighR9EBDown01sigma+process.flashggUntaggedMCScaleHighR9EBDown01sigma+process.flashggVBFTagMCScaleHighR9EBDown01sigma+process.flashggTTHLeptonicTagMCScaleHighR9EBDown01sigma+process.flashggVHEtTagMCScaleHighR9EBDown01sigma+process.flashggTTHHadronicTagMCScaleHighR9EBDown01sigma+process.flashggVHLooseTagMCScaleHighR9EBDown01sigma+process.flashggVHTightTagMCScaleHighR9EBDown01sigma+process.flashggVHHadronicTagMCScaleHighR9EBDown01sigma+process.flashggTagSorterMCScaleHighR9EBDown01sigma)


process.flashggTagSequenceMCScaleLowR9EBDown01sigma = cms.Sequence(process.flashggDiPhotonMVAMCScaleLowR9EBDown01sigma+process.flashggDiPhotonMVANewMCScaleLowR9EBDown01sigma+process.flashggDiPhotonMVAPUPPIMCScaleLowR9EBDown01sigma+process.flashggUnpackedJetsMCScaleLowR9EBDown01sigma+process.flashggUnpackedPuppiJetsMCScaleLowR9EBDown01sigma+process.flashggVBFMVAMCScaleLowR9EBDown01sigma+process.flashggVBFMVALegacyMCScaleLowR9EBDown01sigma+process.flashggVBFMVAPUPPIMCScaleLowR9EBDown01sigma+process.flashggVBFDiPhoDiJetMVAMCScaleLowR9EBDown01sigma+process.flashggVBFDiPhoDiJetMVALegacyMCScaleLowR9EBDown01sigma+process.flashggVBFDiPhoDiJetMVAPUPPIMCScaleLowR9EBDown01sigma+process.flashggUntaggedMCScaleLowR9EBDown01sigma+process.flashggVBFTagMCScaleLowR9EBDown01sigma+process.flashggTTHLeptonicTagMCScaleLowR9EBDown01sigma+process.flashggVHEtTagMCScaleLowR9EBDown01sigma+process.flashggTTHHadronicTagMCScaleLowR9EBDown01sigma+process.flashggVHLooseTagMCScaleLowR9EBDown01sigma+process.flashggVHTightTagMCScaleLowR9EBDown01sigma+process.flashggVHHadronicTagMCScaleLowR9EBDown01sigma+process.flashggTagSorterMCScaleLowR9EBDown01sigma)


process.flashggTagSequenceMCScaleLowR9EEDown01sigma = cms.Sequence(process.flashggDiPhotonMVAMCScaleLowR9EEDown01sigma+process.flashggDiPhotonMVANewMCScaleLowR9EEDown01sigma+process.flashggDiPhotonMVAPUPPIMCScaleLowR9EEDown01sigma+process.flashggUnpackedJetsMCScaleLowR9EEDown01sigma+process.flashggUnpackedPuppiJetsMCScaleLowR9EEDown01sigma+process.flashggVBFMVAMCScaleLowR9EEDown01sigma+process.flashggVBFMVALegacyMCScaleLowR9EEDown01sigma+process.flashggVBFMVAPUPPIMCScaleLowR9EEDown01sigma+process.flashggVBFDiPhoDiJetMVAMCScaleLowR9EEDown01sigma+process.flashggVBFDiPhoDiJetMVALegacyMCScaleLowR9EEDown01sigma+process.flashggVBFDiPhoDiJetMVAPUPPIMCScaleLowR9EEDown01sigma+process.flashggUntaggedMCScaleLowR9EEDown01sigma+process.flashggVBFTagMCScaleLowR9EEDown01sigma+process.flashggTTHLeptonicTagMCScaleLowR9EEDown01sigma+process.flashggVHEtTagMCScaleLowR9EEDown01sigma+process.flashggTTHHadronicTagMCScaleLowR9EEDown01sigma+process.flashggVHLooseTagMCScaleLowR9EEDown01sigma+process.flashggVHTightTagMCScaleLowR9EEDown01sigma+process.flashggVHHadronicTagMCScaleLowR9EEDown01sigma+process.flashggTagSorterMCScaleLowR9EEDown01sigma)


process.flashggTagSequenceMCSmearHighR9EBPhiUp01sigma = cms.Sequence(process.flashggDiPhotonMVAMCSmearHighR9EBPhiUp01sigma+process.flashggDiPhotonMVANewMCSmearHighR9EBPhiUp01sigma+process.flashggDiPhotonMVAPUPPIMCSmearHighR9EBPhiUp01sigma+process.flashggUnpackedJetsMCSmearHighR9EBPhiUp01sigma+process.flashggUnpackedPuppiJetsMCSmearHighR9EBPhiUp01sigma+process.flashggVBFMVAMCSmearHighR9EBPhiUp01sigma+process.flashggVBFMVALegacyMCSmearHighR9EBPhiUp01sigma+process.flashggVBFMVAPUPPIMCSmearHighR9EBPhiUp01sigma+process.flashggVBFDiPhoDiJetMVAMCSmearHighR9EBPhiUp01sigma+process.flashggVBFDiPhoDiJetMVALegacyMCSmearHighR9EBPhiUp01sigma+process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearHighR9EBPhiUp01sigma+process.flashggUntaggedMCSmearHighR9EBPhiUp01sigma+process.flashggVBFTagMCSmearHighR9EBPhiUp01sigma+process.flashggTTHLeptonicTagMCSmearHighR9EBPhiUp01sigma+process.flashggVHEtTagMCSmearHighR9EBPhiUp01sigma+process.flashggTTHHadronicTagMCSmearHighR9EBPhiUp01sigma+process.flashggVHLooseTagMCSmearHighR9EBPhiUp01sigma+process.flashggVHTightTagMCSmearHighR9EBPhiUp01sigma+process.flashggVHHadronicTagMCSmearHighR9EBPhiUp01sigma+process.flashggTagSorterMCSmearHighR9EBPhiUp01sigma)


process.flashggTagSequenceMCScaleHighR9EEDown01sigma = cms.Sequence(process.flashggDiPhotonMVAMCScaleHighR9EEDown01sigma+process.flashggDiPhotonMVANewMCScaleHighR9EEDown01sigma+process.flashggDiPhotonMVAPUPPIMCScaleHighR9EEDown01sigma+process.flashggUnpackedJetsMCScaleHighR9EEDown01sigma+process.flashggUnpackedPuppiJetsMCScaleHighR9EEDown01sigma+process.flashggVBFMVAMCScaleHighR9EEDown01sigma+process.flashggVBFMVALegacyMCScaleHighR9EEDown01sigma+process.flashggVBFMVAPUPPIMCScaleHighR9EEDown01sigma+process.flashggVBFDiPhoDiJetMVAMCScaleHighR9EEDown01sigma+process.flashggVBFDiPhoDiJetMVALegacyMCScaleHighR9EEDown01sigma+process.flashggVBFDiPhoDiJetMVAPUPPIMCScaleHighR9EEDown01sigma+process.flashggUntaggedMCScaleHighR9EEDown01sigma+process.flashggVBFTagMCScaleHighR9EEDown01sigma+process.flashggTTHLeptonicTagMCScaleHighR9EEDown01sigma+process.flashggVHEtTagMCScaleHighR9EEDown01sigma+process.flashggTTHHadronicTagMCScaleHighR9EEDown01sigma+process.flashggVHLooseTagMCScaleHighR9EEDown01sigma+process.flashggVHTightTagMCScaleHighR9EEDown01sigma+process.flashggVHHadronicTagMCScaleHighR9EEDown01sigma+process.flashggTagSorterMCScaleHighR9EEDown01sigma)


process.flashggTagSequenceMCSmearLowR9EEDown01sigma = cms.Sequence(process.flashggDiPhotonMVAMCSmearLowR9EEDown01sigma+process.flashggDiPhotonMVANewMCSmearLowR9EEDown01sigma+process.flashggDiPhotonMVAPUPPIMCSmearLowR9EEDown01sigma+process.flashggUnpackedJetsMCSmearLowR9EEDown01sigma+process.flashggUnpackedPuppiJetsMCSmearLowR9EEDown01sigma+process.flashggVBFMVAMCSmearLowR9EEDown01sigma+process.flashggVBFMVALegacyMCSmearLowR9EEDown01sigma+process.flashggVBFMVAPUPPIMCSmearLowR9EEDown01sigma+process.flashggVBFDiPhoDiJetMVAMCSmearLowR9EEDown01sigma+process.flashggVBFDiPhoDiJetMVALegacyMCSmearLowR9EEDown01sigma+process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearLowR9EEDown01sigma+process.flashggUntaggedMCSmearLowR9EEDown01sigma+process.flashggVBFTagMCSmearLowR9EEDown01sigma+process.flashggTTHLeptonicTagMCSmearLowR9EEDown01sigma+process.flashggVHEtTagMCSmearLowR9EEDown01sigma+process.flashggTTHHadronicTagMCSmearLowR9EEDown01sigma+process.flashggVHLooseTagMCSmearLowR9EEDown01sigma+process.flashggVHTightTagMCSmearLowR9EEDown01sigma+process.flashggVHHadronicTagMCSmearLowR9EEDown01sigma+process.flashggTagSorterMCSmearLowR9EEDown01sigma)


process.flashggTagSequenceMCSmearHighR9EEUp01sigma = cms.Sequence(process.flashggDiPhotonMVAMCSmearHighR9EEUp01sigma+process.flashggDiPhotonMVANewMCSmearHighR9EEUp01sigma+process.flashggDiPhotonMVAPUPPIMCSmearHighR9EEUp01sigma+process.flashggUnpackedJetsMCSmearHighR9EEUp01sigma+process.flashggUnpackedPuppiJetsMCSmearHighR9EEUp01sigma+process.flashggVBFMVAMCSmearHighR9EEUp01sigma+process.flashggVBFMVALegacyMCSmearHighR9EEUp01sigma+process.flashggVBFMVAPUPPIMCSmearHighR9EEUp01sigma+process.flashggVBFDiPhoDiJetMVAMCSmearHighR9EEUp01sigma+process.flashggVBFDiPhoDiJetMVALegacyMCSmearHighR9EEUp01sigma+process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearHighR9EEUp01sigma+process.flashggUntaggedMCSmearHighR9EEUp01sigma+process.flashggVBFTagMCSmearHighR9EEUp01sigma+process.flashggTTHLeptonicTagMCSmearHighR9EEUp01sigma+process.flashggVHEtTagMCSmearHighR9EEUp01sigma+process.flashggTTHHadronicTagMCSmearHighR9EEUp01sigma+process.flashggVHLooseTagMCSmearHighR9EEUp01sigma+process.flashggVHTightTagMCSmearHighR9EEUp01sigma+process.flashggVHHadronicTagMCSmearHighR9EEUp01sigma+process.flashggTagSorterMCSmearHighR9EEUp01sigma)


process.flashggTagSequenceMCScaleLowR9EEUp01sigma = cms.Sequence(process.flashggDiPhotonMVAMCScaleLowR9EEUp01sigma+process.flashggDiPhotonMVANewMCScaleLowR9EEUp01sigma+process.flashggDiPhotonMVAPUPPIMCScaleLowR9EEUp01sigma+process.flashggUnpackedJetsMCScaleLowR9EEUp01sigma+process.flashggUnpackedPuppiJetsMCScaleLowR9EEUp01sigma+process.flashggVBFMVAMCScaleLowR9EEUp01sigma+process.flashggVBFMVALegacyMCScaleLowR9EEUp01sigma+process.flashggVBFMVAPUPPIMCScaleLowR9EEUp01sigma+process.flashggVBFDiPhoDiJetMVAMCScaleLowR9EEUp01sigma+process.flashggVBFDiPhoDiJetMVALegacyMCScaleLowR9EEUp01sigma+process.flashggVBFDiPhoDiJetMVAPUPPIMCScaleLowR9EEUp01sigma+process.flashggUntaggedMCScaleLowR9EEUp01sigma+process.flashggVBFTagMCScaleLowR9EEUp01sigma+process.flashggTTHLeptonicTagMCScaleLowR9EEUp01sigma+process.flashggVHEtTagMCScaleLowR9EEUp01sigma+process.flashggTTHHadronicTagMCScaleLowR9EEUp01sigma+process.flashggVHLooseTagMCScaleLowR9EEUp01sigma+process.flashggVHTightTagMCScaleLowR9EEUp01sigma+process.flashggVHHadronicTagMCScaleLowR9EEUp01sigma+process.flashggTagSorterMCScaleLowR9EEUp01sigma)


process.flashggTagSequenceMCSmearHighR9EBPhiDown01sigma = cms.Sequence(process.flashggDiPhotonMVAMCSmearHighR9EBPhiDown01sigma+process.flashggDiPhotonMVANewMCSmearHighR9EBPhiDown01sigma+process.flashggDiPhotonMVAPUPPIMCSmearHighR9EBPhiDown01sigma+process.flashggUnpackedJetsMCSmearHighR9EBPhiDown01sigma+process.flashggUnpackedPuppiJetsMCSmearHighR9EBPhiDown01sigma+process.flashggVBFMVAMCSmearHighR9EBPhiDown01sigma+process.flashggVBFMVALegacyMCSmearHighR9EBPhiDown01sigma+process.flashggVBFMVAPUPPIMCSmearHighR9EBPhiDown01sigma+process.flashggVBFDiPhoDiJetMVAMCSmearHighR9EBPhiDown01sigma+process.flashggVBFDiPhoDiJetMVALegacyMCSmearHighR9EBPhiDown01sigma+process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearHighR9EBPhiDown01sigma+process.flashggUntaggedMCSmearHighR9EBPhiDown01sigma+process.flashggVBFTagMCSmearHighR9EBPhiDown01sigma+process.flashggTTHLeptonicTagMCSmearHighR9EBPhiDown01sigma+process.flashggVHEtTagMCSmearHighR9EBPhiDown01sigma+process.flashggTTHHadronicTagMCSmearHighR9EBPhiDown01sigma+process.flashggVHLooseTagMCSmearHighR9EBPhiDown01sigma+process.flashggVHTightTagMCSmearHighR9EBPhiDown01sigma+process.flashggVHHadronicTagMCSmearHighR9EBPhiDown01sigma+process.flashggTagSorterMCSmearHighR9EBPhiDown01sigma)


process.flashggTagSequenceMCSmearLowR9EBRhoDown01sigma = cms.Sequence(process.flashggDiPhotonMVAMCSmearLowR9EBRhoDown01sigma+process.flashggDiPhotonMVANewMCSmearLowR9EBRhoDown01sigma+process.flashggDiPhotonMVAPUPPIMCSmearLowR9EBRhoDown01sigma+process.flashggUnpackedJetsMCSmearLowR9EBRhoDown01sigma+process.flashggUnpackedPuppiJetsMCSmearLowR9EBRhoDown01sigma+process.flashggVBFMVAMCSmearLowR9EBRhoDown01sigma+process.flashggVBFMVALegacyMCSmearLowR9EBRhoDown01sigma+process.flashggVBFMVAPUPPIMCSmearLowR9EBRhoDown01sigma+process.flashggVBFDiPhoDiJetMVAMCSmearLowR9EBRhoDown01sigma+process.flashggVBFDiPhoDiJetMVALegacyMCSmearLowR9EBRhoDown01sigma+process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearLowR9EBRhoDown01sigma+process.flashggUntaggedMCSmearLowR9EBRhoDown01sigma+process.flashggVBFTagMCSmearLowR9EBRhoDown01sigma+process.flashggTTHLeptonicTagMCSmearLowR9EBRhoDown01sigma+process.flashggVHEtTagMCSmearLowR9EBRhoDown01sigma+process.flashggTTHHadronicTagMCSmearLowR9EBRhoDown01sigma+process.flashggVHLooseTagMCSmearLowR9EBRhoDown01sigma+process.flashggVHTightTagMCSmearLowR9EBRhoDown01sigma+process.flashggVHHadronicTagMCSmearLowR9EBRhoDown01sigma+process.flashggTagSorterMCSmearLowR9EBRhoDown01sigma)


process.flashggTagSequenceMCSmearHighR9EBRhoUp01sigma = cms.Sequence(process.flashggDiPhotonMVAMCSmearHighR9EBRhoUp01sigma+process.flashggDiPhotonMVANewMCSmearHighR9EBRhoUp01sigma+process.flashggDiPhotonMVAPUPPIMCSmearHighR9EBRhoUp01sigma+process.flashggUnpackedJetsMCSmearHighR9EBRhoUp01sigma+process.flashggUnpackedPuppiJetsMCSmearHighR9EBRhoUp01sigma+process.flashggVBFMVAMCSmearHighR9EBRhoUp01sigma+process.flashggVBFMVALegacyMCSmearHighR9EBRhoUp01sigma+process.flashggVBFMVAPUPPIMCSmearHighR9EBRhoUp01sigma+process.flashggVBFDiPhoDiJetMVAMCSmearHighR9EBRhoUp01sigma+process.flashggVBFDiPhoDiJetMVALegacyMCSmearHighR9EBRhoUp01sigma+process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearHighR9EBRhoUp01sigma+process.flashggUntaggedMCSmearHighR9EBRhoUp01sigma+process.flashggVBFTagMCSmearHighR9EBRhoUp01sigma+process.flashggTTHLeptonicTagMCSmearHighR9EBRhoUp01sigma+process.flashggVHEtTagMCSmearHighR9EBRhoUp01sigma+process.flashggTTHHadronicTagMCSmearHighR9EBRhoUp01sigma+process.flashggVHLooseTagMCSmearHighR9EBRhoUp01sigma+process.flashggVHTightTagMCSmearHighR9EBRhoUp01sigma+process.flashggVHHadronicTagMCSmearHighR9EBRhoUp01sigma+process.flashggTagSorterMCSmearHighR9EBRhoUp01sigma)


process.flashggTagSequenceMCSmearLowR9EBPhiDown01sigma = cms.Sequence(process.flashggDiPhotonMVAMCSmearLowR9EBPhiDown01sigma+process.flashggDiPhotonMVANewMCSmearLowR9EBPhiDown01sigma+process.flashggDiPhotonMVAPUPPIMCSmearLowR9EBPhiDown01sigma+process.flashggUnpackedJetsMCSmearLowR9EBPhiDown01sigma+process.flashggUnpackedPuppiJetsMCSmearLowR9EBPhiDown01sigma+process.flashggVBFMVAMCSmearLowR9EBPhiDown01sigma+process.flashggVBFMVALegacyMCSmearLowR9EBPhiDown01sigma+process.flashggVBFMVAPUPPIMCSmearLowR9EBPhiDown01sigma+process.flashggVBFDiPhoDiJetMVAMCSmearLowR9EBPhiDown01sigma+process.flashggVBFDiPhoDiJetMVALegacyMCSmearLowR9EBPhiDown01sigma+process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearLowR9EBPhiDown01sigma+process.flashggUntaggedMCSmearLowR9EBPhiDown01sigma+process.flashggVBFTagMCSmearLowR9EBPhiDown01sigma+process.flashggTTHLeptonicTagMCSmearLowR9EBPhiDown01sigma+process.flashggVHEtTagMCSmearLowR9EBPhiDown01sigma+process.flashggTTHHadronicTagMCSmearLowR9EBPhiDown01sigma+process.flashggVHLooseTagMCSmearLowR9EBPhiDown01sigma+process.flashggVHTightTagMCSmearLowR9EBPhiDown01sigma+process.flashggVHHadronicTagMCSmearLowR9EBPhiDown01sigma+process.flashggTagSorterMCSmearLowR9EBPhiDown01sigma)


process.flashggTagSequenceMCSmearHighR9EEDown01sigma = cms.Sequence(process.flashggDiPhotonMVAMCSmearHighR9EEDown01sigma+process.flashggDiPhotonMVANewMCSmearHighR9EEDown01sigma+process.flashggDiPhotonMVAPUPPIMCSmearHighR9EEDown01sigma+process.flashggUnpackedJetsMCSmearHighR9EEDown01sigma+process.flashggUnpackedPuppiJetsMCSmearHighR9EEDown01sigma+process.flashggVBFMVAMCSmearHighR9EEDown01sigma+process.flashggVBFMVALegacyMCSmearHighR9EEDown01sigma+process.flashggVBFMVAPUPPIMCSmearHighR9EEDown01sigma+process.flashggVBFDiPhoDiJetMVAMCSmearHighR9EEDown01sigma+process.flashggVBFDiPhoDiJetMVALegacyMCSmearHighR9EEDown01sigma+process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearHighR9EEDown01sigma+process.flashggUntaggedMCSmearHighR9EEDown01sigma+process.flashggVBFTagMCSmearHighR9EEDown01sigma+process.flashggTTHLeptonicTagMCSmearHighR9EEDown01sigma+process.flashggVHEtTagMCSmearHighR9EEDown01sigma+process.flashggTTHHadronicTagMCSmearHighR9EEDown01sigma+process.flashggVHLooseTagMCSmearHighR9EEDown01sigma+process.flashggVHTightTagMCSmearHighR9EEDown01sigma+process.flashggVHHadronicTagMCSmearHighR9EEDown01sigma+process.flashggTagSorterMCSmearHighR9EEDown01sigma)


process.flashggTagSequenceMCScaleHighR9EEUp01sigma = cms.Sequence(process.flashggDiPhotonMVAMCScaleHighR9EEUp01sigma+process.flashggDiPhotonMVANewMCScaleHighR9EEUp01sigma+process.flashggDiPhotonMVAPUPPIMCScaleHighR9EEUp01sigma+process.flashggUnpackedJetsMCScaleHighR9EEUp01sigma+process.flashggUnpackedPuppiJetsMCScaleHighR9EEUp01sigma+process.flashggVBFMVAMCScaleHighR9EEUp01sigma+process.flashggVBFMVALegacyMCScaleHighR9EEUp01sigma+process.flashggVBFMVAPUPPIMCScaleHighR9EEUp01sigma+process.flashggVBFDiPhoDiJetMVAMCScaleHighR9EEUp01sigma+process.flashggVBFDiPhoDiJetMVALegacyMCScaleHighR9EEUp01sigma+process.flashggVBFDiPhoDiJetMVAPUPPIMCScaleHighR9EEUp01sigma+process.flashggUntaggedMCScaleHighR9EEUp01sigma+process.flashggVBFTagMCScaleHighR9EEUp01sigma+process.flashggTTHLeptonicTagMCScaleHighR9EEUp01sigma+process.flashggVHEtTagMCScaleHighR9EEUp01sigma+process.flashggTTHHadronicTagMCScaleHighR9EEUp01sigma+process.flashggVHLooseTagMCScaleHighR9EEUp01sigma+process.flashggVHTightTagMCScaleHighR9EEUp01sigma+process.flashggVHHadronicTagMCScaleHighR9EEUp01sigma+process.flashggTagSorterMCScaleHighR9EEUp01sigma)


process.flashggTagSequenceMCSmearLowR9EEUp01sigma = cms.Sequence(process.flashggDiPhotonMVAMCSmearLowR9EEUp01sigma+process.flashggDiPhotonMVANewMCSmearLowR9EEUp01sigma+process.flashggDiPhotonMVAPUPPIMCSmearLowR9EEUp01sigma+process.flashggUnpackedJetsMCSmearLowR9EEUp01sigma+process.flashggUnpackedPuppiJetsMCSmearLowR9EEUp01sigma+process.flashggVBFMVAMCSmearLowR9EEUp01sigma+process.flashggVBFMVALegacyMCSmearLowR9EEUp01sigma+process.flashggVBFMVAPUPPIMCSmearLowR9EEUp01sigma+process.flashggVBFDiPhoDiJetMVAMCSmearLowR9EEUp01sigma+process.flashggVBFDiPhoDiJetMVALegacyMCSmearLowR9EEUp01sigma+process.flashggVBFDiPhoDiJetMVAPUPPIMCSmearLowR9EEUp01sigma+process.flashggUntaggedMCSmearLowR9EEUp01sigma+process.flashggVBFTagMCSmearLowR9EEUp01sigma+process.flashggTTHLeptonicTagMCSmearLowR9EEUp01sigma+process.flashggVHEtTagMCSmearLowR9EEUp01sigma+process.flashggTTHHadronicTagMCSmearLowR9EEUp01sigma+process.flashggVHLooseTagMCSmearLowR9EEUp01sigma+process.flashggVHTightTagMCSmearLowR9EEUp01sigma+process.flashggVHHadronicTagMCSmearLowR9EEUp01sigma+process.flashggTagSorterMCSmearLowR9EEUp01sigma)


process.systematicsTagSequences = cms.Sequence(process.flashggTagSequenceMCSmearHighR9EEUp01sigma+process.flashggTagSequenceMCSmearHighR9EBRhoUp01sigma+process.flashggTagSequenceMCSmearHighR9EBPhiUp01sigma+process.flashggTagSequenceMCScaleHighR9EBUp01sigma+process.flashggTagSequenceMCScaleHighR9EEUp01sigma+process.flashggTagSequenceMCSmearHighR9EEDown01sigma+process.flashggTagSequenceMCSmearHighR9EBRhoDown01sigma+process.flashggTagSequenceMCSmearHighR9EBPhiDown01sigma+process.flashggTagSequenceMCScaleHighR9EBDown01sigma+process.flashggTagSequenceMCScaleHighR9EEDown01sigma+process.flashggTagSequenceMCSmearLowR9EEUp01sigma+process.flashggTagSequenceMCSmearLowR9EBRhoUp01sigma+process.flashggTagSequenceMCSmearLowR9EBPhiUp01sigma+process.flashggTagSequenceMCScaleLowR9EBUp01sigma+process.flashggTagSequenceMCScaleLowR9EEUp01sigma+process.flashggTagSequenceMCSmearLowR9EEDown01sigma+process.flashggTagSequenceMCSmearLowR9EBRhoDown01sigma+process.flashggTagSequenceMCSmearLowR9EBPhiDown01sigma+process.flashggTagSequenceMCScaleLowR9EBDown01sigma+process.flashggTagSequenceMCScaleLowR9EEDown01sigma)


process.p = cms.Path(process.flashggDiPhotonSystematics+process.flashggMuonSystematics+process.flashggElectronSystematics+process.flashggTagSequence+process.systematicsTagSequences+process.flashggSystTagMerger+process.tagsDumper)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(10)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring('warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    flashggDiPhotonSystematics = cms.PSet(
        initialSeed = cms.untracked.uint32(664)
    ),
    flashggElectronSystematics = cms.PSet(
        initialSeed = cms.untracked.uint32(11)
    ),
    flashggMuonSystematics = cms.PSet(
        initialSeed = cms.untracked.uint32(13)
    )
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('test.root')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring('HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER')
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.CastorDbProducer = cms.ESProducer("CastorDbProducer")


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.MuonNumberingInitialization = cms.ESProducer("MuonNumberingInitialization")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.XMLFromDBSource = cms.ESProducer("XMLIdealGeometryESProducer",
    label = cms.string('Extended'),
    rootDDName = cms.string('cms:OCMS')
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    appendToDataLabel = cms.string(''),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False),
    trackerGeometryConstants = cms.PSet(
        BIG_PIX_PER_ROC_X = cms.int32(1),
        BIG_PIX_PER_ROC_Y = cms.int32(2),
        COLS_PER_ROC = cms.int32(52),
        ROCS_X = cms.int32(0),
        ROCS_Y = cms.int32(0),
        ROWS_PER_ROC = cms.int32(80),
        upgradeGeometry = cms.bool(False)
    )
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        ))
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(cms.PSet(
        Label = cms.untracked.string(''),
        NormalizationFactor = cms.untracked.double(1.0),
        Record = cms.string('SiStripApvGainRcd')
    ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiStripDetVOffRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False),
    trackerGeometryConstants = cms.PSet(
        BIG_PIX_PER_ROC_X = cms.int32(1),
        BIG_PIX_PER_ROC_Y = cms.int32(2),
        COLS_PER_ROC = cms.int32(52),
        ROCS_X = cms.int32(0),
        ROCS_Y = cms.int32(0),
        ROWS_PER_ROC = cms.int32(80),
        upgradeGeometry = cms.bool(False)
    )
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.trackerTopologyConstants = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string(''),
    pxb_ladderMask = cms.uint32(255),
    pxb_ladderStartBit = cms.uint32(8),
    pxb_layerMask = cms.uint32(15),
    pxb_layerStartBit = cms.uint32(16),
    pxb_moduleMask = cms.uint32(63),
    pxb_moduleStartBit = cms.uint32(2),
    pxf_bladeMask = cms.uint32(63),
    pxf_bladeStartBit = cms.uint32(10),
    pxf_diskMask = cms.uint32(15),
    pxf_diskStartBit = cms.uint32(16),
    pxf_moduleMask = cms.uint32(63),
    pxf_moduleStartBit = cms.uint32(2),
    pxf_panelMask = cms.uint32(3),
    pxf_panelStartBit = cms.uint32(8),
    pxf_sideMask = cms.uint32(3),
    pxf_sideStartBit = cms.uint32(23),
    tec_moduleMask = cms.uint32(7),
    tec_moduleStartBit = cms.uint32(2),
    tec_petalMask = cms.uint32(15),
    tec_petalStartBit = cms.uint32(8),
    tec_petal_fw_bwMask = cms.uint32(3),
    tec_petal_fw_bwStartBit = cms.uint32(12),
    tec_ringMask = cms.uint32(7),
    tec_ringStartBit = cms.uint32(5),
    tec_sideMask = cms.uint32(3),
    tec_sideStartBit = cms.uint32(18),
    tec_sterMask = cms.uint32(3),
    tec_sterStartBit = cms.uint32(0),
    tec_wheelMask = cms.uint32(15),
    tec_wheelStartBit = cms.uint32(14),
    tib_layerMask = cms.uint32(7),
    tib_layerStartBit = cms.uint32(14),
    tib_moduleMask = cms.uint32(3),
    tib_moduleStartBit = cms.uint32(2),
    tib_sterMask = cms.uint32(3),
    tib_sterStartBit = cms.uint32(0),
    tib_strMask = cms.uint32(63),
    tib_strStartBit = cms.uint32(4),
    tib_str_fw_bwMask = cms.uint32(3),
    tib_str_fw_bwStartBit = cms.uint32(12),
    tib_str_int_extMask = cms.uint32(3),
    tib_str_int_extStartBit = cms.uint32(10),
    tid_moduleMask = cms.uint32(31),
    tid_moduleStartBit = cms.uint32(2),
    tid_module_fw_bwMask = cms.uint32(3),
    tid_module_fw_bwStartBit = cms.uint32(7),
    tid_ringMask = cms.uint32(3),
    tid_ringStartBit = cms.uint32(9),
    tid_sideMask = cms.uint32(3),
    tid_sideStartBit = cms.uint32(13),
    tid_sterMask = cms.uint32(3),
    tid_sterStartBit = cms.uint32(0),
    tid_wheelMask = cms.uint32(3),
    tid_wheelStartBit = cms.uint32(11),
    tob_layerMask = cms.uint32(7),
    tob_layerStartBit = cms.uint32(14),
    tob_moduleMask = cms.uint32(7),
    tob_moduleStartBit = cms.uint32(2),
    tob_rodMask = cms.uint32(127),
    tob_rodStartBit = cms.uint32(5),
    tob_rod_fw_bwMask = cms.uint32(3),
    tob_rod_fw_bwStartBit = cms.uint32(12),
    tob_sterMask = cms.uint32(3),
    tob_sterStartBit = cms.uint32(0)
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService'),
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionRetrialPeriod = cms.untracked.int32(10),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        enableConnectionSharing = cms.untracked.bool(True),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0)
    ),
    connect = cms.string('frontier://FrontierProd/CMS_COND_31X_GLOBALTAG'),
    globaltag = cms.string('POSTLS170_V5::All'),
    toGet = cms.VPSet()
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HERecalibration = cms.bool(False),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalibration = cms.bool(False),
    HcalReLabel = cms.PSet(
        RelabelHits = cms.untracked.bool(False),
        RelabelRules = cms.untracked.PSet(
            CorrectPhi = cms.untracked.bool(False),
            Eta1 = cms.untracked.vint32(1, 2, 2, 2, 3, 
                3, 3, 3, 3, 3, 
                3, 3, 3, 3, 3, 
                3, 3, 3, 3),
            Eta16 = cms.untracked.vint32(1, 1, 2, 2, 2, 
                2, 2, 2, 2, 3, 
                3, 3, 3, 3, 3, 
                3, 3, 3, 3),
            Eta17 = cms.untracked.vint32(1, 1, 2, 2, 3, 
                3, 3, 4, 4, 4, 
                4, 4, 5, 5, 5, 
                5, 5, 5, 5)
        )
    ),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    ),
    iLumi = cms.double(-1.0),
    toGet = cms.untracked.vstring('GainWidths')
)


process.prefer("es_hardcode")

process.CondDBSetup = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionRetrialPeriod = cms.untracked.int32(10),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        enableConnectionSharing = cms.untracked.bool(True),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0)
    )
)

process.HcalReLabel = cms.PSet(
    RelabelHits = cms.untracked.bool(False),
    RelabelRules = cms.untracked.PSet(
        CorrectPhi = cms.untracked.bool(False),
        Eta1 = cms.untracked.vint32(1, 2, 2, 2, 3, 
            3, 3, 3, 3, 3, 
            3, 3, 3, 3, 3, 
            3, 3, 3, 3),
        Eta16 = cms.untracked.vint32(1, 1, 2, 2, 2, 
            2, 2, 2, 2, 3, 
            3, 3, 3, 3, 3, 
            3, 3, 3, 3),
        Eta17 = cms.untracked.vint32(1, 1, 2, 2, 3, 
            3, 3, 4, 4, 4, 
            4, 4, 5, 5, 5, 
            5, 5, 5, 5)
    )
)

process.binInfo = cms.PSet(
    bins = cms.VPSet(cms.PSet(
        lowBounds = cms.vdouble(1.0),
        uncertainties = cms.vdouble(0.05, 0.3),
        upBounds = cms.vdouble(25.0),
        values = cms.vdouble(0.8)
    ), 
        cms.PSet(
            lowBounds = cms.vdouble(25.0),
            uncertainties = cms.vdouble(0.05, 0.3),
            upBounds = cms.vdouble(100.0),
            values = cms.vdouble(0.9)
        ), 
        cms.PSet(
            lowBounds = cms.vdouble(100.0),
            uncertainties = cms.vdouble(0.05, 0.3),
            upBounds = cms.vdouble(300.0),
            values = cms.vdouble(0.95)
        )),
    variables = cms.vstring('pt')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

process.scaleBins = cms.PSet(
    bins = cms.VPSet(cms.PSet(
        lowBounds = cms.vdouble(0.0, 0.94),
        uncertainties = cms.vdouble(0.0005),
        upBounds = cms.vdouble(1.0, 999.0),
        values = cms.vdouble(0.0)
    ), 
        cms.PSet(
            lowBounds = cms.vdouble(0.0, -999.0),
            uncertainties = cms.vdouble(0.0005),
            upBounds = cms.vdouble(1.0, 0.94),
            values = cms.vdouble(0.0)
        ), 
        cms.PSet(
            lowBounds = cms.vdouble(1.0, 0.94),
            uncertainties = cms.vdouble(0.0006),
            upBounds = cms.vdouble(1.5, 999.0),
            values = cms.vdouble(0.0)
        ), 
        cms.PSet(
            lowBounds = cms.vdouble(1.0, -999.0),
            uncertainties = cms.vdouble(0.0012),
            upBounds = cms.vdouble(1.5, 0.94),
            values = cms.vdouble(0.0)
        ), 
        cms.PSet(
            lowBounds = cms.vdouble(1.5, -999.0),
            uncertainties = cms.vdouble(0.002),
            upBounds = cms.vdouble(2.0, 0.94),
            values = cms.vdouble(0.0)
        ), 
        cms.PSet(
            lowBounds = cms.vdouble(1.5, 0.94),
            uncertainties = cms.vdouble(0.003),
            upBounds = cms.vdouble(2.0, 999.0),
            values = cms.vdouble(0.0)
        ), 
        cms.PSet(
            lowBounds = cms.vdouble(2.0, -999.0),
            uncertainties = cms.vdouble(0.002),
            upBounds = cms.vdouble(3.0, 0.94),
            values = cms.vdouble(0.0)
        ), 
        cms.PSet(
            lowBounds = cms.vdouble(2.0, 0.94),
            uncertainties = cms.vdouble(0.003),
            upBounds = cms.vdouble(3.0, 999.0),
            values = cms.vdouble(0.0)
        )),
    variables = cms.vstring('abs(superCluster.eta)', 
        'r9')
)

process.smearBins = cms.PSet(
    bins = cms.VPSet(cms.PSet(
        lowBounds = cms.vdouble(0.0, -999.0),
        uncertainties = cms.vdouble(0.00063, 0.16),
        upBounds = cms.vdouble(1.0, 0.94),
        values = cms.vdouble(0.0077, 0.0, 6.73)
    ), 
        cms.PSet(
            lowBounds = cms.vdouble(0.0, 0.94),
            uncertainties = cms.vdouble(0.00065, 0.16),
            upBounds = cms.vdouble(1.0, 999.0),
            values = cms.vdouble(0.0074, 0.0, 6.6)
        ), 
        cms.PSet(
            lowBounds = cms.vdouble(1.0, -999.0),
            uncertainties = cms.vdouble(0.00103, 0.07),
            upBounds = cms.vdouble(1.5, 0.94),
            values = cms.vdouble(0.0126, 0.0, 6.73)
        ), 
        cms.PSet(
            lowBounds = cms.vdouble(1.0, 0.94),
            uncertainties = cms.vdouble(0.00132, 0.22),
            upBounds = cms.vdouble(1.5, 999.0),
            values = cms.vdouble(0.0112, 0.0, 6.52)
        ), 
        cms.PSet(
            lowBounds = cms.vdouble(1.5, -999.0),
            uncertainties = cms.vdouble(0.00303),
            upBounds = cms.vdouble(2.0, 0.94),
            values = cms.vdouble(0.0198)
        ), 
        cms.PSet(
            lowBounds = cms.vdouble(1.5, 0.94),
            uncertainties = cms.vdouble(0.00122),
            upBounds = cms.vdouble(2.0, 999.0),
            values = cms.vdouble(0.0163)
        ), 
        cms.PSet(
            lowBounds = cms.vdouble(2.0, -999.0),
            uncertainties = cms.vdouble(0.00092),
            upBounds = cms.vdouble(3.0, 0.94),
            values = cms.vdouble(0.0192)
        ), 
        cms.PSet(
            lowBounds = cms.vdouble(2.0, 0.94),
            uncertainties = cms.vdouble(0.00078),
            upBounds = cms.vdouble(3.0, 999.0),
            values = cms.vdouble(0.0186)
        )),
    variables = cms.vstring('abs(superCluster.eta)', 
        'r9')
)

process.tagsDumpConfig = cms.PSet(
    cat