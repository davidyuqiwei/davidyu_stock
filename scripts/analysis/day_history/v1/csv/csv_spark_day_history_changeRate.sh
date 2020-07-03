#!/usr/bin/sh
source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
base_dir=$(dirname "$PWD")

# run the spark to make the table
shell_table_dir=$base_dir/shell
shell_file=$shell_table_dir/"spark_day_history_changeRate.sh"

start_date="2018-01-01"
end_date="2018-12-31"

#sh $shell_file $start_date $end_date


## save the table to csv
start_date_no=${start_date//\-/}
end_date_no=${end_date//\-/}

save_dir=$stock_data"/test/"
stk_index="stock_change_rate_"$start_date_no"_"$end_date_no
file_name=$stk_index
f1=${save_dir}${file_name}.csv
#final_file=${file_name}_f1.csv


## run hive to export data
hive -e "set hive.cli.print.header=true;
set hive.exec.compress.output=false;
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;


select * from stock_test.$stk_index
a;
" \
| sed 's/[\t]/\t/g' > $f1
echo $f1



