#!/usr/bin/sh
#####################################################
##---- set the system envr, no need to change ---####
#####################################################
source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
programName=${0##*/} ### filename without type e.g.  test.sh  > test
source $shell_function_dir"create_log.sh"






###
Rfile="download_SH_SZ_index.r"
funWithParam $Rfile
#################################
####  start the run #############
#################################
Rscript --no-save --no-restore --verbose $Rfile> $Thelog 2>&1
echo -e "\n\n The program run DIR is "$curr_dir >> $Thelog

#---- scala -----#
scalaFile="to_hive_all_new.scala"
`/bin/cp -f $THE_functions$scalaFile $curr_dir`
##-----------------------------------##
##------------- set it --------------##
target_table="stock_dev.SH_index"
target_csv="shanghai_index_all.csv"
##-----------------------------------##
##-----------------------------------##
run_scala="to_hive.scala"
funWithParam $run_scala
sed -r 's/all.csv/'$target_csv'/g' $scalaFile | sed -r 's/stock_dev.fin_report/'$target_table'/g' > $run_scala
nohup spark-shell < $run_scala > $Thelog 2>&1 &
#`rm -rf *.csv`
echo -e "\n\n sucess '$programName' in the path "$curr_dir >> $Thelog
`mv -f *.log $log_dir`

## if sucess rm the csv and scala
if [ $? -ne 0  ];then
    echo "Something failed check the log"
else
    `rm -rf *.csv *.scala`
fi

#rm -rf *.Rout



