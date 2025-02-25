# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: Configuration/Generator/python/SingleNuE10_cfi.py --python_filename aToTauTau_GEN-SIM_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:aToTauTau_GEN-SIM.root --conditions 130X_mcRun3_2023_realistic_postBPix_v5 --beamspot Realistic25ns13p6TeVEarly2023Collision --step GEN,SIM --geometry DB:Extended --era Run3_2023 --no_exec --mc -n 10
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_2023_cff import Run3_2023

process = cms.Process('SIM',Run3_2023)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13p6TeVEarly2023Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.genTauFilter_unphysical = cms.EDFilter("GenTauFilter_unphysical",
    src       = cms.InputTag("genParticles"), #GenParticles collection as input
    tauPtCut  = cms.double(0.01),              #at least a GenTau with this minimum pT
    tauEtaCut = cms.double(2.4)              #GenTau eta

)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/Generator/python/SingleNuE10_cfi.py nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:Tau_decay_below_m3p6_pt30To300_GEN_SIM.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
if hasattr(process, "XMLFromDBSource"): process.XMLFromDBSource.label="Extended"
if hasattr(process, "DDDetectorESProducerFromDB"): process.DDDetectorESProducerFromDB.label="Extended"
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '130X_mcRun3_2023_realistic_postBPix_v5', '')


process.generator = cms.EDFilter("Pythia8PtGunV3p1",
    PGunParameters = cms.PSet(
        AddAntiParticle = cms.bool(True),
        MaxCTau = cms.double(3.0),
        MaxEta = cms.double(2.4),
        MaxMass = cms.double(3.6),
        MaxPhi = cms.double(3.14159265359),
        MaxPt = cms.double(300.0),
        MinCTau = cms.double(0.0),
        MinEta = cms.double(-2.4),
        MinMass = cms.double(0),
        MinPhi = cms.double(-3.14159265359),
        MinPt = cms.double(30.0),
        ParticleID = cms.vint32(25)
    ),

    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring('processParameters'),
        processParameters = cms.vstring(
            'ProcessLevel:all = off',
            # '25:new = PA PAbar 2 3 0 2.6 0.9 1.79999 3.59999 0.',
            # '25:oneChannel = 1 1.00 101 15 -15', # onMode bRatio meMode product1 product2
            '15:new = PTau PTaubar 2 -3 0 1.77682 0 1.77682 1.77682 8.71100e-02.',# name antiName spinType chargeType colType m0 mWidth mMin mMax tau0
            # Turn off all default tau decays
            '15:onMode = off',

            # Add decay channels from the table
            '15:oneChannel = 1 0.1076825 1521 16 -211',                     # tau- -> nu_tau pi-
            '15:addChannel = 1 0.0069601 1521 16 -321',                     # tau- -> nu_tau K-
            '15:addChannel = 0 0.1772832 1531 16 13 -14',                   # tau- -> nu_tau mu- anti_nu_mu (off)
            '15:addChannel = 0 0.1731072 1531 16 11 -12',                   # tau- -> nu_tau e- anti_nu_e (off)
            '15:addChannel = 1 0.2537447 1532 16 111 -211',                 # tau- -> nu_tau pi0 pi-
            '15:addChannel = 1 0.0015089 1532 16 311 -321',                 # tau- -> nu_tau K0 K-
            '15:addChannel = 1 0.0001511 1532 16 221 -321',                 # tau- -> nu_tau eta K-
            '15:addChannel = 1 0.0083521 1533 16 -211 -311',                # tau- -> nu_tau  pi- K0bar
            '15:addChannel = 1 0.0042655 1533 16 111  -321',                # tau- -> nu_tau pi0 K-
            '15:addChannel = 1 0.0924697 1541 16 111 111 -211',             # tau- -> nu_tau pi0 pi0 pi-
            '15:addChannel = 1 0.0925691 1541 16 -211 -211 211',            # tau- -> nu_tau pi- pi- pi+
            '15:addChannel = 1 0.0039772 1542 16 111 -211 -311',            # tau- -> nu_tau pi0 pi- K0bar
            '15:addChannel = 1 0.0034701 1542 16 -211 211 -321',            # tau- -> nu_tau pi- pi+ K-
            '15:addChannel = 1 0.0014318 1542 16 -211 -321 321',            # tau- -> nu_tau pi- K- K+
            '15:addChannel = 1 0.0015809 1542 16 111 311 -321',             # tau- -> nu_tau pi0 K0 K-
            '15:addChannel = 1 0.0011912 1542 16 130 -211 310',             # tau- -> nu_tau K_L0 pi- K_S0
            '15:addChannel = 1 0.0006435 1542 16 111 111 -321',             # tau- -> nu_tau pi0 pi0 K-
            '15:addChannel = 1 0.0002386 1542 16 130 130 -211',             # tau- -> nu_tau K_L0 K_L0 pi-
            '15:addChannel = 1 0.0017520 1542 16 -211 310 310',             # tau- -> nu_tau pi- K_S0 K_S0
            '15:addChannel = 1 0.0459365 1543 16 111 -211 221',             # tau- -> nu_tau pi0 pi- eta
            '15:addChannel = 1 0.0104401 1544 16 22 111 -211',              # tau- -> nu_tau gamma pi0 pi-
            '15:addChannel = 1 0.0459365 1551 16 111 -211 -211 211',        # tau- -> nu_tau pi0 pi- pi- pi+
            '15:addChannel = 1 0.0104401 1551 16 111 111 111 -211',         # tau- -> nu_tau pi0 pi0 pi0 pi-
            '15:addChannel = 1 0.0049069 1561 16 111 111 -211 -211 211',    # tau- -> nu_tau pi0 pi0 pi- pi- pi+
            '15:addChannel = 1 0.0009515 1561 16 111 111 111 -211',         # tau- -> nu_tau pi0 pi0 pi0 pi-
            '15:addChannel = 1 0.0008342 1561 16 -211 -211 -211 211 211',   # tau- -> nu_tau pi0 pi- pi- pi- pi+ pi+
            '15:addChannel = 1 0.0001631 0 16 -211 211 211 221',            # tau- -> nu_tau pi- pi+ pi+ eta
            '15:addChannel = 1 0.0001491 0 16 111 111 -211 221',            # tau- -> nu_tau pi0 pi0 pi- eta
            '15:addChannel = 1 0.0001392 0 16 111 111 -211 223',            # tau- -> nu_tau pi0 pi0 pi- omega
            '15:addChannel = 1 0.0001193 0 16 -211 -211 211 223',           # tau- -> nu_tau pi- pi- pi+ omega
            '15:addChannel = 1 0.0004077 0 16 223 -321',                    # tau- -> nu_tau omega K-
            '15:addChannel = 1 0.0004773 0 16 111 111 111 -321',            # tau- -> nu_tau pi0 pi0 pi0 K-
            '15:addChannel = 1 0.0003052 0 16 111 -211 211 -321',           # tau- -> nu_tau pi0 pi- pi+ K-
            '15:addChannel = 1 0.0002784 0 16 221 -323',                    # tau- -> nu_tau eta -f0
            '15:addChannel = 1 0.0002366 0 16 -211 -211 211 -311',          # tau- -> nu_tau pi- pi- pi+ K0bar
            '15:addChannel = 1 0.0002237 0 16 -211 -211 211 -311',          # tau- -> nu_tau pi- pi- pi+ K0bar
            '15:addChannel = 1 0.0002953 0 16 111 -211 -311 311',           # tau- -> nu_tau pi0 pi-  K0bar K0
            '15:addChannel = 1 0.0000590 0 16 111 -211 -321 321'            # tau- -> nu_tau pi0 pi- K- K+

        )
    ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    psethack = cms.string('a to tautau pTgun')
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen+process.genTauFilter_unphysical)
# process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path).insert(0, process.generator)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
