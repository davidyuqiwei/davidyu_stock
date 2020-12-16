#!/usr/bin/sh
#-----------------------------------------------------------------#
#----------- system script---------------#
source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
echo "current dir++++ "$curr_dir
programName=${0##*/} ### filename without type e.g.  test.sh  > test
source $shell_function_dir"create_log.sh"  ## source function to make the logs


## cp all the data in folder to the current folder
###############################
###----- scala  script ----### 
###############################
echo "start scala"
##-----------------------------------##
##------------- set it --------------##
target_table="stock_dev.fin_report"
target_csv="all.csv"

scalaFile="to_hive_all_new.scala"
run_scala="to_hive.scala" ## run this file
Thelog=$(funWithParam $run_scala)  ## make the log

##--------- copy the scala file to insert to database ---------#
################################################################
echo "copy the file ++++ "$THE_functions$scalaFile
`/bin/cp -f $THE_functions$scalaFile $curr_dir`
################################################################
#---------------- change the input file name ------------------#
## and the target table
################################################################
sed -r 's/all.csv/'$target_csv'/g' $scalaFile | sed -r 's/stock_dev.fin_report/'$target_table'/g' > $run_scala


spark-shell < $run_scala
## if sucess rm the csv and scala
if [ $? -ne 0  ];then
    echo "Something failed check the log"
    exit 2
else
    echo 'OK'
    #sleep 1h
    `rm -rf *.csv *.scala`
fi

echo -e "\n\n sucess '$programName' in the path "$curr_dir

#####################################################################################
#----------------- finish save to hive ------------------------------------#
#####################################################################################

#`mv -f *.log $log_dir`
#echo $?
## zip the data
#`zip -r $stock_data/zip_data/day_history_$(date "+%Y%m%d").zip $stock_data/day_history_insert/*.csv`

