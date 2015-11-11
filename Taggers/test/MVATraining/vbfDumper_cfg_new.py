#!/usr/bin/env cmsRun

import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils
from FWCore.ParameterSet.VarParsing import VarParsing
from flashgg.MetaData.samples_utils import SamplesManager


## I/O SETUP ##
process = cms.Process("VBFTagsDumper")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1))
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 1 )
process.source = cms.Source ("PoolSource",
                             fileNames = cms.untracked.vstring("file:myMicroAODOutputFile_1.root"))

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("VBFTagsDump.root"),
                                   closeFileFast = cms.untracked.bool(True))


from flashgg.Taggers.flashggTagOutputCommands_cff import tagDefaultOutputCommand
import flashgg.Taggers.dumperConfigTools as cfgTools
from  flashgg.Taggers.tagsDumpers_cfi import createTagDumper

process.load("flashgg.Taggers.flashggTagSequence_cfi")
process.load("flashgg.Taggers.flashggTagTester_cfi")

#process.flashggVBFMVA.MVAMethod     = cms.untracked.string("")
process.flashggVBFMVA.UseJetID      = cms.untracked.bool(True)
process.flashggVBFMVA.JetIDLevel    = cms.untracked.string("Loose")

# some options on the VBFTag
process.flashggVBFTag.Boundaries    = cms.untracked.vdouble(-2,0,2)

process.vbfTagDumper = createTagDumper("VBFTag")
process.vbfTagDumper.dumpTrees     = True
process.vbfTagDumper.dumpHistos    = True
process.vbfTagDumper.dumpWorkspace = False

dipho_variables=[
    "dipho_sumpt      := diPhoton.sumPt",
    "dipho_cosphi     := abs(cos(diPhoton.leadingPhoton.phi - diPhoton.subLeadingPhoton.phi))",
    "mass             := diPhoton.mass",
    "leadPt           := diPhoton.leadingPhoton.pt",
    "leadEt           := diPhoton.leadingPhoton.et",
    "leadEta          := diPhoton.leadingPhoton.eta",
    "leadPhi          := diPhoton.leadingPhoton.phi",
    "lead_sieie       := diPhoton.leadingPhoton.sigmaIetaIeta",
    "lead_hoe         := diPhoton.leadingPhoton.hadronicOverEm",
    "lead_sigmaEoE    := diPhoton.leadingPhoton.sigEOverE",
    "lead_ptoM        := diPhoton.leadingPhoton.pt/diPhoton.mass",
    "leadR9           := diPhoton.leadingPhoton.r9",
    "subleadPt        := diPhoton.subLeadingPhoton.pt",
    "subleadEt        := diPhoton.subLeadingPhoton.et",
    "subleadEta       := diPhoton.subLeadingPhoton.eta",
    "subleadPhi       := diPhoton.subLeadingPhoton.phi",
    "sublead_sieie    := diPhoton.subLeadingPhoton.sigmaIetaIeta",
    "sublead_hoe      := diPhoton.subLeadingPhoton.hadronicOverEm",
    "sublead_sigmaEoE := diPhoton.subLeadingPhoton.sigEOverE",
    "sublead_ptoM     := diPhoton.subLeadingPhoton.pt/diPhoton.mass",
    "subleadR9        := diPhoton.subLeadingPhoton.r9",
    "leadIDMVA        := diPhoton.leadingView.phoIdMvaWrtChosenVtx",
    "subleadIDMVA     := diPhoton.subLeadingView.phoIdMvaWrtChosenVtx",]

dijet_variables=[
    "dijet_abs_dEta      :=  VBFMVA.dijet_abs_dEta   ",
    "dijet_leadEta       :=  VBFMVA.dijet_leadEta    ",
    "dijet_subleadEta    :=  VBFMVA.dijet_subleadEta ",
    "dijet_leady         :=  VBFMVA.dijet_leady      ",
    "dijet_subleady      :=  VBFMVA.dijet_subleady   ",
    "dijet_LeadJPt       :=  VBFMVA.dijet_LeadJPt    ",
    "dijet_SubJPt        :=  VBFMVA.dijet_SubJPt     ",
    "dijet_Zep           :=  VBFMVA.dijet_Zep        ",
    "dijet_Mjj           :=  VBFMVA.dijet_Mjj        ",
    "dipho_PToM          :=  VBFMVA.dipho_PToM       ",
    "leadPho_PToM        :=  VBFMVA.leadPho_PToM     ",
    "sublPho_PToM        :=  VBFMVA.sublPho_PToM     ",
    "dijet_dphi_trunc    :=  VBFMVA.dijet_dphi_trunc ",
    "dijet_dipho_pt      :=  VBFMVA.dijet_dipho_pt   ",
    "dijet_dphi          :=  deltaPhi(VBFMVA.leadJet.phi,VBFMVA.subleadJet.phi)",
    "dijet_dipho_dphi    :=  VBFMVA.dijet_dipho_dphi",
    "dijet_minDRJetPho   :=  VBFMVA.dijet_minDRJetPho",
    "has3Jet             :=  hasValidVBFTriJet",
    "dijet_MVA           :=  VBFMVA.VBFMVAValue",
    "dijet_dipho_dphi_trunc :=  VBFMVA.dijet_dipho_dphi ",
    # new variables
    "jet1_pt             := leadingJet.pt",
    "jet2_pt             := subLeadingJet.pt",
    "jet3_pt             := subSubLeadingJet.pt",
    "jet1_eta            := leadingJet.pt",
    "jet2_eta            := subLeadingJet.pt",
    "jet3_eta            := subSubLeadingJet.pt",
    # tag truth information
    "genZ                                 :=tagTruth().genPV().z", # try that !!
    "pt_genJetMatchingToJ1                := tagTruth().pt_genJetMatchingToJ1",
    "pt_genJetMatchingToJ2                := tagTruth().pt_genJetMatchingToJ2",
    "pt_genJetMatchingToJ3                := tagTruth().pt_genJetMatchingToJ3",
    "eta_genJetMatchingToJ1               := tagTruth().eta_genJetMatchingToJ1",
    "eta_genJetMatchingToJ2               := tagTruth().eta_genJetMatchingToJ2",
    "eta_genJetMatchingToJ3               := tagTruth().eta_genJetMatchingToJ3",
    "hasClosestGenJetToLeadingJet         := tagTruth().hasClosestGenJetToLeadingJet",
    "hasClosestGenJetToSubLeadingJet      := tagTruth().hasClosestGenJetToSubLeadingJet",
    "hasClosestParticleToLeadingJet       := tagTruth().hasClosestParticleToLeadingJet",
    "hasClosestParticleToSubLeadingJet    := tagTruth().hasClosestParticleToSubLeadingJet",
    "hasClosestParticleToLeadingPhoton    := tagTruth().hasClosestParticleToLeadingPhoton",
    "hasClosestParticleToSubLeadingPhoton := tagTruth().hasClosestParticleToSubLeadingPhoton",
    "Mjj:=sqrt((leadingJet.energy+subLeadingJet.energy)^2-(leadingJet.px+subLeadingJet.px)^2-(leadingJet.py+subLeadingJet.py)^2-(leadingJet.pz+subLeadingJet.pz)^2)"    
]

cfgTools.addCategories(process.vbfTagDumper,
                       [
                           ("VBFDiJet","VBFMVA.dijet_LeadJPt>=0",0),
                           ("excluded","1",0)
                       ],
                       variables= dipho_variables + dijet_variables,
                       histograms=[]
)

#process.vbfTagDumper.nameTemplate ="$PROCESS_$SQRTS_$LABEL_$SUBCAT_$CLASSNAME"
process.vbfTagDumper.nameTemplate = "$PROCESS_$SQRTS_$CLASSNAME_$SUBCAT_$LABEL"

from flashgg.MetaData.JobConfig import customize
customize.setDefault("maxEvents",10000)
customize.setDefault("targetLumi",1.e+4)
customize(process)

process.p1 = cms.Path(
    process.flashggTagSequence*
    process.flashggTagTester*
    process.vbfTagDumper
)

print process.p1
