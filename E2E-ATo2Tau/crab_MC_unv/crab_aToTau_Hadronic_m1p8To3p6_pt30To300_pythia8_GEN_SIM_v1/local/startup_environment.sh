declare -x APPTAINER_PID="true"
declare -- BASH="/bin/sh"
declare -r BASHOPTS="cmdhist:complete_fullquote:extquote:force_fignore:hostcomplete:interactive_comments:progcomp:promptvars:sourcepath"
declare -ir BASHPID
declare -A BASH_ALIASES=()
declare -a BASH_ARGC=()
declare -a BASH_ARGV=()
declare -A BASH_CMDS=()
declare -- BASH_COMMAND
declare -x BASH_ENV="/usr/share/lmod/lmod/init/bash"
declare -- BASH_EXECUTION_STRING="eval \`scram unsetenv -sh\`; 
echo \$PWD && ls -lrth
. ./submit_env.sh && save_env && setup_local_env;
tar xzmf CMSRunAnalysis.tar.gz
sh CMSRunAnalysis.sh --json DryRunJobArg.json"
declare -a BASH_LINENO=([0]="2")
declare -a BASH_SOURCE=([0]="./submit_env.sh")
declare -- BASH_SUBSHELL
declare -ar BASH_VERSINFO=([0]="4" [1]="4" [2]="20" [3]="1" [4]="release" [5]="x86_64-redhat-linux-gnu")
declare -- BASH_VERSION="4.4.20(1)-release"
declare -x CMSSW_GIT_REFERENCE="/cvmfs/cms.cern.ch/cmssw.git.daily"
declare -x CMS_PATH="/cvmfs/cms.cern.ch"
declare -- COMP_WORDBREAKS
declare -x CVSROOT=":gserver:cmssw.cvs.cern.ch:/local/reps/CMSSW"
declare -x CVS_RSH="ssh"
declare -x DBUS_SESSION_BUS_ADDRESS="unix:abstract=/tmp/dbus-pSMWXKpWmG,guid=06efe78c68564b73262177a36790175a"
declare -x DEBUGINFOD_URLS="https://debuginfod.centos.org/ "
declare -a DIRSTACK=()
declare -x DISPLAY="localhost:11.0"
declare -ir EUID="57337"
declare -x FPATH="/usr/share/lmod/lmod/init/ksh_funcs"
declare -a FUNCNAME=([0]="save_env")
declare -x GDK_BACKEND="x11"
declare -a GROUPS=()
declare -i HISTCMD
declare -x HISTCONTROL="ignoredups"
declare -x HISTSIZE="1000"
declare -x HOME="/uscms/home/bbbam"
declare -x HOSTNAME="cmslpc202.fnal.gov"
declare -- HOSTTYPE="x86_64"
declare -- IFS=" 	
"
declare -x JOBSTARTDIR="/uscms_data/d3/bbbam/analysis_run3/MCGeneration/CMSSW_13_0_17/src/MCProduction_run3/E2E-ATo2Tau/crab_MC_unv/crab_aToTau_Hadronic_m1p8To3p6_pt30To300_pythia8_GEN_SIM_v1/local"
declare -x KRB5CCNAME="FILE:/tmp/krb5cc_57337_OKUffaYg36"
declare -x LANG="en_US.UTF-8"
declare -x LC_CTYPE="C.UTF-8"
declare -x LESSOPEN="||/usr/bin/lesspipe.sh %s"
declare -i LINENO
declare -x LMOD_CMD="/usr/share/lmod/lmod/libexec/lmod"
declare -x LMOD_DIR="/usr/share/lmod/lmod/libexec"
declare -x LMOD_PKG="/usr/share/lmod/lmod"
declare -x LMOD_ROOT="/usr/share/lmod"
declare -x LMOD_SETTARG_FULL_SUPPORT="no"
declare -x LMOD_VERSION="8.7.55"
declare -x LMOD_sys="Linux"
declare -x LOGNAME="bbbam"
declare -x LS_COLORS="rs=0:di=38;5;33:ln=38;5;51:mh=00:pi=40;38;5;11:so=38;5;13:do=38;5;5:bd=48;5;232;38;5;11:cd=48;5;232;38;5;3:or=48;5;232;38;5;9:mi=01;05;37;41:su=48;5;196;38;5;15:sg=48;5;11;38;5;16:ca=48;5;196;38;5;226:tw=48;5;10;38;5;16:ow=48;5;10;38;5;21:st=48;5;21;38;5;15:ex=38;5;40:*.tar=38;5;9:*.tgz=38;5;9:*.arc=38;5;9:*.arj=38;5;9:*.taz=38;5;9:*.lha=38;5;9:*.lz4=38;5;9:*.lzh=38;5;9:*.lzma=38;5;9:*.tlz=38;5;9:*.txz=38;5;9:*.tzo=38;5;9:*.t7z=38;5;9:*.zip=38;5;9:*.z=38;5;9:*.dz=38;5;9:*.gz=38;5;9:*.lrz=38;5;9:*.lz=38;5;9:*.lzo=38;5;9:*.xz=38;5;9:*.zst=38;5;9:*.tzst=38;5;9:*.bz2=38;5;9:*.bz=38;5;9:*.tbz=38;5;9:*.tbz2=38;5;9:*.tz=38;5;9:*.deb=38;5;9:*.rpm=38;5;9:*.jar=38;5;9:*.war=38;5;9:*.ear=38;5;9:*.sar=38;5;9:*.rar=38;5;9:*.alz=38;5;9:*.ace=38;5;9:*.zoo=38;5;9:*.cpio=38;5;9:*.7z=38;5;9:*.rz=38;5;9:*.cab=38;5;9:*.wim=38;5;9:*.swm=38;5;9:*.dwm=38;5;9:*.esd=38;5;9:*.jpg=38;5;13:*.jpeg=38;5;13:*.mjpg=38;5;13:*.mjpeg=38;5;13:*.gif=38;5;13:*.bmp=38;5;13:*.pbm=38;5;13:*.pgm=38;5;13:*.ppm=38;5;13:*.tga=38;5;13:*.xbm=38;5;13:*.xpm=38;5;13:*.tif=38;5;13:*.tiff=38;5;13:*.png=38;5;13:*.svg=38;5;13:*.svgz=38;5;13:*.mng=38;5;13:*.pcx=38;5;13:*.mov=38;5;13:*.mpg=38;5;13:*.mpeg=38;5;13:*.m2v=38;5;13:*.mkv=38;5;13:*.webm=38;5;13:*.ogm=38;5;13:*.mp4=38;5;13:*.m4v=38;5;13:*.mp4v=38;5;13:*.vob=38;5;13:*.qt=38;5;13:*.nuv=38;5;13:*.wmv=38;5;13:*.asf=38;5;13:*.rm=38;5;13:*.rmvb=38;5;13:*.flc=38;5;13:*.avi=38;5;13:*.fli=38;5;13:*.flv=38;5;13:*.gl=38;5;13:*.dl=38;5;13:*.xcf=38;5;13:*.xwd=38;5;13:*.yuv=38;5;13:*.cgm=38;5;13:*.emf=38;5;13:*.ogv=38;5;13:*.ogx=38;5;13:*.aac=38;5;45:*.au=38;5;45:*.flac=38;5;45:*.m4a=38;5;45:*.mid=38;5;45:*.midi=38;5;45:*.mka=38;5;45:*.mp3=38;5;45:*.mpc=38;5;45:*.ogg=38;5;45:*.ra=38;5;45:*.wav=38;5;45:*.oga=38;5;45:*.opus=38;5;45:*.spx=38;5;45:*.xspf=38;5;45:"
declare -- MACHTYPE="x86_64-redhat-linux-gnu"
declare -x MAIL="/var/spool/mail/bbbam"
declare -x MANPATH="/cvmfs/cms.cern.ch/share/man:/usr/share/lmod/lmod/share/man:/opt/puppetlabs/puppet/share/man"
declare -x MODULEPATH="/etc/modulefiles:/usr/share/modulefiles:/usr/share/modulefiles/Linux:/usr/share/modulefiles/Core:/usr/share/lmod/lmod/modulefiles/Core"
declare -x MODULEPATH_ROOT="/usr/share/modulefiles"
declare -x MODULESHOME="/usr/share/lmod/lmod"
declare -x OLDPWD="/uscms/home/bbbam/nobackup/analysis_run3/MCGeneration/CMSSW_13_0_17/src"
declare -- OPTERR="1"
declare -i OPTIND="1"
declare -- OSTYPE="linux-gnu"
declare -x PATH="/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.241125.00/bin:/cvmfs/cms.cern.ch/common:/opt/puppetlabs/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/opt/puppetlabs/bin"
declare -a PIPESTATUS=([0]="0")
declare -- POSIXLY_CORRECT="y"
declare -ir PPID="2206306"
declare -- PS4="+ "
declare -x PWD="/uscms_data/d3/bbbam/analysis_run3/MCGeneration/CMSSW_13_0_17/src/MCProduction_run3/E2E-ATo2Tau/crab_MC_unv/crab_aToTau_Hadronic_m1p8To3p6_pt30To300_pythia8_GEN_SIM_v1/local"
declare -x PYTHONNOUSERSITE="true"
declare -x PYTHONPATH="/cvmfs/cms.cern.ch/rucio/x86_64/rhel8/py3/current/lib/python3.6/site-packages:/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.241125.00/lib"
declare -i RANDOM
declare -x RUCIO_HOME="/cvmfs/cms.cern.ch/rucio/x86_64/rhel8/py3/current"
declare -x SCRAM_ARCH="el8_amd64_gcc11"
declare -- SECONDS
declare -x SHELL="/bin/bash"
declare -r SHELLOPTS="braceexpand:hashall:interactive-comments:posix"
declare -x SHLVL="3"
declare -x SITECONFIG_PATH="/cvmfs/cms.cern.ch/SITECONF/local"
declare -x SSH_AUTH_SOCK="/tmp/ssh-pkBfe3KDAI/agent.1961728"
declare -x SSH_CLIENT="2620:6a:0:8421::211 53403 22"
declare -x SSH_CONNECTION="2620:6a:0:8421::211 53403 2620:6a:0:8421:f0:0:777:19 22"
declare -x SSH_TTY="/dev/pts/1"
declare -x S_COLORS="auto"
declare -x TERM="xterm-256color"
declare -ir UID="57337"
declare -x USER="bbbam"
declare -x X509_USER_PROXY="/uscms/home/bbbam/x509up_u57337"
declare -x XDG_RUNTIME_DIR="/run/user/57337"
declare -x XDG_SESSION_ID="1042"
declare -- _="HOME"
declare -x _CONDOR_JOB_AD="Job.submit"
declare -x which_declare="declare -f"
