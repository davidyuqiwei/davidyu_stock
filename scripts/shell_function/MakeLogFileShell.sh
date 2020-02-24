#!/bin/bash
#-------------------  Use   ------------------------#
#            MakeLogFile.sh  xxx.py                 #
#---------------------------------------------------#
#cd `dirname $0`
source ~/.bashrc
curr_dir=`pwd`
#echo $curr_dir  ## the running program
#workdir=$(cd $(dirname $0); pwd)
CurrentFile=$0
programName="${CurrentFile##*/}"  ### filename without type e.g.xxx.sh
#echo $programName
file_name=${programName%.*} ## filename   'xxx'
#echo $file_name
date_run=`date +"%Y-%m-%d" `

source $shell_function_dir"create_log_update.sh" #  get function  【CreateLogFile】
ShellFile=$1
ShellFileName=${ShellFile%.*}
Thelog=$(CreateLogFile $ShellFile)
`touch $Thelog`
`sh $ShellFile >> $Thelog`
if [ $? != 0 ];then
    echo "##########################################################" >> $Thelog
    echo "$ShellFile failed" >> $Thelog
else
    echo "##########################################################" >> $Thelog
    echo "$ShellFile executed successfully" >> $Thelog
fi
echo "run time; `date '+%Y%m%d %H:%M:%S'`" >> $Thelog
mv $Thelog $log_dir
