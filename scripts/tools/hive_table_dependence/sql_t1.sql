select t1.*,t2.avg_trade_price,
from_unixtime(unix_timestamp(), 'yyyy-MM-dd HH:mm:ss') as update_time
from
(
    select
    stock_index,stock_name,dt,status,max(money_sum) as daily_max_money
    from stock_dws.dadan_realtime_daily_minute_sum
    group by 1,2,3,4

) t1
inner join
(
    select
    stock_index,stock_name,dt,avg_trade_price,money_sum,status
    from stock_dws.dadan_realtime_daily_minute_sum

) t2
on t1.stock_index=t2.stock_index and t1.stock_name=t2.stock_name and t1.dt=t2.dt and t1.daily_max_money=t2.money_sum
and t1.status=t2.status
;


