#!/usr/bin/sh
save_dir=$stock_data"/test/for_every_stock/"
stk_index="stock_mv_avg"
file_name=$stk_index
f1=${save_dir}${file_name}.csv
#final_file=${file_name}_f1.csv


## run hive to export data
hive -e "set hive.cli.print.header=true;
set hive.exec.compress.output=false;
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;

select * from stock_analysis.day_history_mv_avg limit 20000
;
" \
| sed 's/[\t]/,/g' > $f1
echo $f1
#| sed 's/[\t]/\t/g' > $f1
