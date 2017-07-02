#include "flashgg/DataFormats/interface/DiPhotonCandidate.h"
#include "flashgg/DataFormats/interface/ZPlusGammaTag.h"
#include "CommonTools/CandUtils/interface/AddFourMomenta.h"

using namespace flashgg;

ZPlusGammaTag::ZPlusGammaTag() {}

ZPlusGammaTag::~ZPlusGammaTag() {}

ZPlusGammaTag::ZPlusGammaTag( edm::Ptr<DiPhotonCandidate> diPho, edm::Ptr<DiPhotonMVAResult> mvaRes, edm::Ptr<Photon> thePhoton) :
    DiPhotonTagBase::DiPhotonTagBase( diPho, mvaRes ) 
{
    thePhoton_ = thePhoton;
}

// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

