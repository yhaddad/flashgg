/*  rootlogon.C
 *  Autor: Haddad Yacine
 *  Mail : yhaddad@cern.ch  
 *  All rights reserved.
 */

#include "TStyle.h"
#include <iomanip>
#include <time.h>

TStyle* YacineStyle;

void setYacineStyle(){
  YacineStyle = new  TStyle("YacineStyle", "Yacine Style");
  
  gInterpreter->ProcessLine(".! ps | grep root");
  
  // General
  YacineStyle->SetFillColor(10);
  YacineStyle->SetTitleFillColor(10);
  //YacineStyle->SetTextFont(18); //@
  YacineStyle->SetLineWidth(2); //@
  
  YacineStyle->SetPaperSize(20, 24);
  
  // For Canvas
  //YacineStyle->SetCanvasPreferGL(true); // as a test
  YacineStyle->SetCanvasBorderMode(0);
  YacineStyle->SetCanvasColor(0);     // chaned fron kWhite to -1 
  YacineStyle->SetCanvasDefH(600);    //Height of canvas
  YacineStyle->SetCanvasDefW(600);    //Width of canvas
  YacineStyle->SetCanvasDefX(900);    //POsition on screen
  YacineStyle->SetCanvasDefY(20);
  
  // For Pad
  YacineStyle->SetPadBorderMode(0);
  YacineStyle->SetPadColor(0);        // chaned fron kWhite to -1 
  YacineStyle->SetPadGridX(false);
  YacineStyle->SetPadGridY(false);
  YacineStyle->SetGridColor(kGray);
  YacineStyle->SetGridStyle(3);
  YacineStyle->SetGridWidth(1);
  YacineStyle->SetPadTickX(1);  
  YacineStyle->SetPadTickY(1);
  
  // for frame
  YacineStyle->SetFrameBorderMode(0);
  YacineStyle->SetFrameBorderSize(1);
  YacineStyle->SetFrameFillColor(0);   // chaned fron kWhite to -1  
  YacineStyle->SetFrameFillStyle(0);
  YacineStyle->SetFrameLineColor(1);
  YacineStyle->SetFrameLineStyle(1);
  YacineStyle->SetFrameLineWidth(1);   // default : 2 
  
  // For Hito
  YacineStyle->SetHistFillColor(0);    // changed from kWhite to -1
  YacineStyle->SetHistLineColor(kBlue+3);
  YacineStyle->SetHistLineStyle(0); //@
  YacineStyle->SetHistLineWidth(2); //@
  YacineStyle->SetEndErrorSize(0);
  YacineStyle->SetErrorX(0.);
  YacineStyle->SetMarkerColor(kBlue+3);
  YacineStyle->SetMarkerSize (0.7); //@
  YacineStyle->SetMarkerStyle(20); //@
  
  // for function
  YacineStyle->SetFuncColor(kOrange-3);
  YacineStyle->SetFuncStyle(1);
  YacineStyle->SetFuncWidth(2);
  YacineStyle->SetOptFit(01100); 
  YacineStyle->SetFitFormat("3.4f"); //gStyle->SetFitFormat("3.1g");
  
  
  // for the statistic box
  YacineStyle->SetOptStat(0);
  YacineStyle->SetStatBorderSize(0);
  YacineStyle->SetStatFont(42);
  YacineStyle->SetStatFontSize(0.07);
  YacineStyle->SetStatColor(0);
  YacineStyle->SetStatStyle(0);
  YacineStyle->SetStatW(0.25);
  YacineStyle->SetStatH(0.125);
  YacineStyle->SetStatX(0.90);
  YacineStyle->SetStatY(0.90);
  YacineStyle->SetStatBorderSize(0);
  
  //YacineStyle->SetStatX(1.0-YacineStyle->GetPadRightMargin()-0.02);
  //YacineStyle->SetStatY(1.0-YacineStyle->GetPadTopMargin()-0.02);
  
  // Margins
  YacineStyle->SetPadBottomMargin(0.15);
  YacineStyle->SetPadTopMargin   (0.13);
  YacineStyle->SetPadRightMargin (0.13);
  YacineStyle->SetPadLeftMargin  (0.15);
  
  // Global Title
  YacineStyle->SetTitleFont  (42); //@
  YacineStyle->SetTitleSize  (0.07);//@
  YacineStyle->SetTitleColor (1);
  YacineStyle->SetTitleTextColor(1);
  YacineStyle->SetTitleFillColor(0);                // Changed -- JEK
  YacineStyle->SetTitleFontSize(0.05); //@
  YacineStyle->SetTitleBorderSize(0);
  YacineStyle->SetTitleAlign(33);
  YacineStyle->SetTitleX(0.8);
  YacineStyle->SetTitleY(0.95);
  // Axis Titles
  YacineStyle->SetTitleColor (1,   "xyz");
  YacineStyle->SetTitleFont  (42,  "xyz");
  YacineStyle->SetTitleSize  (0.055,"xyz");         
  YacineStyle->SetTitleOffset(1.3 ,"yz");
  YacineStyle->SetTitleOffset(1.2 ,"x");
  //YacineStyle->SetTitleXOffset(1.08);
  //YacineStyle->SetTitleYOffset(1.2);
  
  // Axis Labels
  YacineStyle->SetLabelColor (kBlack,"xyz");
  YacineStyle->SetLabelFont  (42,    "xyz");
  YacineStyle->SetLabelOffset(0.015, "xyz");
  YacineStyle->SetLabelSize  (0.05,  "xyz");
  
  // Legend
  YacineStyle->SetLegendBorderSize(0);
  
  // Axis
  YacineStyle->SetAxisColor  (1,    "XYZ");
  YacineStyle->SetTickLength (0.03, "XYZ");
  YacineStyle->SetNdivisions (508,  "XYZ");
  YacineStyle->SetStripDecimals(kTRUE);
  
  // Change for log plots
  YacineStyle->SetOptLogx(0);
  YacineStyle->SetOptLogy(0);
  YacineStyle->SetOptLogz(0);


  
  // histogram titles
  // YacineStyle->SetOptTitle(0);
  // For a Pretty Plalette
  //const Int_t NRGBs = 5;
  const Int_t NCont = 200;
  //Double_t stops[NRGBs] = { 0.00, 0.34, 0.61, 0.84, 1.00 };
  //Double_t red[NRGBs]   = { 0.00, 0.00, 0.87, 1.00, 0.51 };
  //Double_t green[NRGBs] = { 0.00, 0.81, 1.00, 0.20, 0.00 };
  //Double_t blue[NRGBs]  = { 0.51, 1.00, 0.12, 0.00, 0.00 };
  //TColor::CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont);
  //YacineStyle->SetNumberContours(NCont); 
  
  YacineStyle->SetPalette(53,0); 
  YacineStyle->SetNumberContours(NCont);
  
  //====> done
  YacineStyle->cd();
  gROOT->ForceStyle();
  gStyle->ls();

}


void rootlogon(){
  setYacineStyle();
}

// on the grid 
void onGrid(bool gridOn) {
  YacineStyle->SetPadGridX(gridOn);
  YacineStyle->SetPadGridY(gridOn);
}

// on the stat option
void onStatOpt(bool onStat)
{
  if(onStat) YacineStyle->SetOptStat("emr");
  else       YacineStyle->SetOptStat(0);
} 

void onFitOpt(bool onStat)
{
  if(onStat) YacineStyle->SetOptStat("emr");
  else       YacineStyle->SetOptStat(0);
} 

void onTranspacy(bool trans){
  YacineStyle->SetCanvasColor(-1);     // chaned fron kWhite to -1 
  YacineStyle->SetPadColor(-1);        // chaned fron kWhite to -1
  YacineStyle->SetFrameFillColor(-1); 
  YacineStyle->SetTitleFillColor(-1);
  YacineStyle->SetHistFillColor(-1);
  
}


