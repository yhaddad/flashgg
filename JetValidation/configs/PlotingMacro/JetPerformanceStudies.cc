/** JetPerformanceStudies.cc --- 
 *
 * Copyright (C) 2014 yhaddad
 *
 * Author: yhaddad <y.haddad@imperial.ac.uk>
 *
 */

#include <map>
#include <iostream>
#include <TTree.h>
#include <TH1F.h>
#include <TFile.h>
#include <TH2F.h>
#include <TProfile.h>
#include <TCanvas.h>
#include "./roomacro.C"
#include <TMath.h>
#include <TCut.h>
#include <TGraphAsymmErrors.h>

TGraph* GetRocCurve(TGraph* gx, TGraph* gy, TString name){
  TGraph* roc = new TGraph();
  roc->SetName(name.Data());
  double* y = gx->GetY();
  double* x = gy->GetY();
  
  for(int i=0; i < gx->GetN(); i++ ){
    roc->SetPoint(i, 1-x[i], y[i]);
  }
  return roc;
}




void JetPerformanceStudies(){
  
  //double* pt_bins[] = {};
  
  std::map<TString,TCanvas*> Canv;
  
  std::map<TString,TTree*>     JetTree;
  std::map<TString,TTree*>     GenJetTree;
  
  std::map<TString,TH1F*>      h_pt_all;
  std::map<TString,TH1F*>      h_pt_sel;

  std::map<TString,TH1F*>      h_effpt_all;
  std::map<TString,TH1F*>      h_effpt_sel;
  
  
  std::map<TString,TGraphAsymmErrors*>      fake_rate_vs_pt;
  std::map<TString,TGraphAsymmErrors*>      fake_rate_vs_eat;
  
  std::map<TString,TGraphAsymmErrors*>      eff_vs_pt;
  std::map<TString,TGraphAsymmErrors*>      eff_vs_eat;

  std::map<TString,TGraph*>      roc_curve;
  
  TFile *file        = TFile::Open("/afs/cern.ch/work/y/yhaddad/jetValidationTrees_VBF_HToGG_PU20bx25.root");
  JetTree["PF"]      = (TTree*)file->Get("flashggJetValidationTreeMaker/jetTree_PF");
  JetTree["PFCHS0"]  = (TTree*)file->Get("flashggJetValidationTreeMakerPFCHS0/jetTree_PFCHS0"); 
  JetTree["PFCHSLeg"]= (TTree*)file->Get("flashggJetValidationTreeMakerPFCHSLeg/jetTree_PFCHSLeg"); 
  //JetTree["PUPPI0"]  = (TTree*)file->Get("flashggJetValidationTreeMakerPUPPI0/jetTree_PUPPI0"); 
  //JetTree["PUPPILeg"]= (TTree*)file->Get("flashggJetValidationTreeMakerPUPPILeg/jetTree_PUPPILeg"); 
  
  GenJetTree["PF"]      = (TTree*)file->Get("flashggJetValidationTreeMaker/genJetTree_PF");
  GenJetTree["PFCHS0"]  = (TTree*)file->Get("flashggJetValidationTreeMakerPFCHS0/genJetTree_PFCHS0"); 
  GenJetTree["PFCHSLeg"]= (TTree*)file->Get("flashggJetValidationTreeMakerPFCHSLeg/genJetTree_PFCHSLeg"); 
  //GenJetTree["PUPPI0"]  = (TTree*)file->Get("flashggJetValidationTreeMakerPUPPI0/jetTree_PUPPI0"); 
  //GenJetTree["PUPPILeg"]= (TTree*)file->Get("flashggJetValidationTreeMakerPUPPILeg/jetTree_PUPPILeg"); 
  //====> cuts
  
  TCut cut_photon_rej = "!(photonMatch==1 && GenPhotonPt/bestPt > 0.5 && photondRmin < 0.2)";
  TCut cut_PUID       = "passesPUJetID";
  TCut cut_pt         = "bestPt>20.";
  TCut cut_jetmatch   = "genJetMatch";
  
  TCut cut_all = cut_pt && cut_photon_rej && cut_PUID;
  //TCut cut_sel = cut_pt && cut_jetmatch   && cut_photon_rej && cut_PUID;
  
  // ===> Only for def
  for (std::map<TString,TTree*>::iterator it=JetTree.begin(); it!=JetTree.end(); ++it){
    h_pt_all[it->first] = new TH1F(Form("h_pt_all_%s",it->first.Data()),
				   Form("%s;p_{t};#varepsilon_{fake}",it->first.Data()),
				   50,0,200);
    h_pt_sel[it->first] = new TH1F(Form("h_pt_sel_%s",it->first.Data()),
				   Form("%s;p_{t};#varepsilon_{fake}",it->first.Data()),
				   50,0,200);

    h_effpt_all[it->first] = new TH1F(Form("h_effpt_all_%s",it->first.Data()),
				   Form("%s;p_{t};#varepsilon_{fake}",it->first.Data()),
				   50,0,200);
    h_effpt_sel[it->first] = new TH1F(Form("h_effpt_sel_%s",it->first.Data()),
				   Form("%s;p_{t};#varepsilon_{fake}",it->first.Data()),
				   50,0,200);
    
    JetTree[it->first]->Draw(Form("bestPt>>h_pt_all_%s",it->first.Data()),cut_all,"");
    JetTree[it->first]->Draw(Form("bestPt>>h_pt_sel_%s",it->first.Data()),cut_all && !cut_jetmatch,"");
    
    fake_rate_vs_pt[it->first] = new TGraphAsymmErrors(h_pt_sel[it->first], h_pt_all[it->first]);
    fake_rate_vs_pt[it->first] -> SetName(Form("g_fake_%s",it->first.Data()));
    fake_rate_vs_pt[it->first] -> SetTitle(Form("%s;p_{t};#varepsilon_{fake}",it->first.Data()));
  
    h_pt_all[it->first]->Clear();
    h_pt_sel[it->first]->Clear();
    
    GenJetTree[it->first]->Draw(Form("pt>>h_effpt_all_%s",it->first.Data()), "pt > 20","");
    GenJetTree[it->first]->Draw(Form("pt>>h_effpt_sel_%s",it->first.Data()), "recoJetMatch==1 && pt>20","");
    
    eff_vs_pt[it->first] = new TGraphAsymmErrors(h_effpt_sel[it->first], h_effpt_all[it->first]);
    eff_vs_pt[it->first] -> SetName(Form("g_eff_%s",it->first.Data()));
    eff_vs_pt[it->first] -> SetTitle(Form("%s;p_{t};#varepsilon",it->first.Data()));
    
    roc_curve[it->first] = GetRocCurve(eff_vs_pt[it->first],
				       fake_rate_vs_pt[it->first],
				       it->first);
    
  }
  
  std::cout << "====> ploting"<< std::endl;
  std::cout << "      fake rate"<< std::endl;
  TCanvas *c_fake_pt  = new TCanvas("c_fake_pt","",500,500);
  c_fake_pt->cd();
  int count = 1;
  TMultiGraph *gmul_fake_pt = new TMultiGraph();
  for (std::map<TString,TTree*>::iterator it=JetTree.begin(); it!=JetTree.end(); ++it){
    fake_rate_vs_pt[it->first]->SetLineColor  (count);//int(55 + count*10));
    fake_rate_vs_pt[it->first]->SetMarkerColor(count);//int(55 + count*10));
    gmul_fake_pt->Add(fake_rate_vs_pt[it->first]);
    count++;
  }
  gmul_fake_pt->Draw("AP");
  Draw3Legend(fake_rate_vs_pt["PF"],
	      fake_rate_vs_pt["PFCHS0"],
	      fake_rate_vs_pt["PFCHSLeg"],
	      "PF",
	      "PFCHS0",
	      "PFCHSLeg");
  
  std::cout << "      efficiency"<< std::endl;
  TCanvas *c_eff_pt  = new TCanvas("c_eff_pt","",500,500);
  c_eff_pt->cd();
  count = 1;
  TMultiGraph *gmul_eff_pt = new TMultiGraph();
  for (std::map<TString,TTree*>::iterator it=JetTree.begin(); it!=JetTree.end(); ++it){
    eff_vs_pt[it->first]->SetLineColor  (count);//int(55 + count*10));
    eff_vs_pt[it->first]->SetMarkerColor(count);//int(55 + count*10));
    gmul_eff_pt->Add(eff_vs_pt[it->first]);
    count++;
  }
  gmul_eff_pt->Draw("AP");
  Draw3Legend(eff_vs_pt["PF"],
	      eff_vs_pt["PFCHS0"],
	      eff_vs_pt["PFCHSLeg"],
	      "PF",
	      "PFCHS0",
	      "PFCHSLeg");

  TCanvas *c_roc  = new TCanvas("c_roc","",500,500);
  c_roc->cd();
  count = 1;
  TMultiGraph *gmul_roc = new TMultiGraph();
  for (std::map<TString,TTree*>::iterator it=JetTree.begin(); it!=JetTree.end(); ++it){
    roc_curve[it->first]->SetLineColor  (count);//int(55 + count*10));
    roc_curve[it->first]->SetMarkerColor(count);//int(55 + count*10));
    gmul_roc->Add(roc_curve[it->first]);
    count++;
  }
  gmul_roc->Draw("AP");
  Draw3Legend(roc_curve["PF"],
	      roc_curve["PFCHS0"],
	      roc_curve["PFCHSLeg"],
	      "PF",
	      "PFCHS0",
	      "PFCHSLeg");
  
}
