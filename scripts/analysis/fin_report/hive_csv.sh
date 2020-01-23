#!/usr/bin/sh
save_dir=$stock_data"/test/"
stk_index="002810"
file_name=$stk_index"fin_report"
f1=${save_dir}${file_name}.csv
#final_file=${file_name}_f1.csv


## run hive to export data
hive -e "set hive.cli.print.header=true;
set hive.exec.compress.output=false;
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;

select x1,x33,x94 from 
stock_dev.fin_report 
where x1 >= '2015-01-01' and x1 <= '2018-11-19'
and x94 = $stk_index
order by x1
;
" \
| sed 's/[\t]/,/g' > $f1
 $f1
#| sed 's/[\t]/\t/g' > $f1
