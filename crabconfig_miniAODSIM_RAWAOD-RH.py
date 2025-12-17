from CRABClient.UserUtilities import config
from CRABAPI.RawCommand import crabCommand
config = config()


sample_list = ['14','DY2L','TTbar','QCD','WLNu','HTauTau']
Mass = sample_list[5]
inputProcess_ = {
    '14': "/HToAATo4Tau_hadronic_tauDecay_M14_Run3_2023/lpcml-signal_Mass_14_AODSIM_multiThreads-953b1873547799e513f8a43f2c57e3b2/USER"
    ,'DY2L': "/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/lpcml-DYto2L_AODSIM_multiThreads-953b1873547799e513f8a43f2c57e3b2/USER"
    ,'TTbar': "/TT_TuneCP5_13p6TeV_powheg-pythia8/lpcml-TTbar_AODSIM_v1-953b1873547799e513f8a43f2c57e3b2/USER"
    ,'QCD': "/QCD_PT-15to7000_TuneCP5_13p6TeV_pythia8/lpcml-QCD_AODSIM_v1-953b1873547799e513f8a43f2c57e3b2/USER"
    ,'WLNu': "/WtoLNu_2Jets_TuneCP5_13p6TeV_amcatnloFXFX_pythia8_v1/lpcml-WJets_AODSIM_v1-953b1873547799e513f8a43f2c57e3b2/USER"
    ,'HTauTau': "/GluGluHToTauTau_M-125_TuneCP5_13p6TeV_powheg-pythia8/lpcml-HTauTau_AODSIM_multiThreads-953b1873547799e513f8a43f2c57e3b2/USER"

}.get(Mass,None)

#config.section_('General')
config.General.requestName = '%s_miniAODSIM_RAWAOD-RecHits'%Mass
config.General.workArea = 'crab_projects_June7_RAWAOD-RecHits'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step4_miniAOD_with_RAWAOD_RecHit_cfg.py'
config.JobType.maxMemoryMB = 10000

config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True
config.Data.inputDataset = inputProcess_
#config.Data.userInputFiles = open('H2AA4Tau_hadronic_tauDecay_M14_AOD.txt').readlines()

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
#config.Data.totalUnits = 10
config.JobType.numCores = 4
#config.Data.outputPrimaryDataset = 'HToAATo4Tau_hadronic_tauDecay_M14_Run3_2023'
config.Data.ignoreLocality = True

config.Site.whitelist = [
    'T3_US_FNALLPC','T2_AT_Vienna', 'T2_BE_IIHE', 'T2_BE_UCL', 'T2_BR_SPRACE', 'T2_BR_UERJ',
    'T2_CH_CERN', 'T2_CN_Beijing', 'T2_DE_DESY', 'T2_DE_RWTH',
    'T2_EE_Estonia', 'T2_ES_CIEMAT', 'T2_ES_IFCA', 'T2_FI_HIP',
    'T2_FR_IPHC', 'T2_GR_Ioannina', 'T2_HU_Budapest', 'T2_IN_TIFR',
    'T2_IT_Bari', 'T2_IT_Legnaro', 'T2_IT_Pisa', 'T2_IT_Rome',
    'T2_KR_KISTI', 'T2_PK_NCP', 'T2_PL_Cyfronet',
    'T2_PT_NCG_Lisbon', 'T2_RU_IHEP',
    'T2_TR_METU', 'T2_TW_NCHC', 'T2_UA_KIPT',
    'T2_UK_London_Brunel', 'T2_UK_London_IC', 'T2_UK_SGrid_Bristol',
    'T2_UK_SGrid_RALPP', 'T2_US_Caltech', 'T2_US_Florida',
    'T2_US_MIT', 'T2_US_Nebraska', 'T2_US_Purdue', 'T2_US_UCSD',
    'T2_US_Vanderbilt', 'T2_US_Wisconsin'
]



config.Data.outLFNDirBase = '/store/group/lpcml/rchudasa/MCGenerationRun3'
config.Site.storageSite = 'T3_US_FNALLPC'
config.Data.publication = True
config.Data.outputDatasetTag = config.General.requestName
