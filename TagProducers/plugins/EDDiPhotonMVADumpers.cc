#include "FWCore/Framework/interface/MakerMacros.h"
#include "flashgg/TagAlgos/interface/DiPhotonMVADumper.h"
#include "PhysicsTools/UtilAlgos/interface/EDAnalyzerWrapper.h"

typedef edm::AnalyzerWrapper<flashgg::DiPhotonMVAResultDumper> DiPhotonMVAResultDumper;
typedef edm::AnalyzerWrapper<flashgg::CutBasedDiPhotonMVAResultDumper> CutBasedDiPhotonMVAResultDumper;

DEFINE_FWK_MODULE(DiPhotonMVAResultDumper);
DEFINE_FWK_MODULE(CutBasedDiPhotonMVAResultDumper);

