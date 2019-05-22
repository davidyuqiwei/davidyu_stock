cd `dirname $0`
curr_dir=`pwd`
sep="_____"
programName=${0##*/}
echo $programName

script_name="run_day_history_insert.sh"
#rm -rf $HOME/python.log $HOME/scala.log
#$HOME/test.scala > $HOME/test.log 2>&1 &
#python download_data_insert.py
#echo $script_log_path/${programName%.*}.log
ech 'ss'
if [ $? -ne 0 ];then
  echo "failed"
else 
  echo "OK"
fi

#echo "failed"$sep$curr_dir$sep$programName > $script_log_path/${programName%.*}.log

