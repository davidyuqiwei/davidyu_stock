#!/usr/bin/sh
save_dir=$stock_data"/test/"
stk_index="dfcf_fuquan_kdj_reg_add_mv_avg"
file_name=$stk_index
f1=${save_dir}${file_name}.csv

## run hive to export data
spark-sql \
    --executor-memory   5G \
    --driver-memory     5G \
    --conf spark.sql.autoBroadcastJoinThreshold=-1 \
    --conf spark.shuffle.file.buffer=64K \
    --conf spark.driver.maxResultSize=4g \
    --conf spark.serializer=org.apache.spark.serializer.KryoSerializer \
    --conf spark.dynamicAllocation.enabled=true \
    --conf spark.shuffle.service.enabled=true \
    -e "
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
case when t1.slopes<-0.14  then 0
    when t1.slopes>=-0.14 and t1.slopes<=0.14 then 1
    when t1.slopes>=0.14 then 2
    else null end as slope3,
rsi_6,rsi_12,rsi_24,kdjk,
kdjd,kdjj,macdh,
boll_ub,boll_lb,round(boll_ub/boll_lb,3) as boll_ratio,
mv_avg_3_5,
mv_avg_3_8,
mv_avg_3_13,
mv_avg_5_8,
close_mvavg3,
close_mvavg5,
close_mvavg8,
close_mvavg13,
close_mvavg21,
high_mvavg3,
high_mvavg5,
high_mvavg8,
high_mvavg13,
high_mvavg21,
low_mvavg3,
low_mvavg5,
low_mvavg8,
low_mvavg13,
low_mvavg21,
open_mvavg5,
open_mvavg8,
open_mvavg13,
open_mvavg21
from 
(
    select * from 
    dfcf_fuquan_roll_reg 
    where stock_index is not null and slope_num_in=days_default and days_default=5
    and dt>='2017-01-01'
) t1
left join 
(
    select * from dfcf_fuquan_kdj
    where stock_date>='2017-01-01' 
) t2
on lpad(t1.stock_index,6,'0') = lpad(t2.stock_index,6,'0') and t1.dt = t2.stock_date
left join 
(   
    select * from dfcf_fuquan_mv_avg_feature
    where stock_date>='2017-01-01'
) t3
on lpad(t1.stock_index,6,'0') = t3.stock_index and t1.dt = t3.stock_date
inner join
(
    select distinct stock_index_raw as stock_index,dt
    from stock_dev.baostock_byyear 
    where tradestatus=1 and year>=2017 and stock_index_raw in (select stock_index from stock_dev.sample_stock_index)
) t4
on lpad(t1.stock_index,6,'0') = t4.stock_index and t1.dt = t4.dt
;
" \
| sed 's/[\t]/\t/g' > $f1
