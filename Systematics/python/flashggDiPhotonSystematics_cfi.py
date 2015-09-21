import FWCore.ParameterSet.Config as cms

scaleBins = cms.PSet(
    variables = cms.vstring("abs(superCluster.eta)","r9"),
    bins = cms.VPSet(
                     cms.PSet( lowBounds = cms.vdouble(0.000,0.940), upBounds = cms.vdouble(1.000,999.000),
                              values = cms.vdouble( 0.00000 ), uncertainties = cms.vdouble( 0.00050 ) ),
                     cms.PSet( lowBounds = cms.vdouble(0.000,-999.000), upBounds = cms.vdouble(1.000,0.940),
                              values = cms.vdouble( 0.00000 ), uncertainties = cms.vdouble( 0.00050 ) ),
                     cms.PSet( lowBounds = cms.vdouble(1.000,0.940), upBounds = cms.vdouble(1.500,999.000),
                              values = cms.vdouble( 0.00000 ), uncertainties = cms.vdouble( 0.00060 ) ),
                     cms.PSet( lowBounds = cms.vdouble(1.000,-999.000), upBounds = cms.vdouble(1.500,0.940),
                              values = cms.vdouble( 0.00000 ), uncertainties = cms.vdouble( 0.00120 ) ),
                     cms.PSet( lowBounds = cms.vdouble(1.500,-999.000), upBounds = cms.vdouble(2.000,0.940),
                              values = cms.vdouble( 0.00000 ), uncertainties = cms.vdouble( 0.00200 ) ),
                     cms.PSet( lowBounds = cms.vdouble(1.500,0.940), upBounds = cms.vdouble(2.000,999.000),
                              values = cms.vdouble( 0.00000 ), uncertainties = cms.vdouble( 0.00300 ) ),
                     cms.PSet( lowBounds = cms.vdouble(2.000,-999.000), upBounds = cms.vdouble(3.000,0.940),
                              values = cms.vdouble( 0.00000 ), uncertainties = cms.vdouble( 0.00200 ) ),
                     cms.PSet( lowBounds = cms.vdouble(2.000,0.940), upBounds = cms.vdouble(3.000,999.000),
                              values = cms.vdouble( 0.00000 ), uncertainties = cms.vdouble( 0.00300 ) ),
                    ))


smearBins = cms.PSet(
    variables = cms.vstring("abs(superCluster.eta)","r9"),
    bins = cms.VPSet(
                     cms.PSet( lowBounds = cms.vdouble(0.000,-999.000), upBounds = cms.vdouble(1.000,0.940),
                              values = cms.vdouble( 0.00770, 0.00000, 6.73000 ), uncertainties = cms.vdouble( 0.00063, 0.16000 ) ),
                     cms.PSet( lowBounds = cms.vdouble(0.000,0.940), upBounds = cms.vdouble(1.000,999.000),
                              values = cms.vdouble( 0.00740, 0.00000, 6.60000 ), uncertainties = cms.vdouble( 0.00065, 0.16000 ) ),
                     cms.PSet( lowBounds = cms.vdouble(1.000,-999.000), upBounds = cms.vdouble(1.500,0.940),
                              values = cms.vdouble( 0.01260, 0.00000, 6.73000 ), uncertainties = cms.vdouble( 0.00103, 0.07000 ) ),
                     cms.PSet( lowBounds = cms.vdouble(1.000,0.940), upBounds = cms.vdouble(1.500,999.000),
                              values = cms.vdouble( 0.01120, 0.00000, 6.52000 ), uncertainties = cms.vdouble( 0.00132, 0.22000 ) ),
                     cms.PSet( lowBounds = cms.vdouble(1.500,-999.000), upBounds = cms.vdouble(2.000,0.940),
                              values = cms.vdouble( 0.01980 ), uncertainties = cms.vdouble( 0.00303 ) ),
                     cms.PSet( lowBounds = cms.vdouble(1.500,0.940), upBounds = cms.vdouble(2.000,999.000),
                              values = cms.vdouble( 0.01630 ), uncertainties = cms.vdouble( 0.00122 ) ),
                     cms.PSet( lowBounds = cms.vdouble(2.000,-999.000), upBounds = cms.vdouble(3.000,0.940),
                              values = cms.vdouble( 0.01920 ), uncertainties = cms.vdouble( 0.00092 ) ),
                     cms.PSet( lowBounds = cms.vdouble(2.000,0.940), upBounds = cms.vdouble(3.000,999.000),
                              values = cms.vdouble( 0.01860 ), uncertainties = cms.vdouble( 0.00078 ) ),
                    ))

flashggDiPhotonSystematics = cms.EDProducer('FlashggDiPhotonSystematicProducer',
		src = cms.InputTag("flashggFinalEGamma","finalDiPhotons"),
                SystMethods2D = cms.VPSet(
                                          cms.PSet( PhotonMethodName = cms.string("FlashggPhotonSmearStochastic"),
                                                    MethodName = cms.string("FlashggDiPhotonFromPhoton2D"),
                                                    Label = cms.string("MCSmearHighR9EB"),
                                                    OverallRange = cms.string("r9>0.94&&abs(eta)<1.5"),
                                                    NSigmas = cms.PSet( firstVar = cms.vint32(1,-1,0,0),
                                                                        secondVar = cms.vint32(0,0,1,-1)),
                                                    BinList = smearBins,
                                                    Debug = cms.untracked.bool(False),
                                                    ExaggerateShiftUp = cms.untracked.bool(True),
                                                    ),
                                          cms.PSet( PhotonMethodName = cms.string("FlashggPhotonSmearStochastic"),
                                                    MethodName = cms.string("FlashggDiPhotonFromPhoton2D"),
                                                    Label = cms.string("MCSmearLowR9EB"),
                                                    OverallRange = cms.string("r9<0.94&&abs(eta)<1.5"),
                                                    NSigmas = cms.PSet( firstVar = cms.vint32(1,-1,0,0),
                                                                        secondVar = cms.vint32(0,0,1,-1)),
                                                    BinList = smearBins,
                                                    Debug = cms.untracked.bool(False),
                                                    ExaggerateShiftUp = cms.untracked.bool(True),
                                                    )
                                          ),
		SystMethods = cms.VPSet(
                                        cms.PSet( PhotonMethodName = cms.string("FlashggPhotonScale"),
                                                  MethodName = cms.string("FlashggDiPhotonFromPhoton"),
                                                  Label = cms.string("MCScaleHighR9EB"),
                                                  NSigmas = cms.vint32(-1,1),
                                                  OverallRange = cms.string("r9>0.94&&abs(eta)<1.5"),
                                                  BinList = scaleBins,
                                                  Debug = cms.untracked.bool(False)
                                                  ),
                                        cms.PSet( PhotonMethodName = cms.string("FlashggPhotonScale"),
                                                  MethodName = cms.string("FlashggDiPhotonFromPhoton"),
                                                  Label = cms.string("MCScaleLowR9EB"),
                                                  NSigmas = cms.vint32(-1,1),
                                                  OverallRange = cms.string("r9<0.94&&abs(eta)<1.5"),
                                                  BinList = scaleBins,
                                                  Debug = cms.untracked.bool(False)
                                                  ),
                                        cms.PSet( PhotonMethodName = cms.string("FlashggPhotonScale"),
                                                  MethodName = cms.string("FlashggDiPhotonFromPhoton"),
                                                  Label = cms.string("MCScaleHighR9EE"),
                                                  NSigmas = cms.vint32(-1,1),
                                                  OverallRange = cms.string("r9>0.94&&abs(eta)>=1.5"),
                                                  BinList = scaleBins,
                                                  Debug = cms.untracked.bool(False)
                                                  ),
                                        cms.PSet( PhotonMethodName = cms.string("FlashggPhotonScale"),
                                                  MethodName = cms.string("FlashggDiPhotonFromPhoton"),
                                                  Label = cms.string("MCScaleLowR9EE"),
                                                  NSigmas = cms.vint32(-1,1),
                                                  OverallRange = cms.string("r9<0.94&&abs(eta)>=1.5"),
                                                  BinList = scaleBins,
                                                  Debug = cms.untracked.bool(False)
                                                  ),
                                        cms.PSet( PhotonMethodName = cms.string("FlashggPhotonSmearConstant"),
                                                  MethodName = cms.string("FlashggDiPhotonFromPhoton"),
                                                  Label = cms.string("MCSmearHighR9EE"),
                                                  NSigmas = cms.vint32(-1,1),
                                                  OverallRange = cms.string("r9>0.94&&abs(eta)>=1.5"),
                                                  BinList = smearBins,
                                                  Debug = cms.untracked.bool(False),
                                                  ExaggerateShiftUp = cms.untracked.bool(True),
                                                  ),
                                        cms.PSet( PhotonMethodName = cms.string("FlashggPhotonSmearConstant"),
                                                  MethodName = cms.string("FlashggDiPhotonFromPhoton"),
                                                  Label = cms.string("MCSmearLowR9EE"),
                                                  NSigmas = cms.vint32(-1,1),
                                                  OverallRange = cms.string("r9<0.94&&abs(eta)>=1.5"),
                                                  BinList = smearBins,
                                                  Debug = cms.untracked.bool(False),
                                                  ExaggerateShiftUp = cms.untracked.bool(True),
                                                  )
                                        )
                                      )

