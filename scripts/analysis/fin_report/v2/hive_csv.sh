#!/usr/bin/sh
save_dir=$stock_data"/test/"
file_name="fin_report_index_cnt"
#file_name=$stk_index"fin_report"
f1=${save_dir}${file_name}.csv
#final_file=${file_name}_f1.csv


## run hive to export data
hive -e "set hive.cli.print.header=true;
set hive.exec.compress.output=false;
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;

select * from stock_test.fin_report_index_cnt
;
" \
| sed 's/[\t]/,/g' > $f1
#| sed 's/[\t]/\t/g' > $f1
