#!/usr/bin/sh
source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
base_dir=$(dirname "$PWD")

database="stock_analysis"
tgt_table="owner_cnt"
datetimes="2019-06-30"

sql_dir=$base_dir/sql
sql_file=$sql_dir/"run_liutong_owner_cnt.sql"
echo $sql_file
spark-sql \
    -f $sql_file \
    -d database=${database} \
    -d tgt_table=${tgt_table} \
    -d datetimes=${datetimes} \
    -S
