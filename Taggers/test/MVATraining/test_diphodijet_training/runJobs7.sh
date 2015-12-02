#!/bin/bash

WD=$PWD
echo
echo
echo
cd /afs/cern.ch/work/j/jwright/private/VBFMVAStudy/CMSSW_7_4_15
eval $(scram runtime -sh)
cd $WD
mkdir /afs/cern.ch/work/j/jwright/private/VBFMVAStudy/CMSSW_7_4_15/src/flashgg/Taggers/test/MVATraining/test_diphodijet_training
echo "ls $X509_USER_PROXY"
ls $X509_USER_PROXY
cmsRun /afs/cern.ch/work/j/jwright/private/VBFMVAStudy/CMSSW_7_4_15/src/flashgg/Taggers/test/MVATraining/test_diphodijet_training/vbfDumper_cfg_new.py maxEvents=-1 campaign=RunIISpring15-ReMiniAOD-BetaV7-25ns processIdMap=/afs/cern.ch/work/j/jwright/private/VBFMVAStudy/CMSSW_7_4_15/src/flashgg/Taggers/test/MVATraining/test_diphodijet_training/config.json dataset=GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8 outputFile=/afs/cern.ch/work/j/jwright/private/VBFMVAStudy/CMSSW_7_4_15/src/flashgg/Taggers/test/MVATraining/test_diphodijet_training/output_GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8.root
retval=$?
if [[ $retval == 0 ]]; then
    errors=""
    for file in $(find -name '*.root' -or -name '*.xml'); do
        cp -pv $file /afs/cern.ch/work/j/jwright/private/VBFMVAStudy/CMSSW_7_4_15/src/flashgg/Taggers/test/MVATraining/test_diphodijet_training
        if [[ $? != 0 ]]; then
            errors="$errors $file($?)"
        fi
    done
    if [[ -n "$errors" ]]; then
       echo "Errors while staging files"
       echo "$errors"
       exit -2
    fi
fi

exit $retval

