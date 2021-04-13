#!/usr/bin/sh
save_dir=$stock_data"/test/"
stk_index="SH_index_data"
file_name=$stk_index
f1=${save_dir}${file_name}.csv
#final_file=${file_name}_f1.csv


## run hive to export data
hive -e "set hive.cli.print.header=true;
set hive.exec.compress.output=false;
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;


select * from stock_dev.SH_index
where stock_date<=to_date(date_sub(current_date(),1))
;
" \
| sed 's/[\t]/,/g' > $f1
echo $f1
