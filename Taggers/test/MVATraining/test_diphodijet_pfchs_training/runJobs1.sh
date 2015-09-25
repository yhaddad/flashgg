#!/bin/bash
mkdir -p $TMP/sgejob-$JOB_ID
cd $TMP/sgejob-$JOB_ID

WD=$PWD
echo
echo
echo
cd /home/hep/yhaddad/work/CMSSW_7_4_12
eval $(scram runtime -sh)
cd $WD
mkdir /home/hep/yhaddad/work/CMSSW_7_4_12/src/flashgg/Taggers/test/MVATraining/test_diphodijet_pfchs_training
echo "ls $X509_USER_PROXY"
ls $X509_USER_PROXY
cmsRun /home/hep/yhaddad/work/CMSSW_7_4_12/src/flashgg/Taggers/test/MVATraining/test_diphodijet_pfchs_training/VBFDiPhoDiJetMVA_Training.py maxEvents=5000 useAAA=1 campaign=flashggMicroAODSpring15 processIdMap=/home/hep/yhaddad/work/CMSSW_7_4_12/src/flashgg/Taggers/test/MVATraining/test_diphodijet_pfchs_training/config.json dataset=GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8 outputFile=/home/hep/yhaddad/work/CMSSW_7_4_12/src/flashgg/Taggers/test/MVATraining/test_diphodijet_pfchs_training/output_GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8.root
retval=$?
if [[ $retval == 0 ]]; then
    errors=""
    for file in $(find -name '*.root' -or -name '*.xml'); do
        cp -pv $file /home/hep/yhaddad/work/CMSSW_7_4_12/src/flashgg/Taggers/test/MVATraining/test_diphodijet_pfchs_training
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
if [[ $retval == 0 ]]; then
    touch runJobs1.sh.done
    cp -pv runJobs1.sh.done /home/hep/yhaddad/work/CMSSW_7_4_12/src/flashgg/Taggers/test/MVATraining/test_diphodijet_pfchs_training
else
    touch runJobs1.sh.fail
    cp -pv runJobs1.sh.fail /home/hep/yhaddad/work/CMSSW_7_4_12/src/flashgg/Taggers/test/MVATraining/test_diphodijet_pfchs_training
fi

exit $retval
