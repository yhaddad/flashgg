#!/bin/bash

today=`date +%F`
outdir=/vols/cms/yhaddad/vbf-trees-RunII16Fall-80x/data-signal-region-${today}
fggRunJobs.py --load control_DoubleEG.json -d ${outdir} -x cmsRun standard_vbf_dumper_cfg_base.py maxEvents=-1 forwardJetRMSCut=0.03 runOnZee=False pujidWP=none -q hepshort.q --no-use-tarball useAAA=0 atIC=1 targetLumi=1.00e+3 -n 500 lumiMask=/home/hep/szenz/fromscratch29/CMSSW_8_0_8_patch1/src/flashgg/Taggers/test/submit_for_ed/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON.txt
