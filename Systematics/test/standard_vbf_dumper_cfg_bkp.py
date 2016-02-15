#!/usr/bin/env cmsRun

doSystematics        = True
requireTriggerOnData = True
SystematicsDebug     = False
runOnZee             = True 

import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils
from FWCore.ParameterSet.VarParsing import VarParsing
from flashgg.MetaData.samples_utils import SamplesManager
from PhysicsTools.PatAlgos.tools.helpers import massSearchReplaceAnyInputTag,cloneProcessingSnippet
from flashgg.MetaData.JobConfig import customize

process = cms.Process("VBFTagsDumper")


process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag.globaltag = '76X_mcRun2_asymptotic_RunIIFall15DR76_v0' # 76X_mcRun2_asymptotic_v13'#'74X_mcRun2_asymptotic_v4'

process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents    = cms.untracked.PSet( input = cms.untracked.int32(-1  ))
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 1 )
process.source = cms.Source ("PoolSource",
                             fileNames = cms.untracked.vstring(
        "root://eoscms.cern.ch//eos/cms/store/group/phys_higgs/cmshgg/ferriff/flashgg/RunIIFall15DR76-1_3_0-25ns_ext1/1_3_1/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15DR76-1_3_0-25ns_ext1-1_3_1-v0-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/160210_045908/0000/myMicroAODOutputFile_1.root",
        ))

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("VBFTagsDump.root"),
                                   closeFileFast = cms.untracked.bool(True))


from   flashgg.Taggers.flashggTagOutputCommands_cff import tagDefaultOutputCommand
import flashgg.Taggers.dumperConfigTools as cfgTools
from   flashgg.Taggers.tagsDumpers_cfi import createTagDumper

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
# process.flashggVBFMVA.vbfMVAweightfile = cms.FileInPath("flashgg/Taggers/data/TMVAClassification_dijet_mva_11_01_16_BDTG.weights.xml")
# process.flashggVBFMVA.MVAMethod        = cms.string("BDTG")
# process.flashggVBFMVA.rmsforwardCut    = cms.double(0.03)

# process.flashggDiPhotonMVA.diphotonMVAweightfile = cms.FileInPath("flashgg/Taggers/data/TMVAClassification_BDT_QCDeroded_v100_rereco.weights.xml")
# QCD Recovery 
# process.flashggVBFMVA.merge3rdJet   = cms.untracked.bool(False)
# process.flashggVBFMVA.thirdJetDRCut = cms.untracked.double(1.5)

# combined MVA boundary set
process.flashggVBFTag.Boundaries  = cms.vdouble(-2)
process.systematicsTagSequences   = cms.Sequence()

from flashgg.MetaData.JobConfig import customize
customize.parse()

print "customize.processId:",customize.processId
from flashgg.Systematics.flashggDiPhotonSystematics_cfi import smearBins, scaleBins, smearBinsRereco, scaleBinsRereco
# Do systematics on all MC (n.b. different from ordinary workspaces) but not on data

process.load("flashgg.Systematics.flashggDiPhotonSystematics_cfi")
massSearchReplaceAnyInputTag(process.flashggTagSequence,cms.InputTag("flashggDiPhotons"),cms.InputTag("flashggDiPhotonSystematics"))
systlabels    = [""]
jetsystlabels = []
if customize.processId == "Data":
    systprodlist = [getattr(process,"flashggJetSystematics%i"%i) for i in range(len(UnpackedJetCollectionVInputTag))]
    for systprod in systprodlist:
        # systprod.SystMethods = cms.VPSet() # do no systematics
        # For any MicroAOD up to 1_3_0 the JEC in Data MicroAOD 
        # were bugged and this line makes sure they are fixed
        # It should be a noop in cases where they are already correct
        newvpset = cms.VPSet()
        for pset in systprod.SystMethods:
            if pset.Label.value().count("JEC"):
                pset.NSigmas = cms.vint32() # Do not perform shifts, central value only
                pset.Debug = False
                newvpset  += [pset]
        systprod.SystMethods  = newvpset        
        systprod.DoCentralJEC = True
        systprod.JECLabel     = "ak4PFCHSL1FastL2L3Residual"
        process.load("JetMETCorrections/Configuration/JetCorrectionServices_cff")
    newvpset = cms.VPSet()
    for pset in process.flashggDiPhotonSystematics.SystMethods:
        #print 'pset.Label.value()==', pset.Label.value()
        if pset.Label.value().count("Scale"):
            pset.NSigmas = cms.vint32(0,0) # Do not perform shift
            pset.NoCentralShift = cms.bool(False)
            pset.Debug   = cms.untracked.bool(SystematicsDebug) 
            newvpset    += [pset]
        if pset.Label.value().count("SigmaEOverESmearing"):
            pset.NSigmas = cms.vint32(0,0) # Do not perform shift 
            pset.Debug   = cms.untracked.bool(SystematicsDebug) 
            newvpset    += [pset]
    process.flashggDiPhotonSystematics.SystMethods = newvpset
else:
    for direction in ["Up","Down"]:
        jetsystlabels.append("JEC%s01sigma" % direction)
        jetsystlabels.append("JER%s01sigma" % direction)
    systlabels += jetsystlabels
    newvpset = cms.VPSet()
    for pset in process.flashggDiPhotonSystematics.SystMethods:
        if pset.Label.value().count("MCSmear"):
            pset.NSigmas     = cms.vint32(-1,1)
            pset.RandomLabel = cms.string("rnd_g_E")
            pset.ExaggerateShiftUp = cms.bool(False)
        elif pset.Label.value().count("SigmaEOverESmearing"):
            pset.NSigmas = cms.vint32() 
        else:
            pset.NSigmas = cms.vint32()
            
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
    #use the trigger-diphoton-preselection
    massSearchReplaceAnyInputTag(process.flashggTagSequence,cms.InputTag("flashggDiPhotons"),cms.InputTag("flashggPreselectedDiPhotons"))
    
if runOnZee:
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
process.vbfTagDumper.nameTemplate = "$PROCESS_$SQRTS_$CLASSNAME_$SUBCAT_$LABEL"

customize.setDefault("maxEvents" ,  500     ) # max-number of events
customize.setDefault("targetLumi",  1.00e+3 ) # define integrated lumi
customize(process)

from HLTrigger.HLTfilters.hltHighLevel_cfi import hltHighLevel

#process.hltHighLevel = hltHighLevel.clone(HLTPaths = cms.vstring("HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v*") )
#process.hltHighLevel = hltHighLevel.clone(HLTPaths = cms.vstring("HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*") )
if runOnZee:
    if customize.processId == "Data":
        process.hltHighLevel = hltHighLevel.clone(HLTPaths = cms.vstring("HLT_Ele27_eta2p1_WPLoose_Gsf_v*") )
    else:
        process.hltHighLevel = hltHighLevel.clone(HLTPaths = cms.vstring("HLT_Ele27_eta2p1_WP75_Gsf_v*") )
else:
    process.hltHighLevel = hltHighLevel.clone(HLTPaths = cms.vstring("HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v*"))
    
process.options      = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

from  flashgg.Systematics.SystematicsCustomize import *
printSystematicInfo(process)

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
