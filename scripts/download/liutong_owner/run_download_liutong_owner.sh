#!/usr/bin/sh
cd `dirname $0`
curr_dir=`pwd`
sep="_____"
programName=${0##*/}   ### filename without type e.g.  test.sh  test
#echo $programName
file_name=${programName%.*} ## filename   'test.sh'
date_run=`date +"%Y-%m-%d" `
`sh clean_dir.sh`


#nohup python download_liutong_owner.py
python download_liutong_owner.py

if [ $? -ne 0 ];then
  echo "failed"$sep$curr_dir$sep$programName$sep"python"$date > $script_log_path/$file_name.log
else
  echo "succeed"$sep$curr_dir$sep$programName$sep"python"$date > $script_log_path/$file_name.log
  #nohup spark-shell  < $curr_dir/to_hive.scala > $curr_dir/scala.log 2>&1 &
fi
#if [ $? -ne 0 ];then
#    echo "failed"$sep$curr_dir$sep$programName$sep"scala"$date >> $script_log_path/${programName%.*}.log
#  else
#    echo "succeed"$sep$curr_dir$sep$programName$sep"scala"$date >> $script_log_path/$file_name.log
#    `rm -rf all.csv`
#  fi
#fi

#cd `dirname $0`
#curr_dir=`pwd`
#nohup spark-shell < $curr_dir/to_hive.scala > $curr_dir/scala.log 2>&1 &
