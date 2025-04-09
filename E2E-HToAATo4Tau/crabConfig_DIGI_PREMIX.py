from CRABClient.UserUtilities import config
config = config()


Mass = '14'#14


inputProcess_ = {
'3p7': "/VBFH_HToAATo4Tau_GEN_SIM_M3p7/lpcml-crab_VBFH_HToAATo4Tau_GEN_SIM_M3p7-8896b106d14ae2a51abc053e46116753/USER"
# ,'4': "/HToAATo4Tau_hadronic_tauDecay_M4_Run3_2023/lpcml-crab_GEN_SIM_HToAATo4Tau_tauDecay_M4-65fda359da575d58201444a7a8375d6b/USER"
# ,'5': "/HToAATo4Tau_hadronic_tauDecay_M5_Run3_2023/lpcml-crab_GEN_SIM_HToAATo4Tau_tauDecay_M5-eb1606952c4e09f97648e0927768ea7f/USER"
# ,'6': "/HToAATo4Tau_hadronic_tauDecay_M6_Run3_2023/lpcml-crab_GEN_SIM_HToAATo4Tau_tauDecay_M6-8c4e993c2f7de8c3cb712019877abf5a/USER"
# ,'8': "/HToAATo4Tau_hadronic_tauDecay_M8_Run3_2023/lpcml-crab_GEN_SIM_HToAATo4Tau_tauDecay_M8-9f22b64db8f402465d5692c03dca94de/USER"
# ,'10': "/HToAATo4Tau_hadronic_tauDecay_M10_Run3_2023/lpcml-crab_GEN_SIM_HToAATo4Tau_tauDecay_M10-a0ac0cabdcc7bcdf8c5d0dc549c90a3a/USER"
# ,'12': "/HToAATo4Tau_hadronic_tauDecay_M12_Run3_2023/lpcml-crab_GEN_SIM_HToAATo4Tau_tauDecay_M12-b2b081357876569531c4037b31596938/USER"
,'14': "/VBFH_HToAATo4Tau_GEN_SIM_M14/lpcml-crab_VBFH_HToAATo4Tau_GEN_SIM_M14-f0685d2f07281f8fdad190e33185ca4a/USER"
}.get(Mass, None)

#config.section_('General')
config.General.requestName = 'VBFH_HToAATo4Tau_DIGI_Premix_%s'%Mass
config.General.workArea = 'crab_VBFH'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_DIGI-RAW-HLT_pileupFileList_cfg.py'
config.JobType.maxMemoryMB = 10000
config.JobType.numCores = 4


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
config.Data.outLFNDirBase = '/store/group/lpcml/bbbam/MCGeneration_run3/VBF_signals'
config.Site.storageSite = 'T3_US_FNALLPC'
config.Data.publication = True
config.Data.outputDatasetTag = config.General.requestName
