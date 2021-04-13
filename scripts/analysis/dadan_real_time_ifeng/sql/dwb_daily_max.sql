drop table if exists stock_dws.dadan_realtime_daily_max;
create table stock_dws.dadan_realtime_daily_max as
select t1.*,t2.price 
from 
(
    select
    stock_index,stock_name,dt,max(trade_money_wan) as daily_max_money
    from stock_dev.dadan_real_time_ifeng
    group by 1,2,3
    
) t1
inner join
(
    select
    stock_index,stock_name,dt,price,trade_money_wan
    from stock_dev.dadan_real_time_ifeng
    
) t2
on t1.stock_index=t2.stock_index and t1.stock_name=t2.stock_name and t1.dt=t2.dt and t1.daily_max_money=t2.trade_money_wan
;




drop table if exists stock_dws.dadan_realtime_period_max;
create table stock_dws.dadan_realtime_period_max as 
select * from
(
    select 
    stock_index,stock_name,dt,
    max(dt) over(partition by stock_index,stock_name ) as max_dt,
    max(daily_max_money) over(partition by stock_index,stock_name ORDER BY dt desc) as money_max_today,
    max(daily_max_money) over(partition by stock_index,stock_name ORDER BY dt desc ROWS BETWEEN 1 following AND 6 following) as money_max_5,
    max(daily_max_money) over(partition by stock_index,stock_name ORDER BY dt desc ROWS BETWEEN 1 following AND 8 following) as money_max_7,
    max(daily_max_money) over(partition by stock_index,stock_name ORDER BY dt desc ROWS BETWEEN 1 following AND 15 following) as money_max_14,
    max(daily_max_money) over(partition by stock_index,stock_name ORDER BY dt desc ROWS BETWEEN 1 following AND 31 following) as money_max_30,
    max(daily_max_money) over(partition by stock_index,stock_name ORDER BY dt desc ROWS BETWEEN 1 following AND 61 following) as money_max_60
    from
    (
        select 
        stock_index,stock_name,dt,daily_max_money
        from stock_dws.dadan_realtime_daily_max
        where dt>=to_date(date_sub(now(),60)) and dt <=now()
        
    )
    
)
where  dt>=to_date(date_sub(now(),7)) and dt <=now()
;







select t1.*,t2.period_max_trade_money
from 
(
select stock_index,stock_name,max(trade_money_wan) today_max
from 
stock_dev.dadan_real_time_ifeng
where dt='2021-03-12'
group by 1,2
) t1
inner join 
stock_dws.dadan_realtime_daily_max t2
on t1.stock_index=t2.stock_index and t1.stock_name=t2.stock_name 
and t1.today_max>t2.period_max_trade_money
limit 50
;


