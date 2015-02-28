
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
#include <TLatex.h>
#include <TGraphAsymmErrors.h>
#include <TGraphErrors.h>

void VertexVal(int event=-1){
  
  
  std::map<double ,TCanvas*>     varpt_Canv;
  std::map<double ,TH1F*>     h_varpt_CHS0;
  std::map<double ,TH1F*>     h_varpt_CHSLeg;
  
  TFile *file =  TFile::Open("../SethTEST_jetValidationTrees_VBF_HToGG_1k.root");
  
  TTree*     tree_CHS0  =(TTree*)file->Get("flashggPFCollAnalyzer/tree_PFCHS0");;
  TTree*     tree_CHSLeg=(TTree*)file->Get("flashggPFCollAnalyzer/tree_PFCHSLeg");;
  
  //TLatex *latex;
  //latex.SetTextSize(0.025);
  //latex.SetTextAlign(13);  //align at top
  
  
  double cut_pt= 0;
  double step  = 5;
  for(int i=0; i < 5; i++){
    cut_pt = i*step; 
    if(event ==-1){
      h_varpt_CHS0  [cut_pt] = new TH1F(Form("h_varpt_CHS0_%i",i)  ,Form("p_{t}> %3.1f;dZ [mm]",cut_pt),100,-50,50);
      h_varpt_CHSLeg[cut_pt] = new TH1F(Form("h_varpt_CHSLeg_%i",i),Form("p_{t}> %3.1f;dZ [mm]",cut_pt),100,-50,50);
    }else{
      h_varpt_CHS0  [cut_pt] = new TH1F(Form("h_varpt_CHS0_%i",i)  ,Form("event No %i (p_{t}> %3.1f);dZ [mm]",cut_pt,event),100,-50,50);
      h_varpt_CHSLeg[cut_pt] = new TH1F(Form("h_varpt_CHSLeg_%i",i),Form("event No %i (p_{t}> %3.1f);dZ [mm]",cut_pt,event),100,-50,50);
    }
    h_varpt_CHSLeg[cut_pt]->SetLineColor(kRed);	
    
    if(event ==-1 ){
      tree_CHS0  -> Project(Form("h_varpt_CHS0_%i",i)  ,"dZ",Form("pt>%f",cut_pt));
      tree_CHSLeg-> Project(Form("h_varpt_CHSLeg_%i",i),"dZ",Form("pt>%f",cut_pt));
    }else{
      tree_CHS0  -> Project(Form("h_varpt_CHS0_%i",i)  ,"dZ",Form("pt>%f && event==%i",cut_pt,event));
      tree_CHSLeg-> Project(Form("h_varpt_CHSLeg_%i",i),"dZ",Form("pt>%f && event==%i",cut_pt,event));
    }
    varpt_Canv[cut_pt] = new TCanvas(Form("c_%i",i),"",500,500);
    varpt_Canv[cut_pt]->cd();
    gPad->SetLogy();
    //latex.DrawLatex(.7,.9,Form("Tracks with : p_{t} > %3.1f",cut_pt));
    h_varpt_CHS0  [cut_pt]->GetYaxis()->SetRangeUser(0.1,1.5e5);
    h_varpt_CHS0  [cut_pt]->Draw();
    h_varpt_CHSLeg[cut_pt]->Draw("same");
    if(event ==-1){
      varpt_Canv[cut_pt]->SaveAs(Form("plots/vertex_CHS0_CHSLeg_pt_%i.pdf",i));
      varpt_Canv[cut_pt]->SaveAs(Form("plots/vertex_CHS0_CHSLeg_pt_%i.png",i));
    }else{
      varpt_Canv[cut_pt]->SaveAs(Form("plots/vertex_CHS0_CHSLeg_evtNo_%i_pt_%i.pdf",i,event));
      varpt_Canv[cut_pt]->SaveAs(Form("plots/vertex_CHS0_CHSLeg_evtNo_%i_pt_%i.png",i,event));
    }
  }

}
