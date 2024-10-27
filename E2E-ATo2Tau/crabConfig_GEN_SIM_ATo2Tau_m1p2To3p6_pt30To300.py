from CRABClient.UserUtilities import config
config = config()
# See parameter defintions here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters

# Local job directory will be created in:
config.General.requestName = 'aToTauTau_Hadronic_m1p2To3p6_pt30To300_GEN_SIM_noOCC'
config.General.workArea = 'crab_MC'
config.General.transferOutputs = True
config.General.transferLogs = True

# CMS cfg file goes here:
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'GEN_SIM_ATo2Tau_m1p2To3p6_pt30To300_cfg.py'
config.Data.outputPrimaryDataset = 'GEN_SIM_ATo2Tau_m1p2To3p6_pt30To300_noOCC'

#config.JobType.maxMemoryMB = 2800

# Define units per job here:
config.JobType.allowUndistributedCMSSW = True
config.JobType.eventsPerLumi=600
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000 # units: large number is given because aToTauTau has filters and cut on pt and eta
NJOBS = 1000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True

# Output files will be stored in config.Site.storageSite at directory:
config.Data.outLFNDirBase = '/store/user/bhbam/MCGeneration_run3'
config.Site.storageSite = 'T3_US_FNALLPC'
