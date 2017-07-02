#!/bin/bash

today=`date +%F`
outdir=/vols/cms/yhaddad/HggPaper2017/mc-driven-trees-${today}
mask=/home/hep/szenz/fromscratch26/CMSSW_8_0_8_patch1/src/flashgg/MetaData/work/jsons/Cert_271036-274421_13TeV_PromptReco_Collisions16_JSON.txt
mkdir -p ${outdir}


fggRunJobs.py --load samples_additional_mc.json -d ${outdir} \
	      -x cmsRun moriond_vbf_dumper_cfg.py maxEvents=-1 runOnZee=False -q hepshort.q \
	      --no-use-tarball useAAA=0 targetLumi=1.00e+3 pujidWP=tight -n 200 --hadd-process \
	      lumiMask=${mask} puTarget=2.39e+05,8.38e+05,2.31e+06,3.12e+06,4.48e+06,6e+06,7e+06,1.29e+07,3.53e+07,7.87e+07,1.77e+08,3.6e+08,6.03e+08,8.77e+08,1.17e+09,1.49e+09,1.76e+09,1.94e+09,2.05e+09,2.1e+09,2.13e+09,2.15e+09,2.13e+09,2.06e+09,1.96e+09,1.84e+09,1.7e+09,1.55e+09,1.4e+09,1.24e+09,1.09e+09,9.37e+08,7.92e+08,6.57e+08,5.34e+08,4.27e+08,3.35e+08,2.58e+08,1.94e+08,1.42e+08,1.01e+08,6.9e+07,4.55e+07,2.88e+07,1.75e+07,1.02e+07,5.64e+06,2.99e+06,1.51e+06,7.32e+05,3.4e+05,1.53e+05,6.74e+04,3.05e+04,1.52e+04,8.98e+03,6.5e+03,5.43e+03,4.89e+03,4.52e+03,4.21e+03,3.91e+03,3.61e+03,3.32e+03,3.03e+03,2.75e+03,2.47e+03,2.21e+03,1.97e+03,1.74e+03,1.52e+03,1.32e+03,1.14e+03,983,839


#puTarget=6.87,6.3e+03,2.79e+04,4.2e+04,7.25e+04,1.22e+05,1.46e+05,3.3e+05,8.76e+05,2.47e+06,6.24e+06,1.24e+07,2e+07,2.9e+07,3.88e+07,4.56e+07,4.74e+07,4.23e+07,3.17e+07,2.07e+07,1.3e+07,8.45e+06,5.67e+06,3.6e+06,2.03e+06,9.96e+05,4.24e+05,1.59e+05,5.65e+04,2.31e+04,1.37e+04,1.12e+04,1.01e+04,9.27e+03,8.45e+03,7.71e+03,7.08e+03,6.6e+03,6.25e+03,6.01e+03,5.85e+03,5.73e+03,5.61e+03,5.49e+03,5.34e+03,5.15e+03,4.94e+03,4.69e+03,4.41e+03,4.12e+03


#1.34e+05,6.34e+05,8.42e+05,1.23e+06,2.01e+06,4.24e+06,1.26e+07,4.88e+07,1.56e+08,3.07e+08,4.17e+08,4.48e+08,4.04e+08,3.05e+08,1.89e+08,9.64e+07,4.19e+07,1.71e+07,7.85e+06,4.2e+06,2.18e+06,9.43e+05,3.22e+05,8.9e+04,2.16e+04,5.43e+03,1.6e+03,551,206,80.1,31.2,11.9,4.38,1.54,0.518,0.165,0.0501,0.0144,0.00394,0.00102,0.000251,5.87e-05,1.3e-05,2.74e-06,5.47e-07,1.04e-07,1.86e-08,3.18e-09,5.16e-10,9.35e-11,0,0
