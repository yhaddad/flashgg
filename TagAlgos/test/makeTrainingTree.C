{
	float x=0;
	float y=0;
	float z=0;
	float xS=0;
	float yS=0;
	float zS=0;
	float xB=0;
	float yB=0;
	float zB=0;
	float w=1;
	TGraph2D *tg = new TGraph2D();
	TFile *f = new TFile ("training.root","RECREATE");;
	TTree *tS = new TTree ("TreeS","TreeS"); 
	tS->Branch("x", &xS, "x/F");
	tS->Branch("y", &yS, "y/F");
	tS->Branch("z", &zS, "z/F");

	TTree *tB = new TTree ("TreeB","TreeB"); 
	tB->Branch("x", &xB, "x/F");
	tB->Branch("y", &yB, "y/F");
	tB->Branch("z", &zB, "z/F");
	tB->Branch("weight", &w, "weight/F");

	TRandom3 rand;
	int p =0;
	int nTs =0;
	int nTb =0;

	for (int i =0; i<1000000; i++){
		x =100*(2*(rand.Rndm()-0.5));
		y =100*(2*(rand.Rndm()-0.5));
		z =100*(2*(rand.Rndm()-0.5));

		if (i%1000 ==0){

		std::cout << "filling event " << i<< std::endl;
		}

	//	std::cout << "x" << x << ", y " << y << ", z " << z << std::endl ;

		//if (sqrt(x*x+y*y+z*z) < 100){
		float R = 50;
		float r =20;
		if ((R-sqrt(x*x + y*y))*(R-sqrt(x*x+y*y)) + z*z < r*r){

			xS =x;
			yS =y;
			zS =z;
			tS->Fill();
			tg->SetPoint(p,xS,yS,zS);
			p++;
			nTs++;
		//	std::cout << "in shape" << std::endl;


		} else {

			xB =x;
			yB =y;
			zB =z;
			tB->Fill();
			nTb++;
		//	std::cout << "NOT in shape" << std::endl;



		}

	}
tS->Write("", TObject::kOverwrite);
tB->Write("", TObject::kOverwrite);
tg->GetZaxis()->SetRangeUser(-100,100);
tg->Draw("pcont");
tg->Write();
std::cout << "signal : " << nTs << ", nTb : " << nTb << std::endl;
}

















