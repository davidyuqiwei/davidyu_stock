#!/usr/bin/sh
cd `dirname $0`
curr_dir=`pwd`
sep="_____"
programName=${0##*/}   ### filename without type e.g.  test.sh  test
#echo $programName
file_name=${programName%.*} ## filename   'test.sh'
date_run=`date +"%Y-%m-%d" `
`sh clean_dir.sh`
#rm -rf $curr_dir/python.log $curr_dir/scala.log

##   python to download the data and combine
nohup python download_data_insert.py > $curr_dir/python.log 

<<<<<<< HEAD
# if success or not and write to the log file
=======
>>>>>>> 1f748b377819d67350ada8ca8130fda7752e2a91
if [ $? -ne 0 ];then
  echo "failed"$sep$curr_dir$sep$programName$sep"python"$date > $script_log_path/$file_name.log
else
  echo "succeed"$sep$curr_dir$sep$programName$sep"python"$date > $script_log_path/$file_name.log
  nohup spark-shell  < $curr_dir/to_hive.scala > $curr_dir/scala.log 2>&1 &
  #`rm -rf all.csv`
fi

if [ $? -ne 0 ];then
  echo "failed"$sep$curr_dir$sep$programName$sep"scala"$date >> $script_log_path/${programName%.*}.log
else
  echo "succeed"$sep$curr_dir$sep$programName$sep"scala"$date >> $script_log_path/$file_name.log
fi
