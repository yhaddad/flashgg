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

#include "TMVAGui.C"

#endif
using namespace std;
// --------- MAIN -------------------
void jetvarMVA(int catbin=1)
//void VBFMVA_Training(int argc, char** argv)
{
  // options
  TCut cat;
  TString catname;
  if(catbin == 1 ){
    cat = "abs(eta) < 2.5";
    catname = "  (|#eta| < 2.5)";
  }else if(catbin ==2){
    cat = "abs(eta) > 2.5 && abs(eta) < 3";
    catname = "(2.5 <|#eta| < 3.0)";
  }else if(catbin ==3){
    cat = "abs(eta) > 3";
    catname = "  (|#eta| > 3.0)";
  }
  // you must define $WORKSPACE first
  TString path("${WORKSPACE}/");
  TFile *inputf = TFile::Open(path + "TEST_jetValTrees_VBF_HToGG.root");
  
  // for the moment looking only on the PF jets
  TTree *tree_in = (TTree*)inputf->Get("flashggJetValidationTreeMaker/jetTree_PF");
  
  TCut commonCut = "bestPt>20.0 && !(photonMatch==1)" ;
  
  TCut mycuts = TCut("genJetMatch==1") && commonCut && cat ;// " leadPho_PToM > (60./120.) && sublPho_PToM> (30./120.)";
  TCut mycutb = TCut("genJetMatch==0") && commonCut && cat ;// " leadPho_PToM> (60./120.) && sublPho_PToM> (30./120.)";
  
  std::cout << " ---- yacine :: the jets selection " << std::endl;
  std::cout << " ---- yacine :: cut s ("<< mycuts <<") " << std::endl;
  std::cout << " ---- yacine :: cut b ("<< mycutb <<") " << std::endl;
  
  std::cout << " ---- yacine :: trees copy " << std::endl;
  TTree *tree_s    = tree_in->CopyTree(mycuts);
  TTree *tree_b    = tree_in->CopyTree(mycutb);
  std::cout << " ---- yacine :: trees s ("<< tree_s->GetEntries() <<") " << std::endl;
  std::cout << " ---- yacine :: trees b ("<< tree_b->GetEntries() <<") " << std::endl;
  
  //float  betaStar        = 0;
  //float  rms             = 0;
  //float  W               = 0;
  //float  dR2Mean         = 0;
  //float  dRMean          = 0;
  //float  dZ              = 0;
  //float  ptD             = 0;
  //
  //
  //tree->SetBranchAddress("betaStar  ", &betaStar  );
  //tree->SetBranchAddress("rms       ", &rms       );
  //tree->SetBranchAddress("W         ", &W         );
  //tree->SetBranchAddress("dR2Mean   ", &dR2Mean   );
  //tree->SetBranchAddress("dRMean    ", &dRMean    );
  //tree->SetBranchAddress("dZ        ", &dZ        );
  //tree->SetBranchAddress("ptD       ", &ptD       );
  
  // Create a new root output file.
  string outputFileName = "Yacine";
  outputFileName = outputFileName +"_pujid";
  
  TFile* outputFile = TFile::Open((outputFileName+".root").c_str(), "RECREATE" );
  TMVA::Factory* factory = new TMVA::Factory(outputFileName.c_str(), outputFile,
					     "!V:!Silent:Color:DrawProgressBar:Transformations=I;D;P;G,D:AnalysisType=Classification" );
  // -- variables
  factory->AddVariable( "betaStar  ");
  factory->AddVariable( "log(dZ)   ");
  factory->AddVariable( "rms       ");
  factory->AddVariable(	"nPV       ");
  factory->AddVariable(	"nJets     ");
  
  // -- spectators
  Double_t signalWeight     = 1.0;
  Double_t backgroundWeight = 1.0;
  
  factory->AddSignalTree    ( tree_s, signalWeight    , "Training" );
  factory->AddSignalTree    ( tree_s, signalWeight    , "Test"     );
  
  factory->AddBackgroundTree( tree_b, backgroundWeight, "Training" );
  factory->AddBackgroundTree( tree_b, backgroundWeight, "Test"     );
  
  // tell the factory to use all remaining events in the trees after training for testing:
  factory->PrepareTrainingAndTestTree( "", "",
				       "SplitMode=Random:NormMode=NumEvents:!V" );
  // Boosted Decision Trees: use BDTG ( Gradient Boost )
  factory->BookMethod( TMVA::Types::kBDT, "BDTG",
		       "!H:!V:NTrees=1000:BoostType=Grad:Shrinkage=0.30:UseBaggedGrad:GradBaggingFraction=0.6:SeparationType=GiniIndex:nCuts=20:NNodesMax=5:MaxDepth=3" );
  
  //factory->BookMethod( TMVA::Types::kBDT, "BDT",		       "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20" );
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
  
  if (!gROOT->IsBatch()) TMVAGui( (outputFileName+".root").c_str() );
}
