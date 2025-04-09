#!/bin/bash

# Convert first submit delay to seconds (3 hours)
first_submit_hour=$((2 * 60 * 60))  # 3 hours in seconds

# Total duration in seconds (12 days)
total_days=$(( 12 * 60 * 60))   # 10 hours in seconds

# Interval between submissions (1 hours)
interval_seconds=$((1 * 60 * 60))   # 60 minutes in seconds

# Get the current timestamp
start_time=$(date +%s)
end_time=$((start_time + total_days))
'''
# Initial delay before first submit
echo "Sleeping for initial delay of $first_submit_hour seconds..."
sleep $first_submit_hour

# First submission
echo "Submitting job at $(date)"
crab submit -c crabConfig_nanoAODSIM.py
'''
# Loop until total time elapses
while [ $(date +%s) -lt $end_time ]
do
    echo "Running resubmit tasks at $(date)"
    echo "Sleeping for $interval_seconds seconds..."
    sleep $interval_seconds
    # Task 1
    crab resubmit -d crab_VBFH/crab_NANOAODSIM_VBFH_HToAATo4Tau_M3p7

    # sleep 2
    # # Task 2
    # crab resubmit -d crab_VBFH/crab_NANOAODSIM_VBFH_HToAATo4Tau_M14
    # sleep 2


done

echo "Task completed after $(($total_days / 3600)) hours."
#### nohup ./submit_later.sh > submit.log 2>&1 &
