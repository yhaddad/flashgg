#!/usr/bin/env cmsRun

#runOnZee = False
dumpJetSysTrees = False

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
if   os.environ["CMSSW_VERSION"].count("CMSSW_7_6"):
    process.GlobalTag.globaltag = '76X_mcRun2_asymptotic_v12'
elif os.environ["CMSSW_VERSION"].count("CMSSW_8_0"):
    process.GlobalTag.globaltag = '80X_mcRun2_asymptotic_2016_miniAODv2'
elif os.environ["CMSSW_VERSION"].count("CMSSW_8_0_20"):
    process.GlobalTag.globaltag = '80X_mcRun2_asymptotic_2016_miniAODv2_v1'
elif os.environ["CMSSW_VERSION"].count("CMSSW_8_0_25"):
        process.GlobalTag.globaltag = '80X_mcRun2_asymptotic_2016_TrancheIV_v6'
elif os.environ["CMSSW_VERSION"].count("CMSSW_7_4"):
    process.GlobalTag.globaltag = '74X_mcRun2_asymptotic_v4'
else:
    raise Exception,"Could not find a sensible CMSSW_VERSION for default globaltag"

process.maxEvents   = cms.untracked.PSet( input  = cms.untracked.int32( 50000 ) )
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 1000 )

from flashgg.Systematics.SystematicsCustomize import *
jetSystematicsInputTags = createStandardSystematicsProducers(process)

process.load("flashgg.Taggers.flashggTagSequence_cfi")
process.load("flashgg.Taggers.flashggTagTester_cfi")

mva_wp = {
    "none"  : [
        [],
        [],
        []
    ],
    "tight" : [
        [0.69, -0.35, -0.26, -0.21],
        [0.86, -0.1 , -0.05, -0.01],
        [0.95,  0.28,  0.31,  0.28]
    ],
    "medium": [
        [0.18, -0.55, -0.42, -0.36],
        [0.61, -0.35, -0.23, -0.17],
        [0.87,  0.03,  0.13,  0.12]
    ],
    "loose" :[
        [-0.97, -0.68, -0.53, -0.47],
        [-0.89, -0.52, -0.38, -0.3 ],
        [-0.56, -0.17, -0.04, -0.01],
    ],
    "forward_tight" : [
        [-1, -0.35, -0.26, -0.21],
        [-1, -0.1 , -0.05, -0.01],
        [-1,  0.28,  0.31,  0.28]
    ],
    "forward_medium": [
        [-1, -0.55, -0.42, -0.36],
        [-1, -0.35, -0.23, -0.17],
        [-1,  0.03,  0.13,  0.12]
    ],
    "forward_loose" :[
        [-1, -0.68, -0.53, -0.47],
        [-1, -0.52, -0.38, -0.3 ],
        [-1, -0.17, -0.04, -0.01],
    ]
}




# Keep an extra category as 'would go elsewhere instead', ignore preselection
process.flashggVBFTag.Boundaries             = cms.vdouble(-999.,0.62, 0.94)
process.flashggVBFTag.SetArbitraryNonGoldMC  = cms.bool(False)
process.flashggVBFTag.DropNonGoldData        = cms.bool(False)
process.flashggVBFTag.RequireVBFPreselection = cms.bool(False)

process.flashggVBFTagMerger = cms.EDProducer("VBFTagMerger",src=cms.VInputTag("flashggVBFTag"))
modifyTagSequenceForSystematics(process,jetSystematicsInputTags,dumpJetSysTrees)

systlabels    = [""]
phosystlabels = []
jetsystlabels = []
elesystlabels = []
musystlabels  = []

# import flashgg customization to check if we have signal or background
from flashgg.MetaData.JobConfig import customize
# Register forwardJetRMSCut to be used from customize
customize.options.register('forwardJetRMSCut',
                           3.00,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.float,
                           'forwardJetRMSCut')

customize.options.register('pujidWP',
                           'none',#'tight',
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.string,
                           'pujidWP')

customize.options.register('runOnZee',
                           False,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'runOnZee')

customize.parse()
print "customize.processId:",customize.processId

useEGMTools(process)

#== Only run systematics for signal events
from flashgg.Taggers.flashggTags_cff import UnpackedJetCollectionVInputTag

# load the correctors
process.load("JetMETCorrections.Configuration.JetCorrectors_cff")

if customize.processId == "Data":
    print "Data, so turn of all shifts and systematics, with some exceptions"
    variablesToUse = minimalNonSignalVariables

    #process.flashggElectronSystematics.src = cms.InputTag("flashggElectrons")
    customizeSystematicsForData(process)
else:
    print "Background MC, so store mgg and central only"
    variablesToUse = minimalNonSignalVariables

    if dumpJetSysTrees:
        print "Running jet systematics and putting them in ntuples because doJetSystTrees is set"
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

cloneTagSequenceForEachSystematic(process,systlabels,phosystlabels,jetsystlabels,jetSystematicsInputTags,dumpJetSysTrees)

# ========================================================================
# Dumper section
from FWCore.ParameterSet.VarParsing import VarParsing
from flashgg.MetaData.samples_utils import SamplesManager

process.source = cms.Source ("PoolSource",
                             fileNames = cms.untracked.vstring(
                                 #"/store/group/phys_higgs/cmshgg/ferriff/flashgg/RunIISpring16DR80X-2_3_0-25ns_Moriond17_MiniAODv2/2_3_0/QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8/RunIISpring16DR80X-2_3_0-25ns_Moriond17_MiniAODv2-2_3_0-v0-RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/161114_094221/0000/myMicroAODOutputFile_62.root"
                                 #"/store/group/phys_higgs/cmshgg/sethzenz/flashgg/RunIISummer16-2_4_1-25ns_Moriond17/2_4_1/VBFHToGG_M125_13TeV_amcatnlo_pythia8_CUETP8M1Down/RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/170114_093048/0000/myMicroAODOutputFile_2.root"
                                 "/store/group/phys_higgs/cmshgg/sethzenz/flashgg/RunIISummer16-2_4_1-25ns_Moriond17/2_4_1/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/170114_100547/0000/myMicroAODOutputFile_218.root"
                             )
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("test.root"))

import flashgg.Taggers.dumperConfigTools as cfgTools
from   flashgg.Taggers.tagsDumpers_cfi   import createTagDumper

process.vbfTagDumper = createTagDumper("VBFTag")
process.vbfTagDumper.dumpTrees     = True
process.vbfTagDumper.dumpHistos    = True
process.vbfTagDumper.dumpWorkspace = False

# Use JetID
process.flashggVBFMVA.UseJetID      = cms.bool(True)
process.flashggVBFMVA.JetIDLevel    = cms.string("Tight") #cms.string("Loose")
process.flashggVBFMVA.DrJetPhoton   = cms.double(0.4) # this is the right number

process.flashggVBFTag.Boundaries  = cms.vdouble(-2)
process.systematicsTagSequences   = cms.Sequence()

process.flashggVBFMVA.rmsforwardCut = cms.double(customize.forwardJetRMSCut)
process.flashggVBFMVA.pujidWpPtBin1 = cms.vdouble(mva_wp[customize.pujidWP][0])
process.flashggVBFMVA.pujidWpPtBin2 = cms.vdouble(mva_wp[customize.pujidWP][1])
process.flashggVBFMVA.pujidWpPtBin3 = cms.vdouble(mva_wp[customize.pujidWP][2])

print '------------------------------------------------------------'
print ' PUJID Working point    ::' , customize.pujidWP
print '------------------------------------------------------------'
print ' PUJID wp cuts          ::' , mva_wp[customize.pujidWP]
print '------------------------------------------------------------'
print ' formward RMS Cut value ::' , customize.forwardJetRMSCut
print '------------------------------------------------------------'
print ' running on Zee         ::' , customize.runOnZee
print '------------------------------------------------------------'

# use custum TMVA weights
# process.flashggVBFMVA.vbfMVAweightfile = cms.FileInPath("flashgg/Taggers/data/TMVAClassification_dijetMVA_76x_17_02_15_BDTG.weights.xml")
process.flashggVBFMVA.vbfMVAweightfile = cms.FileInPath("flashgg/Taggers/data/sklearn_training_moriond17_v7.xml")
process.flashggVBFMVA.MVAMethod        = cms.string("BDTG")

process.flashggDiPhotonMVA.diphotonMVAweightfile = cms.FileInPath("flashgg/Taggers/data/Flashgg_DiPhoton_Moriond17.weights.xml")
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

for syst in jetsystlabels:
    getattr(process,"flashggPreselectedDiPhotons%s"%syst).variables = process.flashggPreselectedDiPhotons.variables
# get the variable list
import flashgg.Taggers.VBFTagVariables as var
new_variables = [
    "dijet_jet1_RMS       := leading_rms",
    "dijet_jet2_RMS       := subLeading_rms",
    "dijet_jet1_QGL       := leading_QGL",
    "dijet_jet2_QGL       := subLeading_QGL",
    "dijet_jet1_pujid_mva := leading_pujidMVA()",
    "dijet_jet2_pujid_mva := subleading_pujidMVA()",
    "dipho_pt             := diPhoton.pt"
]

matching_photon = [
    "dijet_jet1_match := leadingJet_match",
    "dijet_jet2_match := subLeadingJet_match",
    "prompt_pho_1 := diPhoton.leadingPhoton.genMatchType()",
    "prompt_pho_2 := diPhoton.subLeadingPhoton.genMatchType()"
]

all_variables = var.dipho_variables + var.dijet_variables +  new_variables
if customize.processId != "Data":
    all_variables += matching_photon

cats = [
    ("VBFDiJet","1",0)#,
]
if dumpJetSysTrees :
    for syst in jetsystlabels:
        systcutstring = "hasSyst(\"%s\") "%syst
        cats += [
            ("VBFDiJet_%s"%syst,"%s"%systcutstring,0)]#,


cfgTools.addCategories(process.vbfTagDumper,
                       cats,
                       variables  = all_variables,
                       histograms = []
)
process.vbfTagDumper.nameTemplate = "$PROCESS_$SQRTS_$CLASSNAME_$SUBCAT_$LABEL"
from HLTrigger.HLTfilters.hltHighLevel_cfi import hltHighLevel
if customize.runOnZee:
    if customize.processId == "Data":
        process.hltHighLevel = hltHighLevel.clone(HLTPaths = cms.vstring("HLT_Ele27_WPTight_Gsf_v*") )
else:
    process.hltHighLevel = hltHighLevel.clone(HLTPaths = cms.vstring("HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v*"))

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
                     #* process.flashggMuonSystematics
                     * process.flashggElectronSystematics
                     * (process.flashggUnpackedJets
                        * process.ak4PFCHSL1FastL2L3CorrectorChain
                        * process.jetSystematicsSequence)
                     * (process.flashggTagSequence
                        + process.systematicsTagSequences)
                     * process.flashggVBFTagMerger
                     * process.vbfTagDumper
                     )

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

# set default options if needed
customize.setDefault("maxEvents"  ,10000   )
customize.setDefault("targetLumi" ,1.00e+3)

# call the customization
customize(process)
