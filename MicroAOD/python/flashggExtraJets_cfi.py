# y. haddad Imperial College
# this is based on the jet 74X recipe for jet re-clustering
# twiki source : https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2015#Advanced_topics_re_clustering_ev

import FWCore.ParameterSet.Config as cms
from RecoJets.JetProducers.PileupJetIDParams_cfi import cutbased_new as pu_jetid
from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection
from flashgg.MicroAOD.flashggJets_cfi import flashggBTag



def addFlashggPF(process, label='', doQGTagging = True):
  print 'addFlashggPF .... '
  postfix = 'postfix' + label
  
  from RecoJets.JetProducers.ak4PFJets_cfi  import ak4PFJets
  print ':: process ==', process
  # process.ak4PFJets  = ak4PFJets.clone (src = 'packedPFCandidates', doAreaFastjet = True)
  setattr(process, 'ak4PFJets' + postfix, ak4PFJets.clone (src = 'packedPFCandidates', doAreaFastjet = True))
  # cluster the jets
  print ':: 1'
  
  addJetCollection(
    process,
    postfix            = postfix,
    labelName          = 'AK4PF' ,
    jetSource          = cms.InputTag('ak4PFJets'+postfix),
    pvSource           = cms.InputTag('offlineSlimmedPrimaryVertices'),
    pfCandidates       = cms.InputTag('packedPFCandidates'),
    svSource           = cms.InputTag('slimmedSecondaryVertices'),
    btagDiscriminators = [ flashggBTag ],
    jetCorrections     = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None'),
    genJetCollection   = cms.InputTag('slimmedGenJets'),
    genParticles       = cms.InputTag('prunedGenParticles'),
    algo = 'AK', rParam = 0.4
  )
  print ':: 2'
  # adjust PV used for Jet Corrections
  # getattr(process, 'patJetCorrFactors'+_labelName+postfix)
  getattr(process, 'patJetCorrFactorsAK4PF' + postfix).primaryVertices = "offlineSlimmedPrimaryVertices"
  #process.patJetCorrFactorsAK4PF.primaryVertices = "offlineSlimmedPrimaryVertices"
  print ' --> patJetCorrFactorsAK4PF == ',  getattr(process, 'patJetCorrFactorsAK4PF' + postfix)
  print ' --> patJetsAK4PF           == ',  getattr(process, 'patJetsAK4PF' + postfix)
  flashggJetsPF = cms.EDProducer('FlashggJetProducer',
                                 DiPhotonTag=cms.InputTag('flashggDiPhotons'),
                                 VertexTag=cms.InputTag('offlineSlimmedPrimaryVertices'),
                                 JetTag=cms.InputTag('patJetsAK4PF' + postfix ),
                                 VertexCandidateMapTag = cms.InputTag("flashggVertexMapForCHS"),
                                 PileupJetIdParameters=cms.PSet(pu_jetid),
                               )
  print ':: 4'
  setattr(process, 'flashggJetsPF' + postfix, flashggJetsPF)
  print ':: 5'
  if doQGTagging:
    from RecoJets.JetProducers.QGTagger_cfi import QGTagger
    # QGTaggerPF     =  QGTagger.clone( srcJets   = 'flashggJetsPF' ,jetsLabel = 'QGL_AK4PF')
    setattr(process, 'QGTaggerPF' + postfix, QGTagger.clone( srcJets   = 'flashggJetsPF' + postfix ,jetsLabel = 'QGL_AK4PF'))
    
    
  return getattr(process, 'flashggJetsPF' + postfix)  


#def addFlashggPFCHS0(process, doQGTagging = True):
#  print "JET PRODUCER :: Flashgg PFCHS producer ::"
#  
#  # leptons to remove as per default CHS workflow
#  # select the isolated leptons : electrons + muons
#  process.selectedMuons     = cms.EDFilter("CandPtrSelector", 
#                                           src = cms.InputTag("slimmedMuons"), 
#                                           cut = cms.string('''abs(eta)<2.5 && pt>10. &&
#                                           (pfIsolationR04().sumChargedHadronPt+
#                                           max(0.,pfIsolationR04().sumNeutralHadronEt+
#                                           pfIsolationR04().sumPhotonEt-
#                                           0.50*pfIsolationR04().sumPUPt))/pt < 0.20 && 
#                                           (isPFMuon && (isGlobalMuon || isTrackerMuon) )'''))
#  
#  process.selectedElectrons = cms.EDFilter("CandPtrSelector", 
#                                           src = cms.InputTag("slimmedElectrons"), 
#                                           cut = cms.string('''abs(eta)<2.5 && pt>20. &&
#                                           gsfTrack.isAvailable() &&
#                                           gsfTrack.hitPattern().numberOfLostHits(\'MISSING_INNER_HITS\') < 2 &&
#                                           (pfIsolationVariables().sumChargedHadronPt+
#                                           max(0.,pfIsolationVariables().sumNeutralHadronEt+
#                                           pfIsolationVariables().sumPhotonEt-
#                                           0.5*pfIsolationVariables().sumPUPt))/pt < 0.15'''))
#  
#  # Simple producer which just removes the Candidates which
#  # don't come from the legacy vertex according to the Flashgg Vertex Map
#  process.flashggCHSLegacyVertexCandidates = cms.EDProducer('FlashggCHSLegacyVertexCandidateProducer',
#                                                            PFCandidatesTag       = cms.InputTag('packedPFCandidates'),
#                                                            DiPhotonTag           = cms.InputTag('flashggDiPhotons'),
#                                                            VertexCandidateMapTag = cms.InputTag("flashggVertexMapForCHS"),
#                                                            VertexTag = cms.InputTag('offlineSlimmedPrimaryVertices')
#                                                          )
#  
#  process.pfCHS0 = cms.EDFilter("CandPtrSelector", 
#                                src = cms.InputTag("flashggCHSLegacyVertexCandidates"), 
#                                cut = cms.string(""))
#  
#  # then remove the previously selected muons
#  process.pfNoMuonCHS0      = cms.EDProducer("CandPtrProjector", 
#                                             src  = cms.InputTag("pfCHS0"), 
#                                             veto = cms.InputTag("selectedMuons"))
#  # then remove the previously selected electrons
#  process.pfNoElectronsCHS0 = cms.EDProducer("CandPtrProjector", 
#                                             src  = cms.InputTag("pfNoMuonCHS0"), 
#                                             veto = cms.InputTag("selectedElectrons"))
#  
#  #Import RECO jet producer for ak4 PF and GEN jet
#  from RecoJets.JetProducers.ak4PFJets_cfi  import ak4PFJets
#  process.ak4PFJetsCHS0 = ak4PFJets.clone ( src = 'pfNoElectronsCHS0', doAreaFastjet = True)
#  
#  # NOTE : these line are from the new Jet recipe 
#  # The following is make patJets, but EI is done with the above
#  process.load("Configuration.StandardProcesss.MagneticField_cff")
#  process.load("Configuration.Geometry.GeometryRecoDB_cff")
#  process.load("Configuration.StandardProcesss.FrontierConditions_GlobalTag_cff")
#  
#  
#  
#  # cluster the jets
#  # NOTE: this is the 74X recipe for the jet clustering 
#  addJetCollection(
#    process,
#    labelName      = 'AK4PFCHS0',
#    jetSource      = cms.InputTag('ak4PFJetsCHS0'),
#    pvSource       = cms.InputTag('offlineSlimmedPrimaryVertices'),
#    pfCandidates   = cms.InputTag('packedPFCandidates'),
#    svSource       = cms.InputTag('slimmedSecondaryVertices'),
#    btagDiscriminators =  [ flashggBTag ],
#    jetCorrections = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None'),
#    
#    genParticles     = cms.InputTag('prunedGenParticles'),
#    genJetCollection = cms.InputTag('slimmedGenJets'),
#    # jet param
#    algo = 'AK', rParam = 0.4
#    )
#  
#  #adjust PV used for Jet Corrections
#  process.patJetCorrFactorsAK4PFCHS0.primaryVertices = "offlineSlimmedPrimaryVertices"
#  
#  if doQGTagging:
#    process.load('RecoJets.JetProducers.QGTagger_cfi')
#    process.QGTaggerPFCHS0 =  process.QGTagger.clone( srcJets   = 'flashggJetsPFCHS0' ,jetsLabel = 'ak4PFJetsCHS')
#    
#    #process.QGTaggerPFCHS0.jec              = cms.InputTag('')# keept empty, because are already corrected
#    #process.QGTaggerPFCHS0.systematicsLabel = cms.string('')# Produce systematic smearings (not yet available, keep empty)
#    
#
#    
#  process.flashggJetsPFCHS0 = cms.EDProducer('FlashggJetProducer',
#                                             DiPhotonTag=cms.InputTag('flashggDiPhotons'),
#                                             VertexTag=cms.InputTag('offlineSlimmedPrimaryVertices'),
#                                             JetTag=cms.InputTag('patJetsAK4PFCHS0'),
#                                             VertexCandidateMapTag = cms.InputTag("flashggVertexMapForCHS"),
#                                             PileupJetIdParameters=cms.PSet(pu_jetid),
#                                           )
  
