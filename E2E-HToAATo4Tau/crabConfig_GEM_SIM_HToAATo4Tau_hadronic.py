from CRABClient.UserUtilities import config
config = config()
# See parameter defintions here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters
Mass='14'# Mass of A is generally integer but put as string if need decimal.
# Local job directory will be created in:
inputPSet_ ={
'3p7':'VBFH_HToAA4Tau_GEN_SIM_M3p7_cfg.py'
# ,'4':'GEN_SIM_HToAATo4Tau_M4_cfg.py'
# ,'5':'GEN_SIM_HToAATo4Tau_M5_cfg.py'
# ,'6':'GEN_SIM_HToAATo4Tau_M6_cfg.py'
# ,'8':'GEN_SIM_HToAATo4Tau_M8_cfg.py'
# ,'10':'GEN_SIM_HToAATo4Tau_M10_cfg.py'
# ,'12':'GEN_SIM_HToAATo4Tau_M12_cfg.py'
,'14':'VBFH_HToAA4Tau_GEN_SIM_M14_cfg.py'
}.get(Mass, None)


config.General.requestName = 'VBFH_HToAATo4Tau_GEN_SIM_M%s'%Mass
config.General.workArea = 'crab_VBFH'
config.General.transferOutputs = True
config.General.transferLogs = True

# CMS cfg file goes here:
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = inputPSet_
config.Data.outputPrimaryDataset = 'VBFH_HToAATo4Tau_GEN_SIM_M%s'%Mass

#config.JobType.maxMemoryMB = 2800
config.JobType.maxMemoryMB = 5000
# config.JobType.numCores = 4

# Define units per job here:
config.JobType.allowUndistributedCMSSW = True
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 5000 # units: large number is given because HToaaTo4Tau has filters about 60% eff
NJOBS = 20
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.whitelist = ['T3_US_FNALLPC', 'T2_AT_Vienna', 'T2_BE_IIHE', 'T2_BE_UCL', 'T2_BR_SPRACE', 'T2_BR_UERJ', 'T2_CH_CERN', 'T2_CN_Beijing', 'T2_DE_DESY', 'T2_DE_RWTH', 'T2_EE_Estonia', 'T2_ES_CIEMAT', 'T2_ES_IFCA', 'T2_FI_HIP', 'T2_FR_IPHC', 'T2_GR_Ioannina', 'T2_HU_Budapest', 'T2_IN_TIFR', 'T2_IT_Bari', 'T2_IT_Legnaro', 'T2_IT_Pisa', 'T2_IT_Rome', 'T2_KR_KISTI', 'T2_PK_NCP', 'T2_PL_Cyfronet', 'T2_PT_NCG_Lisbon', 'T2_RU_IHEP', 'T2_TR_METU', 'T2_TW_NCHC', 'T2_UA_KIPT', 'T2_UK_London_Brunel', 'T2_UK_London_IC', 'T2_UK_SGrid_Bristol', 'T2_UK_SGrid_RALPP', 'T2_US_Caltech', 'T2_US_Florida', 'T2_US_MIT', 'T2_US_Nebraska', 'T2_US_Purdue', 'T2_US_UCSD', 'T2_US_Vanderbilt', 'T2_US_Wisconsin' ]
# Output files will be stored in config.Site.storageSite at directory:

config.Data.outLFNDirBase = '/store/group/lpcml/bbbam/MCGeneration_run3/VBF_signals'
config.Site.storageSite = 'T3_US_FNALLPC'
#config.Data.outLFNDirBase = '/store/group/phys_diffraction/rchudasa/MCGeneration'
#config.Site.storageSite = 'T2_CH_CERN'
