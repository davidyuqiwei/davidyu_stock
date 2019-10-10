#!/usr/bin/sh
source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
base_dir=$(dirname "$PWD") 


sql_dir=$base_dir/sql
sql_file=$sql_dir/"run_liutong_owner_owner_number_sort_list.sql"
echo $sql_file
spark-sql -f $sql_file

