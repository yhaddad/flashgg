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

void DrawVariable(TH1 *h1, TH1 *h2, TString name="", bool logy=false, bool norm=true)
{
  TCanvas *c_ = new TCanvas(name + "_cvar", name , 500,500);
  c_->cd();
  if(logy) gPad->SetLogy();
  
  h1->SetLineColor(kRed);
  h2->SetLineColor(kBlue);
  if(norm){
    h2->Scale(1.0/h2->Integral());
    h1->Scale(1.0/h1->Integral());
  }
  
  if(h1->GetMaximum() >= h2->GetMaximum()){
    h1->Draw();
    h2->Draw("same");
  }else{
    h2->Draw();
    h1->Draw("same");
  }
  Draw2Legend (h1,h2, h1->GetTitle(), h2->GetTitle());
  c_->SaveAs("plots/" + name + ".png");
  c_->SaveAs("plots/" + name + ".pdf");
}
void Draw3Variable(TH1 *h1, TH1 *h2, TH1 *h3, TString name="", bool logy=false, bool norm=true)
{
  TCanvas *c_ = new TCanvas(name + "_cvar", name , 600,600);
  c_->cd();
  if(logy) gPad->SetLogy();
  
  h1->SetLineColor(kRed);
  h2->SetLineColor(kBlue);
  h3->SetLineColor(8);
  h3->SetFillColor(8);
  h3->SetLineWidth(1);
  h3->SetFillStyle(3003);
  if(norm){
    h3->Scale(1.0/h3->Integral());
    h2->Scale(1.0/h2->Integral());
    h1->Scale(1.0/h1->Integral());
  }
  
  if(h1->GetMaximum() >= h2->GetMaximum() && 
     h1->GetMaximum() >= h3->GetMaximum() ){
    h1->Draw();
    h2->Draw("same");
    h3->Draw("same");
  }else{
    if(h2->GetMaximum() >= h3->GetMaximum()){
      h2->Draw();
      h1->Draw("same");
      h3->Draw("same");
    }else{
      h3->Draw();
      h1->Draw("same");
      h2->Draw("same");
    }
  }
  Draw3Legend (h1,h2,h3, h1->GetTitle(), h2->GetTitle(),h3->GetTitle());
  c_->SaveAs("plots/" + name + ".png");
  c_->SaveAs("plots/" + name + ".pdf");
}

void Draw4Variable(TH1 *h1, TH1 *h2, TH1 *h3, TH1 *h4 , TString name="", bool logy=false, bool norm=true)
{
  TCanvas *c_ = new TCanvas(name + "_cvar", name , 600,600);
  c_->cd();
  if(logy) gPad->SetLogy();
  
  h1->SetLineColor(kRed);
  h2->SetLineColor(kBlue);
  h3->SetLineColor(8);
  h3->SetFillColor(8);
  h3->SetLineWidth(1);
  h3->SetFillStyle(3003);
  
  h4->SetLineColor(6);
  //h4->SetFillColor(6);
  h4->SetLineWidth(1);
  //h4->SetFillStyle(3001);
  if(norm){
    h3->Scale(1.0/h3->Integral());
    h2->Scale(1.0/h2->Integral());
    h1->Scale(1.0/h1->Integral());
    h4->Scale(1.0/h4->Integral());
  }
  
  if(h1->GetMaximum() >= h2->GetMaximum() && 
     h1->GetMaximum() >= h3->GetMaximum() ){
    h1->Draw();
    h2->Draw("same");
    h3->Draw("same");
    h4->Draw("same");
  }else{
    if(h2->GetMaximum() >= h3->GetMaximum()){
      h2->Draw();
      h1->Draw("same");
      h3->Draw("same");
      h4->Draw("same");
    }else{
      h3->Draw();
      h1->Draw("same");
      h2->Draw("same");
      h4->Draw("same");
    }
  }
  Draw4Legend (h1,h2,h3,h4, 
	       h1->GetTitle(), 
	       h2->GetTitle(),
	       h3->GetTitle(),
	       h4->GetTitle());
  c_->SaveAs("plots/" + name + ".png");
  c_->SaveAs("plots/" + name + ".pdf");
}
void PFCHSLegVsPFCHS0(int catbin=1, TString sample ="VBF", bool vetex=true){
  
  std::map<TString,TTree*>     JetTree;
  
  // --> /afs/cern.ch/work/y/yhaddad/jetValidationTrees_VBF_HToGG.root
  // --> /afs/cern.ch/work/y/yhaddad/jetValidationTrees_VBF_HToGG.root
  
  // --> /afs/cern.ch/work/y/yhaddad/VBF_HToGG_M-125_13TeV_JetValidationTree.root
  // --> /afs/cern.ch/work/y/yhaddad/GluGluToHToGG_M-125_13TeV_JetValidationTree.root
  
  TFile *file;
  
  if     (sample == "VBF") 
    file = TFile::Open("/afs/cern.ch/work/y/yhaddad/VBF_HToGG_M-125_13TeV_JetValidationTree.root");
  else if(sample == "GGF") 
    file = TFile::Open("/afs/cern.ch/work/y/yhaddad/GluGluToHToGG_M-125_13TeV_JetValidationTree.root");
  else return;
  
  //JetTree["PF"]      = (TTree*)file->Get("flashggJetValidationTreeMaker/jetTree_PF");
  JetTree["PFCHS0"]  = (TTree*)file->Get("flashggJetValidationTreeMakerPFCHS0/jetTree_PFCHS0"); 
  JetTree["PFCHSLeg"]= (TTree*)file->Get("flashggJetValidationTreeMakerPFCHSLeg/jetTree_PFCHSLeg"); 
  
  //====> cuts
  TCut cat;
  TString catname;
  TCut weight;
  if(catbin == 1 ){
    cat = "abs(eta) < 2.5";
    catname = "(|#eta| < 2.5)";
    weight  = "3.48*(0.976-exp(-bestPt*9.017e-03))";
  }else if(catbin ==2){
    cat = "abs(eta) > 2.5 && abs(eta) < 3";
    catname = "(2.5 <|#eta| < 3.0)";
    weight  = "8.08*(0.955-exp(-bestPt*4.76e-03))";
  }else if(catbin ==3){
    cat = "abs(eta) > 3";
    catname = "(|#eta| > 3.0)";
    weight  = "4.22*(0.778-exp(-bestPt*0.0204))";
  }
  
  TCut cut_pt             = "bestPt>20.0 && genJetPt>10.0";
  TCut cut_genjetmatch    = "genJetMatch==1";
  TCut cut_vertex         = "LegIsPV0";
  TString  sampleName = "";
  
  if     (sample == "VBF") sampleName = "VBF(H#rightarrow#gamma#gamma) 13TeV";
  else if(sample == "GGF") sampleName = "GGF(H#rightarrow#gamma#gamma) 13TeV";
  
  TCut cut_PUJ = cut_pt && cat && !cut_genjetmatch;
  TCut cut_JET = cut_pt && cat &&  cut_genjetmatch;
  
  // ===> Only for def
  std::cout << ":: PUJ == " << cut_PUJ.GetTitle() << std::endl;
  std::cout << ":: JET == " << cut_JET.GetTitle() << std::endl;
  
  std::map<TString,TH1F*> h_ratio; 
  std::map<TString,TH1F*> h_LegIsPV0; 
  
  for (std::map<TString,TTree*>::iterator it=JetTree.begin(); it!=JetTree.end(); ++it){
    h_ratio[it->first]  = new TH1F(Form("h_ratio_%s"                 ,it->first.Data()),
				   Form("%s;p^{reco}_{t}/p^{gen}_{t}",it->first.Data()),
				   150,0,3);
    
    h_LegIsPV0[it->first]  = new TH1F(Form("h_LegIsPV0_%s",it->first.Data()),
				      Form("%s;LegIsPV0"  ,it->first.Data()),
				      4,-0.5,3.5);
    
    JetTree[it->first]->Project(Form("h_ratio_%s",it->first.Data())   ,"bestPt/genJetPt",cut_JET,"");
    JetTree[it->first]->Project(Form("h_LegIsPV0_%s",it->first.Data()),"LegIsPV0",cut_JET,"");
  }
  h_ratio["PFCHSLeg_vtx"]  = new TH1F("h_ratio_PFCHSLeg_vtx",
				      "PFCHSLeg (PV_{0} = PV_{Leg});p^{reco}_{t}/p^{gen}_{t}",
				      150,0,3);
  h_ratio["PFCHSLeg_vtx_other"]  = new TH1F("h_ratio_PFCHSLeg_vtx_other",
					    "PFCHSLeg (PV_{0} #neq PV_{Leg});p^{reco}_{t}/p^{gen}_{t}",
					    150,0,3);
  
  JetTree["PFCHSLeg"]->Project("h_ratio_PFCHSLeg_vtx","bestPt/genJetPt",cut_JET + cut_vertex  ,"");
  JetTree["PFCHSLeg"]->Project("h_ratio_PFCHSLeg_vtx_other","bestPt/genJetPt",cut_JET + !cut_vertex  ,"");
  
  DrawVariable( h_ratio["PFCHS0"],  h_ratio["PFCHSLeg"], sample + "_response");
  DrawVariable( h_LegIsPV0["PFCHS0"],  h_LegIsPV0["PFCHSLeg"], sample + "_LegIsPV0");
  
  Draw3Variable( h_ratio["PFCHS0"],  
		 h_ratio["PFCHSLeg"],  
		 h_ratio["PFCHSLeg_vtx"], 
		 sample + "_2response", true);
  
  Draw4Variable( h_ratio["PFCHS0"],  
		 h_ratio["PFCHSLeg"],  
		 h_ratio["PFCHSLeg_vtx"], 
		 h_ratio["PFCHSLeg_vtx_other"], 
		 sample + "_4response", true);
  
}
