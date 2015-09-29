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
#include <TLegendEntry.h>

#include <vector>
#include <map>

TCanvas* DrawVariable(TH1 *h1, TH1 *h2, TString name="", bool logy=false, bool norm=true,bool addSum=false)
{
    TCanvas *c_ = new TCanvas(name + "_cvar", name , 500,500 + int(500/10.));
    c_->cd();
    if(logy) gPad->SetLogy();
    TH1F *sum = (TH1F*) h1->Clone("sum");
    
    if(addSum)
        {
            sum->Add(h2);
        }

    
    
    h1->SetLineColor(kRed);
    h2->SetLineColor(kBlue);
    
    h1->SetMarkerColor(kRed);
    h2->SetMarkerColor(kBlue);
    
    if(norm){
        h2->Scale(1.0/h2->Integral());
        h1->Scale(1.0/h1->Integral());
    }
    
    if(h1->GetMaximum() >= h2->GetMaximum()){
        if(addSum){
            if(!logy)sum->GetYaxis()->SetRangeUser(0,sum->GetMaximum()*1.1);
            sum->Draw("hist" );
            h1->Draw ("hist same");
            h2->Draw ("hist same");
        }else{
            if(!logy)h1->GetYaxis()->SetRangeUser(0,h1->GetMaximum()*1.1);
            h1->Draw ("hist");
            h2->Draw ("hist same");
        }
    }else{
        if(addSum){
            if(!logy)sum->GetYaxis()->SetRangeUser(0,sum->GetMaximum()*1.1);
            sum->Draw("hist");
            h1->Draw ("hist same");
            h2->Draw ("hist same");
        }else{
            if(!logy)h2->GetYaxis()->SetRangeUser(0,h2->GetMaximum()*1.1);
            h2->Draw ("hist ");
            h1->Draw ("hist same");
        }
        
    }
    return c_;
}
TGraph *makeROC( TH1 *sig, TH1 *bkg )
{
    
    gStyle->SetOptStat( 0 );
    sig->Sumw2( 0 );
    bkg->Sumw2( 0 );
    TGraph *g_e = new TGraph();

    g_e->SetMarkerSize( 1 );
    //g_e->SetMarkerStyle(21);

    bool printFlag = 0;
    int N0 = bkg->GetNbinsX();
    std::cout << "debug " << N0 << std::endl;
    const unsigned int N = N0;
    float y[N];
    float signal[N];
    int i = 0;

    for( unsigned int n = 0; n < N; n++ ) {
        signal[n] =  sig->Integral( 0, n ) / sig->Integral( 0, N );
        y[n]     = ( bkg->Integral( 0, n ) / bkg->Integral( 0, N ) );

        if( y[n] == 0 ) {
            i++;
            continue;
        }

        if( signal[n] > 0.98 && printFlag == 0 ) {
            std::cout << "Better than 97 pc eff.("
                      << signal[n] << "). Bin "
                      << n << ", x value "
                      << n *sig->GetBinWidth( n ) << std::endl;

            printFlag = 1;
        }
        //g_e->SetPoint(n-i,1-signal[n], y[n]);
        g_e->SetPoint( n - i, 1 - y[n], 1 - signal[n] );

        //use 1-n for signal because I am integrating from bin 0 to bin N, which is techincally asking how to reject signal.
    }
    return g_e;
    //leg->Draw();
}

void Draw2Legend( TH1 *histo1,
                  TH1 *histo2,
                  std::string label1,
                  std::string label2 )
{
    TLegend *legend ;
    
    legend = new TLegend( 0.5, 0.77, 1.0 - gStyle->GetPadRightMargin(), 1.0 - gStyle->GetPadTopMargin(), NULL, "brNDC" );
    
    legend->SetTextAlign( 12 );
    TLegendEntry *entry1 = legend->AddEntry( histo1, label1.c_str(), "L" );
    entry1->SetTextColor( histo1->GetLineColor() );

    TLegendEntry *entry2 = legend->AddEntry( histo2, label2.c_str(), "L" );
    entry2->SetTextColor( histo2->GetLineColor() );

    legend->SetFillColor( 0 );
    legend->SetFillStyle( 0 );
    legend->Draw();
}


void Draw2Legend( TGraph *histo1,
                  TGraph *histo2,
                  std::string label1,
                  std::string label2 )
{
    TLegend *legend ;
    
    legend = new TLegend( 0.6, 0.8, 0.9, 0.9, NULL, "brNDC" );
    
    legend->SetTextAlign( 11 );
    TLegendEntry *entry1 = legend->AddEntry( histo1, label1.c_str(), "L" );
    entry1->SetTextColor( histo1->GetLineColor() );

    TLegendEntry *entry2 = legend->AddEntry( histo2, label2.c_str(), "L" );
    entry2->SetTextColor( histo2->GetLineColor() );

    legend->SetFillColor( 0 );
    legend->SetFillStyle( 0 );
    legend->Draw();
}

void SaveCanvas(TCanvas *cc, TString name="_c_"){
    cc->cd();
    cc->SaveAs("plots/" + name + ".png");
    cc->SaveAs("plots/" + name + ".pdf");
}

void makeROC_CHS_PUPPI( TString Nevent = "10000", TString Level = "VBF" , TString method = "BDT" )
{

    TString path   = "test_diphodijet_compare/";
    TString branch = "Presel";

    std::map<TString, TString>  samples_name;
    std::map<TString, float>  samples_weight;
    
    std::map<TString, std::map<TString,TH1F*> >   inputHistoPFCHS;
    std::map<TString, std::map<TString,TH1F*> >   inputHistoPUPPI;
    
    std::map<TString, TTree* >   outputTree_PFCHS;
    std::map<TString, TTree* >   outputTree_PUPPI;
    std::map<TString, TFile*>  inputFiles;
    
    
    std::map<TString,TString> var_list; // var name and histogram binning
    std::map<TString,bool>    var_logscale; // var name and histogram binning

    var_list["dijet_abs_dEta"     ] = "(100, 0,10)"; 
    //var_list["dijet_leadEta"      ] = "(100,-5,5)"; 
    //var_list["dijet_subleadEta"   ] = "(100,-5,5)"; 
    //var_list["dijet_LeadJPt"      ] = "(125,0,500)"; 
    //var_list["dijet_SubJPt"       ] = "(125,0,500)"; 
    //var_list["dijet_Zep"          ] = "(100,0,10)"; 
    //var_list["dijet_Mjj"          ] = "(120,0,1200)"; 
    //var_list["dipho_PToM"         ] = "(100,0,4)"; 
    //var_list["leadPho_PToM"       ] = "(100,0,4)"; 
    //var_list["sublPho_PToM"       ] = "(100,0,4)"; 
    //var_list["dijet_dPhi_trunc"   ] = "(75,0,3)";
    var_list["vbfMvaResult_value" ] = "(200,-1,1)"; 

    var_logscale["dijet_abs_dEta"     ] = false; 
    var_logscale["dijet_leadEta"      ] = false;
    var_logscale["dijet_subleadEta"   ] = false;
    var_logscale["dijet_LeadJPt"      ] = true; 
    var_logscale["dijet_SubJPt"       ] = true; 
    var_logscale["dijet_Zep"          ] = false;
    var_logscale["dijet_Mjj"          ] = true; 
    var_logscale["dipho_PToM"         ] = true;
    var_logscale["leadPho_PToM"       ] = true;
    var_logscale["sublPho_PToM"       ] = true;
    var_logscale["dijet_dPhi_trunc"   ] = true;
    var_logscale["vbfMvaResult_value" ] = false;
    
    
    
    // the file sample names
    if (Nevent != "") Nevent = "_numEvent" + Nevent;
    samples_name["vbf_m125_13TeV"     ] =  path + "output_VBFHToGG_M-125_13TeV_powheg_pythia8" + Nevent + "_histos.root";
    samples_name["gamJet40toInf_13TeV"] =  path + "output_GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8" + Nevent + "_histos.root";
    samples_name["gamJet20to40_13TeV" ] =  path + "output_GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8" + Nevent + "_histos.root";
    samples_name["ggf_m125_13TeV"     ] =  path + "output_GluGluHToGG_M-125_13TeV_powheg_pythia8" + Nevent + "_histos.root";
    //samples_name["dy_toll_m50_13TeV"  ] =  path + "output_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8" + Nevent + "_histos.root";
    samples_name["gamgamjetbox_13TeV" ] =  path + "output_DiPhotonJetsBox_MGG-80toInf_13TeV-Sherpa" + Nevent + "_histos.root";
    //samples_name["qcd_30to40_13TeV"   ] =  path + "output_QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8" + Nevent + "_histos.root";
    //samples_name["qcd_30toInf_13TeV"  ] =  path + "output_QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8" + Nevent + "_histos.root";
    //samples_name["qcd_40toInf_13TeV"  ] =  path + "output_QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8" + Nevent + "_histos.root";
    //samples_name[""        ] =  path + "" + Nevent + "_histos.root";
    
    // retrival of all the plots for different samples
    float weight = 0;
    for(std::map<TString, TString>::iterator it = samples_name.begin();
        it != samples_name.end(); it++){
        inputFiles[it->first] = TFile::Open( it->second );
        //std::vector<TH1F*> test;
        //inputHistoPFCHS[it->first] =  std::vector<TH1F*>();//std::vector<TH1F*>() ;
        //inputHistoPUPPI[it->first] =  std::vector<TH1F*>();//std::vector<TH1F*>() ;
        
        //outputBDT_PFCHS[it->first] = (TH1F*)inputFiles[it->first]->Get( Level + "MVADumper/histograms/"     + it->first +"_"+ branch + Level + "DiJetoutputBDT");
        //outputBDT_PUPPI[it->first] = (TH1F*)inputFiles[it->first]->Get( Level + "MVADumperPUPPI/histograms/"+ it->first +"_"+ branch + Level + "DiJetoutputBDT");
        
        // get the weights
        //std::cout << ":: "<< Level + "MVADumper/trees/"+it->first +"_"+ branch + Level + "DiJet" << std::endl;
        outputTree_PFCHS[it->first]= (TTree*) inputFiles[it->first]->Get( Level + "MVADumper/trees/"     +it->first +"_"+ branch + Level + "DiJet");
        outputTree_PUPPI[it->first]= (TTree*) inputFiles[it->first]->Get( Level + "MVADumperPUPPI/trees/"+it->first +"_"+ branch + Level + "DiJet");
        
        for(std::map<TString, TString>::iterator iv = var_list.begin();
            iv != var_list.end(); iv++)
            {
                gDirectory->cd();
                
                outputTree_PFCHS[it->first]->Project("h_PFCHS_" + iv->first + iv->second, iv->first,"weight");
                outputTree_PUPPI[it->first]->Project("h_PUPPI_" + iv->first + iv->second, iv->first,"weight");
                //gDirectory->ls();
                std::cout << "create plot::" <<  "h_PFCHS_" + iv->first + iv->second << "\t pointer::"<< (TH1F*)gDirectory->Get( "h_PFCHS_" + iv->first + iv->second ) << std::endl;
                inputHistoPFCHS[it->first][iv->first] = (TH1F*)gDirectory->Get( "h_PFCHS_" + iv->first );
                inputHistoPUPPI[it->first][iv->first] = (TH1F*)gDirectory->Get( "h_PUPPI_" + iv->first );
            }
        //inputFiles[it->first]->Close();
    }
    //    
    std::map<TString, TH1F*>    var_bkg_PFHCS;
    std::map<TString, TH1F*>    var_bkg_PUPPI;
    
    for(std::map<TString, TString>::iterator iv = var_list.begin();
        iv != var_list.end(); iv++)
        {
            std::cout << "sum backgrounds :: " << iv->first << " p::"<< inputHistoPFCHS["vbf_m125_13TeV"][iv->first] << std::endl;
            var_bkg_PFHCS[iv->first] =  (TH1F*)inputHistoPFCHS["vbf_m125_13TeV"][iv->first]->Clone("bkg_PFCHS_" + var_list[iv->first]) ;
            var_bkg_PFHCS[iv->first]->Clear();
            var_bkg_PUPPI[iv->first] =  (TH1F*)inputHistoPUPPI["vbf_m125_13TeV"][iv->first]->Clone("bkg_PUPPI_" + var_list[iv->first]) ;
            var_bkg_PUPPI[iv->first]->Clear();
            
            inputHistoPFCHS["vbf_m125_13TeV"][iv->first]->SetLineColor( kRed );
            inputHistoPUPPI["vbf_m125_13TeV"][iv->first]->SetLineColor( kRed );
            
            for(std::map<TString, TString>::iterator it = samples_name.begin();
                it != samples_name.end(); it++){
                if( it->first == "vbf_m125_13TeV") continue;
                var_bkg_PFHCS[iv->first]->Add(inputHistoPFCHS[it->first][iv->first]);//,double(samples_weight[it->first]));
                var_bkg_PUPPI[iv->first]->Add(inputHistoPUPPI[it->first][iv->first]);//,double(samples_weight[it->first]));
            }
            
            var_bkg_PFHCS[iv->first]->SetLineColor(kBlack);
            var_bkg_PUPPI[iv->first]->SetLineColor(kBlack);
            
            DrawVariable(var_bkg_PFHCS[iv->first],inputHistoPFCHS["vbf_m125_13TeV"][iv->first],"PFCHS_" + iv->first,var_logscale[iv->first],true);
            Draw2Legend (var_bkg_PFHCS[iv->first],inputHistoPFCHS["vbf_m125_13TeV"][iv->first],"(PFCHS) sum background","(PFCHS) vbf signal");
            
            DrawVariable(var_bkg_PUPPI[iv->first],inputHistoPUPPI["vbf_m125_13TeV"][iv->first],"PUPPI_" + iv->first,var_logscale[iv->first],true);
            Draw2Legend (var_bkg_PUPPI[iv->first],inputHistoPUPPI["vbf_m125_13TeV"][iv->first],"(PUPPI) sum background","(PUPPI) vbf signal");
            std::cout << "------------------------" << std::endl;
        }
   
    //TH1F * outputBDT_PFCHS_allbkg = (TH1F*) outputBDT_PFCHS["vbf_m125_13TeV"]->Clone("bkg_PFCHS_outputBDT") ;
    //outputBDT_PFCHS_allbkg->Clear();
    //TH1F * outputBDT_PUPPI_allbkg = (TH1F*) outputBDT_PUPPI["vbf_m125_13TeV"]->Clone("bkg_PUPPI_outputBDT") ;
    //outputBDT_PFCHS_allbkg->Clear();
    //
    //for(std::map<TString, TString>::iterator it = samples_name.begin();
    //    it != samples_name.end(); it++){
    //    if( it->first == "vbf_m125_13TeV" ) continue;
    //    outputBDT_PFCHS_allbkg->Add(outputBDT_PFCHS[it->first]);//,double(samples_weight[it->first]));
    //    outputBDT_PUPPI_allbkg->Add(outputBDT_PUPPI[it->first]);//,double(samples_weight[it->first]));
    //}
    //
    //TGraph *gr_pfchs = makeROC( outputBDT_PFCHS["vbf_m125_13TeV"], outputBDT_PFCHS_allbkg);
    //TGraph *gr_puppi = makeROC( outputBDT_PUPPI["vbf_m125_13TeV"], outputBDT_PUPPI_allbkg );
    //
    //TCanvas *crocs = new TCanvas( "crocs", "ROCs", 600, 600 );
    //crocs->cd();
    //
    //TMultiGraph *mul  = new TMultiGraph();
    //gr_pfchs->SetMarkerColor( kBlack );
    //gr_pfchs->SetLineColor  ( kBlack );
    //gr_puppi->SetMarkerColor( kRed );
    //gr_puppi->SetLineColor  ( kRed );
    //
    //mul->Add( gr_pfchs );
    //mul->Add( gr_puppi );
    //
    //mul->SetTitle( ";background efficiency;signal efficiency" );
    //mul->Draw( "AL" );
    //
    //Draw2Legend( gr_pfchs, gr_puppi, "PFCHS DiJet MVA", "PUPPI DiJet MVA" );
    //
    //crocs->SaveAs( "plots/" + Level + "_ROCs.pdf" );
    //crocs->SaveAs( "plots/" + Level + "_ROCs.png" );
    

}

// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

