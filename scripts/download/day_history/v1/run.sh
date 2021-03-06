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
#rm -rf *.log
#echo "source it"
###########################################################


#   ./run.sh > run.log  2>&1 &


###############################
###----- python sccript ----### 
###############################
PythonFile="download_data_insert.py"
funWithParam $PythonFile  ## make the log file >> $Thelog
`touch $Thelog`
echo "The running time is "$(date "+%Y%m%d-%H%M%S") >> $Thelog
## count how many stock index in the file
## for loop
file_in=$stock_data/basic_info/stock_basic_info.csv
stk_count=`wc -l $file_in`
## how many rows in the file and assign to the parameter
stk_index_count=`echo $stk_count | awk '{print $1}'`  
stk_loop=$((stk_index_count-1))
#stk_loop=2  # for test
echo $stk_loop
for i in $(seq 0 $stk_loop)
do 
    #echo $i
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
###########   python script finished ##################



###############################
###----- scala  script ----### 
###############################
echo "start scala"
##-----------------------------------##
##------------- set it --------------##
target_table="stock_dev.day_history_insert"
target_csv="all.csv"
##-----------------------------------##
scalaFile="to_hive_all_new.scala"
`/bin/cp -f $THE_functions$scalaFile $curr_dir`
run_scala="to_hive.scala"
funWithParam $run_scala
sed -r 's/all.csv/'$target_csv'/g' $scalaFile | sed -r 's/stock_dev.fin_report/'$target_table'/g' > $run_scala
spark-shell < $run_scala > $Thelog 2>&1
echo -e "\n\n sucess '$programName' in the path "$curr_dir >> $Thelog

#####################################################################################
#----------------- finish save to hive ------------------------------------#
#####################################################################################

`mv -f *.log $log_dir`
## if sucess rm the csv and scala
if [ $? -ne 0  ];then
    echo "Something failed check the log"
else
    echo 'OK'
    #sleep 1h
    `rm -rf *.csv *.scala`
fi

## zip the data
`zip -r $stock_data/zip_data/day_history_$(date "+%Y%m%d").zip $stock_data/day_history_insert/*.csv`

