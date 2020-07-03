#!/usr/bin/sh
source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
base_dir=$(dirname "$PWD")


tgt_database="stock_test"
src_database="stock_dev"
src_table="day_history_insert"
## set start and end date
start_date=$1
end_date=$2
if [ ! $start_date ];then
    start_date="2017-01-01"
fi
if [ ! $end_date ];then
    end_date="2017-12-31"
fi

## replace "-" to ""
tgt_table="stock_change_rate_"${start_date//-/}"_"${end_date//-/}
#a1=${start_date//-/}
#echo $a1


sql_dir=$base_dir/sql
sql_file=$sql_dir/"day_history_changeRate.sql"
echo $sql_file
spark-sql \
    -f $sql_file \
    -d src_database=${src_database} \
    -d tgt_database=${tgt_database} \
    -d src_table=${src_table} \
    -d tgt_table=${tgt_table} \
    -d start_date=${start_date} \
    -d end_date=${end_date} \
    -S

