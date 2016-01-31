#!/usr/bin/env cmsRun

doSystematics = True
requireTriggerOnData = True

import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils
from FWCore.ParameterSet.VarParsing import VarParsing
from flashgg.MetaData.samples_utils import SamplesManager
from PhysicsTools.PatAlgos.tools.helpers import massSearchReplaceAnyInputTag,cloneProcessingSnippet
from flashgg.MetaData.JobConfig import customize

process = cms.Process("VBFTagsDumper")

if doSystematics:
    process.load("Configuration.StandardSequences.GeometryDB_cff")
    process.load("Configuration.StandardSequences.MagneticField_cff")
    process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
    from Configuration.AlCa.GlobalTag import GlobalTag
    process.GlobalTag.globaltag = '74X_mcRun2_asymptotic_v4' # keep updated for JEC
#    process.GlobalTag.globaltag = '74X_dataRun2_reMiniAOD_v0' # Original for checks against MiniAOD

process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1))
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 1000 )
process.source = cms.Source ("PoolSource",
                             fileNames = cms.untracked.vstring(
        "root://eoscms.cern.ch//eos/cms/store/group/phys_higgs/cmshgg/sethzenz/flashgg/RunIISpring15-ReMiniAOD-1_1_0-25ns/1_1_0/DoubleEG/RunIISpring15-ReMiniAOD-1_1_0-25ns-1_1_0-v0-Run2015C_25ns-05Oct2015-v1/160105_222657/0000/myMicroAODOutputFile_41.root"
        ))

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("VBFTagsDump.root"),
                                   closeFileFast = cms.untracked.bool(True))


from flashgg.Taggers.flashggTagOutputCommands_cff import tagDefaultOutputCommand
import flashgg.Taggers.dumperConfigTools as cfgTools
from  flashgg.Taggers.tagsDumpers_cfi import createTagDumper

if doSystematics:
    from flashgg.Taggers.flashggTags_cff import UnpackedJetCollectionVInputTag
    from flashgg.Systematics.flashggJetSystematics_cfi import createJetSystematics
    process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService")
    jetSystematicsInputTags = createJetSystematics(process,UnpackedJetCollectionVInputTag)

process.load("flashgg.Taggers.flashggTagSequence_cfi")
process.load("flashgg.Taggers.flashggTagTester_cfi")

if doSystematics:
    process.flashggTagSequence.remove(process.flashggUnpackedJets)
    for i in range(len(UnpackedJetCollectionVInputTag)):
        massSearchReplaceAnyInputTag(process.flashggTagSequence,UnpackedJetCollectionVInputTag[i],jetSystematicsInputTags[i])
    process.flashggVBFTagMerger = cms.EDProducer("VBFTagMerger",src=cms.VInputTag("flashggVBFTag"))

# Use JetID
process.flashggVBFMVA.UseJetID      = cms.bool(True)
process.flashggVBFMVA.JetIDLevel    = cms.string("Loose")

# use custum TMVA weights
process.flashggVBFMVA.vbfMVAweightfile = cms.FileInPath("flashgg/Taggers/data/TMVAClassification_dijet_mva_11_01_16_BDTG.weights.xml")
process.flashggVBFMVA.MVAMethod        = cms.string( "BDTG" )
process.flashggVBFMVA.rmsforwardCut    = cms.double(  0.04  )

process.flashggDiPhotonMVA.diphotonMVAweightfile = cms.FileInPath("flashgg/Taggers/data/TMVAClassification_BDT_QCDeroded_v100_rereco.weights.xml")
# QCD Recovery 
# process.flashggVBFMVA.merge3rdJet   = cms.untracked.bool(False)
# process.flashggVBFMVA.thirdJetDRCut = cms.untracked.double(1.5)

# combined MVA boundary set
process.flashggVBFTag.Boundaries    = cms.vdouble(-2,0,2)

process.systematicsTagSequences = cms.Sequence()

from flashgg.MetaData.JobConfig import customize
customize.parse()
print "customize.processId:",customize.processId

# Do systematics on all MC (n.b. different from ordinary workspaces) but not on data
if doSystematics:
    process.load("flashgg.Systematics.flashggDiPhotonSystematics_cfi")
    massSearchReplaceAnyInputTag(process.flashggTagSequence,cms.InputTag("flashggDiPhotons"),cms.InputTag("flashggDiPhotonSystematics"))
    systlabels = [""]
    jetsystlabels = []
    if customize.processId == "Data":
        systprodlist = [getattr(process,"flashggJetSystematics%i"%i) for i in range(len(UnpackedJetCollectionVInputTag))]
        for systprod in systprodlist:
            #            systprod.SystMethods = cms.VPSet() # do no systematics

            # For any MicroAOD up to 1_3_0 the JEC in Data MicroAOD were bugged and this line makes sure they are fixed
            # It should be a noop in cases where they are already correct
            newvpset = cms.VPSet()
            for pset in systprod.SystMethods:
                if pset.Label.value().count("JEC"):
                    pset.NSigmas = cms.vint32() # Do not perform shifts, central value only
                    pset.Debug = False
                    newvpset += [pset]
            systprod.SystMethods = newvpset        
            systprod.DoCentralJEC = True
            systprod.JECLabel = "ak4PFCHSL1FastL2L3Residual"
            process.load("JetMETCorrections/Configuration/JetCorrectionServices_cff")
        newvpset = cms.VPSet()
        for pset in process.flashggDiPhotonSystematics.SystMethods:
            if pset.Label.value().count("Scale"):
                pset.NoCentralShift = cms.bool(False) # Turn on central shift for data (it is off for MC)
                pset.NSigmas = cms.vint32() # Do not perform shift
            newvpset += [pset]
        process.flashggDiPhotonSystematics.SystMethods = newvpset
    else:
        for direction in ["Up","Down"]:
            jetsystlabels.append("JEC%s01sigma" % direction)
            jetsystlabels.append("JER%s01sigma" % direction)
        systlabels += jetsystlabels
        for pset in process.flashggDiPhotonSystematics.SystMethods:
            pset.NSigmas = cms.vint32() # Central value only
    for systlabel in systlabels:
        if systlabel == "":
            continue
        newseq = cloneProcessingSnippet(process,process.flashggTagSequence,systlabel)
        if systlabel in jetsystlabels:    
            for i in range(len(jetSystematicsInputTags)):
                massSearchReplaceAnyInputTag(newseq,jetSystematicsInputTags[i],cms.InputTag(jetSystematicsInputTags[i].moduleLabel,systlabel))
        for name in newseq.moduleNames():
            module = getattr(process,name)
            if hasattr(module,"SystLabel"):
                module.SystLabel = systlabel
        process.systematicsTagSequences += newseq
        process.flashggVBFTagMerger.src.append(cms.InputTag("flashggVBFTag" + systlabel))
        
        
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
                                                             'passElectronVeto')
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
if doSystematics:
    for syst in jetsystlabels:
        systcutstring = "hasSyst(\"%s\") "%syst
        cats += [
            ("VBFDiJet_%s"%syst,"%s"%systcutstring,0)]#,
else:
    cats = [
        ("VBFDiJet","1",0)#,
        ]

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

customize.setDefault("maxEvents" , -1        ) # max-number of events
customize.setDefault("targetLumi",  1.00e+3  ) # define integrated lumi
customize(process)

from HLTrigger.HLTfilters.hltHighLevel_cfi import hltHighLevel
process.hltHighLevel = hltHighLevel.clone(HLTPaths = cms.vstring("HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v*") )
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
        process.vbfTagDumper
        )

print process.p1
