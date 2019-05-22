#!/usr/bin/sh
curr_dir=`pwd`
#Rscript download_SH_SZ_index.r  
nohup spark-shell < to_hive.scala > scala.log

