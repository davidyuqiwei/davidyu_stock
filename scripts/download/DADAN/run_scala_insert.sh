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
#`cat $stock_data/liutong_owner/*.csv > $curr_dir/all.csv`
#`cat /home/davidyu/stock/data/tmp/*.csv > $curr_dir/all.csv`
###############################
###----- scala  script ----### 
###############################
echo "start scala"
##-----------------------------------##
##------------- set it --------------##
#whereis_data="/home/davidyu/stock/data/tmp/"
target_table="stock_test.dadan_200"
target_csv="all.csv"

scalaFile="to_hive_insert.scala"
run_scala="to_hive.scala" ## run this file
#Thelog=$(funWithParam $run_scala)  ## make the log
#today_date=`date +%Y_%m_%d`
#yesterday_date=`date -d "last day" +%Y_%m_%d`
#to_database_file=$whereis_data/"DADAN_"$yesterday_date".csv"
#to_database_file=$whereis_data"DADAN_"$today_date".csv"
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

spark-shell < $run_scala
#echo -e "\n\n sucess '$programName' in the path "$curr_dir >> $Thelog

#####################################################################################
#----------------- finish save to hive ------------------------------------#
#####################################################################################

## if sucess rm the csv and scala
if [ $? -ne 0  ];then
    echo "Something failed check the log"
    exit 2
else
    echo 'OK'
    #sleep 1h
    `rm -rf *.csv *.scala`
    exit 0
fi
echo $?
## zip the data
#`zip -r $stock_data/zip_data/day_history_$(date "+%Y%m%d").zip $stock_data/day_history_insert/*.csv`

