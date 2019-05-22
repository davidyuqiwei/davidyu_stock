#!/usr/bin/sh
cd `dirname $0`
curr_dir=`pwd`
programName=${0##*/} ### filename without type e.g.  test.sh  test
Rscript --no-save --no-restore --verbose download_SH_SZ_index.r > download_SH_SZ_index.Rout 2>&1
nohup spark-shell < to_hive.scala > scala.log
`rm -rf *.csv`
echo 'sucess '$programName' in the path'$curr_dir
