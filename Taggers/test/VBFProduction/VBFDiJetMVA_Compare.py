import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils
import FWCore.ParameterSet.VarParsing as VarParsing

from flashgg.MetaData.samples_utils import SamplesManager

process = cms.Process("VBFDiJetMVACompare")
#
# ======================================================================
#
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
from flashgg.Taggers.flashggTagOutputCommands_cff import tagDefaultOutputCommand

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.source = cms.Source ("PoolSource",
                             fileNames = cms.untracked.vstring())

process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc')
process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('myTagOutputFile.root'),
                               outputCommands = tagDefaultOutputCommand
)
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("histo.root"),
                                   closeFileFast = cms.untracked.bool(True)
)
#
# ======================================================================
#
import flashgg.Taggers.dumperConfigTools as cfgTools

process.load("flashgg.Taggers.flashggTagSequence_cfi")
process.load("flashgg.Taggers.flashggTagTester_cfi")
process.flashggVBFMVA.MVAMethod      = cms.untracked.string("BDTG")
process.flashggVBFMVAPUPPI.MVAMethod = cms.untracked.string("BDTG")

process.flashggVBFMVA.UseJetID      = cms.untracked.bool(True)
process.flashggVBFMVA.JetIDLevel    = cms.untracked.string("Tight")

process.flashggVBFMVA.vbfMVAweightfile      = cms.FileInPath(
    "flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_CHS_BDTG.weights.xml"
)
process.flashggVBFMVAPUPPI.vbfMVAweightfile = cms.FileInPath(
    "flashgg/Taggers/test/MVATraining/weights/Flashgg_VBF_PUPPI_BDTG.weights.xml"
)

process.load("flashgg/Taggers/VBFMVADumper_cff")
process.VBFMVADumper.dumpTrees     = True
process.VBFMVADumper.dumpWorkspace = False
process.VBFMVADumper.quietRooFit   = True

process.load("flashgg/Taggers/VBFMVADumperPUPPI_cff")
process.VBFMVADumperPUPPI.dumpTrees     = True
process.VBFMVADumperPUPPI.dumpWorkspace = False
process.VBFMVADumperPUPPI.quietRooFit   = True

VBFMVAvariables=[
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
    "dijet_dipho_dphi    :=  dijet_dipho_dphi ",
    "dijet_dipho_pt      :=  dijet_dipho_pt   ",
    "dijet_dy            :=  dijet_dy ",
    "minDRJetPho         :=  minDRJetPho ",
    "vbfMvaResult        :=  vbfMvaResult"
]

preselection_cut="dijet_LeadJPt>30 && dijet_SubJPt>20 && dijet_leadEta<4.7 && dijet_leadEta>-4.7 && dijet_leadEta<4.7 && dijet_leadEta>-4.7 && dijet_Mjj>250 && leadPho_PToM>0.5"
#
# ===============================================================================
# setup the dumpers
cfgTools.addCategories(process.VBFMVADumper,
                       [## cuts are applied in cascade
        #("PreselVBFDiJet","%s" % preselection_cut ,0),
        ("VBFDiJet"      ,"dijet_LeadJPt > 0"     ,0),
        ("excluded"      ,"1"                     ,0) # really importent to avoid having an error
                       ],
                       variables  = VBFMVAvariables, 
                       histograms = []
)

process.VBFMVADumper.nameTemplate ="$PROCESS_$SQRTS_$LABEL_$SUBCAT"
cfgTools.addCategories(process.VBFMVADumperPUPPI,
                       [## cuts are applied in cascade
        ("PreselVBFDiJet","%s" % preselection_cut ,0),
        ("VBFDiJet"      ,"dijet_LeadJPt > 0"     ,0),
        ("excluded"      ,"1"                     ,0)
                       ],
                       variables  = VBFMVAvariables, 
                       histograms = []
                       
)
process.VBFMVADumperPUPPI.nameTemplate ="$PROCESS_$SQRTS_$LABEL_$SUBCAT"
#
# ======================================================================
# cutomize
from flashgg.MetaData.JobConfig import customize

customize.setDefault("maxEvents",-1)
customize.setDefault("targetLumi",1.e+4)
customize(process)

process.p = cms.Path(process.flashggTagSequence*
                     process.VBFMVADumper*
                     process.VBFMVADumperPUPPI
)

#process.e = cms.EndPath(process.out)
