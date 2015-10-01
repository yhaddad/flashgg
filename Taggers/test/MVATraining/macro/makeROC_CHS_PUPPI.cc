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

TGraph *makeROC2( TH1 *sig, TH1 *bkg )
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

TGraph *makeROC( TH1 *sig, TH1 *bkg, TLegend *leg, int tc )
{

    gStyle->SetOptStat( 0 );
    sig->Sumw2( 0 );
    bkg->Sumw2( 0 );
    TGraph *g_e = new TGraph();

    g_e->SetMarkerColor( tc );
    g_e->SetLineColor( tc );
    g_e->SetMarkerSize( 1 );
    //g_e->SetMarkerStyle(21);

    bool printFlag = 0;
    int N0 = bkg->GetNbinsX();
    const unsigned int N = N0;
    float y[N];
    float signal[N];
    int i = 0;
    for( unsigned int n = 0; n < N; n++ ) {


        signal[n] = sig->Integral( 0, n ) / sig->Integral( 0, N );

        y[n] = ( bkg->Integral( 0, n ) / bkg->Integral( 0, N ) );

        if( y[n] == 0 ) {
            i++;
            continue;
        }
        if( signal[n] > 0.98 && printFlag == 0 ) {

            std::cout << "Better than 97 pc eff.(" << signal[n] << "). Bin " << n << ", x value " << n *sig->GetBinWidth( n ) << std::endl;
            printFlag = 1;
        }
        g_e->SetPoint( n - i, 1 - signal[n], y[n] );
        //use 1-n for signal because I am integrating from bin 0 to bin N, which is techincally asking how to reject signal.


    }
    g_e->SetTitle( "ROCs" );



    g_e->GetXaxis()->SetTitle( "signal efficiency" );
    g_e->GetXaxis()->SetRangeUser( 0, 1 );
    g_e->GetYaxis()->SetRangeUser( 0, 1 );
    g_e->GetYaxis()->SetTitle( "background rejection" );
    if( tc == 1 ) {
        g_e->Draw( "apl same" );
    } else {
        g_e->Draw( "pl same" );

    }
    //g_g->Draw("pl same");:w
    //
    //g_eg->Draw("pl same");
    //std::string name2 = name.str().replace(name.str().find("_signal_h"), 6, "");

    if( tc == 1 ) {
        leg->AddEntry( g_e, "PFCHS DiJet-MVA", "l" );
    } else {
        leg->AddEntry( g_e, "PUPPI DiJet-MVA", "l" );
    }

    //leg->Draw();
    return g_e;
}


void Draw2Legend( TGraph *histo1,
                  TGraph *histo2,
                  std::string label1,
                  std::string label2 )
{
    TLegend *legend ;

    legend = new TLegend( 0.3, 0.3, 0.65, 0.4, NULL, "brNDC" );

    legend->SetTextAlign( 22 );
    TLegendEntry *entry1 = legend->AddEntry( histo1, label1.c_str(), "L" );
    entry1->SetTextColor( histo1->GetLineColor() );

    TLegendEntry *entry2 = legend->AddEntry( histo2, label2.c_str(), "L" );
    entry2->SetTextColor( histo2->GetLineColor() );

    legend->SetFillColor( 0 );
    legend->SetFillStyle( 0 );
    legend->Draw();
}

void makeROC_CHS_PUPPI( TString Nevent = "10000", TString Level = "VBF" , TString method = "BDT" )
{

    
    TString path ;
    //if(Level =="VBF") {path="${WORKSPACE}/test_vbfmva_compare/";}
    //else if(Level =="VBFDiPhoDiJet") {
    //path = "${WORKSPACE}/test_diphodijet_compare/";
    path  = "test_diphodijet_compare/";
    //}
    //	else {
    //	std::cout << " Please specify option 2 as 'VBF' or 'VBFDiPhoDiJet' only" << std::endl;
    //	return;
    //	}

    //
    std::map<TString, TCanvas*> canv_pfchs;
    std::map<TString, TCanvas*> canv_puppi;
    std::map<TString, TH1F*>    h_sig_pfchs;
    std::map<TString, TH1F*>    h_bkg_pfchs;
    std::map<TString, TH1F*>    h_sig_puppi;
    std::map<TString, TH1F*>    h_bkg_puppi;
    std::vector<TString> var_list;
    
    //var_list.push_back("vbfMvaResult_value"); 
    var_list.push_back("dijet_abs_dEta"    ); 
    var_list.push_back("dijet_leadEta"     ); 
    var_list.push_back("dijet_subleadEta"  ); 
    var_list.push_back("dijet_LeadJPt"     ); 
    var_list.push_back("dijet_SubJPt"      ); 
    var_list.push_back("dijet_Zep"         ); 
    var_list.push_back("dijet_Mjj"         ); 
    var_list.push_back("dipho_PToM"        ); 
    var_list.push_back("leadPho_PToM"      ); 
    var_list.push_back("sublPho_PToM"      ); 
    var_list.push_back("dijet_dPhi_trunc"  ); 
                      
    
    TFile *f_sig = TFile::Open( path + "output_VBFHToGG_M-125_13TeV_powheg_pythia8_numEvent" + Nevent + "_histos.root" );
    TH1F  *pfchs_sig = ( TH1F * ) f_sig->Get( Level + "MVADumper/histograms/vbf_m125_13TeV_" + Level + "DiJetoutput" + method );
    TH1F  *puppi_sig = ( TH1F * ) f_sig->Get( Level + "MVADumperPUPPI/histograms/vbf_m125_13TeV_" + Level + "DiJetoutput" + method );
    
    // extract all the hisgrams in a directory
    for(int i=0; i < var_list.size() ; i++)
        {
            
            h_sig_pfchs[var_list[i]] =   ( TH1F * ) f_sig->Get( Level + "MVADumper/histograms/vbf_m125_13TeV_" + Level + "DiJet" + var_list[i] );
            h_sig_puppi[var_list[i]] =   ( TH1F * ) f_sig->Get( Level + "MVADumperPUPPI/histograms/vbf_m125_13TeV_" + Level + "DiJet" + var_list[i] );
            std::cout << "getting sig histogram :: ["<< h_sig_pfchs[var_list[i]] <<"] "<< Level + "MVADumper/histograms/vbf_m125_13TeV_" + Level + "DiJet" + var_list[i] << std::endl;
            h_sig_pfchs[var_list[i]]->SetLineColor( kBlue );
            h_sig_puppi[var_list[i]]->SetLineColor( kBlue );
        }
    
    
    TFile *f_bkg = TFile::Open( path + "output_GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8_numEvent" + Nevent + "_histos.root" );
    TH1F  *pfchs_bkg = ( TH1F * ) f_bkg->Get( Level + "MVADumper/histograms/gamJet_13TeV_" + Level + "DiJetoutput" + method );
    TH1F  *puppi_bkg = ( TH1F * ) f_bkg->Get( Level + "MVADumperPUPPI/histograms/gamJet_13TeV_" + Level + "DiJetoutput" + method );
    for(int i=0; i < var_list.size() ; i++)
        {
            h_bkg_pfchs[var_list[i]] =   ( TH1F * ) f_bkg->Get( Level + "MVADumper/histograms/gamJet_13TeV_" + Level + "DiJet" + var_list[i] );
            h_bkg_puppi[var_list[i]] =   ( TH1F * ) f_bkg->Get( Level + "MVADumperPUPPI/histograms/gamJet_13TeV_" + Level + "DiJet" + var_list[i] );
            std::cout << "getting bkg histogram :: ["<< h_bkg_pfchs[var_list[i]] <<"] "<< Level + "MVADumper/histograms/gamJet_13TeV_" + Level + "DiJet" + var_list[i] << std::endl;
            h_bkg_pfchs[var_list[i]]->SetLineColor( kRed );
            h_bkg_puppi[var_list[i]]->SetLineColor( kRed );
        }
    
    for(int i=0; i < var_list.size() ; i++)
        {
            canv_pfchs[var_list[i]] = new TCanvas("c_pfchs_" + var_list[i],"PFCHS",500,500); 
            canv_pfchs[var_list[i]]->cd();
            if ( h_sig_pfchs[var_list[i]]->GetMaximum() > h_sig_pfchs[var_list[i]]->GetMaximum() ){
                h_sig_pfchs[var_list[i]]->DrawNormalized("hist ");
                h_bkg_pfchs[var_list[i]]->DrawNormalized("hist same");
            }else{
                h_bkg_pfchs[var_list[i]]->DrawNormalized("hist ");
                h_sig_pfchs[var_list[i]]->DrawNormalized("hist same");
                
            }
        }
    for(int i=0; i < var_list.size() ; i++)
        {
            canv_puppi[var_list[i]] = new TCanvas("c_puppi_" + var_list[i],"PUPPI",500,500); 
            canv_puppi[var_list[i]]->cd();
            if ( h_sig_puppi[var_list[i]]->GetMaximum() > h_sig_puppi[var_list[i]]->GetMaximum() ){
                h_sig_puppi[var_list[i]]->DrawNormalized("hist ");
                h_bkg_puppi[var_list[i]]->DrawNormalized("hist same");
            }else{
                h_bkg_puppi[var_list[i]]->DrawNormalized("hist ");
                h_sig_puppi[var_list[i]]->DrawNormalized("hist same");
                
            }
        }
    
    puppi_sig->SetLineColor( kBlue );
    puppi_bkg->SetLineColor( kRed );
    
    pfchs_sig->SetLineColor( kBlue );
    pfchs_bkg->SetLineColor( kRed );
    
    TCanvas *cchs  = new TCanvas( "cchs", "BDT outputs", 700 , 700 );
    cchs->cd();
    pfchs_bkg->DrawNormalized( "hist " );
    pfchs_sig->DrawNormalized( "hist same" );
    
    TCanvas *cppi  = new TCanvas( "cppi", "BDT outputs", 700 , 700 );
    cppi->cd();
    puppi_sig->DrawNormalized( "hist" );
    puppi_bkg->DrawNormalized( "hist same" );






    
    TCanvas *c1 = new TCanvas( "c1", "ROCs", 600, 600 );
    c1->cd();
    c1->SetGridx();
    c1->SetGridy();
    c1->Modified();
    c1->Update();

    // old_bkg->Draw();
    std::vector<std::string> xxx;//={"signal","hgg"};
    xxx.push_back( "PFCHS DiJet-MVA" );
    xxx.push_back( "PUPPI DiJet-MVA" );

    int itc = 1;


    TMultiGraph *mul  = new TMultiGraph();

    TGraph *gr_pfchs = makeROC2( pfchs_sig, pfchs_bkg );
    TGraph *gr_puppi = makeROC2( puppi_sig, puppi_bkg );
    gr_pfchs->SetMarkerColor( kBlack );
    gr_pfchs->SetLineColor( kBlack );
    gr_puppi->SetMarkerColor( kRed );
    gr_puppi->SetLineColor( kRed );

    mul->Add( gr_pfchs );
    mul->Add( gr_puppi );

    mul->SetTitle( ";background efficiency;signal efficiency" );
    mul->Draw( "AL" );

    Draw2Legend( gr_pfchs, gr_puppi, "PFCHS DiJet MVA", "PUPPI DiJet MVA" );

    c1->SaveAs( "plots/" + Level + "_ROCs.pdf" );
    c1->SaveAs( "plots/" + Level + "_ROCs.png" );
    //TCanvas *c2 = new TCanvas("c2","",600,600);
    //c2->cd();
    //new_bkg->SetLineColor(kBlue);
    //new_sig->SetLineColor(kRed);
    //new_bkg->Draw();
    //new_sig->Draw("same");


}

// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

