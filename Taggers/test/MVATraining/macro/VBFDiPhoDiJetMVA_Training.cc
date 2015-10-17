///==== include ====
#include "TFile.h"
#include "TChain.h"
#include "TMinuit.h"
#include <sstream>
#include <iostream>
#include "TMVA/Factory.h"
#if not defined(__CINT__) || defined(__MAKECINT__)
#include "TMVA/Tools.h"
#include "TMVA/Reader.h"
#include <map>
//#include "TMVAGui.C"

#endif
using namespace std;

// --------- MAIN -------------------
void VBFDiPhoDiJetMVA_Training( TString Nevent = "10000", TString Level = "VBFDiPhoDiJet", TString JetPUType = "CHS", bool skipEvtWNoVBF = true )
{
    // you must define $WORKSPACE first
    TString path= "./test_diphodijet_training/";

    bool useDiphotonPt = 0;
    bool usePhotonsPt = true;
    
    if (JetPUType == "CHS") JetPUType = ""; // yeah !! 
    
    std::map<TString, TString> samples_name;
    std::map<TString, TTree*> inputTrees;
    std::map<TString, TFile*> inputFiles;
    
    // the file sample names
    samples_name["vbf_m125_13TeV"     ] =  path + "output_VBFHToGG_M-125_13TeV_powheg_pythia8_numEvent" + Nevent + "_histos.root";
    samples_name["gamJet40toInf_13TeV"] =  path + "output_GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8_numEvent" + Nevent + "_histos.root";
    samples_name["gamJet20to40_13TeV" ] =  path + "output_GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8_numEvent" + Nevent + "_histos.root";
    samples_name["ggf_m125_13TeV"     ] =  path + "output_GluGluHToGG_M-125_13TeV_powheg_pythia8_numEvent" + Nevent + "_histos.root";
    samples_name["dy_toll_m50_13TeV"  ] =  path + "output_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_numEvent" + Nevent + "_histos.root";
    samples_name["gamgamjetbox_13TeV" ] =  path + "output_DiPhotonJetsBox_MGG-80toInf_13TeV-Sherpa_numEvent" + Nevent + "_histos.root";
    samples_name["qcd_30to40_13TeV"   ] =  path + "output_QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8_numEvent" + Nevent + "_histos.root";
    samples_name["qcd_30toInf_13TeV"  ] =  path + "output_QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8_numEvent" + Nevent + "_histos.root";
    samples_name["qcd_40toInf_13TeV"  ] =  path + "output_QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8_numEvent" + Nevent + "_histos.root";
    for(std::map<TString, TString>::iterator it = samples_name.begin();
        it != samples_name.end(); it++){
        inputFiles[it->first] = TFile::Open( it->second );
        inputTrees[it->first] = (TTree*)inputFiles[it->first]->Get( Level + "MVADumper" + JetPUType + "/trees/" + it->first + "_PreselVBFDiJet" );
    }
    
    // Declaration of leaf types
    // float dijet_mva       ;
    // float dipho_mva       ;
    // float dipho_PToM      ;
    // float dijet_abs_dEta  ;
    // float dijet_leadEta   ;
    // float dijet_subleadEta;
    // float dijet_LeadJPt   ;
    // float dijet_SubJPt    ;
    // float dijet_Zep       ;
    // float dijet_Mjj       ;
    // float leadPho_PToM    ;
    // float sublPho_PToM    ;
    // float dijet_dPhi_trunc;
    
    //if( Level == "VBFDiPhoDiJet" ) {
    //    treeS->SetBranchAddress( "dipho_mva"       , &dipho_mva );
    //    treeS->SetBranchAddress( "dijet_mva"       , &dijet_mva );
    //    treeS->SetBranchAddress( "dipho_PToM"      , &dipho_PToM );
    //} else  if( Level == "VBF" ) {
    //    treeS->SetBranchAddress( "dijet_abs_dEta"  , &dijet_abs_dEta );
    //    treeS->SetBranchAddress( "dijet_leadEta"   , &dijet_leadEta );
    //    treeS->SetBranchAddress( "dijet_subleadEta", &dijet_subleadEta );
    //    treeS->SetBranchAddress( "dijet_LeadJPt"   , &dijet_LeadJPt );
    //    treeS->SetBranchAddress( "dijet_SubJPt"    , &dijet_SubJPt );
    //    treeS->SetBranchAddress( "dijet_Zep"       , &dijet_Zep );
    //    treeS->SetBranchAddress( "dijet_Mjj"       , &dijet_Mjj );
    //    treeS->SetBranchAddress( "dipho_PToM"      , &dipho_PToM );
    //    treeS->SetBranchAddress( "leadPho_PToM"    , &leadPho_PToM );
    //    treeS->SetBranchAddress( "sublPho_PToM"    , &sublPho_PToM );
    //    treeS->SetBranchAddress( "dijet_dPhi_trunc", &dijet_dPhi_trunc );
    //}


    // Create a new root output file.
    TString outputFileName;
    if( Level == "VBF" ) {
        outputFileName = "Flashgg_VBF_" + JetPUType;
    } else {
        outputFileName = "Flashgg_DiPhoDiJet_" + JetPUType;
    }

    // -- reader
    TFile *outputFile = TFile::Open( ( outputFileName + ".root" ).Data(), "RECREATE" );
    TMVA::Factory *factory = new TMVA::Factory( outputFileName.Data(), outputFile,
            "!V:!Silent:Color:DrawProgressBar:Transformations=I;D;P;G,D:AnalysisType=Classification" );
    // -- variables
    if( Level == "VBFDiPhoDiJet" ) {
        factory->AddVariable( "dipho_mva" );
        factory->AddVariable( "dijet_mva" );
        factory->AddVariable( "dipho_PToM" );
    
    } else  if( Level == "VBF" ) {
        
        factory->AddVariable( "dijet_LeadJPt" );
        factory->AddVariable( "dijet_SubJPt" );
        factory->AddVariable( "dijet_abs_dEta" );
        factory->AddVariable( "dijet_Mjj" );
        factory->AddVariable( "dijet_Zep" );
        factory->AddVariable( "dijet_dPhi_trunc" );
        
        //if( useDiphotonPt ) {
        factory->AddVariable( "dipho_PToM" );
        factory->AddVariable( "leadPho_PToM" );
        factory->AddVariable( "sublPho_PToM" );
        // new var
        factory->AddVariable( "dijet_dy" );
        factory->AddVariable( "minDRJetPho" );
        //}
    }
    
    
    //event weights per tree (see below for setting event-wise weights)
    Double_t signalWeight = 1.0;
    Double_t backgroundWeight = 1.0;


    // ====== register trees ====================================================
    factory->AddSignalTree( inputTrees["vbf_m125_13TeV"], signalWeight         , "Training" );
    factory->AddSignalTree( inputTrees["vbf_m125_13TeV"], signalWeight         , "Test" );
    for(std::map<TString, TTree*>::iterator it = inputTrees.begin();
        it != inputTrees.end(); it++){
        if (it->first.Contains("vbf_m125_13TeV") ) continue;
        factory->AddBackgroundTree( it->second, backgroundWeight , "Training" );
        factory->AddBackgroundTree( it->second, backgroundWeight , "Test" );
    }
    // == supress the the negative points on the input variables
    factory->SetSignalWeightExpression("weight");
	factory->SetBackgroundWeightExpression("weight");
    
    // == this high correlation between variables
    TCut mycuts = "weight>0"; // " leadPho_PToM > (60./120.) && sublPho_PToM> (30./120.)";
    TCut mycutb = "weight>0"; // " leadPho_PToM> (60./120.) && sublPho_PToM> (30./120.)";
    if( skipEvtWNoVBF ) {
        mycuts += TCut("dipho_PToM>=0"); // Skip the event with -999
        mycutb += TCut("dipho_PToM>=0"); //
    }
    
    // tell the factory to use all remaining events in the trees after training for testing:
    factory->PrepareTrainingAndTestTree( mycuts, mycutb,
                                         "SplitMode=Random:NormMode=NumEvents:!V" );
    // Boosted Decision Trees: use BDTG ( Gradient Boost )
    factory->BookMethod( TMVA::Types::kBDT, "BDTG",
                         "!H:!V:NTrees=1000:BoostType=Grad:Shrinkage=0.30:UseBaggedGrad:GradBaggingFraction=0.6:SeparationType=GiniIndex:nCuts=20:NNodesMax=5:MaxDepth=3" );
    factory->BookMethod( TMVA::Types::kBDT, "BDT",
                         "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20" );
    //"!H:!V:NTrees=1000:BoostType=Grad:Shrinkage=0.30:UseBaggedGrad:GradBaggingFraction=0.6:SeparationType=GiniIndex:nCuts=20:NNodesMax=15:MaxDepth=5" );
    // book Cuts
    //factory->BookMethod( TMVA::Types::kCuts, "CutsGA",
    // "H:!V:FitMethod=GA:CutRangeMin[0]=20:CutRangeMax[0]=500:CutRangeMin[1]=20:CutRangeMax[1]=500:VarProp=FSmart:VarProp[4]=FMin:EffSel:Steps=30:Cycles=3:PopSize=500:SC_steps=10:SC_rate=5:SC_factor=0.95" );
    // ---- Now you can tell the factory to train, test, and evaluate the MVAs
    // Train MVAs using the set of training events
    factory->TrainAllMethods();
    // ---- Evaluate all MVAs using the set of test events
    factory->TestAllMethods();
    // ----- Evaluate and compare performance of all configured MVAs
    factory->EvaluateAllMethods();
    // --------------------------------------------------------------
    // Save the output
    outputFile->Close();
    std::cout << "==> Wrote root file: " << outputFile->GetName() << std::endl;
    std::cout << "==> TMVAClassification is done!" << std::endl;
    delete factory;

    //if (!gROOT->IsBatch()) TMVAGui( (outputFileName+".root").c_str() );
}
// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

