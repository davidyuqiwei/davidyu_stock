source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
programName=${0##*/} ### filename without type e.g.  test.sh  > test
#source $shell_function_dir"create_log.sh" 

config=$1
scalaFile="to_hive_v2.scala"
run_scalaFile="to_hive_run.scala"
`/bin/cp -f $THE_functions$scalaFile $curr_dir`

sed -r 's/CONFIG/'$config'/g' $scalaFile > $run_scalaFile
spark-shell < $run_scalaFile
 
rm -rf $scalaFile $run_scalaFile 






