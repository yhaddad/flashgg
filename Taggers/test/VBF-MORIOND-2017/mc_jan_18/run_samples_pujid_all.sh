#!/bin/bash

lumiMask=/home/hep/yhaddad/work/moriod17_jan_17/CMSSW_8_0_25/src/flashgg/Taggers/test/VBF-MORIOND-2017/mc_jan_18/Cert_271036-282092_13TeV_PromptReco_Collisions16_JSON.txt
json=/home/hep/yhaddad/work/moriod17_jan_17/CMSSW_8_0_25/src/flashgg/Taggers/test/VBF-MORIOND-2017/mc_jan_18/run_mc_files.json

# 
for wp in "tight" #"none" "tight" "medium" "loose"
do 
    today=`date +%F`
    outdir=/vols/cms/yhaddad/VBF-Tree-Moriond17/pujid-test-sklean-MVA-${wp}-${today}
    fggRunJobs.py --load ${json} -d ${outdir} \
		  -x cmsRun moriond_vbf_dumper_cfg.py maxEvents=-1 runOnZee=False \
		  -q hepmedium.q --no-use-tarball useAAA=1 targetLumi=1.00e+3 pujidWP=$wp \
		  lumiMask=${lumiMask} \
		  -n 100 puTarget=3.53e+03,3.16e+05,1.16e+06,2.05e+06,2.89e+06,3.93e+06,5.12e+06,9.83e+06,3.11e+07,7.43e+07,1.55e+08,2.83e+08,4.48e+08,6.2e+08,8.04e+08,1.01e+09,1.19e+09,1.31e+09,1.38e+09,1.41e+09,1.41e+09,1.39e+09,1.34e+09,1.28e+09,1.2e+09,1.1e+09,9.87e+08,8.67e+08,7.46e+08,6.3e+08,5.2e+08,4.19e+08,3.28e+08,2.49e+08,1.83e+08,1.31e+08,9.05e+07,6.07e+07,3.94e+07,2.47e+07,1.49e+07,8.62e+06,4.79e+06,2.55e+06,1.31e+06,6.4e+05,3.02e+05,1.39e+05,6.26e+04,2.91e+04
done 

#puTarget=6.87,6.3e+03,2.79e+04,4.2e+04,7.25e+04,1.22e+05,1.46e+05,3.3e+05,8.76e+05,2.47e+06,6.24e+06,1.24e+07,2e+07,2.9e+07,3.88e+07,4.56e+07,4.74e+07,4.23e+07,3.17e+07,2.07e+07,1.3e+07,8.45e+06,5.67e+06,3.6e+06,2.03e+06,9.96e+05,4.24e+05,1.59e+05,5.65e+04,2.31e+04,1.37e+04,1.12e+04,1.01e+04,9.27e+03,8.45e+03,7.71e+03,7.08e+03,6.6e+03,6.25e+03,6.01e+03,5.85e+03,5.73e+03,5.61e+03,5.49e+03,5.34e+03,5.15e+03,4.94e+03,4.69e+03,4.41e+03,4.12e+03


#1.34e+05,6.34e+05,8.42e+05,1.23e+06,2.01e+06,4.24e+06,1.26e+07,4.88e+07,1.56e+08,3.07e+08,4.17e+08,4.48e+08,4.04e+08,3.05e+08,1.89e+08,9.64e+07,4.19e+07,1.71e+07,7.85e+06,4.2e+06,2.18e+06,9.43e+05,3.22e+05,8.9e+04,2.16e+04,5.43e+03,1.6e+03,551,206,80.1,31.2,11.9,4.38,1.54,0.518,0.165,0.0501,0.0144,0.00394,0.00102,0.000251,5.87e-05,1.3e-05,2.74e-06,5.47e-07,1.04e-07,1.86e-08,3.18e-09,5.16e-10,9.35e-11,0,0
