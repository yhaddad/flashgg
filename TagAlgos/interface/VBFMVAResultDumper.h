#ifndef flashgg_VBFMVAResultDumpers_h
#define flashgg_VBFMVAResultDumpers_h

#include "flashgg/TagFormats/interface/VBFMVAResult.h"

#include "flashgg/TagAlgos/interface/CollectionDumper.h"

namespace flashgg 
{ 
	typedef CollectionDumper<std::vector<VBFMVAResult> > VBFMVAResultDumper;
	typedef CollectionDumper<std::vector<VBFMVAResult> ,
					VBFMVAResult,
					CutBasedClassifier<VBFMVAResult> > CutBasedVBFMVAResultDumper;
}

#endif 
