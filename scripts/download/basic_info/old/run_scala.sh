#!/usr/bin/sh
source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
programName=$0   # program name  xx.sh
echo "this file is "$programName
file_name=${programName%.*} ### filename without type e.g.  test.sh > test
source $shell_function_dir"create_log_update.sh"

scalaFile="to_hive_all_new.scala"
`/bin/cp -f $THE_functions$scalaFile $curr_dir`

##-----------------------------------##
##------------- set it --------------##
target_table=$1
target_csv=$2
run_scala="to_hive_"$file_name".scala"
Thelog=$(CreateLogFile $run_scala)
`touch $Thelog`
echo $Thelog
sed -r 's/all.csv/'$target_csv'/g' $scalaFile | sed -r 's/stock_dev.fin_report/'$target_table'/g' > $run_scala
spark-shell < $run_scala > $Thelog 2>&1


check_string="ALLOK"
## if sucess rm the csv and scala
if cat $Thelog | grep "$check_string";then
    echo 'OK'
    sleep 2s
    `rm -rf *.csv *.scala`
    `mv -f *.log $log_dir`
else
    echo "Something failed check the log"
fi


