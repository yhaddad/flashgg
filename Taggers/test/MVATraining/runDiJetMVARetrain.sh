#!/usr/bin/bash

# Author: Louie Corpe, adapated from Y.Haddad
# Email : lcorpe@cern.ch


export WORKSPACE=$PWD
TAGGERS=${CMSSW_BASE}/flashgg/Taggers/test
NEvent=10000

if [ -n $1 ]
then
    NEvent=$1
fi

echo
echo -e "##################################################"
echo -e "######     RETRAINING VBF DIJET MVA         ######"
echo -e "##################################################"
echo
echo -e "+++++++++++ Generate the Training Trees ++++++++++"
echo -e "+++++++++++ with := ${NEvent}     ++++++++++++++++"
echo 

# run the script
# fggRunJobs.py --load test_jobs.json -d test_jobs_26 -x cmsRun MicroAODtoWorkspace.py maxEvents=-1 -n 50 -q hepshort.q -D -P useAAA=1 --no-use-tarball
# this is for the CHS
echo -e "+++++++++++ Generate PFCHS Traininig +++++++++++++"
fggRunJobs.py --load VBFMVATrainingSamplesWithPUPPI.json \
    -d ${WORKSPACE}/test_diphodijet_pfchs_training \
    -x cmsRun VBFDiPhoDiJetMVA_Training.py maxEvents=${NEvent}  \
    -q hepshort.q useAAA=1 --no-use-tarball
#
#echo -e "+++++++++++ Generate PUPPI Traininig +++++++++++++"
#fggRunJobs.py --load VBFMVATrainingSamplesWithPUPPI.json \
#    -d ${WORKSPACE}/test_diphodijet_puppi_training \
#    -x cmsRun VBFDiPhoDiJetMVA_PUPPI_Training.py maxEvents=${NEvent}  \
#    -q hepshort.q useAAA=1 --no-use-tarball
#
#echo 
#echo -e "+++++++++++ Run the training macro ++++++++++++++"
#echo
## run the training on background and without diplays
#mkdir -p plots
#
#root  -l -q VBFDiPhoDiJetMVA_Training.cc++\(\"${NEvent}\",\"VBF\",\"CHS\"\)
#root  -l -q VBFDiPhoDiJetMVA_Training.cc++\(\"${NEvent}\",\"VBF\",\"PUPPI\"\)
#
#echo 
#echo -e "+++++++++++ Applying the MVA +++++++++++++++++"
#echo
#
#fggRunJobs.py --load VBFMVATrainingSamplesWithPUPPI.json \
#    -d ${WORKSPACE}/test_diphodijet_pfchs_compare \
#    -x cmsRun VBFDiPhoDiJetMVA_Compare.py maxEvents=${NEvent}  \
#    -q hepshort.q useAAA=1 --no-use-tarball
#
#fggRunJobs.py --load VBFMVATrainingSamplesWithPUPPI.json \
#    -d ${WORKSPACE}/test_diphodijet_puppi_compare \
#    -x cmsRun VBFDiPhoDiJetMVA_PUPPI_Compare.py maxEvents=${NEvent}  \
#    -q hepshort.q useAAA=1 --no-use-tarball
#
#echo 
#echo -e "+++++++++++ Generating ROC curves ++++++++++++++++"
#echo
#
#root -l -q makeROC_CHS_PUPPI.cc++\(\"${NEvent}\",\"VBF\"\)
#
#echo 
#echo -e "##################################################"
#echo -e "######          RETRAINING COMPLETE         ######"
#echo -e "##################################################"
#echo
##echo -e " You can retrieve your ROC curve for this training from plots/VBF_ROCs.pdf
