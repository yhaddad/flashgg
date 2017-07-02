#ifndef FLASHgg_ZPlusGammaTag_h
#define FLASHgg_ZPlusGammaTag_h


#include "flashgg/DataFormats/interface/DiPhotonTagBase.h"
#include "flashgg/DataFormats/interface/DiPhotonMVAResult.h"
#include "flashgg/DataFormats/interface/Photon.h"
#include "DataFormats/Math/interface/deltaPhi.h"

namespace flashgg {

    class ZPlusGammaTag: public DiPhotonTagBase
    {
    public:
        ZPlusGammaTag();
        ~ZPlusGammaTag();

        ZPlusGammaTag *clone() const { return ( new ZPlusGammaTag( *this ) ); }

        ZPlusGammaTag( edm::Ptr<DiPhotonCandidate>, edm::Ptr<DiPhotonMVAResult>, edm::Ptr<Photon>);

        edm::Ptr<Photon> photon() const { return thePhoton_; }
        
        const float photonPt () const { return thePhoton_->pt(); }
        const float photonEta() const { return thePhoton_->eta(); }
        const float photonPhi() const { return thePhoton_->phi(); }

        edm::Ptr<DiPhotonCandidate> theZ() const { return diPhoton(); }
        const float zMass() const { return diPhoton()->mass(); }
        const float zPt  () const { return diPhoton()->pt(); }
        const float zEta () const { return diPhoton()->eta(); }
        const float zPhi () const { return diPhoton()->phi(); }
        const float deltaPhiZPhoton() const { return deltaPhi( diPhoton()->phi(), thePhoton_->phi() ) ; }
        const float vtxZCoord      () const { return diPhoton()->vtx()->z(); }

    private:
        edm::Ptr<Photon> thePhoton_;
    };

}

#endif
// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

