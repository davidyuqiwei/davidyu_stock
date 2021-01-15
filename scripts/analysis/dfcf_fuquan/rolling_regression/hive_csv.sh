#!/usr/bin/sh
save_dir=$stock_data"/test/"
stk_index="dfcf_fuquan_kdj_reg"
file_name=$stk_index
f1=${save_dir}${file_name}.csv

## run hive to export data
spark-sql \
    --executor-memory   3G \
    --driver-memory     3G \
    --conf spark.sql.autoBroadcastJoinThreshold=-1 \
    --conf spark.shuffle.file.buffer=64K \
    -e "set hive.cli.print.header=true;
set hive.exec.compress.output=false;
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;

use stock_dw;

select lpad(t1.stock_index,6,'0') as stock_index,
t1.dt as dt,
t1.slopes as slope,
slope_num_in,days_default,
case when t1.slopes>0 then 1
    else -1 end as slope_cls,
case when t1.slopes>0 and t1.slopes<=0.05  then 1
    when t1.slopes>0.05 and t1.slopes<=0.1  then 2
    when t1.slopes>0.1  then 3
    when t1.slopes>-0.05 and t1.slopes<=0  then -1
    when t1.slopes>=-0.1 and t1.slopes<=-0.05 then -2
    when t1.slopes<-0.1  then -3
    else null end as slope_cls2,
rsi_6,rsi_12,rsi_24,kdjk,
kdjd,kdjj,macdh,
boll_ub,boll_lb,round(boll_ub/boll_lb,3) as boll_ratio
from dfcf_fuquan_roll_reg t1
left join dfcf_fuquan_kdj t2
on lpad(t1.stock_index,6,'0') = lpad(t2.stock_index,6,'0') 
and t1.dt = t2.stock_date
where t1.stock_index is not null and t2.stock_date>='2016-01-01'
and slope_num_in=days_default
;
" \
| sed 's/[\t]/\t/g' > $f1
