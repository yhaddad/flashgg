
struct manualLimit {
    TString branchName;
    float   minValue;
    float   maxValue;
};

void TestMacro() {

    TFile *inputFile  = TFile::Open("output_numEvent150000.root");
    TFile *outputFile = new TFile("PlotOutput.root","RECREATE");

    TTree *tree = (TTree*)inputFile->Get("vbfTagDumper/trees/vbfh_13TeV_VBFDiJet");

    //Set manual ranges for certain variables - move this to an external file...
    std::vector<manualLimit> userLimits(16);
    userLimits[0].branchName = "jet1_pt_test"; userLimits[0].minValue = 0; userLimits[0].maxValue = 400; 
    userLimits[1].branchName = "jet2_pt_test"; userLimits[1].minValue = 0; userLimits[1].maxValue = 120; 
    userLimits[2].branchName = "jet3_pt_test"; userLimits[2].minValue = 0; userLimits[2].maxValue = 60; 
    userLimits[3].branchName = "J1J2_mjj"; userLimits[3].minValue = 0; userLimits[3].maxValue = 2000; 
    userLimits[4].branchName = "J1J3_mjj"; userLimits[4].minValue = 0; userLimits[4].maxValue = 100; 
    userLimits[5].branchName = "J2J3_mjj"; userLimits[5].minValue = 0; userLimits[5].maxValue = 50; 
    userLimits[6].branchName = "dMjj_d12_13"; userLimits[6].minValue = -1000; userLimits[6].maxValue = 2000; 
    userLimits[7].branchName = "dMjj_d12_23"; userLimits[7].minValue = -1000; userLimits[7].maxValue = 2000; 
    userLimits[8].branchName = "dMjj_d13_23"; userLimits[8].minValue = -1000; userLimits[8].maxValue = 1000; 
    userLimits[9].branchName = "dMjj_d12_13plus23"; userLimits[9].minValue = -1000; userLimits[9].maxValue = 2000; 
    userLimits[10].branchName = "Mjjj"; userLimits[10].minValue = 0; userLimits[10].maxValue = 2500; 
    userLimits[11].branchName = "J1J2J3_dipho_dPhi"; userLimits[11].minValue = 1; userLimits[11].maxValue = 3.14;
    userLimits[12].branchName = "misPt_mag_2J"; userLimits[12].minValue = 0; userLimits[12].maxValue = 200;
    userLimits[13].branchName = "misPt_mag_3J"; userLimits[13].minValue = 0; userLimits[13].maxValue = 200;
    userLimits[14].branchName = "misPt_mag_d3J2J"; userLimits[14].minValue = -100; userLimits[14].maxValue = 100;
    userLimits[15].branchName = "momentum4Volume"; userLimits[15].minValue = 0; userLimits[15].maxValue = 1e7;

    TObjArray *branchNames = tree->GetListOfBranches();

    unsigned numBins(100);
    std::vector<std::pair<float,float>> rangeVector(branchNames->GetEntries()); 
    std::vector<std::vector<TH1F*>> histograms(branchNames->GetEntries());
    std::vector<TString> categoryLabels(4);
    categoryLabels[0] = "FFF"; categoryLabels[1] = "JFF"; categoryLabels[2] = "JJF"; categoryLabels[3] = "JJJ";

    for (unsigned branch(0);branch<branchNames->GetEntries();branch++) {

        rangeVector[branch].first  = 999.;
        rangeVector[branch].second = 0.0;

        
        //Find range
        //Is it user-defined?
        bool userDefinedLimits = false; unsigned userLimitIndex(0);
        for (unsigned var(0);var<userLimits.size();var++) {
            if (branchNames->At(branch)->GetName() == userLimits[var].branchName) {
                userDefinedLimits = true;
                userLimitIndex = var;
            }
        }

        if (userDefinedLimits) {
            //Set predefined range
            std::cout << "--- User-defined range ---" << std::endl;
            rangeVector[branch].first  = userLimits[userLimitIndex].minValue;           
            rangeVector[branch].second = userLimits[userLimitIndex].maxValue;
        }else{
            //Find min and max, then set
            for (unsigned event(0);event<tree->GetEntries();event++) {    
                tree->GetEntry(event);
                float value = (float)tree->GetBranch(branchNames->At(branch)->GetName())->GetLeaf(branchNames->At(branch)->GetName())->GetValue();
                if (value < rangeVector[branch].first  && value > -990) rangeVector[branch].first = value;
                if (value > rangeVector[branch].second && value > -990) rangeVector[branch].second = value;
            }
        }

        std::cout << "The min is " << rangeVector[branch].first;
        std::cout << " and the max is " << rangeVector[branch].second;
        std::cout << " for branch " << branchNames->At(branch)->GetName() << std::endl;

        std::vector<TH1F*> catHists(categoryLabels.size());
        for (unsigned category(0);category<catHists.size();category++) {
            catHists[category] = new TH1F(branchNames->At(branch)->GetName() + TString("_") + categoryLabels[category], 
                                          branchNames->At(branch)->GetName(),
                                          numBins,rangeVector[branch].first,rangeVector[branch].second);
        }

        histograms[branch] = catHists;
    }

    for (unsigned branch(0);branch<branchNames->GetEntries();branch++) {
        for (unsigned event(0);event<tree->GetEntries();event++) {
            tree->GetEntry(event);
            unsigned category = (unsigned)tree->GetBranch("numberOfMatches")->GetLeaf("numberOfMatches")->GetValue();
            float value   = (float)tree->GetBranch(branchNames->At(branch)->GetName())->GetLeaf(branchNames->At(branch)->GetName())->GetValue();
            bool isTrijet = (bool)tree->GetBranch("has3Jet")->GetLeaf("has3Jet")->GetValue();
            if (value > -9990.0 && isTrijet) {
                histograms[branch][category]->Fill(value);
            }
        }
    }            

    
    TCanvas c1( "c1" );
    gStyle->SetOptStat( 0 );
    for (unsigned branch(0);branch<branchNames->GetEntries();branch++) {

        std::cout << branchNames->At(branch)->GetName() << std::endl;
        float peak(0); unsigned maxCat(0);           
        std::vector<TH1F*> scaledHists(histograms[branch].size());

        for (unsigned category(0);category<categoryLabels.size();category++) {
            if (category == 4) {histograms[branch][category]->SetLineColor(6);}
            else if (category == 2) {histograms[branch][category]->SetLineColor(8);}
            else {histograms[branch][category]->SetLineColor(category+1);}
            histograms[branch][category]->SetLineWidth(2);

            scaledHists[category] = histograms[branch][category];
            if (scaledHists[category]->Integral() > 0.0) {
                scaledHists[category]->Scale(1/histograms[branch][category]->Integral());
            }
        }

        for (unsigned category(0);category<categoryLabels.size();category++) {
            if (scaledHists[category]->GetMaximum() > peak) {
                peak   = scaledHists[category]->GetMaximum();
                maxCat = category; 
            }
        }

        scaledHists[maxCat]->Draw();
        for (unsigned category(0);category<categoryLabels.size();category++) {
            if (category != maxCat) {scaledHists[category]->Draw("same");}
        }
        c1.Print("Plots/" + TString(branchNames->At(branch)->GetName() + TString(".pdf")));

    }

}
