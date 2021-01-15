#!/usr/bin/sh
f1=$1


## run hive to export data
hive -e "set hive.cli.print.header=true;
set hive.exec.compress.output=false;
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;

select distinct 
    stock_index,stock_name,
    yeji_predict,regexp_replace(yeji_abstract,',','_'),
    stock_date from
    stock_dev.yejiyuqi
    where yeji_predict in ('业绩预盈','业绩大幅上升') and
    stock_date >= '2020-01-01' and stock_date<='2020-03-31'
;
" \
| sed 's/[\t]/,/g' > $f1
echo $f1


cp $f1 /home/davidyu/stock/data/tmp_data/feature_center
