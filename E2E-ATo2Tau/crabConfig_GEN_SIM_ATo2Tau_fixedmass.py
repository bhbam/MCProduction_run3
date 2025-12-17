from CRABClient.UserUtilities import config
config = config()
# See parameter defintions here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters
# Local job directory will be created in:
Mass ='3p7'
config.General.requestName = 'GEN_SIM_ATo2Tau_Mass%s_GeV_pt30To300_GeV_valid'%Mass
config.General.workArea = 'crab_MC_ATo2Tau_validation'
config.General.transferOutputs = True
config.General.transferLogs = True

# CMS cfg file goes here:
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'GEN_SIM_ATo2Tau_mass%s_pt30To300_cfg.py'%Mass
config.Data.outputPrimaryDataset = 'GEN_SIM_ATo2Tau_Mass%s_GeV_pt30To300_GeV_valid'%Mass

#config.JobType.maxMemoryMB = 2800
# config.JobType.maxMemoryMB = 10000
# config.JobType.numCores = 4

# Define units per job here:
config.JobType.allowUndistributedCMSSW = True
config.JobType.eventsPerLumi=500
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
NJOBS = 100
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True

config.Data.ignoreLocality = True
config.Site.whitelist = ['T3_US_FNALLPC', 'T2_AT_Vienna', 'T2_BE_IIHE', 'T2_BE_UCL', 'T2_BR_SPRACE', 'T2_BR_UERJ', 'T2_CH_CERN', 'T2_CN_Beijing', 'T2_DE_DESY', 'T2_DE_RWTH', 'T2_EE_Estonia', 'T2_ES_CIEMAT', 'T2_ES_IFCA', 'T2_FI_HIP', 'T2_FR_IPHC', 'T2_GR_Ioannina', 'T2_HU_Budapest', 'T2_IN_TIFR', 'T2_IT_Bari', 'T2_IT_Legnaro', 'T2_IT_Pisa', 'T2_IT_Rome', 'T2_KR_KISTI', 'T2_PK_NCP', 'T2_PL_Cyfronet', 'T2_PT_NCG_Lisbon', 'T2_RU_IHEP', 'T2_TR_METU', 'T2_TW_NCHC', 'T2_UA_KIPT', 'T2_UK_London_Brunel', 'T2_UK_London_IC', 'T2_UK_SGrid_Bristol', 'T2_UK_SGrid_RALPP', 'T2_US_Caltech', 'T2_US_Florida', 'T2_US_MIT', 'T2_US_Nebraska', 'T2_US_Purdue', 'T2_US_UCSD', 'T2_US_Vanderbilt', 'T2_US_Wisconsin' ]
# Output files will be stored in config.Site.storageSite at directory:
# config.Data.outLFNDirBase = '/store/user/bhbam/MCGeneration_run3'
config.Data.outLFNDirBase = '/store/group/lpcml/bbbam/MCGeneration_run3'
config.Site.storageSite = 'T3_US_FNALLPC'
