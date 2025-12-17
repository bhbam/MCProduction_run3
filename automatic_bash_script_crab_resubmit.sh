#!/bin/bash

# Total duration in minutes (24 hours = 24 * 60)
total_minutes=$((24 * 60))
# total_minutes=60

# Interval in minutes (e.g., every 60 minutes = 1 hour)
interval_minutes=$((1 * 60))
# interval_minutes=2

# Convert to seconds
total_seconds=$((total_minutes * 60))
interval_seconds=$((interval_minutes * 60))

# Get the current timestamp
start_time=$(date +%s)
end_time=$((start_time + total_seconds))

# Define the sample list
sample_list=('14' 'DY2L' 'TTbar' 'QCD' 'WLNu' 'HTauTau')

# Main loop
while [ $(date +%s) -lt $end_time ]; do
    echo "Running tasks at $(date)"

    for sample in "${sample_list[@]}"; do
        echo "Resubmitting for sample: $sample"
        crab resubmit -d crab_projects_June7_RAWAOD-RecHits/crab_"$sample"_miniAODSIM_RAWAOD-RecHits
        sleep 2
    done

    echo "Sleeping for $interval_minutes minutes..."
    sleep $interval_seconds
done

echo "Task completed after $total_minutes minutes."
