#!/usr/bin/bash

export SOURCE=${CMSSW_BASE}/flashgg/Taggers/test/VBFProduction

fggRunJobs.py --load data/VBFTraining-RunIISpring15-ReMiniAOD-BetaV7-25ns.json \
    -d ./output_vbfDumper_cfg_3rdjetmerge_dijet \
    -x cmsRun vbfDumper_cfg_3rdjetmerge_dijet.py maxEvents=-1 -n 50 \
    -q hepmedium.q --no-use-tarball useAAA=1 
