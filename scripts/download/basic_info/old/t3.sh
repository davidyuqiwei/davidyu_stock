#!/usr/bin/sh
cd `dirname $0`
curr_dir=`pwd`
programName={${0##*/}  ### filename without type e.g.  test.sh  test
#echo $programName
file_name=${programName%.*} ## filename   'test.sh'
date_run=`date +"%Y-%m-%d" `
#`sh clean_dir.sh`
source $shell_function_dir"create_log_update.sh" #  get function  >【CreateLogFile】
##
PythonFile="download_news_report.py"
Thelog=$(CreateLogFile $PythonFile)
`touch $Thelog`
echo $Thelog
