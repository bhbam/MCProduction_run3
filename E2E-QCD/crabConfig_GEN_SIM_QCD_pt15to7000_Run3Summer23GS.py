from CRABClient.UserUtilities import config
config = config()
# See parameter defintions here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters

# Local job directory will be created in:
config.General.requestName = 'GEN_SIM_QCD_pt15to7000_Run3Summer23GS'
config.General.workArea = 'crab_MC'
config.General.transferOutputs = True
config.General.transferLogs = True

# CMS cfg file goes here:
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'GEN_SIM_QCD_pt15to7000_Run3Summer23GS_00004_1_cfg.py'
config.Data.outputPrimaryDataset = 'GEN_SIM_QCD_pt15to7000_Run3Summer23GS'

config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 4
# Define units per job here:
config.JobType.allowUndistributedCMSSW = True
config.JobType.eventsPerLumi=600
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 2000 # units: large number is given because aToTauTau has filters and cut on pt and eta
NJOBS = 100
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True

# Output files will be stored in config.Site.storageSite at directory:
# config.Data.outLFNDirBase = '/store/user/bhbam/MCGeneration_run3'
config.Data.outLFNDirBase = '/store/group/lpcml/bbbam/MCGeneration_run3'
config.Site.storageSite = 'T3_US_FNALLPC'
