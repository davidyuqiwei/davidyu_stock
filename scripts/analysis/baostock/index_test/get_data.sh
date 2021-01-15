#!/usr/bin/sh
f1=$1


## run hive to export data
spark-sql -e "set hive.cli.print.header=true;
set hive.exec.compress.output=false;
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;

select stock_index,dt,close 
from 
stock_dev.baostock
where dt>='2020-09-01' and dt <='2020-12-10'
and stock_index like '60%'
order by dt
;
" \
| sed 's/[\t]/,/g' > $f1
echo $f1
