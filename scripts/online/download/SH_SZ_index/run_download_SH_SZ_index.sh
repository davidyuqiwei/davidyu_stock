#!/usr/bin/sh
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
scalaFile="to_hive.scala"
funWithParam $scalaFile
nohup spark-shell < to_hive.scala > $Thelog
#`rm -rf *.csv`
echo -e "\n\n sucess '$programName' in the path "$curr_dir >> $Thelog
`mv *.log $log_dir`

#rm -rf *.Rout



