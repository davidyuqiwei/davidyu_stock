#!/usr/bin/sh
save_dir=$stock_data"/test/"
stk_index="all_test"
file_name=$stk_index
f1=${save_dir}${file_name}.csv
#final_file=${file_name}_f1.csv


## run hive to export data
hive -e "set hive.cli.print.header=true;
set hive.exec.compress.output=false;
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;

select x1,x13,x30,x32,x33,x68,x94 from 
stock_dev.fin_report 
where x1 >= '2015-01-01' and x1 <= '2018-11-19'
;
" \
| sed 's/[\t]/,/g' > $f1
echo $f1
#| sed 's/[\t]/\t/g' > $f1
