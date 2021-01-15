#!/usr/bin/sh
save_dir=$stock_data"/test/"
file_name="stock_index_daily_data"
f1=${save_dir}${file_name}.csv


## run hive to export data
hive -e "set hive.cli.print.header=true;
set hive.exec.compress.output=false;
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;

select *  
from stock_raw.baostock
where stock_index in ('601398','000917','000333','601318')
order by dt
;
" \
| sed 's/[\t]/,/g' > $f1
echo $f1
