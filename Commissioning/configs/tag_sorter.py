import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils

process = cms.Process("FLASHggMicroAOD")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'POSTLS170_V5::All'

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32( 100) )
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 1 )

<<<<<<< HEAD
#process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/cmst3/user/gpetrucc/miniAOD/v1/GluGluToHToGG_M-125_13TeV-powheg-pythia6_Flat20to50_PAT.root"))
process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/mc/Spring14miniaod/TTbarH_HToGG_M-125_13TeV_amcatnlo-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/049C0F9C-E61E-E411-9388-D8D385AE8466.root"))
=======
process.source = cms.Source("PoolSource",
#fileNames=cms.untracked.vstring("/store/cmst3/user/gpetrucc/miniAOD/v1/GluGluToHToGG_M-125_13TeV-powheg-pythia6_Flat20to50_PAT.root")
fileNames=cms.untracked.vstring("file:/afs/cern.ch/work/l/lcorpe/private/FLASHgg/CMSSW_7_0_7_patch1/src/flashgg/CE926731-9607-E411-B0BA-001E67248A1B.root")
)
>>>>>>> b944880a6bfc7eb6894ca611f28e85ca174ca0ec


process.load("flashgg/MicroAODProducers/flashggVertexMaps_cfi")
process.load("flashgg/MicroAODProducers/flashggPhotons_cfi")
process.load("flashgg/MicroAODProducers/flashggDiPhotons_cfi")
process.load("flashgg/MicroAODProducers/flashggPreselectedDiPhotons_cfi")
process.load("flashgg/MicroAODProducers/flashggJets_cfi")
process.load("flashgg/MicroAODProducers/flashggElectrons_cfi")

#Tag stuff
process.load("flashgg/TagProducers/flashggDiPhotonMVA_cfi")
process.load("flashgg/TagProducers/flashggVBFMVA_cfi")
process.load("flashgg/TagProducers/flashggVBFDiPhoDiJetMVA_cfi")
process.load("flashgg/TagProducers/flashggTags_cfi")

process.flashggTagSorter = cms.EDProducer('FlashggTagSorter',
<<<<<<< HEAD
                                          DiPhotonTag = cms.untracked.InputTag('flashggDiPhotons'),
                                          TagVectorTag = cms.untracked.VInputTag(
        								cms.untracked.InputTag('flashggTTHleptonicTag'),
                                                                        cms.untracked.InputTag('flashggTTHhadronicTag'),
        								cms.untracked.InputTag('flashggVBFTag'),
									cms.untracked.InputTag('flashggUntaggedCategory'),
                                                                        ),
                                          massCutUpper=cms.untracked.double(180.),
                                          massCutLower=cms.untracked.double(100)
                                          )
=======
		DiPhotonTag = cms.untracked.InputTag('flashggDiPhotons'),
		TagVectorTag = cms.untracked.VInputTag(
			cms.untracked.InputTag('flashggVBFTag'),
			cms.untracked.InputTag('flashggUntaggedCategory'),
			),
		massCutUpper=cms.untracked.double(180),
		massCutLower=cms.untracked.double(100)

		)
>>>>>>> b944880a6bfc7eb6894ca611f28e85ca174ca0ec


process.TFileService = cms.Service("TFileService",fileName = cms.string("flashggTreeWithTags.root"))

process.flashggTreeMakerWithTagSorter = cms.EDAnalyzer('FlashggFlashggTreeMakerWithTagSorter',
		VertexTag=cms.untracked.InputTag('offlineSlimmedPrimaryVertices'),
		GenParticleTag=cms.untracked.InputTag('prunedGenParticles'),
		VertexCandidateMapTagDz=cms.InputTag('flashggVertexMapUnique'),
		VertexCandidateMapTagAOD = cms.InputTag('flashggVertexMapValidator'),
		JetTagDz = cms.InputTag("flashggJets"),
		DiPhotonTag = cms.untracked.InputTag('flashggDiPhotons'),
		METTag = cms.untracked.InputTag('slimmedMETs'),
		PileUpTag = cms.untracked.InputTag('addPileupInfo'),
		TagSorter = cms.untracked.InputTag('flashggTagSorter'),
		rhoFixedGridCollection = cms.InputTag('fixedGridRhoAll'),
		)



process.out = cms.OutputModule("PoolOutputModule", fileName = cms.untracked.string('myOutputFile.root'),
<<<<<<< HEAD
                               outputCommands = cms.untracked.vstring("drop *",
                                                                      "keep *_flashgg*_*_*",
                                                                      "drop *_flashggVertexMap*_*_*",
                                                                      "keep *_offlineSlimmedPrimaryVertices_*_*",
                                                                      "keep *_reducedEgamma_reduced*Clusters_*",
                                                                      "keep *_reducedEgamma_*PhotonCores_*",
                                                                      "keep *_slimmedElectrons_*_*",
                                                                      "keep *_slimmedMuons_*_*",
                                                                      "keep *_slimmedMETs_*_*",
                                                                      "keep *_slimmedTaus_*_*",
                                                                      "keep *_fixedGridRhoAll_*_*"
                                                                     )
#                               outputCommands = cms.untracked.vstring("keep *",
#                                                                     )
                               )
=======
		#   outputCommands = cms.untracked.vstring("drop *",
			#                                         "keep *_flashgg*_*_*",
			#                                        "drop *_flashggVertexMap*_*_*",
			#                                       "keep *_offlineSlimmedPrimaryVertices_*_*",
			#                                      "keep *_reducedEgamma_reduced*Clusters_*",
			#                                     "keep *_reducedEgamma_*PhotonCores_*",
			#                                    "keep *_slimmedElectrons_*_*",
			#                                   "keep *_slimmedMuons_*_*",
			#                                  "keep *_slimmedMETs_*_*",
			#                                 "keep *_slimmedTaus_*_*",
			#                                "keep *_fixedGridRhoAll_*_*"
			#                              )
		outputCommands = cms.untracked.vstring("keep *",
			)
		)
>>>>>>> b944880a6bfc7eb6894ca611f28e85ca174ca0ec

process.commissioning = cms.EDAnalyzer('flashggCommissioning',
		PhotonTag=cms.untracked.InputTag('flashggPhotons'),
		DiPhotonTag = cms.untracked.InputTag('flashggDiPhotons'),
		VertexTag=cms.untracked.InputTag('offlineSlimmedPrimaryVertices')
		)

process.TFileService = cms.Service("TFileService",
		fileName = cms.string("tree.root")
		)

process.p = cms.Path(process.flashggVertexMapUnique*
<<<<<<< HEAD
                     process.flashggVertexMapNonUnique*
                     process.flashggPhotons*
                     process.flashggDiPhotons*
                     process.flashggPreselectedDiPhotons*
                     (process.flashggDiPhotonMVA+process.flashggJets+process.flashggElectrons)*
                     (process.flashggVBFMVA)* # Needs to happen after Jets
                     (process.flashggVBFDiPhoDiJetMVA)* # Needs to happen after VBF MVA and DiPho MVA

                     # Tag producers, once written, can run in parallel, so they go in here with +
                     (process.flashggUntaggedCategory+process.flashggVBFTag+process.flashggTTHleptonicTag+process.flashggTTHhadronicTag)*

                     process.flashggTagSorter*
                     process.flashggTreeMakerWithTagSorter
                    )
=======
		process.flashggVertexMapNonUnique*
		process.flashggPhotons*
		process.flashggDiPhotons*
		process.flashggPreselectedDiPhotons*
		(process.flashggDiPhotonMVA+process.flashggJets)* # These two could run in parallel, so use +
		process.flashggUntaggedCategory*
		(process.flashggVBFMVA)* # Needs to happen after Jets
		(process.flashggVBFDiPhoDiJetMVA)* # Needs to happen after VBF MVA and DiPho MVA
		(process.flashggVBFTag)* # Tag producers, once written, can run in parallel, so they go in here with +
		process.flashggTagSorter*
		process.flashggTreeMakerWithTagSorter
		#process.commissioning*
		)
>>>>>>> b944880a6bfc7eb6894ca611f28e85ca174ca0ec

process.e = cms.EndPath(process.out)
