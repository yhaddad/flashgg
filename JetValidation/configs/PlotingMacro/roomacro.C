/** MyRoot.C --- 
 *
 * Copyright (C) 2014 haddad yacine
 * Author: haddad yacine <yhaddad@cern.ch>
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation; either version 2, or (at
 * your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
 * Boston, MA 02110-1301, USA.
 */


#include <TGraphErrors.h>
#include <TGraph.h>
#include <string>
#include <TH1.h>
#include <TCanvas.h>
#include <TLegendEntry.h>
#include <TLegend.h>
#include <TPaveStats.h>
#include <TMultiGraph.h>
#include <map>

void DrawErrorBand(TGraphErrors *graph, std::string name="")
{
  TCanvas *c_ = new TCanvas((name+"_c").c_str(),"",500,500);
  c_->cd();
  graph->SetTitle(name.c_str());
  graph->SetFillColor(kAzure+1);
  graph->DrawClone("E3AL");
  TGraphErrors *gr = (TGraphErrors*)graph->Clone("gr_");
  
  for(int i=0; i < gr->GetN(); i++){
    gr->SetPointError(i,0.0,0.0);
  }
  gr->SetMarkerStyle(20);
  gr->SetFillColor(0);
  gr->DrawClone("PELSame");
}
void DrawGraph(TGraph *graph, std::string name="", bool onlyline = false)
{
  TCanvas *c_ = new TCanvas((name+"_c").c_str(),"",500,500);
  c_->cd();
  graph->SetTitle(name.c_str());
  if(onlyline){
    graph->DrawClone("AL");
  }else{
    graph->DrawClone("APL");
  }
}

void DrawMultiGraph(TMultiGraph *graph, std::string name="")
{
  TCanvas *c_ = new TCanvas((name+"_c").c_str(),"",500,500);
  c_->cd();
  graph->SetTitle(name.c_str());
  graph->DrawClone("APL");
}


void Draw2Legend(TH1 *histo1, 
		 TH1 *histo2,
		 std::string label1, 
		 std::string label2, std::string opt="1")
{
  TLegend *legend ;
  if(opt=="1") legend = new TLegend(0.5,0.75,0.85,0.85,NULL,"brNDC");
  if(opt=="2") legend = new TLegend(0.5,0.65,0.85,0.75,NULL,"brNDC");
  
  legend->SetTextAlign(22);
  TLegendEntry* entry1 = legend->AddEntry(histo1,label1.c_str(),"LP");  
  entry1->SetTextColor(histo1->GetLineColor());
  
  TLegendEntry* entry2 = legend->AddEntry(histo2,label2.c_str(),"LP");
  entry2->SetTextColor(histo2->GetLineColor());
  
  legend->SetFillColor(0); 
  legend->SetFillStyle(0); 
  legend->Draw(); 
}

void Draw3Legend(TH1 *histo1, 
		 TH1 *histo2,
		 TH1 *histo3,
		 std::string label1, 
		 std::string label2, 
		 std::string label3, 
		 std::string opt="1")
{
  TLegend *legend ;
  if(opt=="1") legend = new TLegend(0.5,0.75,0.85,0.85,NULL,"brNDC");
  if(opt=="2") legend = new TLegend(0.5,0.65,0.85,0.75,NULL,"brNDC");
  
  legend->SetTextAlign(22);
  TLegendEntry* entry1 = legend->AddEntry(histo1,label1.c_str(),"LP");  
  entry1->SetTextColor(histo1->GetLineColor());
  
  TLegendEntry* entry2 = legend->AddEntry(histo2,label2.c_str(),"LP");
  entry2->SetTextColor(histo2->GetLineColor());
  
  TLegendEntry* entry3 = legend->AddEntry(histo3,label3.c_str(),"LP");
  entry3->SetTextColor(histo3->GetLineColor());
  
  legend->SetFillColor(0); 
  legend->SetFillStyle(0); 
  legend->Draw(); 
}


void Draw3Legend(TGraph *histo1, 
		 TGraph *histo2,
		 TGraph *histo3,
		 std::string label1, 
		 std::string label2, 
		 std::string label3, 
		 std::string opt="1")
{
  TLegend *legend ;
  if(opt=="1") legend = new TLegend(0.5,0.75,0.85,0.85,NULL,"brNDC");
  if(opt=="2") legend = new TLegend(0.5,0.65,0.85,0.75,NULL,"brNDC");
  
  legend->SetTextAlign(22);
  TLegendEntry* entry1 = legend->AddEntry(histo1,label1.c_str(),"LP");  
  entry1->SetTextColor(histo1->GetLineColor());
  
  TLegendEntry* entry2 = legend->AddEntry(histo2,label2.c_str(),"LP");
  entry2->SetTextColor(histo2->GetLineColor());
  
  TLegendEntry* entry3 = legend->AddEntry(histo3,label3.c_str(),"LP");
  entry3->SetTextColor(histo3->GetLineColor());
  
  legend->SetFillColor(0); 
  legend->SetFillStyle(0); 
  legend->Draw(); 
}

//
//void DrawLegends(std::map<TString,TH1*> histo, 
//		 std::string opt="1")
//{
//  TLegend *legend ;
//  if(opt=="1") legend = new TLegend(0.5,0.75,0.85,0.85,NULL,"brNDC");
//  if(opt=="2") legend = new TLegend(0.5,0.65,0.85,0.75,NULL,"brNDC");
//  
//  legend->SetTextAlign(22);
//  
//  std::map<TString,TLegendEntry*> entries;
//  for (std::map<TString,TH1*>::iterator it=histo.begin(); it!=histo.end(); ++it){
//    entries[it->first] = legend->AddEntry(it->second,it->first.c_str(),"LP");  
//    entries[it->first]->SetTextColor(it->second->GetLineColor());
//  }
//  legend->SetFillColor(0); 
//  legend->SetFillStyle(0); 
//  legend->Draw(); 
//}
//
//void DrawLegends(std::map<TString,TGraphAsymmErrors*> histo, 
//		 std::string opt="1")
//{
//  TLegend *legend ;
//  if(opt=="1") legend = new TLegend(0.5,0.75,0.85,0.85,NULL,"brNDC");
//  if(opt=="2") legend = new TLegend(0.5,0.65,0.85,0.75,NULL,"brNDC");
//  
//  legend->SetTextAlign(22);
//  
//  std::map<TString,TLegendEntry*> entries;
//  for (std::map<TString,TGraphAsymmErrors*>::iterator it=histo.begin(); it!=histo.end(); ++it){
//    entries[it->first] = legend->AddEntry(it->second,it->first.c_str(),"LP");  
//    entries[it->first]->SetTextColor(it->second->GetLineColor());
//  }
//  legend->SetFillColor(0); 
//  legend->SetFillStyle(0); 
//  legend->Draw(); 
//}
