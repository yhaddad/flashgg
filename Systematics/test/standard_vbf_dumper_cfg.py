#!/usr/bin/env cmsRun

#runOnZee = False
dumpJetSysTrees = 2

import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils
import FWCore.ParameterSet.VarParsing as VarParsing
import os
from flashgg.Systematics.SystematicDumperDefaultVariables import minimalVariables,minimalHistograms,minimalNonSignalVariables,systematicVariables

# ========================================================================
# SYSTEMATICS SECTION
process = cms.Process("FLASHggSyst")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")

from Configuration.AlCa.GlobalTag import GlobalTag
if os.environ["CMSSW_VERSION"].count("CMSSW_7_6"):
    process.GlobalTag.globaltag = '76X_mcRun2_asymptotic_v13'
else:
    process.GlobalTag.globaltag = '74X_mcRun2_asymptotic_v4'
    
process.maxEvents    = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 2000 )

from flashgg.Systematics.SystematicsCustomize import *
jetSystematicsInputTags = createStandardSystematicsProducers(process)

#=== Keep an extra category as 'would go elsewhere instead', ignore preselection
process.flashggVBFTag.Boundaries             = cms.vdouble(-2)
process.flashggVBFTag.SetArbitraryNonGoldMC  = cms.bool(False)
process.flashggVBFTag.DropNonGoldData        = cms.bool(False)
process.flashggVBFTag.RequireVBFPreselection = cms.bool(False)

modifyTagSequenceForSystematics(process,jetSystematicsInputTags,dumpJetSysTrees)

systlabels    = [""]
phosystlabels = []
jetsystlabels = []
elesystlabels = []
musystlabels  = []

#=== import flashgg customization to check if we have signal or background
from flashgg.MetaData.JobConfig import customize

#=== Register forwardJetRMSCut to be used from customize
customize.options.register('forwardJetRMSCut',
                           0.03,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.float,
                           'forwardJetRMSCut')

customize.options.register('runOnZee',
                           False,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'runOnZee')

customize.parse()
print " === customize.processId: ", customize.processId
print " === dumpJetSysTrees    : ", dumpJetSysTrees

#=== Only run systematics for signal events
from flashgg.Taggers.flashggTags_cff import UnpackedJetCollectionVInputTag
process.load("flashgg.Systematics.escales.escale76X_16DecRereco_2015")

#=== load the correctors
# process.load("JetMETCorrections.Configuration.JetCorrectors_cff")

if customize.processId == "Data":
    print "-----------------------------------------------------------------"
    print " Data, so turn of all shifts and systematics, with some exceptions"
    print "-----------------------------------------------------------------"
    variablesToUse = minimalNonSignalVariables
    customizeSystematicsForData(process)
else:
    print "-----------------------------------------------------------------"
    print " Background MC, so store mgg and central only"
    print "-----------------------------------------------------------------"
    variablesToUse = minimalNonSignalVariables
    if dumpJetSysTrees:
        print ":: Dumping Jet systematics"
        for direction in ["Up","Down"]:
            jetsystlabels.append("JEC%s01sigma" % direction)
            jetsystlabels.append("JER%s01sigma" % direction)
            jetsystlabels.append("RMSShift%s01sigma" % direction)
        systlabels += jetsystlabels
    else:
        print "Background MC, so store mgg and central only"
        customizeSystematicsForBackground(process)
        
            
print "--- Systematics  with independent collections ---"
print systlabels
print "-------------------------------------------------"
print "--- Variables to be dumped, including systematic weights ---"
print variablesToUse
print "------------------------------------------------------------"

cloneTagSequenceForEachSystematic(process,systlabels,
                                  phosystlabels,jetsystlabels,
                                  jetSystematicsInputTags, dumpJetSysTrees)

# ========================================================================
# Dumper section

from FWCore.ParameterSet.VarParsing import VarParsing
from flashgg.MetaData.samples_utils import SamplesManager

process.source = cms.Source ("PoolSource",
                             fileNames = cms.untracked.vstring(
                                 "root://eoscms.cern.ch//eos/cms//store/group/phys_higgs/cmshgg/ferriff/flashgg/RunIIFall15DR76-1_3_0-25ns_ext1/1_3_1/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15DR76-1_3_0-25ns_ext1-1_3_1-v0-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/160127_112132/0000/myMicroAODOutputFile_156.root"
                                 #"root://eoscms.cern.ch//eos/cms//store/group/phys_higgs/cmshgg/ferriff/flashgg/RunIIFall15DR76-1_3_0-25ns_ext1/1_3_1/DiPhotonJetsBox_MGG-80toInf_13TeV-Sherpa/RunIIFall15DR76-1_3_0-25ns_ext1-1_3_1-v0-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/160211_041113/0000/myMicroAODOutputFile_103.root"
                                 #"root://eoscms.cern.ch//eos/cms//store/group/phys_higgs/cmshgg/sethzenz/flashgg/RunIIFall15DR76-1_3_0-25ns/1_3_0/SingleElectron/RunIIFall15DR76-1_3_0-25ns-1_3_0-v0-Run2015C_25ns-16Dec2015-v1/160116_110208/0000/myMicroAODOutputFile_1.root"
                                 #"root://eoscms.cern.ch//eos/cms/store/group/phys_higgs/cmshgg/ferriff/flashgg/RunIIFall15DR76-1_3_0-25ns_ext1/1_3_1/VBFHToGG_M-130_13TeV_powheg_pythia8/RunIIFall15DR76-1_3_0-25ns_ext1-1_3_1-v0-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/160127_024307/0000/myMicroAODOutputFile_1.root"
                                 #"/store/group/phys_higgs/cmshgg/ferriff/flashgg/RunIIFall15DR76-1_3_0-25ns_ext1/1_3_1/SingleMuon/RunIIFall15DR76-1_3_0-25ns_ext1-1_3_1-v0-Run2015D-16Dec2015-v1/160214_075116/0000/myMicroAODOutputFile_971.root"
                                 #"/store/group/phys_higgs/cmshgg/ferriff/flashgg/RunIIFall15DR76-1_3_0-25ns_ext1/1_3_1/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15DR76-1_3_0-25ns_ext1-1_3_1-v0-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/160127_112132/0000/myMicroAODOutputFile_96.root"
                             ))

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("test.root"))

import flashgg.Taggers.dumperConfigTools as cfgTools
from   flashgg.Taggers.tagsDumpers_cfi   import createTagDumper

process.VBFTagDumper = createTagDumper("VBFTag")
process.VBFTagDumper.dumpTrees     = True
process.VBFTagDumper.dumpHistos    = True
process.VBFTagDumper.dumpWorkspace = False

if dumpJetSysTrees:
    process.VBFTagDumper.src = cms.InputTag("flashggSystTagMerger")
    
# Use JetID
process.flashggVBFMVA.UseJetID               = cms.bool(True)
process.flashggVBFMVA.JetIDLevel             = cms.string("Tight")
# VBF 
# process.flashggVBFTag.Boundaries             = cms.vdouble(-2)
# process.flashggVBFTag.SetArbitraryNonGoldMC  = cms.bool(False)
# process.flashggVBFTag.DropNonGoldData        = cms.bool(False)
# process.flashggVBFTag.RequireVBFPreselection = cms.bool(False)
# process.systematicsTagSequences              = cms.Sequence()

process.flashggVBFMVA.rmsforwardCut = cms.double(customize.forwardJetRMSCut)

print '------------------------------------------------------------'
print ' formward RMS Cut value ::' , customize.forwardJetRMSCut
print '------------------------------------------------------------'
print ' running on Zee         ::' , customize.runOnZee
print '------------------------------------------------------------'

# use custum TMVA weights
# process.flashggVBFMVA.vbfMVAweightfile = cms.FileInPath("flashgg/Taggers/data/TMVAClassification_dijetMVA_76x_17_02_15_BDTG.weights.xml")
# process.flashggVBFMVA.MVAMethod        = cms.string("BDTG")

# QCD Recovery 
# process.flashggVBFMVA.merge3rdJet   = cms.untracked.bool(False)
# process.flashggVBFMVA.thirdJetDRCut = cms.untracked.double(1.5)

# run on Drell-Yan 
if customize.runOnZee:
    process.flashggPreselectedDiPhotons.variables =  cms.vstring('pfPhoIso03', 
                                                                 'trkSumPtHollowConeDR03', 
                                                                 'full5x5_sigmaIetaIeta', 
                                                                 'full5x5_r9', 
                                                                 '1-passElectronVeto')
# get the variable list
if dumpJetSysTrees:
    for syst in jetsystlabels:
        print "jetsystlabels :: ", "flashggPreselectedDiPhotons%s"%syst
        getattr(process,"flashggPreselectedDiPhotons%s"%syst).variables = process.flashggPreselectedDiPhotons.variables
        
import flashgg.Taggers.VBFTagVariables as var
new_variables = [
    "n_jets           := VBFMVA.n_rec_jets",
    "dijet_jet1_RMS   := leading_rms",
    "dijet_jet2_RMS   := subLeading_rms",
    "dijet_jet1_match := leading_match",
    "dijet_jet2_match := subLeading_match",
    "dijet_jet1_QGL   := leading_QGL",
    "dijet_jet2_QGL   := subLeading_QGL"
]

matching_photon = [
    "prompt_pho_1   := diPhoton.leadingPhoton.genMatchType()",
    "prompt_pho_2   := diPhoton.subLeadingPhoton.genMatchType()"
]

all_variables = new_variables + var.dipho_variables + var.dijet_variables 
if customize.processId != "Data":
    all_variables += var.truth_variables + matching_photon
    

cats = []        
if dumpJetSysTrees :
    for syst in jetsystlabels:
        systcutstring = "hasSyst(\"%s\") " % syst
        cats += [("VBFDiJet_%s"%syst,"%s" % systcutstring,0)]#,
cats = [("VBFDiJet","1",0)]        


print "Dumper categories :: ", cats
cfgTools.addCategories(process.VBFTagDumper,
                       cats,
                       variables  = all_variables,
                       histograms = []
)
process.VBFTagDumper.nameTemplate = "$PROCESS_$SQRTS_$CLASSNAME_$SUBCAT_$LABEL"

customize.setDefault("maxEvents" ,  5000        ) # max-number of events
customize.setDefault("targetLumi",  1.00e+3  ) # define integrated lumi
customize(process)

from HLTrigger.HLTfilters.hltHighLevel_cfi import hltHighLevel

if customize.runOnZee:
    if customize.processId == "Data":
        process.hltHighLevel = hltHighLevel.clone(HLTPaths = cms.vstring("HLT_Ele27_eta2p1_WPLoose_Gsf_v*") )
    else:
        process.hltHighLevel = hltHighLevel.clone(HLTPaths = cms.vstring("HLT_Ele27_eta2p1_WP75_Gsf_v*") )
else:
    process.hltHighLevel= hltHighLevel.clone(
        HLTPaths = cms.vstring("HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v1",
                               "HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55_v1",
                               "HLT_Diphoton30EB_18EB_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55_v1"
        )
    )

process.options      = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

# ee bad supercluster filter on data
process.load('RecoMET.METFilters.eeBadScFilter_cfi')
process.eeBadScFilter.EERecHitSource = cms.InputTag("reducedEgamma","reducedEERecHits")

process.dataRequirements = cms.Sequence()
if customize.processId == "Data":
    process.dataRequirements += process.hltHighLevel
    process.dataRequirements += process.eeBadScFilter
    
# Split WH and ZH
process.genFilter = cms.Sequence()
if (customize.processId.count("wh") or customize.processId.count("zh")) and not customize.processId.count("wzh"):
    process.load("flashgg/Systematics/VHFilter_cfi")
    process.genFilter += process.VHFilter
    process.VHFilter.chooseW = bool(customize.processId.count("wh"))
    process.VHFilter.chooseZ = bool(customize.processId.count("zh"))
    
process.p = cms.Path(process.dataRequirements
                     * process.genFilter
                     * process.flashggUpdatedIdMVADiPhotons
                     * process.flashggDiPhotonSystematics
                     * process.flashggMuonSystematics * process.flashggElectronSystematics
                     * ( process.flashggUnpackedJets  * process.jetSystematicsSequence )
                     * ( process.flashggTagSequence   * process.systematicsTagSequences)
)
if dumpJetSysTrees:
    process.p += process.flashggSystTagMerger
    
process.p += process.VBFTagDumper


print "--- Dumping modules that take diphotons as input: ---"
mns = process.p.moduleNames()

for mn in mns:
    module = getattr(process,mn)
    if hasattr(module,"src") and type(module.src) == type(cms.InputTag("")) and module.src.value().count("DiPhoton"):
        print str(module),module.src
    elif hasattr(module,"DiPhotonTag"):
        print str(module),module.DiPhotonTag
print

printSystematicInfo(process)

# process.load("flashgg/Taggers/flashggTagTester_cfi")
# process.flashggTagTester.TagSorter = cms.InputTag("flashggSystTagMerger")
# process.flashggTagTester.ExpectMultiples = cms.untracked.bool(True)
# process.p += process.flashggTagTester

# set default options if needed
customize.setDefault("maxEvents"  ,5000   )
customize.setDefault("targetLumi" ,1.00e+3)

# call the customization
customize(process)
