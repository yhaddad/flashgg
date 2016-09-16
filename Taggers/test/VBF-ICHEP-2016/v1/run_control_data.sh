#!/bin/bash

today=`date +%F`
outdir=/vols/cms/szenz/DY-Systs-Data-${today}
fggRunJobs.py --load control_data.json -d ${outdir} -x cmsRun standard_vbf_dumper_cfg.py maxEvents=-1 forwardJetRMSCut=0.03 runOnZee=True pujidWP=none -q hepshort.q --no-use-tarball useAAA=0 atIC=1 targetLumi=1.00e+3 -n 500 lumiMask=/home/hep/szenz/fromscratch29/CMSSW_8_0_8_patch1/src/flashgg/Taggers/test/submit_for_ed/Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON.txt
