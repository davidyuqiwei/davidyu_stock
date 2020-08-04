#!/usr/bin/sh
# this script download the daily stock data
#####################################################
##---- set the system envr, no need to change ---####
#####################################################
source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
programName=${0##*/} ### filename without type e.g.  test.sh  > test
source $shell_function_dir"create_log.sh"  ## source function to make the logs
###########################################################
#  nohup ./run.sh > run.log  2>&1 &
#########################################################
###----------- python sccript ------------------------### 
########################################################
PythonFile="download_liutong_owner.py"
funWithParam $PythonFile  ## make the log file >> $Thelog
`touch $Thelog`
echo "The running time is "$(date "+%Y%m%d-%H%M%S") >> $Thelog
`python $PythonFile >> $Thelog`
echo "finished the python script" >> $Thelog 
echo "finish python loop"
## combine all the csv
#`cat $stock_data/day_history_insert/*.csv > $curr_dir/all.csv`
#`rm -rf to_download.py`
#`rm -rf num.sh`
###########   python script finished ##################
