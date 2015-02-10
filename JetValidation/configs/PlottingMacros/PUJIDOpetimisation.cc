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

void PUJIDOpetimisation(int catbin=1, TString sample ="VBF"){
  
  std::map<TString,TTree*>     JetTree;
  std::map<TString,TTree*>     GenJetTree;
  
  std::map<TString,TTree*>     JetTree_PUJ;
  std::map<TString,TTree*>     JetTree_JET;
  
  std::map<TString,TH1F*>      h_betaStar_PUJ;	  
  std::map<TString,TH1F*>      h_betaStar_JET;	  
  
  std::map<TString,TH1F*>      h_RMS_PUJ;	  
  std::map<TString,TH1F*>      h_RMS_JET;	  
  
  std::map<TString,TH2F*>      h2_JET;	  
  std::map<TString,TH2F*>      h2_PUJ;	  
  
  std::map<TString,TH2F*>      g_JET_Eff;	  
  std::map<TString,TH2F*>      g_PUJ_Eff;	  
  
  std::map<TString,TH2F*>      g_JET_Rjc;	  
  std::map<TString,TH2F*>      g_PUJ_Rjc;	  
  
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
  
  if     (sample == "VBF") file = TFile::Open("/afs/cern.ch/work/y/yhaddad/VBF_HToGG_M-125_13TeV_JetValidationTree.root");
  else if(sample == "GGF") file = TFile::Open("/afs/cern.ch/work/y/yhaddad/GluGluToHToGG_M-125_13TeV_JetValidationTree.root");
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
  
  TCut cut_photon_rej     = "!(photonMatch==1 && GenPhotonPt/bestPt > 0.5 && photondRmin < 0.2)";
  TCut cut_gen_photon_rej = "!(photonMatch==1 && GenPhotonPt/pt > 0.5     && photondRmin < 0.2)";
  TCut cut_pt             = "bestPt>20.0";
  TCut cut_genjetmatch    = "genJetMatch==1";
  
  TString  sampleName = "";
  if     (sample == "VBF") sampleName = "VBF(H#rightarrow#gamma#gamma) 13TeV";
  else if(sample == "GGF") sampleName = "GGF(H#rightarrow#gamma#gamma) 13TeV";
  
  TCut cut_PUJ = weight * (cut_pt && cut_photon_rej && cat &&!cut_genjetmatch);
  TCut cut_JET = weight * (cut_pt && cut_photon_rej && cat && cut_genjetmatch);
  
  // ===> Only for def
  std::cout << ":: PUJ == " << cut_PUJ.GetTitle() << std::endl;
  std::cout << ":: JET == " << cut_JET.GetTitle() << std::endl;
  
  for (std::map<TString,TTree*>::iterator it=JetTree.begin(); it!=JetTree.end(); ++it){
    h_betaStar_PUJ[it->first]    = new TH1F(Form("h_betaStar_PUJ_%s",it->first.Data()),
					    Form("%s %s %s;#beta^{*};n_{jets}", sampleName.Data(), it->first.Data(),catname.Data()),
					    250,0,1);
    
    h_betaStar_JET[it->first]    = new TH1F(Form("h_betaStar_JET_%s",it->first.Data()),
					    Form("%s %s %s;#beta^{*};n_{jets}", sampleName.Data(),it->first.Data(),catname.Data()),
					    250,0,1);
    
    
    h_RMS_PUJ[it->first]    = new TH1F(Form("h_RMS_PUJ_%s",it->first.Data()),
				       Form("%s %s %s;#LT#Delta R^{2}#GT;n_{jets}", sampleName.Data(),it->first.Data(),catname.Data()),
				       250,0,0.1);
    
    h_RMS_JET[it->first]    = new TH1F(Form("h_RMS_JET_%s",it->first.Data()),
				       Form("%s %s %s;#LT#Delta R^{2}#GT;n_{jets}", sampleName.Data(),it->first.Data(),catname.Data()),
				       250,0,0.1);
    
    
    h2_JET[it->first]    = new TH2F(Form("h2_JET_%s",it->first.Data()),
				    Form("%s %s %s;#beta^{*};#LT#Delta R^{2}#GT", sampleName.Data(),it->first.Data(),catname.Data()),
				    250,0,1,250,0,0.1);
    
    
    h2_PUJ[it->first]    = new TH2F(Form("h2_PUJ_%s",it->first.Data()),
				    Form("%s %s %s;#beta^{*};#LT#Delta R^{2}#GT", sampleName.Data(),it->first.Data(),catname.Data()),
				    250,0,1,250,0,0.1);
    
    
    
    
    std::cout <<" -----------------------------------------------------------------"<< std::endl;
    std::cout <<"beta PUJ::"<<  Form("PUJetID_betaStar>>h_betaStar_PUJ_%s",it->first.Data()) << std::endl;
    std::cout <<"beta JET::"<<  Form("PUJetID_betaStar>>h_betaStar_JET_%s",it->first.Data()) << std::endl;
    std::cout <<"rms  PUJ::"<<  Form("PUJetID_rms>>h_RMS_PUJ_%s",it->first.Data()) << std::endl;
    std::cout <<"rms  JET::"<<  Form("PUJetID_rms>>h_RMS_JET_%s",it->first.Data()) << std::endl;
    std::cout <<" -----------------------------------------------------------------"<< std::endl;
    
    JetTree[it->first]->Project(Form("h_betaStar_PUJ_%s",it->first.Data()),"PUJetID_betaStar",cut_PUJ,"");
    JetTree[it->first]->Project(Form("h_betaStar_JET_%s",it->first.Data()),"PUJetID_betaStar",cut_JET,"");
    
    JetTree[it->first]->Project(Form("h_RMS_PUJ_%s",it->first.Data()),"PUJetID_rms",cut_PUJ,"");
    JetTree[it->first]->Project(Form("h_RMS_JET_%s",it->first.Data()),"PUJetID_rms",cut_JET,"");
    
    JetTree[it->first]->Project(Form("h2_JET_%s",it->first.Data()),"PUJetID_rms:PUJetID_betaStar",cut_JET,"");
    JetTree[it->first]->Project(Form("h2_PUJ_%s",it->first.Data()),"PUJetID_rms:PUJetID_betaStar",cut_PUJ,"");
    
    // canvas
    std::cout << it->first 
	      << "\t :JET: "<<  h_RMS_JET[it->first]->GetEntries() 
	      << "\t :PUJ: "<<  h_RMS_PUJ[it->first]->GetEntries() 
	      << std::endl;
    
    
    
    //g_betaStar_Eff[it->first] = GetEff(h_betaStar_JET[it->first],"BetaStarJetEff");
    //g_betaStar_Rjc[it->first] = GetEff(h_betaStar_PUJ[it->first],"BetaStarPUJRjc");
    
    //g_RMS_Eff[it->first] = GetEff(h_RMS_JET[it->first],Form("RMSJetEff_%s",it->first.Data()));
    //g_RMS_Rjc[it->first] = GetEff(h_RMS_PUJ[it->first],Form("RMSPUJRjc_%s",it->first.Data()));
    
    //g_RMS_ROC[it->first]      = GetROC(h_RMS_JET[it->first],h_RMS_PUJ[it->first],"RMSROC");
    //g_betaStar_ROC[it->first] = GetROC(h_betaStar_JET[it->first],h_betaStar_PUJ[it->first],"betaStarROC");
    
    //g_JET_Eff[it->first]     = Get2DEff(h2_JET[it->first], Form("JET2DEff_%s",it->first.Data()),"eff");
    //g_PUJ_Eff[it->first]     = Get2DEff(h2_PUJ[it->first], Form("PUJ2DEff_%s",it->first.Data()),"eff");
    //h2_purity[it->first]     = Get2DPurity(h2_JET[it->first], h2_PUJ[it->first],"purity");
    
    Canv_Dis[it->first] = new TCanvas(Form("c_Dis_%s",it->first.Data()),
				      Form("c_Dis_%s",it->first.Data()),1000,500);
    Canv_Dis[it->first]->Divide(2,1);
    Canv_Dis[it->first]->cd(1);
    h2_PUJ[it->first]->Draw("colz");
    Canv_Dis[it->first]->cd(2);
    h2_JET[it->first]->Draw("colz");
    
    //Canv_Eff[it->first] = new TCanvas(Form("c_Eff_%s",it->first.Data()),
    //				      Form("c_Eff_%s",it->first.Data()),1000,500);
    //Canv_Eff[it->first]->Divide(2,1);
    //Canv_Eff[it->first]->cd(1);
    //g_PUJ_Eff[it->first]->Draw("colz");
    //Canv_Eff[it->first]->cd(2);
    //g_JET_Eff[it->first]->Draw("colz");
    //
    //Canv_purity[it->first] = new TCanvas(Form("c_Purity_%s",it->first.Data()),
    //					 Form("c_Purity_%s",it->first.Data()),500,500);
    //Canv_purity[it->first]->cd();
    //h2_purity[it->first]->Draw("colz");
    //
    Canv_PUJID[it->first] = new TCanvas(Form("c_PUJID_%s",it->first.Data()),
    					Form("c_PIJID_%s",it->first.Data()),1000,500);
    Canv_PUJID[it->first]->Divide(2,1);
    Canv_PUJID[it->first]->cd(1);
    gPad->SetLogy();
    h_RMS_JET[it->first]->SetLineColor(kRed);
    h_RMS_JET[it->first]->SetMarkerColor(kRed);
    h_RMS_JET[it->first]->DrawNormalized("");
    h_RMS_PUJ[it->first]->DrawNormalized("same");
    Draw2Legend(h_RMS_JET[it->first],h_RMS_PUJ[it->first],"Jets","PU Jets");
    Canv_PUJID[it->first]->cd(2);
    gPad->SetLogy();
    h_betaStar_JET[it->first]->SetLineColor(kRed);
    h_betaStar_JET[it->first]->SetMarkerColor(kRed);
    h_betaStar_JET[it->first]->DrawNormalized("");
    h_betaStar_PUJ[it->first]->DrawNormalized("same");
    Draw2Legend(h_betaStar_JET[it->first],h_betaStar_PUJ[it->first],"Jets","PU Jets");
    
    Canv_PUJID[it->first]->SaveAs(Form("plots/%s_PUJID_var_%s_%i.png",sample.Data(),it->first.Data(),catbin));
    Canv_PUJID[it->first]->SaveAs(Form("plots/%s_PUJID_var_%s_%i.pdf",sample.Data(),it->first.Data(),catbin));
  }
  
}
