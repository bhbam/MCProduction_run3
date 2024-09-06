### For run 3 S log to el8 machine--------------------------------------------------------------------------------
export SCRAM_ARCH=el8_amd64_gcc11
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_13_0_13 # Create CMS release
cd CMSSW_13_0_13/src
eval `scram runtime -sh`  # To evaluate
cmsenv
git cms-init
git cms-addpkg Configuration/Generator

### To add filters for run3 just clone run3 branch only-----------------------------------------------------------
git clone -b run3-generator-interface git@github.com:bhbam/GeneratorInterface.git

### For signal production ----------------------------------------------------------------------------------------
cd E2E-HToAATo4Tau

# Step 1: Generate signal sample of mass 'X' in [3.7,14]. Please check the value of mass set in  script properly
cmsRun GEN_SIM_HToAATo4Tau_M<X>_cfg.py  
# Step 2: Add HLT Trigger and Pielup . Use output file from Step 1 as Input file in step 2 (here)
cmsRun HLT_Pielup_HToAATo4Tau_cfg.py
# Step 3: Convert to AODSIM. Use output file from Step 2 as Input file in step 3 (here)
cmsRun AOD_HToAATo4Tau_cfg.py   
# Step 4: Convert AOD to MiniAOD. Use output file from Step 3 as Input file in step 4 (here)       
cmsRun MiniAOD_HToAATo4Tau_cfg.py  
# Step 5: Convert MiniAOD to NanoAOD. Use output file from Step 4 as Input file in step 5 (here)
cmsRun NanoAOD_HToAATo4Tau_cfg.py
###---------------------------------------------------------------------------------------------------------------
