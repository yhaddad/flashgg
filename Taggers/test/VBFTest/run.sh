#!/usr/bin/sh

fggRunJobs.py --load VBFMVATrainingSamplesWithPUPPI.json \
    -d ${PWD} \
    -x cmsRun vbfDumper_cfg.py maxEvents=$1  \
    -q hepmedium.q --no-use-tarball useAAA=1 
