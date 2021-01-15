select lpad(t1.stock_index,6,'0'),t1.dt,
t1.slopes,
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
t2.rsi_6,rsi_12,rsi_24,kdjk,
kdjd,kdjj,boll_ub,boll_lb,round(boll_ub/boll_lb,3)
from dfcf_fuquan_roll_reg t1
left join dfcf_fuquan_kdj t2
on lpad(t1.stock_index,6,'0') = lpad(t2.stock_index,6,'0') 
and t1.dt = t2.stock_date
where t1.stock_index is not null and t2.stock_date>'2020-01-01'
and slope_num_in=days_default
limit 100
;

