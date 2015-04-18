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

void DrawVariable(TH1 *h1, TH1 *h2, TString name="", bool logy=false, bool norm=true,bool addSum=false)
{
  TCanvas *c_ = new TCanvas(name + "_cvar", name , 500,500);
  c_->cd();
  if(logy) gPad->SetLogy();
  TH1F *sum = (TH1F*) h1->Clone("sum");
  if(addSum)
    {
      sum->Add(h2);  
    }
  
  h1->SetLineColor(kRed);
  h2->SetLineColor(8);
  h1->SetMarkerColor(kRed);
  h2->SetMarkerColor(8);
  if(norm){
    h2->Scale(1.0/h2->Integral());
    h1->Scale(1.0/h1->Integral());
  }
  
  if(h1->GetMaximum() >= h2->GetMaximum()){
    if(addSum){
      sum->Draw();
      h1->Draw("same");
      h2->Draw("same");
    }else{
      h1->Draw();
      h2->Draw("same");
    }
  }else{
    if(addSum){
      sum->Draw();
      h1->Draw("same");
      h2->Draw("same");
    }else{
      h2->Draw();
      h1->Draw("same");
    }
  }
  c_->SaveAs("plots/" + name + ".png");
  c_->SaveAs("plots/" + name + ".pdf");
}


void PUJIDOpetimisation(int catbin=1, TString sample ="VBF"){
  
  std::map<TString,TTree*>     JetTree;
  std::map<TString,TTree*>     GenJetTree;
  
  std::map<TString,TTree*>     JetTree_PUJ;
  std::map<TString,TTree*>     JetTree_JET;
  
  std::map<TString,TH1F*>      h_betaStar_PUJ;	  
  std::map<TString,TH1F*>      h_betaStar_JET;	  
  
  std::map<TString,TH1F*>      h_RMS_PUJ;	  
  std::map<TString,TH1F*>      h_RMS_JET;	  

  std::map<TString,TH1F*>      h_ptD_PUJ;	  
  std::map<TString,TH1F*>      h_ptD_JET;	  

  std::map<TString,TH1F*>      h_dZ_PUJ;	  
  std::map<TString,TH1F*>      h_dZ_JET;	  
  
  std::map<TString,TH1F*>      h_nCharged_PUJ;	  
  std::map<TString,TH1F*>      h_nCharged_JET;	  
  
  std::map<TString,TH1F*>      h_nPart_PUJ;	  
  std::map<TString,TH1F*>      h_nPart_JET;	  
  
  std::map<TString,TH1F*>      h_nPV_PUJ;	  
  std::map<TString,TH1F*>      h_nPV_JET;	  
  
  std::map<TString,TH1F*>      h_W_PUJ;	  
  std::map<TString,TH1F*>      h_W_JET;	  
  
  std::map<TString,TH1F*>      h_area_PUJ;	  
  std::map<TString,TH1F*>      h_area_JET;	  
  
  std::map<TString,TH1F*>      h_pt_PUJ;	  
  std::map<TString,TH1F*>      h_pt_JET;	  
  
  std::map<TString,TH1F*>      h_dRMean_PUJ;	  
  std::map<TString,TH1F*>      h_dRMean_JET;	  
  
  std::map<TString,TH1F*>      h_chgEmFrac_PUJ;	  
  std::map<TString,TH1F*>      h_chgEmFrac_JET;	  
  
  std::map<TString,TH2F*>      h2_JET;	  
  std::map<TString,TH2F*>      h2_PUJ;	  

  std::map<TString,TH2F*>      h2_rms_beta_PUJ;	  
  std::map<TString,TH2F*>      h2_rms_beta_JET;	  
  
  std::map<TString,TH2F*>      h2_dz_beta_PUJ;	  
  std::map<TString,TH2F*>      h2_dz_beta_JET;	  
  
  std::map<TString,TH2F*>      g_JET_Eff;	  
  std::map<TString,TH2F*>      g_PUJ_Eff;	  
  
  std::map<TString,TH2F*>      g_JET_Rjc;	  
  std::map<TString,TH2F*>      g_PUJ_Rjc;	  

  std::map<TString,TProfile*>      p_JET_npv_betaStar;	  
  std::map<TString,TProfile*>      p_PUJ_npv_betaStar;	  
  
  std::map<TString,TProfile*>      p_JET_npv_rms;	  
  std::map<TString,TProfile*>      p_PUJ_npv_rms; 
  
  std::map<TString,TGraph*>      g_betaStar_Eff;	  
  std::map<TString,TGraph*>      g_betaStar_Rjc;	  
  
  std::map<TString,TGraph*>      g_RMS_Eff;	  
  std::map<TString,TGraph*>      g_RMS_Rjc;	  
  
  std::map<TString,TGraph*>      g_RMS_ROC;	  
  std::map<TString,TGraph*>      g_betaStar_ROC;	  
  
  
  std::map<TString,TH2F*>      h2_purity;	  
  
  std::map<TString,TCanvas*> Canv_PUJID;
  
  std::map<TString,TCanvas*> Canv_Dis;
  std::map<TString,TCanvas*> Canv_Eff;
  std::map<TString,TCanvas*> Canv_Rjc;
  
  std::map<TString,TCanvas*> Canv_purity;
  // --> /afs/cern.ch/work/y/yhaddad/jetValidationTrees_VBF_HToGG.root
  // --> /afs/cern.ch/work/y/yhaddad/jetValidationTrees_VBF_HToGG.root
  
  // --> /afs/cern.ch/work/y/yhaddad/VBF_HToGG_M-125_13TeV_JetValidationTree.root
  // --> /afs/cern.ch/work/y/yhaddad/GluGluToHToGG_M-125_13TeV_JetValidationTree.root
  
  TFile *file;
  
  if     (sample == "VBF") 
    file = TFile::Open("${WORKSPACE}/Validation/PUJID/VBF_HToGG_M-125_13TeV-powheg-pythia6.root");
  else if(sample == "GGF") 
    file = TFile::Open("/afs/cern.ch/work/y/yhaddad/GluGluToHToGG_M-125_13TeV_JetValidationTree.root");
  else return;
  
  JetTree["PF"]      = (TTree*)file->Get("flashggJetValidationTreeMaker/jetTree_PF");
  //JetTree["PFCHS0"]  = (TTree*)file->Get("flashggJetValidationTreeMakerPFCHS0/jetTree_PFCHS0"); 
  //JetTree["PFCHSLeg"]= (TTree*)file->Get("flashggJetValidationTreeMakerPFCHSLeg/jetTree_PFCHSLeg"); 
  
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
  
  TCut cut_photon_rej     = "!(photonMatch==1)";
  TCut cut_gen_photon_rej = "!(photonMatch==1)";
  
  TCut cut_pt             = "bestPt>20.0";
  TCut cut_genjetmatch    = "genJetMatch==1 && genJetPt>8";  // the 8 GeV comes from the PUJID note
  
  TString  sampleName = "";
  
  if     (sample == "VBF") sampleName = "VBF(H#rightarrow#gamma#gamma) 13TeV";
  else if(sample == "GGF") sampleName = "GGF(H#rightarrow#gamma#gamma) 13TeV";
  
  //TCut cut_PUJ = weight * (cut_pt && cut_photon_rej && cat &&!cut_genjetmatch);
  //TCut cut_JET = weight * (cut_pt && cut_photon_rej && cat && cut_genjetmatch);
  
  TCut cut_PUJ = cut_pt && cat && !cut_genjetmatch && cut_photon_rej;
  TCut cut_JET = cut_pt && cat &&  cut_genjetmatch && cut_photon_rej;
  
  // ===> Only for def
  std::cout << ":: PUJ == " << cut_PUJ.GetTitle() << std::endl;
  std::cout << ":: JET == " << cut_JET.GetTitle() << std::endl;
  
  for (std::map<TString,TTree*>::iterator it=JetTree.begin(); it!=JetTree.end(); ++it){
    h_betaStar_PUJ[it->first]= new TH1F(Form("h_betaStar_PUJ_%s",it->first.Data()),
					Form("%s %s %s;#beta^{*};n_{jets}", 
					     sampleName.Data(), 
					     it->first.Data() , 
					     catname.Data()  ),
					100,0,1);
    
    h_betaStar_JET[it->first]= new TH1F(Form("h_betaStar_JET_%s",it->first.Data()),
					Form("%s %s %s;#beta^{*};n_{jets}", 
					     sampleName.Data(),
					     it->first.Data() ,
					     catname.Data()  ),
					100,0,1);
    
    
    h_RMS_PUJ[it->first] = new TH1F(Form("h_RMS_PUJ_%s",it->first.Data()),
				    Form("%s %s %s;#LT#Delta R^{2}#GT;n_{jets}", 
					 sampleName.Data(),
					 it->first.Data() ,
					 catname.Data()  ),
				    100,0,0.1);
    
    h_RMS_JET[it->first] = new TH1F(Form("h_RMS_JET_%s",it->first.Data()),
				    Form("%s %s %s;#LT#Delta R^{2}#GT;n_{jets}", 
					 sampleName.Data(),
					 it->first.Data() , 
					 catname.Data()  ),
				    100,0,0.1);
    
    
    h_pt_PUJ[it->first] = new TH1F(Form("h_pt_PUJ_%s",it->first.Data()),
				   Form("%s %s %s;p_{T}[GeV];n_{jets}", 
					sampleName.Data(),
					it->first.Data() ,
					catname.Data()  ),
				   180,20,200);
    
    h_pt_JET[it->first] = new TH1F(Form("h_pt_JET_%s",it->first.Data()),
				   Form("%s %s %s;p_{T}[GeV];n_{jets}", 
					sampleName.Data(),
					it->first.Data() ,
					catname.Data()  ),
				   180,20,200);
    
    h_dZ_PUJ[it->first] =  new TH1F(Form("h_dZ_PUJ_%s",it->first.Data()),
				    Form("%s %s %s;exp(-dZ);n_{jets}", 
					 sampleName.Data(),
					 it->first.Data() ,
					 catname.Data()  ),
				    125,-15,10);
    
    h_dZ_JET[it->first] = new TH1F(Form("h_dZ_JET_%s",it->first.Data()),
				   Form("%s %s %s;exp(-dZ);n_{jets}", 
					sampleName.Data(),
					it->first.Data() ,
					catname.Data()  ),
				   125,-15,10);
    
    h_nCharged_PUJ[it->first] = new TH1F(Form("h_nCharged_PUJ_%s",it->first.Data()),
					 Form("%s %s %s;n^{ch};n_{jets}", 
					      sampleName.Data(),
					      it->first.Data() ,
					      catname.Data()  ),
					 41,0,40);
    
    h_nCharged_JET[it->first] = new TH1F(Form("h_nCharged_JET_%s",it->first.Data()),
					 Form("%s %s %s;n^{ch};n_{jets}", 
					      sampleName.Data(),
					      it->first.Data() ,
					      catname.Data()  ),
					 41,0,40);
    
    h_nPV_PUJ[it->first] = new TH1F(Form("h_nPV_PUJ_%s",it->first.Data()),
				    Form("%s %s %s;n^{PV};n_{jets}", 
					 sampleName.Data(),
					 it->first.Data() ,
					 catname.Data()  ),
				    41,0,40);
    
    h_nPV_JET[it->first] = new TH1F(Form("h_nPV_JET_%s",it->first.Data()),
				    Form("%s %s %s;n^{PV};n_{jets}", 
					 sampleName.Data(),
					 it->first.Data() ,
					 catname.Data()  ),
				    41,0,40);
    
    h_nPart_PUJ[it->first] = new TH1F(Form("h_nPart_PUJ_%s",it->first.Data()),
				      Form("%s %s %s;n^{PF};n_{jets}", 
					   sampleName.Data(),
					   it->first.Data() ,
					   catname.Data()  ),
				      41,0,40);
    
    h_nPart_JET[it->first] = new TH1F(Form("h_nPart_JET_%s",it->first.Data()),
				      Form("%s %s %s;n^{PF};n_{jets}", 
					   sampleName.Data(),
					   it->first.Data() ,
					   catname.Data()  ),
				      41,0,40);
    
    
    h_W_PUJ[it->first] = new TH1F(Form("h_W_PUJ_%s",it->first.Data()),
				  Form("%s %s %s;W;n_{jets}", sampleName.Data(),it->first.Data(),catname.Data()),
				  100,0,0.4);
    
    h_W_JET[it->first] = new TH1F(Form("h_W_JET_%s",it->first.Data()),
				  Form("%s %s %s;W;n_{jets}", sampleName.Data(),it->first.Data(),catname.Data()),
				  100,0,0.4);


    h_area_PUJ[it->first] = new TH1F(Form("h_area_PUJ_%s",it->first.Data()),
				     Form("%s %s %s;area;n_{jets}", sampleName.Data(),it->first.Data(),catname.Data()),
				     100,0,1);
    
    h_area_JET[it->first] = new TH1F(Form("h_area_JET_%s",it->first.Data()),
				     Form("%s %s %s;area;n_{jets}", sampleName.Data(),it->first.Data(),catname.Data()),
				     100,0,1);
    
    
    //h_pt_PUJ[it->first] = new TH1F(Form("h_pt_PUJ_%s",it->first.Data()),
    //				   Form("%s %s %s;W;n_{jets}", sampleName.Data(),it->first.Data(),catname.Data()),
    //				   150,0,150);
    //
    //h_pt_JET[it->first] = new TH1F(Form("h_pt_JET_%s",it->first.Data()),
    //				   Form("%s %s %s;W;n_{jets}", sampleName.Data(),it->first.Data(),catname.Data()),
    //				   150,0,150);
    
    h_dRMean_PUJ[it->first] = new TH1F(Form("h_dRMean_PUJ_%s",it->first.Data()),
				       Form("%s %s %s;#LT#Delta R#GT;n_{jets}", sampleName.Data(),it->first.Data(),catname.Data()),
				       100,0,0.5);
    
    h_dRMean_JET[it->first] = new TH1F(Form("h_dRMean_JET_%s",it->first.Data()),
				       Form("%s %s %s;#LT#Delta R#GT;n_{jets}", sampleName.Data(),it->first.Data(),catname.Data()),
				       100,0,0.5);
    
    
    std::cout <<" -----------------------------------------------------------------"<< std::endl;
    std::cout <<"beta PUJ::"<<  Form("PUJetID_betaStar>>h_betaStar_PUJ_%s",it->first.Data()) << std::endl;
    std::cout <<"beta JET::"<<  Form("PUJetID_betaStar>>h_betaStar_JET_%s",it->first.Data()) << std::endl;
    std::cout <<"rms  PUJ::"<<  Form("PUJetID_rms>>h_RMS_PUJ_%s",it->first.Data()) << std::endl;
    std::cout <<"rms  JET::"<<  Form("PUJetID_rms>>h_RMS_JET_%s",it->first.Data()) << std::endl;
    std::cout <<" -----------------------------------------------------------------"<< std::endl;
    
    JetTree[it->first]->Project(Form("h_betaStar_PUJ_%s",it->first.Data()),"betaStar",cut_PUJ,"");
    JetTree[it->first]->Project(Form("h_betaStar_JET_%s",it->first.Data()),"betaStar",cut_JET,"");
    
    JetTree[it->first]->Project(Form("h_RMS_PUJ_%s",it->first.Data()),"rms",cut_PUJ,"");
    JetTree[it->first]->Project(Form("h_RMS_JET_%s",it->first.Data()),"rms",cut_JET,"");
    
    JetTree[it->first]->Project(Form("h_pt_PUJ_%s",it->first.Data()),"bestPt",cut_PUJ,"");
    JetTree[it->first]->Project(Form("h_pt_JET_%s",it->first.Data()),"bestPt",cut_JET,"");
    
    JetTree[it->first]->Project(Form("h_dZ_PUJ_%s",it->first.Data()),"log(dZ)",cut_PUJ,"");
    JetTree[it->first]->Project(Form("h_dZ_JET_%s",it->first.Data()),"log(dZ)",cut_JET,"");
    
    //JetTree[it->first]->Project(Form("h_nPart_PUJ_%s",it->first.Data()),"nPart",cut_PUJ,"");
    //JetTree[it->first]->Project(Form("h_nPart_JET_%s",it->first.Data()),"nPart",cut_JET,"");
    
    JetTree[it->first]->Project(Form("h_nPV_PUJ_%s",it->first.Data()),"nPV",cut_PUJ,"");
    JetTree[it->first]->Project(Form("h_nPV_JET_%s",it->first.Data()),"nPV",cut_JET,"");
    
    //JetTree[it->first]->Project(Form("h_W_PUJ_%s",it->first.Data()),"W",cut_PUJ,"");
    //JetTree[it->first]->Project(Form("h_W_JET_%s",it->first.Data()),"W",cut_JET,"");

    //JetTree[it->first]->Project(Form("h_pt_PUJ_%s",it->first.Data()),"bestPt",cut_PUJ,"");
    //JetTree[it->first]->Project(Form("h_pt_JET_%s",it->first.Data()),"bestPt",cut_JET,"");
    
    //JetTree[it->first]->Project(Form("h_area_PUJ_%s",it->first.Data()),"area",cut_PUJ,"");
    //JetTree[it->first]->Project(Form("h_area_JET_%s",it->first.Data()),"area",cut_JET,"");
    
    //JetTree[it->first]->Project(Form("h_dRMean_PUJ_%s",it->first.Data()),"dRMean",cut_PUJ,"");
    //JetTree[it->first]->Project(Form("h_dRMean_JET_%s",it->first.Data()),"dRMean",cut_JET,"");
    
    h2_PUJ[it->first] = new TH2F(Form("h2_PUJ_%s",it->first.Data()),
				 Form("%s %s %s;n_{pv};#LT#beta^{*} #GT", 
				      sampleName.Data(),it->first.Data(),catname.Data()),
				 40,0,40,100,0,1);
    
    h2_JET[it->first] = new TH2F(Form("h2_JET_%s",it->first.Data()),
				 Form("%s %s %s;n_{pv};#LT#beta^{*} #GT", 
				      sampleName.Data(),it->first.Data(),catname.Data()),
				 40,0,40,100,0,1);
    
    JetTree[it->first]->Project(Form("h2_JET_%s",it->first.Data()),"betaStar:nPV",cut_JET,"");
    JetTree[it->first]->Project(Form("h2_PUJ_%s",it->first.Data()),"betaStar:nPV",cut_PUJ,"");
    
    
    h2_rms_beta_PUJ[it->first] = new TH2F(Form("h2_rms_beta_PUJ_%s",it->first.Data()),
					  Form("%s %s %s;#beta^{*};#LT#Delta R^{2} #GT", 
					       sampleName.Data(),it->first.Data(),catname.Data()),
					  100,0,1,100,0,0.1);
    h2_rms_beta_JET[it->first] = new TH2F(Form("h2_rms_beta_JET_%s",it->first.Data()),
					  Form("%s %s %s;#beta^{*};#LT#Delta R^{2} #GT", 
					       sampleName.Data(),it->first.Data(),catname.Data()),
					  100,0,1,100,0,0.1);
    
    JetTree[it->first]->Project(Form("h2_rms_beta_JET_%s",it->first.Data()),"rms:betaStar",cut_JET,"");
    JetTree[it->first]->Project(Form("h2_rms_beta_PUJ_%s",it->first.Data()),"rms:betaStar",cut_PUJ,"");
    
    h2_dz_beta_PUJ[it->first] = new TH2F(Form("h2_dz_beta_PUJ_%s",it->first.Data()),
					 Form("%s %s %s;#beta^{*};#LT#Delta R^{2} #GT", 
					      sampleName.Data(),it->first.Data(),catname.Data()),
					 100,0,1,125,-15,10);
    h2_dz_beta_JET[it->first] = new TH2F(Form("h2_dz_beta_JET_%s",it->first.Data()),
					 Form("%s %s %s;#beta^{*};#LT#Delta R^{2} #GT", 
					      sampleName.Data(),it->first.Data(),catname.Data()),
					 100,0,1,125,-15,10);
    
    JetTree[it->first]->Project(Form("h2_dz_beta_JET_%s",it->first.Data()),"log(dZ):betaStar",cut_JET,"");
    JetTree[it->first]->Project(Form("h2_dz_beta_PUJ_%s",it->first.Data()),"log(dZ):betaStar",cut_PUJ,"");
    
    // canvas
    std::cout << it->first 
	      << "\t :JET: "<<  h_RMS_JET[it->first]->GetEntries() 
	      << "\t :PUJ: "<<  h_RMS_PUJ[it->first]->GetEntries() 
	      << std::endl;
    
    // create the profiles
    p_JET_npv_betaStar[it->first] =  h2_JET[it->first]->ProfileX("p_JET_npv_betaStar");
    p_PUJ_npv_betaStar[it->first] =  h2_PUJ[it->first]->ProfileX("p_PUJ_npv_betaStar");
    
    //g_betaStar_Eff[it->first] = GetEff(h_betaStar_JET[it->first],"BetaStarJetEff");
    //g_betaStar_Rjc[it->first] = GetEff(h_betaStar_PUJ[it->first],"BetaStarPUJRjc");
    
    //g_RMS_Eff[it->first] = GetEff(h_RMS_JET[it->first],Form("RMSJetEff_%s",it->first.Data()));
    //g_RMS_Rjc[it->first] = GetEff(h_RMS_PUJ[it->first],Form("RMSPUJRjc_%s",it->first.Data()));
    
    //g_RMS_ROC[it->first]      = GetROC(h_RMS_JET[it->first],h_RMS_PUJ[it->first],"RMSROC");
    //g_betaStar_ROC[it->first] = GetROC(h_betaStar_JET[it->first],h_betaStar_PUJ[it->first],"betaStarROC");
    
    //g_JET_Eff[it->first]     = Get2DEff(h2_JET[it->first], Form("JET2DEff_%s",it->first.Data()),"eff");
    //g_PUJ_Eff[it->first]     = Get2DEff(h2_PUJ[it->first], Form("PUJ2DEff_%s",it->first.Data()),"eff");
    //h2_purity[it->first]     = Get2DPurity(h2_JET[it->first], h2_PUJ[it->first],"purity");
    
    TString cattmp(Form("%i",catbin)); 
    DrawVariable(h_RMS_JET[it->first]     ,h_RMS_PUJ[it->first]     ,it->first +"_" + cattmp + sample + "_rms",false);
    DrawVariable(h_betaStar_JET[it->first],h_betaStar_PUJ[it->first],it->first +"_" + cattmp + sample + "_betaStar",false);
    DrawVariable(h_dZ_JET[it->first]      ,h_dZ_PUJ[it->first]      ,it->first +"_" + cattmp + sample + "_dZ",false);
    
    DrawVariable(h_nPV_JET[it->first],h_nPV_PUJ[it->first],it->first +"_" + cattmp + sample + "_nPV",false);
    
    
    DrawVariable(p_JET_npv_betaStar[it->first],p_PUJ_npv_betaStar[it->first],it->first +"_" + cattmp + sample + "_npv_betaStar",false,false);
    
    //DrawVariable(h_nPart_JET[it->first]   ,h_nPart_PUJ[it->first]   ,it->first +"_" + cattmp + sample + "_nPart");
    //DrawVariable(h_W_JET[it->first]       ,h_W_PUJ[it->first]       ,it->first +"_" + cattmp + sample + "_W");
    //DrawVariable(h_ptD_JET[it->first]     ,h_ptD_PUJ[it->first]     ,it->first +"_" + cattmp + sample + "_ptD");
    DrawVariable(h_pt_JET[it->first]       ,h_pt_PUJ[it->first]       ,it->first +"_" + cattmp + sample + "_pt",true,false,true);
    //DrawVariable(h_area_JET[it->first]   ,h_area_PUJ[it->first]     ,it->first +"_" + cattmp + sample + "_area");
    //DrawVariable(h_dRMean_JET[it->first] ,h_dRMean_PUJ[it->first]   ,it->first +"_" + cattmp + sample + "_dRMean");
    
    Canv_Dis[it->first] = new TCanvas(Form("c_Dis_%s",it->first.Data()),
				      Form("c_Dis_%s",it->first.Data()),1000,500);
    Canv_Dis[it->first]->Divide(2,1);
    Canv_Dis[it->first]->cd(1);
    h2_dz_beta_PUJ[it->first]->Draw("colz");
    Canv_Dis[it->first]->cd(2);
    h2_dz_beta_JET[it->first]->Draw("colz");
    
    Canv_Eff[it->first] = new TCanvas(Form("c_Eff_%s",it->first.Data()),
    				      Form("c_Eff_%s",it->first.Data()),1000,500);
    Canv_Eff[it->first]->Divide(2,1);
    Canv_Eff[it->first]->cd(1);
    h2_rms_beta_PUJ[it->first]->Draw("colz");
    Canv_Eff[it->first]->cd(2);
    h2_rms_beta_JET[it->first]->Draw("colz");
    
    ////Canv_purity[it->first] = new TCanvas(Form("c_Purity_%s",it->first.Data()),
    ////					 Form("c_Purity_%s",it->first.Data()),500,500);
    ////Canv_purity[it->first]->cd();
    ////h2_purity[it->first]->Draw("colz");
    ////
    //Canv_PUJID[it->first] = new TCanvas(Form("c_PUJID_%s",it->first.Data()),
    //					Form("c_PIJID_%s",it->first.Data()),1000,500);
    //Canv_PUJID[it->first]->Divide(2,1);
    //Canv_PUJID[it->first]->cd(1);
    //gPad->SetLogy();
    //h_RMS_JET[it->first]->SetLineColor(kRed);
    //h_RMS_JET[it->first]->SetMarkerColor(kRed);
    //h_RMS_JET[it->first]->DrawNormalized("");
    //h_RMS_PUJ[it->first]->DrawNormalized("same");
    //Draw2Legend(h_RMS_JET[it->first],h_RMS_PUJ[it->first],"Jets","PU Jets");
    //Canv_PUJID[it->first]->cd(2);
    //gPad->SetLogy();
    //h_betaStar_JET[it->first]->SetLineColor(kRed);
    //h_betaStar_JET[it->first]->SetMarkerColor(kRed);
    //h_betaStar_JET[it->first]->DrawNormalized("");
    //h_betaStar_PUJ[it->first]->DrawNormalized("same");
    //Draw2Legend(h_betaStar_JET[it->first],h_betaStar_PUJ[it->first],"Jets","PU Jets");
    //
    //Canv_PUJID[it->first]->SaveAs(Form("plots/%s_PUJID_var_%s_%i.png",sample.Data(),it->first.Data(),catbin));
    //Canv_PUJID[it->first]->SaveAs(Form("plots/%s_PUJID_var_%s_%i.pdf",sample.Data(),it->first.Data(),catbin));
  }
  
}
