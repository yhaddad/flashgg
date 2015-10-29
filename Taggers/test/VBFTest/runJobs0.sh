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
cmsRun /home/hep/yhaddad/CMSSW_7_4_12/src/flashgg/Taggers/test/VBFTest/vbfDumper_cfg.py maxEvents= useAAA=1 campaign=RunIISpring15-50ns processIdMap=/home/hep/yhaddad/CMSSW_7_4_12/src/flashgg/Taggers/test/VBFTest/config.json dataset=VBFHToGG_M-125_13TeV_powheg_pythia8 outputFile=/home/hep/yhaddad/CMSSW_7_4_12/src/flashgg/Taggers/test/VBFTest/output_VBFHToGG_M-125_13TeV_powheg_pythia8.root lastAttempt=1
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
    touch runJobs0.sh.done
    cp -pv runJobs0.sh.done /home/hep/yhaddad/CMSSW_7_4_12/src/flashgg/Taggers/test/VBFTest
else
    touch runJobs0.sh.fail
    cp -pv runJobs0.sh.fail /home/hep/yhaddad/CMSSW_7_4_12/src/flashgg/Taggers/test/VBFTest
fi

exit $retval

