#!/usr/bin/bash

# Author: Yacine Haddad
# Email : yhaddad@cern.ch



NEvent=10000

# this can be set on the flashgg.sh
#export WORKSPACE='/afs/cern.ch/work/y/yhaddad/'



#echo -e "+++++++++++ Generate the Trees ++++++++++++++++"
## create a working space
#mkdir -p ${WORKSPACE}/VBFTagging
#
## run the script
#fggRunJobs.py --load VBFMVATrainingSamples.json -d \
#    ${WORKSPACE}/VBFTagging/test_vbfmvatraining -x \
#    cmsRun VBFMVATag_Training.py maxEvents=${NEvent}
#
#
#echo -e "+++++++++++ Run The training ++++++++++++++++"
## run the training on background and without diplays
#echo -e "run --> '("${NEvent}")'"
#root -l VBFMVA_Training.cc++\(\"${NEvent}\"\)

#produce the trained tree and histograms  
fggRunJobs.py --load VBFMVATrainingSamples.json -d \
    ${WORKSPACE}/VBFTagging/test_vbfmva_compare/ -x \
    cmsRun VBFMVA_Compare.py maxEvents=${NEvent}

