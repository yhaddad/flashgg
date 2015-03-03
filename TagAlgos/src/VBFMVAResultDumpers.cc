#include "flashgg/TagAlgos/interface/VBFMVAResultDumper.h"

#include "flashgg/TagAlgos/interface/PluggableAnalyzer.h"

namespace flashgg {
	
	namespace fwlite {
		PLUGGABLE_ANALYZER(VBFMVAResultDumper);
		PLUGGABLE_ANALYZER(CutBasedVBFMVAResultDumper);
	}
}
