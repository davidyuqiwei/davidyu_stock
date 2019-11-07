source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
programName=${0##*/}   ### filename without type e.g.  test.sh  test
source $shell_function_dir"create_log_update.sh"

PythonFile="download_fin_report_v2.py"
Thelog=$(CreateLogFile $PythonFile)
#`touch $Thelog`
echo $Thelog
