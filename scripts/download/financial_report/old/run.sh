#!/usr/bin/sh
source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
sep="_____"
programName=${0##*/}   ### filename without type e.g.  test.sh  test
source $shell_function_dir"create_log_update.sh"

#################################
####  start the run #############
#################################
PythonFile="download_fin_report_v2.py"
Thelog=${CreateLogFile $PythonFile}
`touch $Thelog`
python $PythonFile >> $Thelog``
#`sh clean_dir.sh`
#python download_fin_report.py > $curr_dir/python.log


scalaFile="to_hive_all_new.scala"
`/bin/cp -f $THE_functions$scalaFile $curr_dir`
##-----------------------------------##
##------------- set it --------------##
target_table="stock_dev.fin_report"
target_csv="all.csv"
run_scala="to_hive.scala"
funWithParam $run_scala
sed -r 's/all.csv/'$target_csv'/g' $scalaFile | sed -r 's/stock_dev.fin_report/'$target_table'/g' > $run_scala
spark-shell < $run_scala > $Thelog
echo -e "\n\n sucess '$programName' in the path "$curr_dir >> $Thelog
`mv -f *.log $log_dir`

#scalaFile="to_hive.scala"
if [ $? -ne 0   ];then
    echo "Something failed check the log"
else
    #`rm -rf *.csv *.scala`
    echo 'success'
fi

