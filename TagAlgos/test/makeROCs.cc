#include "TH1.h"
#include <iostream>
#include "TTree.h"
#include "TFile.h"
#include "TCanvas.h"
#include "TLegend.h"
#include "TStyle.h"
#include "TGraph.h"
#include "TMultiGraph.h"
#include "TString.h"
#include <sstream>

TGraph* makeROC2 (TH1 *sig, TH1* bkg, TLegend *leg, int tc){
  
  gStyle->SetOptStat(0);
  sig->Sumw2(0);
  bkg->Sumw2(0);
  TGraph *g_e = new TGraph();
  
  g_e->SetMarkerColor(tc);
  g_e->SetLineColor(tc);
  g_e->SetMarkerSize(1);
  //g_e->SetMarkerStyle(21);
  
  bool printFlag =0;
  int N0 = bkg->GetNbinsX();
  const unsigned int N =N0;
  float y[N];
  float signal[N];
  int i=0;
  
  for (unsigned int n =0; n<N; n++){
    signal[n]=  sig->Integral(0,n)/ sig->Integral(0,N);
    y[n]     =  (bkg->Integral(0,n)/ bkg->Integral(0,N));
    
    if (y[n]==0) {
      i++;
      continue;
    }
    
    if (signal[n] >0.98 && printFlag==0){
      std::cout << "Better than 97 pc eff.(" 
		<< signal[n] << "). Bin " 
		<< n << ", x value " 
		<< n*sig->GetBinWidth(n) << std::endl;
      
      printFlag =1;
    }
    //g_e->SetPoint(n-i,1-signal[n], y[n]);
    g_e->SetPoint(n-i,1-y[n],1-signal[n]);
    
    //use 1-n for signal because I am integrating from bin 0 to bin N, which is techincally asking how to reject signal.
  }
  g_e->SetTitle(Form("ROCs_%i",tc));
  
  
  //g_e->GetXaxis()->SetRangeUser(0,1);
  //g_e->GetXaxis()->SetTitle("background efficiency");
  //g_e->GetYaxis()->SetRangeUser(0,1);
  //g_e->GetYaxis()->SetTitle("signal efficiency");
  //
  //if (tc ==1){
  //  g_e->Draw("apl same");
  //} else {
  //  g_e->Draw("pl same");
  //}
  //g_g->Draw("pl same");:w
  //
  //g_eg->Draw("pl same");
  //std::string name2 = name.str().replace(name.str().find("_signal_h"), 6, "");
  
  if (tc ==1){
    leg->AddEntry(g_e,"current FLASHgg MVA","lep");
  } else {
    leg->AddEntry(g_e,"retrained MVA","lep");
  }
  return g_e;
  //leg->Draw();
}

void makeROC (TH1 *sig, TH1* bkg, TLegend *leg, int tc){
  
  gStyle->SetOptStat(0);
  sig->Sumw2(0);
  bkg->Sumw2(0);
  TGraph *g_e = new TGraph();
  
  g_e->SetMarkerColor(tc);
  g_e->SetLineColor(tc);
  g_e->SetMarkerSize(1);
  //g_e->SetMarkerStyle(21);
  
  bool printFlag =0;
  int N0 = bkg->GetNbinsX();
  const unsigned int N =N0;
  float y[N];
  float signal[N];
  int i=0;
  for (unsigned int n =0; n<N; n++){
    
    
    signal[n]=sig->Integral(0,n)/ sig->Integral(0,N);
    
    y[n]=  (bkg->Integral(0,n)/ bkg->Integral(0,N));
    
    if (y[n]==0) {
      i++;
      continue;
    }
    if (signal[n] >0.98 && printFlag==0){
      
      std::cout << "Better than 97 pc eff.(" << signal[n] << "). Bin " << n << ", x value " << n*sig->GetBinWidth(n) << std::endl;
      printFlag =1;
    }
    g_e->SetPoint(n-i,1-signal[n], y[n]);
    //use 1-n for signal because I am integrating from bin 0 to bin N, which is techincally asking how to reject signal.
    
    
  }
  g_e->SetTitle("ROCs");
  
  
  
  g_e->GetXaxis()->SetTitle("signal efficiency");
  g_e->GetXaxis()->SetRangeUser(0,1);
  g_e->GetYaxis()->SetRangeUser(0,1);
  g_e->GetYaxis()->SetTitle("background rejection");
  if (tc ==1){
    g_e->Draw("apl same");
  } else {
    g_e->Draw("pl same");

  }
  //g_g->Draw("pl same");:w
  //
  //g_eg->Draw("pl same");
  //std::string name2 = name.str().replace(name.str().find("_signal_h"), 6, "");

  if (tc ==1){
    leg->AddEntry(g_e,"current FLASHgg MVA","lep");
  } else {
    leg->AddEntry(g_e,"retrained MVA","lep");
  }

  //leg->Draw();
}


void makeROCs(){

  
  
  TString path("${WORKSPACE}/VBFTagging/test_vbfmva_compare/");
  
  //
  TFile *f_sig = TFile::Open(path + "output_VBF_HToGG_M-125_13TeV-powheg-pythia6_numEvent10000_histos.root");
  TH1F *old_sig = (TH1F*) f_sig->Get("VBFMVADumper/histograms/vbf_m125_13TeV_AllVBFMVAValue");
  TH1F *new_sig = (TH1F*) f_sig->Get("VBFMVADumperNew/histograms/vbf_m125_13TeV_AllNewVBFMVAValue");
  
  TFile *f_bkg = TFile::Open(path + "output_GJet_Pt40_doubleEMEnriched_TuneZ2star_13TeV-pythia6_numEvent10000_histos.root");
  TH1F *old_bkg = (TH1F*) f_bkg->Get("VBFMVADumper/histograms/gamJet_13TeV_AllVBFMVAValue");
  TH1F *new_bkg = (TH1F*) f_bkg->Get("VBFMVADumperNew/histograms/gamJet_13TeV_AllNewVBFMVAValue");
  
  std::cout << "plotting" << std::endl;
    
  //old_sig->Draw();
  //new_sig->Draw("same");
  

  TCanvas *c1 = new TCanvas("c1","",600,600);
  c1->cd();
  
  std::vector<std::string> xxx;//={"signal","hgg"};
  xxx.push_back("current MVA");
  xxx.push_back("retrained MVA");
  
  int itc=1;
  TLegend *leg = new TLegend(0.3,0.3,0.65,0.5);
  
  TMultiGraph *mul  = new TMultiGraph();
  
  mul->Add(makeROC2( old_sig, old_bkg,leg, itc));
  itc++;
  mul->Add(makeROC2(new_sig, new_bkg,leg, itc));
  mul->SetTitle(";background efficiency;signal efficiency");
  //mul->GetXaxis()->SetTitle("signal efficiency");
  //mul->GetXaxis()->SetRangeUser(0,1);
  //mul->GetYaxis()->SetRangeUser(0,1);
  //mul->GetYaxis()->SetTitle("background rejection");
  
  mul->Draw("APL");
  leg->Draw();
  //c1->Print("ROCs.pdf");
  
  //c1.Draw();
}

