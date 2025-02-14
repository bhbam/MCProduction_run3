#!/bin/bash

. ./submit_env.sh && save_env && setup_local_env
#
export _CONDOR_JOB_AD=Job.${1}.submit
# leading '+' signs must be removed to use JDL as classAd file
sed -e 's/^+//' Job.submit > Job.${1}.submit

./CMSRunAnalysis.sh --json JobArgs-${1}.json
