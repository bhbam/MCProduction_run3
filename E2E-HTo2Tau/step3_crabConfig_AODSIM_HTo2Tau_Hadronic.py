from CRABClient.UserUtilities import config
config = config()

inputProcess_ ="/HTo2Tau_hadronic_GEN_SIM/lpcml-HTo2Tau_hadronic_HLT_Primix-26240d1e6039ee29161351aa2c33106e/USER"

#config.section_('General')
config.General.requestName = 'HTo2Tau_hadronic_AOD'
config.General.workArea = 'crab_HTo2Tau'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_AODSIM_cfg.py'
config.JobType.maxMemoryMB = 3000
# config.JobType.maxMemoryMB = 10000
# config.JobType.numCores = 4


config.Data.inputDBS = 'phys03'
# config.Data.inputDBS = 'global'
config.JobType.allowUndistributedCMSSW = True
config.Data.inputDataset = inputProcess_

#config.Data.userInputFiles = open('%s'%inputProcess_).readlines()
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
#config.Data.outputPrimaryDataset = 'WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8'


config.Data.ignoreLocality = True

config.Site.whitelist = ['T3_US_FNALLPC', 'T2_AT_Vienna', 'T2_BE_IIHE', 'T2_BE_UCL', 'T2_BR_SPRACE', 'T2_BR_UERJ', 'T2_CH_CERN', 'T2_CN_Beijing', 'T2_DE_DESY', 'T2_DE_RWTH', 'T2_EE_Estonia', 'T2_ES_CIEMAT', 'T2_ES_IFCA', 'T2_FI_HIP', 'T2_FR_IPHC', 'T2_GR_Ioannina', 'T2_HU_Budapest', 'T2_IN_TIFR', 'T2_IT_Bari', 'T2_IT_Legnaro', 'T2_IT_Pisa', 'T2_IT_Rome', 'T2_KR_KISTI', 'T2_PK_NCP', 'T2_PL_Cyfronet', 'T2_PT_NCG_Lisbon', 'T2_RU_IHEP', 'T2_TR_METU', 'T2_TW_NCHC', 'T2_UA_KIPT', 'T2_UK_London_Brunel', 'T2_UK_London_IC', 'T2_UK_SGrid_Bristol', 'T2_UK_SGrid_RALPP', 'T2_US_Caltech', 'T2_US_Florida', 'T2_US_MIT', 'T2_US_Nebraska', 'T2_US_Purdue', 'T2_US_UCSD', 'T2_US_Vanderbilt', 'T2_US_Wisconsin' ]
# Output files will be stored in config.Site.storageSite at directory:
config.Data.outLFNDirBase = '/store/group/lpcml/bbbam/MCGeneration_run3/HTo2Tau_hadronic'
config.Site.storageSite = 'T3_US_FNALLPC'
config.Data.publication = True
config.Data.outputDatasetTag = config.General.requestName
