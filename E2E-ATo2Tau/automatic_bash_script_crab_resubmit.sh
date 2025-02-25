#!/bin/bash

# Total duration in days
total_days=12*60*60
# Interval in hours
interval_hours=2*60*60
# Convert days to seconds
let total_seconds=total_days
# Convert interval to seconds
let interval_seconds=interval_hours

# Get the current timestamp
start_time=$(date +%s)
end_time=$((start_time + total_seconds))

while [ $(date +%s) -lt $end_time ]
do
    echo "Running task at $(date)"
    # Place your task or command here
    # Task 1
    crab resubmit -d crab_MC_un/crab_HLT_Pielup_Tau_hadronic_m1p8To3p6_v2
    # sleep 2
    # Task 2
    # crab status -d crab_projects/crab_signal_Mass_10_AODSIM_multiThreads
    # sleep 2
    # # Task 3
    # crab status -d crab_projects/crab_signal_Mass_12_AODSIM_multiThreads
    # sleep 2
    # # Task 4
    # crab status -d crab_projects/crab_signal_Mass_14_AODSIM_multiThreads

    # Sleep for the interval duration
    sleep $interval_seconds
done

echo "Task completed after $total_days hours."
#nohup ./automatic_bash_script_crab_resubmit.sh > HLT.log 2>&1 &
