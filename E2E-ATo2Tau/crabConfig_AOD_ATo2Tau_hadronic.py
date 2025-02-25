from CRABClient.UserUtilities import config#, getUsernameFromSiteDB
config = config()
# See parameter defintions here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters
# To submit to crab:
# crab submit -c crabConfig_data.py
# To check job status:
# crab status -d <config.General.workArea>/<config.General.requestName>
# To resubmit jobs:
# crab resubmit -d <config.General.workArea>/<config.General.requestName>
Mass_tag = 'm1p8To3p6' #
# Local job directory will be created in:
# <config.General.workArea>/<config.General.requestName>
config.General.workArea        = 'crab_MC'
config.General.requestName     = 'AOD_Tau_hadronic_%s_v2'%Mass_tag
config.General.transferOutputs = True
config.General.transferLogs    = True

# CMS cfg file goes here:
config.JobType.pluginName  = 'Analysis' # mass > 8 use this
config.JobType.psetName    = 'AOD_HToAATo4Tau_extra_collection_cfg.py' # cms cfg file for generating events
config.JobType.maxMemoryMB = 10000 #16000
config.JobType.numCores = 4


config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True
# Define input and units per job here:
dataset  = {
'm3p6To18':'/GEN_SIM_ATo2Tau_m3p6To18_pt30To300_v2/lpcml-HLT_Pielup_ATo4Tau_Hadronic_m3p6To18-8a4c70c5aaaf26ad44e675df103c838b/USER'
,'m1p2To3p6':'/GEN_SIM_ATo2Tau_m1p2To3p6_pt30To300_v4/lpcml-HLT_Pielup_ATo4Tau_Hadronic_m1p2To3p6-8a4c70c5aaaf26ad44e675df103c838b/USER'
,'m1p8To3p6':'/GEN_SIM_Tau_hadronic_m1p8To3p6_pt30To300_v2/lpcml-HLT_Pielup_Tau_hadronic_m1p8To3p6_v2-26240d1e6039ee29161351aa2c33106e/USER'
}.get(Mass_tag, None)


config.Data.inputDataset = dataset
config.Data.splitting      = 'FileBased'
config.Data.unitsPerJob    = 1  # units: as defined by config.Data.splitting
config.Data.totalUnits     = -1 # -1: all inputs. total jobs submitted = totalUnits / unitsPerJob. cap of 10k jobs per submission
config.Data.publication    = True



config.Data.ignoreLocality = True
config.Site.whitelist = ['T3_US_FNALLPC', 'T2_AT_Vienna', 'T2_BE_IIHE', 'T2_BE_UCL', 'T2_BR_SPRACE', 'T2_BR_UERJ', 'T2_CH_CERN', 'T2_CN_Beijing', 'T2_DE_DESY', 'T2_DE_RWTH', 'T2_EE_Estonia', 'T2_ES_CIEMAT', 'T2_ES_IFCA', 'T2_FI_HIP', 'T2_FR_IPHC', 'T2_GR_Ioannina', 'T2_HU_Budapest', 'T2_IN_TIFR', 'T2_IT_Bari', 'T2_IT_Legnaro', 'T2_IT_Pisa', 'T2_IT_Rome', 'T2_KR_KISTI', 'T2_PK_NCP', 'T2_PL_Cyfronet', 'T2_PT_NCG_Lisbon', 'T2_RU_IHEP', 'T2_TR_METU', 'T2_TW_NCHC', 'T2_UA_KIPT', 'T2_UK_London_Brunel', 'T2_UK_London_IC', 'T2_UK_SGrid_Bristol', 'T2_UK_SGrid_RALPP', 'T2_US_Caltech', 'T2_US_Florida', 'T2_US_MIT', 'T2_US_Nebraska', 'T2_US_Purdue', 'T2_US_UCSD', 'T2_US_Vanderbilt', 'T2_US_Wisconsin' ]
# Output files will be stored in config.Site.storageSite at directory:
# <config.Data.outLFNDirBase>/<config.Data.outputPrimaryDataset>/<config.Data.outputDatasetTag>/
config.Data.outLFNDirBase = '/store/group/lpcml/bbbam/MCGeneration_run3'
# config.Data.outLFNDirBase = '/store/user/bhbam/MCGeneration'

config.Site.storageSite = 'T3_US_FNALLPC'
config.Data.outputDatasetTag = config.General.requestName
