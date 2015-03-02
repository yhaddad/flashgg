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
#include <TAxis.h>
#include <TGraphAsymmErrors.h>
#include <TGraphErrors.h>
#include <TGraph2D.h>
#include <TH2F.h>
#include <assert.h>


TGraph *GetEff(TH1* h, TString name, int color=1){
  int NBins = h->GetNbinsX();
  float sum = h->Integral(1,NBins);
    
  TGraph *gr = new TGraph();
  gr->SetName(name.Data());
  gr->SetMarkerColor(color);
  gr->SetFillStyle(0);
  
  for (int ib=1; ib<NBins; ib++) {
    float x=h->Integral(ib,NBins);
    float eff = 1.0-(x/sum);
    gr->SetPoint(ib-1,h->GetBinCenter(ib),eff);
  }
  gr->SetTitle(Form(";%s;efficiency",h->GetXaxis()->GetTitle()));
  return gr; 
}

TGraph *GetRjc(TH1* h, TString name, int color=1){
  int NBins = h->GetNbinsX();
  float sum = h->Integral(1,NBins);
  
  TGraph *gr = new TGraph();
  gr->SetName(name.Data());
  gr->SetMarkerColor(color);
  gr->SetFillStyle(0);
  
  for (int ib=1; ib<NBins; ib++) {
    float x=h->Integral(ib,NBins);
    float eff = 1.0 - (x/sum);
    gr->SetPoint(ib-1,h->GetBinCenter(ib),1-eff);
  }
  gr->SetTitle(Form(";%s;rejection",h->GetXaxis()->GetTitle()));
  return gr; 
}

TGraph *GetROC(TH1* h_sig, TH1 *h_bkg, TString name, int color=1){
  int nx_bins = h_sig->GetNbinsX();
  int ny_bins = h_bkg->GetNbinsX();
  
  std::cout << "nx: " << nx_bins
	    << "ny: " << ny_bins
	    << std::endl;
  assert(nx_bins == ny_bins); 
  

  
  float sumx = h_sig->Integral(1,nx_bins);
  float sumy = h_bkg->Integral(1,ny_bins);
  
  TGraph *gr = new TGraph();
  gr->SetName(name.Data());
  gr->SetMarkerColor(color);
  gr->SetFillStyle(0);
  
  
  for (int ib=1; ib<nx_bins; ib++) {
    float x=h_sig->Integral(ib,nx_bins);
    float y=h_bkg->Integral(ib,ny_bins);
    float eff = 1.0 - (x/sumx);
    float rjc = (y/sumy);
    gr->SetPoint(ib-1,eff,rjc);
  }
  gr->SetTitle(Form("%s;#varepsilon(signal);1-#varepsilon (background)",h_sig->GetXaxis()->GetTitle()));
  return gr; 
}


TH2F *Get2DEff(TH2* h2, TString name, TString option="eff"){
  Int_t nx_bins = h2->GetNbinsX();
  Int_t ny_bins = h2->GetNbinsY();
  
  float sum = h2->Integral(1, int(nx_bins),1, int(ny_bins),"");
  
  
  TString hname;
  if(option =="eff") hname = Form("True Jet Efficiency;%s;%s;#varepsilon",h2->GetXaxis()->GetTitle(),h2->GetYaxis()->GetTitle());
  if(option =="rjc") hname = Form("PU Jet rejection;%s;%s;1-#varepsilon",h2->GetXaxis()->GetTitle(),h2->GetYaxis()->GetTitle());
  
  TH2F *hout = new TH2F(name,hname,
			250,0,1.0,
			250,0,0.1);
  
  for (int i=1; i<nx_bins; i++) {
    for (int j=1; j<nx_bins; j++) {
      Double_t frac = h2->Integral(1,i,1,j);
      Double_t eff  = 0;
      if(option == "eff"){
	eff =   (frac/sum);
      }else if(option == "rjc"){
	eff = 1-(frac/sum);
      }
      hout->SetBinContent(i,j,eff);
    }
  }
  return hout; 
}


void DrawRatio(TH1 *h1, TH1* h2, TString name=""){ // Draw h1/h2
  
  TCanvas *c1 = new TCanvas(name+"_c",name,600,700);
  
  TPad *pad1 = new TPad("pad1","pad1",0,0.3,1,1);
  pad1->SetBottomMargin(0);
  pad1->Draw();
  pad1->cd();
  //
  //h1->SetMinimum(0);  // Define Y ..
  //h1->SetMaximum(0.3);  // Define Y ..
  //h1->GetYaxis()->SetRangeUser(0,0.3);
  //h2->GetYaxis()->SetRangeUser(0,0.3);
  h1->Draw("");
  h2->Draw("same");
  //pad1->SetLogy();
  c1->cd();
  
  TPad *pad2 = new TPad("pad2","pad2",0,0,1,0.3);//0,0,1,0.3
  pad2->SetTopMargin(0);
  pad2->SetBottomMargin(0.2); 
  pad2->Draw();
  pad2->cd();
  
  // Define the ratio plot
  TH1F *h3 = (TH1F*)h1->Clone("h3");
  h3->SetLineColor(kBlack);
  h3->SetTitle(";p_{T} [GeV];Weight");
  h3->SetMinimum(0);  // Define Y ..
  h3->SetMaximum(10); // .. range
  h3->Sumw2();
  h3->SetStats(0);      // No statistics on lower plot
  h3->Divide(h2);
  h3->SetMarkerStyle(21);
  h3->Draw("ep");       // Draw the ratio plot
  
}


TH2F *Get2DPurity(TH2* hs,TH2F* hb, TString name){
  Int_t nx_bins = hs->GetNbinsX();
  Int_t ny_bins = hs->GetNbinsY();
  
  float sums = hs->Integral(1, int(nx_bins),1, int(ny_bins),"");
  float sumb = hb->Integral(1, int(nx_bins),1, int(ny_bins),"");
  
  
  TString hname;
  hname = Form("%s  purity ;%s;%s;#varepsilon",name.Data(),hs->GetXaxis()->GetTitle(),hs->GetYaxis()->GetTitle());
  
  TH2F *hout = new TH2F(name,hname,
			250,0,1.0,
			250,0,0.1);
  
  for (int i=1; i<nx_bins; i++) {
    for (int j=1; j<nx_bins; j++) {
      Double_t sf = hs->Integral(1,i,1,j)/sums;
      Double_t bf = hb->Integral(1,i,1,j)/sumb;
      Double_t purity = 0;
      
      //if(sf ==0  && bf ==0 ) purity = 0;
      //else purity = sf/sqrt(sf+bf);
      purity = sf *(1-bf);
      hout->SetBinContent(i,j,purity);
    }
  }
  return hout; 
}


void JetShapeReWeight(int catbin=1){
  
  //double xbin[]={20,22,26,34,50,72,136,264,520}; 
  double xbin[]={20,30,40,50,60,70,80,100,150,200,300}; 
  
  
  std::map<TString,TTree*>     JetTree;
  
  std::map<TString,TH1F*>     h_pt;
  
  std::map<TString,TCanvas*> Canv;
  
  TFile *file_VBF =  TFile::Open("/afs/cern.ch/work/y/yhaddad/VBF_HToGG_M-125_13TeV_JetValidationTree.root");
  TFile *file_GGF =  TFile::Open("/afs/cern.ch/work/y/yhaddad/GluGluToHToGG_M-125_13TeV_JetValidationTree.root");
  
  JetTree["VBF"] = (TTree*)file_VBF->Get("flashggJetValidationTreeMaker/jetTree_PF");
  JetTree["GGF"] = (TTree*)file_GGF->Get("flashggJetValidationTreeMaker/jetTree_PF");
  
  //====> cuts
  TCut cat;
  TString catname;
  if(catbin == 1 ){
    cat = "abs(eta) < 2.5";
    catname = "(|#eta| < 2.5)";
  }else if(catbin ==2){
    cat = "abs(eta) > 2.5 && abs(eta) < 3";
    catname = "(2.5 <|#eta| < 3.0)";
  }else if(catbin ==3){
    cat = "abs(eta) > 3";
    catname = "(|#eta| > 3.0)";
  }
  
  TCut cut_photon_rej     = "!(photonMatch==1 && photondRmin < 0.2)";
  TCut cut_gen_photon_rej = "!(photonMatch==1 && photondRmin < 0.2)";
  TCut cut_pt             = "bestPt>20.0";
  TCut cut_genjetmatch    = "genJetMatch==1";
  
  //TString  sampleName = "";
  //if     (sample == "VBF") sampleName = "VBF(H#rightarrow#gamma#gamma) 13TeV";
  //else if(sample == "GGF") sampleName = "GGF(H#rightarrow#gamma#gamma) 13TeV";
  
  TCut cut_PUJ = cut_pt && cut_photon_rej && cat &&!cut_genjetmatch;
  TCut cut_JET = cut_pt && cut_photon_rej && cat && cut_genjetmatch;
  
  // ===> Only for def
  std::cout << ":: PUJ == " << cut_PUJ.GetTitle() << std::endl;
  std::cout << ":: JET == " << cut_JET.GetTitle() << std::endl;
  
  for (std::map<TString,TTree*>::iterator it=JetTree.begin(); it!=JetTree.end(); ++it){
    h_pt[it->first] = new TH1F(Form("h_pt_%s",it->first.Data()),
			       Form("%s %s;p_{T} [GeV];n_{jets}", it->first.Data(),catname.Data()),
			       (sizeof(xbin)/sizeof(xbin[0]))-1,xbin);
    
    JetTree[it->first]->Project(Form("h_pt_%s",it->first.Data()),"bestPt",cut_JET,"");
  }
  
  //Canv["pts"] = new TCanvas("pts","pt",500,500);
  //gPad->SetLogy();
  h_pt["VBF"]->SetLineColor(kRed);
  //h_pt["GGF"]->SetLineColor(kBlue);
  //h_pt["VBF"]->Scale(1.0/h_pt["VBF"]->GetEntries());
  h_pt["GGF"]->Scale(h_pt["VBF"]->GetEntries()/h_pt["GGF"]->GetEntries());
  
  DrawRatio(h_pt["VBF"],h_pt["GGF"],"pt");
  //h_pt["GGF"]->DrawNormalized("");
  //h_pt["VBF"]->DrawNormalized("same");
  
  
}
