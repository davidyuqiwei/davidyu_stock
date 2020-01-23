#!/usr/bin/sh
save_dir=$stock_data"/test/"
stk_index="600519"
file_name=$stk_index"fin_report"
f1=${save_dir}${file_name}.csv
#final_file=${file_name}_f1.csv


## run hive to export data
hive -e "set hive.cli.print.header=true;
set hive.exec.compress.output=false;
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;

select * from stock_dev.fin_annual_avg
where x94 = '600519'
order by year 
;
" \
| sed 's/[\t]/,/g' > $f1
 $f1
#| sed 's/[\t]/\t/g' > $f1
