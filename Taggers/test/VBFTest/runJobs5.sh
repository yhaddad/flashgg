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
mkdir /home/hep/yhaddad/CMSSW_7_4_12/src/flashgg/Taggers/test/VBFTest
echo "ls $X509_USER_PROXY"
ls $X509_USER_PROXY
cmsRun /home/hep/yhaddad/CMSSW_7_4_12/src/flashgg/Taggers/test/VBFTest/vbfDumper_cfg.py maxEvents= useAAA=1 campaign=RunIISpring15-50ns processIdMap=/home/hep/yhaddad/CMSSW_7_4_12/src/flashgg/Taggers/test/VBFTest/config.json dataset=QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8 outputFile=/home/hep/yhaddad/CMSSW_7_4_12/src/flashgg/Taggers/test/VBFTest/output_QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8.root lastAttempt=1
retval=$?
if [[ $retval == 0 ]]; then
    errors=""
    for file in $(find -name '*.root' -or -name '*.xml'); do
        cp -pv $file /home/hep/yhaddad/CMSSW_7_4_12/src/flashgg/Taggers/test/VBFTest
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
    touch runJobs5.sh.done
    cp -pv runJobs5.sh.done /home/hep/yhaddad/CMSSW_7_4_12/src/flashgg/Taggers/test/VBFTest
else
    touch runJobs5.sh.fail
    cp -pv runJobs5.sh.fail /home/hep/yhaddad/CMSSW_7_4_12/src/flashgg/Taggers/test/VBFTest
fi

exit $retval

