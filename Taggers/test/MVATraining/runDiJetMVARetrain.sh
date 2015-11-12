#!/usr/bin/bash

# Author: Louie Corpe, adapated from Y.Haddad
# Email : lcorpe@cern.ch


export WORKSPACE=$PWD
export SOURCE=${CMSSW_BASE}/flashgg/Taggers/test/MVATraining/

NEvent=40000

if [ -n $1 ]
then
    NEvent=$1
fi

echo
echo -e "##################################################"
echo -e "######     RETRAINING VBF DIJET MVA         ######"
echo -e "##################################################"
echo

echo 
echo -e "+++++++++++ Create working directories  ++++++++++"#
echo 

#if [ ! -d test_diphodijet_training ]; then 
#    mkdir -p ${WORKSPACE}/test_diphodijet_training
#    mkdir -p ${WORKSPACE}/test_diphodijet_compare
#    
#    ln -s ${WORKSPACE}/test_diphodijet_training  test_diphodijet_training
#    ln -s ${WORKSPACE}/test_diphodijet_compare   test_diphodijet_compare
#    
#    ls ${PWD} | grep test_diphodijet_
#else
#    ls ${PWD} | grep test_diphodijet_
#fi 

echo 
echo -e "+++++++++++ Generate the Training Trees ++++++++++"
echo -e "+++++++++++ with := ${NEvent}     ++++++++++++++++"
echo 

echo -e "+++++++++++ Generate VBF Traininigs +++++++++++++"
fggRunJobs.py --load data/VBFTraining-RunIISpring15-ReMiniAOD-BetaV7-25ns.json \

	      -d ${WORKSPACE}/test_diphodijet_training \
	      -x cmsRun vbfDumper_cfg_new.py maxEvents=-1 \
	      -q hepmedium.q --no-use-tarball useAAA=1 
echo 
echo -e "+++++++++++ Run the training macro ++++++++++++++"
echo 

#root  -l -q macro/VBFDiPhoDiJetMVA_Training.cc++\(\"${NEvent}\",\"VBF\",\"CHS\"\)
#root  -l -q macro/VBFDiPhoDiJetMVA_Training.cc++\(\"${NEvent}\",\"VBF\",\"PUPPI\"\)

#echo 
#echo -e "+++++++++++ Applying the MVA +++++++++++++++++"
#echo
#
##fggRunJobs.py --load data/VBFMVATrainingSamplesWithPUPPI.json \
##    -d ${WORKSPACE}/test_diphodijet_compare \
##    -x cmsRun VBFDiJetMVA_Compare.py maxEvents=${NEvent}  \
##    -q 1nh --no-use-tarball #useAAA=1 
##
#echo 
#echo -e "+++++++++++ Generating ROC curves ++++++++++++++++"
#echo
##
###
###root -l macro/makeROC_CHS_PUPPI.cc++\(\"${NEvent}\",\"VBF\"\)
###
##
#echo 
#echo -e "##################################################"
#echo -e "######          RETRAINING COMPLETE         ######"
echo -e "##################################################"
echo
#echo -e " You can retrieve your ROC curve for this training from plots/VBF_ROCs.pdf
