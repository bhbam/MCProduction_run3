from CRABClient.UserUtilities import config#, getUsernameFromSiteDB
config = config()
# See parameter defintions here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters
# To submit to crab:
# crab submit -c crabConfig_data.py
# To check job status:
# crab status -d <config.General.workArea>/<config.General.requestName>
# To resubmit jobs:
# crab resubmit -d <config.General.workArea>/<config.General.requestName>
# Local job directory will be created in:
# <config.General.workArea>/<config.General.requestName>
config.General.workArea        = 'crab_MC'
config.General.requestName     = 'AOD_QCD_pt15to7000_Run3Summer23GS'
config.General.transferOutputs = True
config.General.transferLogs    = True


# CMS cfg file goes here:
config.JobType.pluginName  = 'Analysis' # mass > 8 use this
config.JobType.psetName    = 'AOD_QCD_pt15to7000_Run3Summer23DRPremix_00001_2_cfg.py' # cms cfg file for generating events
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 4

config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True
# Define input and units per job here:
dataset  = "/GEN_SIM_QCD_pt15to7000_Run3Summer23GS/lpcml-HLT_Pielup_QCD_pt15to7000_Run3Summer23GS-26240d1e6039ee29161351aa2c33106e/USER"



# config.Data.userInputFiles = open(f'list_files_GEN_SIM_ATo2Tau_{Mass_tag}_pt30To300.txt').readlines()
# config.Data.outputPrimaryDataset = 'HLT_Pielup_ATo4Tau_Hadronic_%s'%Mass_tag

config.Data.inputDataset = dataset
config.Data.splitting      = 'FileBased'
config.Data.unitsPerJob    = 1  # units: as defined by config.Data.splitting
config.Data.totalUnits     = -1 # -1: all inputs. total jobs submitted = totalUnits / unitsPerJob. cap of 10k jobs per submission
config.Data.publication    = True



# Output files will be stored in config.Site.storageSite at directory:
# <config.Data.outLFNDirBase>/<config.Data.outputPrimaryDataset>/<config.Data.outputDatasetTag>/
config.Data.outLFNDirBase = '/store/group/lpcml/bbbam/MCGeneration_run3'
# config.Data.outLFNDirBase = '/store/user/bhbam/MCGeneration'

config.Site.storageSite = 'T3_US_FNALLPC'
config.Data.outputDatasetTag = config.General.requestName
