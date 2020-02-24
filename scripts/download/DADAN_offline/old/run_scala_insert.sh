#!/usr/bin/sh
#-----------------------------------------------------------------#
#----------- system script---------------#
source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
echo "current dir++++ "$curr_dir
programName=${0##*/} ### filename without type e.g.  test.sh  > test
source $shell_function_dir"create_log_update.sh"  ## source function to make the logs


###############################
###----- scala  script ----### 
###############################
echo "start scala"
##-----------------------------------##
##------------- set it --------------##
whereis_data="/home/davidyu/stock/data/tmp/"
target_table="stock_test.dadan_100"
target_csv="all.csv"
#target_csv="sss.csv"

scalaFile="to_hive_insert.scala"
run_scala="to_hive.scala" ## run this file
Thelog=$(CreateLogFile $run_scala)  ## make the log
#today_date=`date +%Y_%m_%d`
#yesterday_date=`date -d "last day" +%Y_%m_%d`
#to_database_file=$whereis_data/"DADAN_"$yesterday_date".csv"
to_database_file=$whereis_data"DADAN_100_all.csv"
echo "the data to databse $to_database_file" 
#################################################################
##----------put all data in all.csv to current directory-------##
#################################################################
if [ ! -f "$to_database_file" ];then
    echo "no data file $to_database_file"
    exit 2
else
    echo "cat all data in $to_database_file"
fi
`cat $to_database_file> $curr_dir/all.csv`
################################################################
##--------- copy the scala file to insert to database ---------#
################################################################
echo "copy the file ++++ "$THE_functions$scalaFile
`/bin/cp -f $THE_functions$scalaFile $curr_dir`
################################################################
#---------------- change the input file name ------------------#
## and the target table
################################################################
sed -r 's/all.csv/'$target_csv'/g' $scalaFile | sed -r 's/stock_dev.fin_report/'$target_table'/g' > $run_scala
spark-shell < $run_scala > $Thelog 2>&1
echo -e "\n\n sucess '$programName' in the path "$curr_dir >> $Thelog

#####################################################################################
#----------------- finish save to hive ------------------------------------#
#####################################################################################

#`mv -f *.log $log_dir`
## if sucess rm the csv and scala
if [ $? -ne 0  ];then
    echo "Something failed check the log"
else
    echo 'OK'
    #sleep 1h
    `rm -rf *.csv *.scala`
fi
echo $?
## zip the data
#`zip -r $stock_data/zip_data/day_history_$(date "+%Y%m%d").zip $stock_data/day_history_insert/*.csv`

