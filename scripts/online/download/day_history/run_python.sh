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
PythonFile="download_data_insert.py"
funWithParam $PythonFile  ## make the log file >> $Thelog
`touch $Thelog`
echo "The running time is "$(date "+%Y%m%d-%H%M%S") >> $Thelog
## ---------------- for loop ---------------------##
#--------------------------------------------------#
####################################################
###---------- get how many stock index to loop----##
####################################################
file_in=$stock_data/basic_info/stock_basic_info.csv
stk_count=`wc -l $file_in | awk '{print $1}'` ## count how many stock index in the file
## how many rows in the file and assign to the parameter
stk_loop=$((stk_count-1))
#stk_loop=2  # for test
echo "all the loop number of stock index is "$stk_loop
#--------------------------------------------------#
####################################################
###---------- start loop to download the data ----##
####################################################
## record the loop number if killed anyway restart
if [ -f "num.sh" ];then
    start_loop1=`cat num.sh`
    start_loop=$((start_loop1-1))
else 
    start_loop=0
fi
# start loop to download 
for i in $(seq $start_loop $stk_loop)
do 
    #echo $i
    `echo $i > num.sh`
    sed -r 's/TheInput/'$(echo $i)'/g' download_data_insert.py > to_download.py
    `python to_download.py >> $Thelog`
    sleep 2s
done
#python download_data_insert.py >> $Thelog & echo $! > pidfile.log
echo "finished the python script" >> $Thelog 
echo "finish python loop"
## combine all the csv
`cat $stock_data/day_history_insert/*.csv > $curr_dir/all.csv`
`rm -rf to_download.py`
`rm -rf num.sh`
###########   python script finished ##################
