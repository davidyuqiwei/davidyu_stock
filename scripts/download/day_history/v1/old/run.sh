#!/usr/bin/sh
#####################################################
##---- set the system envr, no need to change ---####
#####################################################
source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
programName=${0##*/} ### filename without type e.g.  test.sh  > test
source $shell_function_dir"create_log.sh"


#nohup ./run.sh > log.txt & echo $! > pidfile.txt
PythonFile="download_data_insert.py"
funWithParam $PythonFile
python $PythonFile > $Thelog 2>&1





