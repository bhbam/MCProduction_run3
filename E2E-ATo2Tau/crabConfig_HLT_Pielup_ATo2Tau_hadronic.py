from CRABClient.UserUtilities import config#, getUsernameFromSiteDB
config = config()
# See parameter defintions here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters
# To submit to crab:
# crab submit -c crabConfig_data.py
# To check job status:
# crab status -d <config.General.workArea>/<config.General.requestName>
# To resubmit jobs:
# crab resubmit -d <config.General.workArea>/<config.General.requestName>
Mass_tag = 'ATo2Tau_mass14'#'m1p8To3p6'#'m3p6To18' #
# Local job directory will be created in:
# <config.General.workArea>/<config.General.requestName>
config.General.workArea        = 'crab_MC_ATo2Tau_validation'
config.General.requestName     = 'HLT_Pielup_%s_validation'%Mass_tag
config.General.transferOutputs = True
config.General.transferLogs    = True

# CMS cfg file goes here:
config.JobType.pluginName  = 'Analysis' # mass > 8 use this
config.JobType.psetName    = 'HLT_Pielup_with_pileupFileList_cfg.py' # cms cfg file for generating events
config.JobType.maxMemoryMB = 10000 #16000
config.JobType.numCores = 4


config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True
# Define input and units per job here:
dataset  = {
'm3p6To18':'/GEN_SIM_ATo2Tau_m3p6To18_pt30To300_v2/lpcml-crab_aToTauTau_Hadronic_m3p6To18_pt30To300_pythia8_GEN_SIM_v2-c69efe833fac3615f1b10f8d0416619f/USER'
,'m1p2To3p6':'/GEN_SIM_ATo2Tau_m1p2To3p6_pt30To300_v4/lpcml-crab_aToTauTau_Hadronic_m1p2To3p6_pt30To300_pythia8_GEN_SIM_v4-5aad074e51915d56b4961eb07520b5cb/USER'
,'m1p8To3p6':'/GEN_SIM_Tau_hadronic_m1p8To3p6_pt30To300_v2/lpcml-crab_Tau_hadronic_m1p8To3p6_pt30To300_pythia8_GEN_SIM_v2-d20bf728e40e8dc10734327464b3e73e/USER'
,'ATo2Tau_mass3p7':'/GEN_SIM_ATo2Tau_Mass3p7_GeV_pt30To300_GeV_valid/lpcml-crab_GEN_SIM_ATo2Tau_Mass3p7_GeV_pt30To300_GeV_valid-bdb98a7c09abd572d7b1d4cccf15e587/USER'
,'ATo2Tau_mass8':'/GEN_SIM_ATo2Tau_Mass8_GeV_pt30To300_GeV_valid/lpcml-crab_GEN_SIM_ATo2Tau_Mass8_GeV_pt30To300_GeV_valid-a690c93a687115e46f4d923bf595bb66/USER'
,'ATo2Tau_mass14':'/GEN_SIM_ATo2Tau_Mass14_GeV_pt30To300_GeV_valid/lpcml-crab_GEN_SIM_ATo2Tau_Mass14_GeV_pt30To300_GeV_valid-0fa68b0cf496583de8e27057f4877e6b/USER'
}.get(Mass_tag, None)


# config.Data.userInputFiles = open(f'list_files_GEN_SIM_ATo2Tau_{Mass_tag}_pt30To300.txt').readlines()
# config.Data.outputPrimaryDataset = 'HLT_Pielup_ATo4Tau_Hadronic_%s'%Mass_tag

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
