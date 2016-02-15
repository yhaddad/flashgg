#!/usr/bin/env cmsRun
requireTriggerOnData = True

import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils
from   FWCore.ParameterSet.VarParsing import VarParsing
from   flashgg.MetaData.samples_utils import SamplesManager
from   PhysicsTools.PatAlgos.tools.helpers import massSearchReplaceAnyInputTag,cloneProcessingSnippet

process = cms.Process("VBFDumper")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")

# =====================================================================
# global tag :  set to 76x defaut global tag
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '76X_mcRun2_asymptotic_v13')

# =====================================================================
# files management
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 1000 )
process.maxEvents    = cms.untracked.PSet( input = cms.untracked.int32( -1  ))
process.source = cms.Source ("PoolSource",
                             fileNames = cms.untracked.vstring(
        #"root://eoscms.cern.ch//eos/cms/store/group/phys_higgs/cmshgg/ferriff/flashgg/RunIISpring15-SingleEle2015D-TTG-TTJ-TGJ-WG-ZG-1_2_0-25ns/1_2_0/SingleElectron/RunIISpring15-SingleEle2015D-TTG-TTJ-TGJ-WG-ZG-1_2_0-25ns-1_2_0-v0-Run2015D-04Dec2015-v2/160116_162910/0000/myMicroAODOutputFile_1.root"
        #"root://eoscms.cern.ch//eos/cms/store/group/phys_higgs/cmshgg/sethzenz/flashgg/RunIISpring15-ReMiniAOD-1_1_0-25ns/1_1_0/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15-ReMiniAOD-1_1_0-25ns-1_1_0-v0-RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/160105_222534/0000/myMicroAODOutputFile_137.root"
        "root://eoscms.cern.ch//eos/cms/store/group/phys_higgs/cmshgg/sethzenz/flashgg/RunIISpring15-ReMiniAOD-1_1_0-25ns/1_1_0/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15-ReMiniAOD-1_1_0-25ns-1_1_0-v0-RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/160105_222534/0000/myMicroAODOutputFile_1.root"
        #"file:myMicroAODOutputFile.root"
        ))

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("VBFTagsDump.root"),
                                   closeFileFast = cms.untracked.bool(True))
# =====================================================================
# VBF jets options
from   flashgg.Taggers.flashggTagOutputCommands_cff import tagDefaultOutputCommand
import flashgg.Taggers.dumperConfigTools as cfgTools
from   flashgg.Taggers.tagsDumpers_cfi import createTagDumper
from   flashgg.Taggers.flashggTags_cff import UnpackedJetCollectionVInputTag

process.load("flashgg.Taggers.flashggTagSequence_cfi")
process.load("flashgg.Taggers.flashggTagTester_cfi")

process.flashggVBFMVA.UseJetID      = cms.bool(True)
process.flashggVBFMVA.JetIDLevel    = cms.string("Loose")

# use custum TMVA weights
# process.flashggVBFMVA.vbfMVAweightfile = cms.FileInPath("flashgg/Taggers/data/TMVAClassification_dijet_mva_11_01_16_BDTG.weights.xml")
# process.flashggVBFMVA.MVAMethod        = cms.string("BDTG")
# process.flashggVBFMVA.rmsforwardCut    = cms.double(0.03)

# process.flashggDiPhotonMVA.diphotonMVAweightfile = cms.FileInPath("flashgg/Taggers/data/TMVAClassification_BDT_QCDeroded_v100_rereco.weights.xml")
# QCD Recovery 
# process.flashggVBFMVA.merge3rdJet   = cms.untracked.bool(False)
# process.flashggVBFMVA.thirdJetDRCut = cms.untracked.double(1.5)

# =====================================================================
# combined MVA boundary set
process.flashggVBFTag.Boundaries    = cms.vdouble(-2)
process.systematicsTagSequences = cms.Sequence()

# =====================================================================
# process customize
from flashgg.MetaData.JobConfig import customize
customize.parse()
print "customize.processId:",customize.processId

# =====================================================================
# systematics customizer 
from   flashgg.Systematics.SystematicsCustomize import *
systematicsInputTags = createStandardSystematicsProducers(process)
modifyTagSequenceForSystematics(process,systematicsInputTags)

process.load("flashgg.Taggers.flashggTagSequence_cfi")
process.load("flashgg.Taggers.flashggTagTester_cfi")

process.flashggTagSequence.remove(process.flashggUnpackedJets)
for i in range(len(UnpackedJetCollectionVInputTag)):
    massSearchReplaceAnyInputTag(process.flashggTagSequence,
                                 UnpackedJetCollectionVInputTag[i],
                                 systematicsInputTags[i])
    process.flashggVBFTagMerger = cms.EDProducer("VBFTagMerger",src=cms.VInputTag("flashggVBFTag"))

  

  
if customize.processId == "Data" or customize.processId == "data":
    print "Data, so turn of all shifts and systematics, with some exceptions"
    variablesToUse = minimalNonSignalVariables
    customizeSystematicsForData(process)
else:
    print "Background MC, so store mgg and central only"
    variablesToUse = minimalNonSignalVariables
    customizeSystematicsForBackground(process)
    
print "--- Systematics  with independent collections ---"
print systlabels
print "-------------------------------------------------"
print "--- Variables to be dumped, including systematic weights ---"
print variablesToUse
print "------------------------------------------------------------"
printSystematicInfo(process)
#cloneTagSequenceForEachSystematic(process,systlabels,phosystlabels,jetsystlabels,jetSystematicsInputTags)

# =====================================================================                
# set the VBF dumper
process.vbfTagDumper = createTagDumper("VBFTag")
process.vbfTagDumper.dumpTrees     = True
process.vbfTagDumper.dumpHistos    = True
process.vbfTagDumper.dumpWorkspace = False

if doSystematics:
    process.vbfTagDumper.src = "flashggVBFTagMerger"
else:
    # use the trigger-diphoton-preselection
    massSearchReplaceAnyInputTag(process.flashggTagSequence,cms.InputTag("flashggDiPhotons"),cms.InputTag("flashggPreselectedDiPhotons"))


process.flashggPreselectedDiPhotons.variables =  cms.vstring('pfPhoIso03', 
                                                             'trkSumPtHollowConeDR03', 
                                                             'full5x5_sigmaIetaIeta', 
                                                             'full5x5_r9', 
                                                             '1-passElectronVeto')
# get the variable list
import flashgg.Taggers.VBFTagVariables as var
new_variables = [
    "n_jets         := VBFMVA.n_rec_jets",
    "dijet_jet1_RMS := leading_rms",
    "dijet_jet2_RMS := subLeading_rms",
    "dijet_jet1_QGL := leading_QGL",
    "dijet_jet2_QGL := subLeading_QGL"
]
matching_photon = [
    "prompt_pho_1   := diPhoton.leadingPhoton.genMatchType()",
    "prompt_pho_2   := diPhoton.subLeadingPhoton.genMatchType()"
    ] 
all_variables = var.dijet_variables + var.dipho_variables + new_variables #var.truth_variables
if customize.processId != "Data":
    all_variables += var.truth_variables + matching_photon
    
cats = []
for syst in jetsystlabels:
    systcutstring = "hasSyst(\"%s\") "%syst
    cats += [
        ("VBFDiJet_%s"%syst,"%s"%systcutstring,0)]#,
    
cats += [
    ("VBFDiJet","1",0)#,
    ]

cfgTools.addCategories(process.vbfTagDumper,
                       cats,
                       variables  = all_variables,
                       histograms = []
                       )

print cats

#process.vbfTagDumper.nameTemplate ="$PROCESS_$SQRTS_$LABEL_$SUBCAT_$CLASSNAME"
process.vbfTagDumper.nameTemplate = "$PROCESS_$SQRTS_$CLASSNAME_$SUBCAT_$LABEL"

customize.setDefault("maxEvents" ,  500     ) # max-number of events
customize.setDefault("targetLumi",  1.00e+3 ) # define integrated lumi
customize(process)

from HLTrigger.HLTfilters.hltHighLevel_cfi import hltHighLevel
#process.hltHighLevel = hltHighLevel.clone(HLTPaths = cms.vstring("HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v*") )
#process.hltHighLevel = hltHighLevel.clone(HLTPaths = cms.vstring("HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*") )


if customize.processId == "Data":
    process.hltHighLevel = hltHighLevel.clone(HLTPaths = cms.vstring("HLT_Ele27_eta2p1_WPLoose_Gsf_v*") )
else:
    process.hltHighLevel = hltHighLevel.clone(HLTPaths = cms.vstring("HLT_Ele27_eta2p1_WP75_Gsf_v*") )

process.options      = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.hltRequirement = cms.Sequence()
if customize.processId == "Data" and requireTriggerOnData:
        process.hltRequirement += process.hltHighLevel

if doSystematics:
    process.p1 = cms.Path(
        process.hltRequirement*
        process.flashggDiPhotonSystematics*
        (process.flashggUnpackedJets*process.jetSystematicsSequence)*
        (process.flashggTagSequence+process.systematicsTagSequences)*
        process.flashggVBFTagMerger*
        process.vbfTagDumper
        )
else:
    process.p1 = cms.Path(
        process.hltRequirement*
        process.flashggTagSequence*
        # process.flashggTagTester* # Uncommment if you what to test VBFtag
        process.vbfTagDumper
        )

print process.p1
