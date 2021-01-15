#!/usr/bin/sh
f1=$1


## run hive to export data
hive -e "set hive.cli.print.header=true;
set hive.exec.compress.output=false;
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;

select * from 
stock_feature.stock_index_mv_avg
where dt>='2000-01-01'
order by dt
;
" \
| sed 's/[\t]/,/g' > $f1
echo $f1

