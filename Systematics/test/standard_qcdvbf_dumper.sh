#!/usr/bin/bash

#rms_cut=(0.01 0.02 0.03 0.04 0.05 1.00)(0.03 0.02 0.04)(0.03 0.02 0.04)

run_on_zee=true
rms_cut=(0.03)
today=$(date +%F)
label="tight_JetID"

for i in ${rms_cut[@]};do
    echo " #######################################"
    echo " # --> rmsCut :: $i label :: ${label}  #"
    echo " # running on zee sample               #"
    echo " #######################################"
    fggRunJobs.py --load training_QCD.json -d /vols/cms04/yhaddad/training-${today}-76x_${label}_rms_${i}_QCD \
		      -x cmsRun standard_vbf_dumper_cfg.py maxEvents=-1 \
		      -q hepshort.q --no-use-tarball useAAA=1 targetLumi=1.00e+3 forwardJetRMSCut=$i runOnZee=false \
		      -n 800 puTarget=1.34e+05,6.34e+05,8.42e+05,1.23e+06,2.01e+06,4.24e+06,1.26e+07,4.88e+07,1.56e+08,3.07e+08,4.17e+08,4.48e+08,4.04e+08,3.05e+08,1.89e+08,9.64e+07,4.19e+07,1.71e+07,7.85e+06,4.2e+06,2.18e+06,9.43e+05,3.22e+05,8.9e+04,2.16e+04,5.43e+03,1.6e+03,551,206,80.1,31.2,11.9,4.38,1.54,0.518,0.165,0.0501,0.0144,0.00394,0.00102,0.000251,5.87e-05,1.3e-05,2.74e-06,5.47e-07,1.04e-07,1.86e-08,3.18e-09,5.16e-10,9.35e-11
done 
