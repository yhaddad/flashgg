#include "flashgg/DataFormats/interface/SinglePhotonView.h"

namespace flashgg {

    bool SinglePhotonView::MakePhoton() const
    {
        //cout << "Inside SinglePhotonView::MakePhoton" << endl;
        if( hasPhoton_ ) {
            //cout << "Leaving SinglePhotonView::MakePhoton" << endl;
            return false;
        } else if( hasVtx_ ) {
            //cout << "Inside SinglePhotonView::MakePhoton as hasVTx_ section" << endl;
            float vtx_X = vtxRef_->x();
            float vtx_Y = vtxRef_->y();
            float vtx_Z = vtxRef_->z();
            //cout << "done vtx assignments" << endl;

            float sc_X; 
            float sc_Y;
            float sc_Z;
            if( phoPtr_->hasFakeIDMVA() ) {
                sc_X = phoPtr_->p4().x();
                sc_Y = phoPtr_->p4().y();
                sc_Z = phoPtr_->p4().z();
            }
            else {
                sc_X = phoPtr_->superCluster()->x();
                sc_Y = phoPtr_->superCluster()->y();
                sc_Z = phoPtr_->superCluster()->z();
            }
            //cout << "done supercluster assignments" << endl;

            math::XYZVector vtx_Pos( vtx_X, vtx_Y, vtx_Z );
            math::XYZVector sc_Pos( sc_X, sc_Y, sc_Z );

            math::XYZVector direction = sc_Pos - vtx_Pos;
            math::XYZVector p = ( direction.Unit() ) * ( phoPtr_->energy() );
            math::XYZTLorentzVector corrected_p4( p.x(), p.y(), p.z(), phoPtr_->energy() );
            //cout << "done math::*vector assignments" << endl;

            pho_ =  flashgg::Photon( *phoPtr_ );
            pho_.setP4( corrected_p4 );
            hasPhoton_ = true;
            //cout << "done final member variable assignments" << endl;
        } else {
            pho_ = flashgg::Photon( *phoPtr_ );
            hasPhoton_ = true;
        }
        //cout << "Leaving SinglePhotonView::MakePhoton" << endl;
        return true;
    }


    void SinglePhotonView::MakePersistent()
    {
        if( !persistVec_.size() ) {
            MakePhoton();
            persistVec_.push_back( pho_ );
        }
    }

    const Photon *SinglePhotonView::photon() const
    {
        if( persistVec_.size() ) {
            return &persistVec_[0];
        } else {
            MakePhoton();
            return &pho_;
        }
    }

    Photon &SinglePhotonView::getPhoton()
    {
        if( !persistVec_.size() ) {
            throw cms::Exception( "IncorrectUsage" ) << "SinglePhotonView not persistified. If you really want a non-const photon, call MakePersistent()";
        }
        return persistVec_[0];
    }


}

// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

