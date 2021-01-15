#!/usr/bin/sh
save_dir=$stock_data"/test/"
stk_index="dfcf_fuquan_kdj"
file_name=$stk_index
f1=${save_dir}${file_name}.csv
#final_file=${file_name}_f1.csv


## run hive to export data
hive -e "set hive.cli.print.header=true;
set hive.exec.compress.output=false;
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;


select * from stock_dw.dfcf_fuquan_kdj
;
" \
| sed 's/[\t]/,/g' > $f1
#echo $f1
