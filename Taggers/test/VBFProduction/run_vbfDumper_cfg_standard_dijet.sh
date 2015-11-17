#!/usr/bin/bash

export SOURCE=${CMSSW_BASE}/flashgg/Taggers/test/VBFProduction

fggRunJobs.py --load data/VBFTraining-RunIISpring15-ReMiniAOD-BetaV7-25ns.json \
    -d output_vbfDumper_cfg_standard_dijet \
    -x cmsRun vbfDumper_cfg_standard_dijet.py maxEvents=-1 \
    -q hepmedium.q --no-use-tarball useAAA=1 \
    -n 50