import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils
import FWCore.ParameterSet.VarParsing as VarParsing

from flashgg.MetaData.samples_utils import SamplesManager

process = cms.Process("VBFDiJetMVATraining")
#
# ======================================================================
#
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag    import GlobalTag
from flashgg.Taggers.flashggTagOutputCommands_cff import tagDefaultOutputCommand

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.source    = cms.Source ("PoolSource",
                                #fileNames = cms.untracked.vstring("/store/group/phys_higgs/cmshgg/yhaddad/flashgg/RunIISpring15-50ns/Spring15MicroAODforJetsV1/VBFHToGG_M-125_13TeV_powheg_pythia8/RunIISpring15-50ns-Spring15MicroAODforJetsV1-v0-RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1/151005_165635/0000/myMicroAODOutputFile_4.root"))
                                fileNames = cms.untracked.vstring("file:myMicroAODOutputFile_1.root"))
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc')
process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('myTagOutputFile.root'),
                               outputCommands = tagDefaultOutputCommand			       
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("histo.root"),
                                   closeFileFast = cms.untracked.bool(True)
)
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1)
#
# ======================================================================
#
import flashgg.Taggers.dumperConfigTools as cfgTools

process.load("flashgg.Taggers.flashggTagSequence_cfi")
process.load("flashgg.Taggers.flashggTagTester_cfi")
process.flashggVBFMVA.MVAMethod      = cms.untracked.string("")
#process.flashggVBFMVAPUPPI.MVAMethod = cms.untracked.string("")

process.flashggVBFMVA.UseJetID      = cms.untracked.bool(True)
process.flashggVBFMVA.JetIDLevel    = cms.untracked.string("Loose")

#process.load("flashgg.Taggers.VBFMVADumperPUPPI_cff")
#process.VBFMVADumperPUPPI.dumpTrees     = True
#process.VBFMVADumperPUPPI.dumpWorkspace = False
#process.VBFMVADumperPUPPI.quietRooFit   = True

process.load("flashgg.Taggers.VBFMVADumper_cff")
process.VBFMVADumper.dumpTrees     = True
process.VBFMVADumper.dumpWorkspace = False
process.VBFMVADumper.quietRooFit   = True

dipho_variables=["dipho_sumpt      := diphoton.sumPt",
                 "dipho_cosphi     := abs(cos(diphoton.leadingPhoton.phi - diphoton.subLeadingPhoton.phi))",
                 "mass             := diphoton.mass",
                 "leadPt           := diphoton.leadingPhoton.pt",
                 "leadEt           := diphoton.leadingPhoton.et",
                 "leadEta          := diphoton.leadingPhoton.eta",
                 "leadPhi          := diphoton.leadingPhoton.phi",
                 "lead_sieie       := diphoton.leadingPhoton.sigmaIetaIeta",
                 "lead_hoe         := diphoton.leadingPhoton.hadronicOverEm",
                 "lead_sigmaEoE    := diphoton.leadingPhoton.sigEOverE",
                 "lead_ptoM        := diphoton.leadingPhoton.pt/diPhoton.mass",
                 "leadR9           := diphoton.leadingPhoton.r9",
                 "subleadPt        := diphoton.subLeadingPhoton.pt",
                 "subleadEt        := diphoton.subLeadingPhoton.et",
                 "subleadEta       := diphoton.subLeadingPhoton.eta",
                 "subleadPhi       := diphoton.subLeadingPhoton.phi",
                 "sublead_sieie    := diphoton.subLeadingPhoton.sigmaIetaIeta",
                 "sublead_hoe      := diphoton.subLeadingPhoton.hadronicOverEm",
                 "sublead_sigmaEoE := diphoton.subLeadingPhoton.sigEOverE",
                 "sublead_ptoM     := diphoton.subLeadingPhoton.pt/diPhoton.mass",
                 "subleadR9        := diphoton.subLeadingPhoton.r9",
                 "leadIDMVA        := diphoton.leadingView.phoIdMvaWrtChosenVtx",
                 "subleadIDMVA     := diphoton.subLeadingView.phoIdMvaWrtChosenVtx",
                 ]

VBFMVAvariables=[
    # diphoton variables
    #"mass             := diphoton.mass",
    #"leadPt           := diphoton.leadingPhoton.pt",
    #"leadEt           := diphoton.leadingPhoton.et",
    #"leadEta          := diphoton.leadingPhoton.eta",
    #"leadPhi          := diphoton.leadingPhoton.phi",
    #"subleadPt        := diphoton.subLeadingPhoton.pt",
    #"subleadEt        := diphoton.subLeadingPhoton.et",
    #"subleadEta       := diphoton.subLeadingPhoton.eta",
    #"subleadPhi       := diphoton.subLeadingPhoton.phi",
    #"leadIDMVA        := diphoton.leadingView.phoIdMvaWrtChosenVtx",
    #"subleadIDMVA     := diphoton.subLeadingView.phoIdMvaWrtChosenVtx",
    #"dipho_sumpt      := diphoton.sumPt",
    #"lead_sieie       := diphoton.leadingPhoton.sigmaIetaIeta",
    #"lead_hoe         := diphoton.leadingPhoton.hadronicOverEm",
    #"lead_sigmaEoE    := diphoton.leadingPhoton.sigEOverE",
    #"lead_ptoM        := diphoton.leadingPhoton.pt/diPhoton.mass",
    #"leadR9           := diphoton.leadingPhoton.r9",                     
    #"sublead_sieie    := diphoton.subLeadingPhoton.sigmaIetaIeta",
    #"sublead_hoe      := diphoton.subLeadingPhoton.hadronicOverEm",
    #"sublead_sigmaEoE := diphoton.subLeadingPhoton.sigEOverE",
    #"sublead_ptoM     := diphoton.subLeadingPhoton.pt/diPhoton.mass",
    #"subleadR9        := diphoton.subLeadingPhoton.r9",  
    # dijet variables
    "dijet_abs_dEta      :=  dijet_abs_dEta   ",
    "dijet_leadEta       :=  dijet_leadEta    ",
    "dijet_subleadEta    :=  dijet_subleadEta ",
    "dijet_leady         :=  dijet_leady      ",
    "dijet_subleady      :=  dijet_subleady   ",
    "dijet_LeadJPt       :=  dijet_LeadJPt    ",
    "dijet_SubJPt        :=  dijet_SubJPt     ",
    "dijet_Zep           :=  dijet_Zep        ",
    "dijet_Mjj           :=  dijet_Mjj        ",
    "dipho_PToM          :=  dipho_PToM       ",
    "leadPho_PToM        :=  leadPho_PToM     ",
    "sublPho_PToM        :=  sublPho_PToM     ",
    "dijet_dphi_trunc    :=  dijet_dphi_trunc ",
    "dijet_dipho_pt      :=  dijet_dipho_pt   ",
    "dijet_dphi          :=  abs(leadJet.phi - subleadJet.phi)",
    "dijet_dipho_dphi    :=  dijet_dipho_dphi",#abs((leadJet.p4+subleadJet.p4).phi - diphoton.phi)",
    "dijet_minDRJetPho   :=  dijet_minDRJetPho      ",
    "dijet_dipho_dphi_trunc    :=  dijet_dipho_dphi ",
    "has3Jet      := hasValidVBFTriJet",
    "jet1_pt      :=       leadJet.pt",
    "jet2_pt      :=    subleadJet.pt",
    "jet3_pt      := subsubleadJet.pt",
    "jet1_eta     :=       leadJet.eta",
    "jet2_eta     :=    subleadJet.eta",
    "jet3_eta     := subsubleadJet.eta"]
    #"trijet_mjjj  := sqrt((leadJet.energy+subleadJet.energy+subsubleadJet.energy)^2-(leadJet.px+subleadJet.px+subsubleadJet.px)^2-(leadJet.py+subleadJet.py+subsubleadJet.py)^2-(leadJet.pz+subleadJet.pz+subsubleadJet.pz)^2)"]

preselection_cut = "dijet_LeadJPt>30 && dijet_SubJPt>20 && dijet_leadEta<4.7 && dijet_leadEta > -4.7 && dijet_subleadEta < 4.7 && dijet_subleadEta > -4.7 && dijet_Mjj> 250 && leadPho_PToM  > 0.5"

# ===============================================================================
# setup the dumpers
cfgTools.addCategories(process.VBFMVADumper,
                       [
                            ("VBFDiJet"            ,"dijet_LeadJPt > 0"     ,0),
                            ("excluded"            ,"1"                     ,0) 
                       ],
                       
                       variables  = VBFMVAvariables ,
                       histograms = []
)

# split tree, histogram and datasets by process
process.VBFMVADumper.nameTemplate ="$PROCESS_$SQRTS_$LABEL_$SUBCAT"
#cfgTools.addCategories(process.VBFMVADumperPUPPI,
#                       [
#                           ("VBFDiJet"            ,"dijet_LeadJPt > 0"     ,0),
#                           ("excluded"            ,"1"                     ,0) 
#                       ],
#                       variables  = VBFMVAvariables ,
#                       histograms = []
#)
#
## split tree, histogram and datasets by process
#process.VBFMVADumperPUPPI.nameTemplate ="$PROCESS_$SQRTS_$LABEL_$SUBCAT"
#
# ======================================================================

process.load("flashgg/Taggers/VBFDiPhoDiJetMVADumper_cff")

process.VBFDiPhoDiJetMVADumper.dumpTrees     = True
process.VBFDiPhoDiJetMVADumper.dumpWorkspace = False
process.VBFDiPhoDiJetMVADumper.quietRooFit   = True

cfgTools.addCategories(process.VBFDiPhoDiJetMVADumper,
                       [
                           ("All","dipho_PToM>=0",0),
                       ],
                       variables=[
                           "dijet_mva  :=  dijet_mva",
                           "dipho_mva  :=  dipho_mva",
                           "dipho_PToM :=  dipho_PToM",
                           "vbfDiPhoDiJetMvaResult := vbfDiPhoDiJetMvaResult",
                       ],
                       histograms=[
                           "VBFDiPhoDiJetMVAResult>>VBFDiPhoDiJetMVAResult(100,-1,1)",
                       ]
)

process.load("flashgg/Taggers/VBFDiPhoDiJetMVADumperPUPPI_cff")
#
#process.VBFDiPhoDiJetMVADumperPUPPI.dumpTrees     = True
#process.VBFDiPhoDiJetMVADumperPUPPI.dumpWorkspace = False
#process.VBFDiPhoDiJetMVADumperPUPPI.quietRooFit   = True
#
#cfgTools.addCategories(process.VBFDiPhoDiJetMVADumperPUPPI,
#                       [
#                           ("All","dipho_PToM>=0",0),
#                       ],
#                       variables=[
#                           "dijet_mva  :=  dijet_mva",
#                           "dipho_mva  :=  dipho_mva",
#                           "dipho_PToM :=  dipho_PToM",
#                           "vbfDiPhoDiJetMvaResult := vbfDiPhoDiJetMvaResult",
#                       ],
#                       histograms=[
#                           "VBFDiPhoDiJetMVAResult>>VBFDiPhoDiJetMVAResult(100,-1,1)",
#                       ]
#)

# split tree, histogram and datasets by process
process.VBFDiPhoDiJetMVADumper.nameTemplate ="$PROCESS_$SQRTS_$LABEL_$SUBCAT"
#process.VBFDiPhoDiJetMVADumperPUPPI.nameTemplate ="$PROCESS_$SQRTS_$LABEL_$SUBCAT"

# cutomize
from flashgg.MetaData.JobConfig import customize
customize.setDefault("maxEvents",-1)
customize.setDefault("targetLumi",1.e+4)
customize(process)

process.p = cms.Path( process.flashggTagSequence*
                      process.VBFDiPhoDiJetMVADumper*
                      #process.VBFDiPhoDiJetMVADumperPUPPI*
                      process.VBFMVADumper#*
                      #process.VBFMVADumperPUPPI
                      )
