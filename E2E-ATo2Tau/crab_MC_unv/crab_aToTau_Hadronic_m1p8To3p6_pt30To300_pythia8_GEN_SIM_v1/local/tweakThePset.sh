#/bin/bash


#
cmd="edm_pset_tweak.py --input_pkl PSet.pkl --output_pkl PSet.pkl-tweaked --json PSetTweak.json --create_untracked_psets"
echo "will execute: "$cmd
$cmd
ec=$?
if ! [ $ec ]; then
  echo "command failed with exit code $ec . Leave PSet unchanged"
else
  mv PSet.pkl-tweaked PSet.pkl
fi

#
cmd="cmssw_handle_random_seeds.py --input_pkl PSet.pkl --output_pkl PSet.pkl-seeds --seeding dummy"
echo "will execute: "$cmd
$cmd
ec=$?
if ! [ $ec ]; then
  echo "command failed with exit code $ec . Leave PSet unchanged"
else
  mv PSet.pkl-seeds PSet.pkl
fi

#
cmd="cmssw_handle_nEvents.py --input_pkl PSet.pkl --output_pkl PSet.pkl-nEvents"
echo "will execute: "$cmd
$cmd
ec=$?
if ! [ $ec ]; then
  echo "command failed with exit code $ec . Leave PSet unchanged"
else
  mv PSet.pkl-nEvents PSet.pkl
fi

