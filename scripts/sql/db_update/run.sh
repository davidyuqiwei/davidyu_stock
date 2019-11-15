#!/usr/bin/sh
python_script=$1
programName=${0##*/}
sql_script=$python_script".sql"
echo $sql_script
python $python_script > $sql_script

`hive -f $sql_script`




