#!/usr/bin/sh
source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
base_dir=$(dirname "$PWD")

tgt_database="stock_dev"
tgt_table="annual_first_last_data"
src_database="stock_dev"
src_table="day_history_insert"
#datetimes="2019-06-30"

sql_dir=$base_dir/sql
sql_file=$sql_dir/"annual_first_last_data.sql"
echo $sql_file
spark-sql \
    -f $sql_file \
    -d tgt_database=${tgt_database} \
    -d tgt_table=${tgt_table} \
    -d src_database=${src_database} \
    -d src_table=${src_table} \
    -S

