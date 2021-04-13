/*
sum on every minute
*/
drop table if exists stock_dws.dadan_realtime_daily_minute_sum;
create table stock_dws.dadan_realtime_daily_minute_sum as 
select
stock_index,stock_name,dt,status,
regexp_replace(substr(trade_time,1,5),":","") as trade_time,
sum(trade_money_wan) as money_sum,
avg(price) as avg_trade_price,
from_unixtime(unix_timestamp(), 'yyyy-MM-dd HH:mm:ss') as update_time
from stock_raw.dadan_real_time_ifeng
group by 1,2,3,4,5
;

/*
daily max minute trade
*/
drop table if exists stock_dws.dadan_realtime_daily_max_minute;
create table stock_dws.dadan_realtime_daily_max_minute as
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

/*
max trade on one time
*/

drop table if exists stock_dws.dadan_realtime_daily_max;
create table stock_dws.dadan_realtime_daily_max as
select t1.*,t2.price,
from_unixtime(unix_timestamp(), 'yyyy-MM-dd HH:mm:ss') as update_time
from
(
    select
    stock_index,stock_name,dt,status,max(trade_money_wan) as daily_max_money
    from stock_raw.dadan_real_time_ifeng
    group by 1,2,3,4

) t1
inner join
(
    select
    stock_index,stock_name,dt,price,trade_money_wan,status
    from stock_raw.dadan_real_time_ifeng

) t2
on t1.stock_index=t2.stock_index and t1.stock_name=t2.stock_name and t1.dt=t2.dt and t1.daily_max_money=t2.trade_money_wan
and t1.status=t2.status
;




drop table if exists stock_dws.dadan_realtime_period_max;
create table stock_dws.dadan_realtime_period_max as
select *,
from_unixtime(unix_timestamp(), 'yyyy-MM-dd HH:mm:ss') as update_time
from
(
    select
    stock_index,stock_name,dt,price,
    max(dt) over(partition by stock_index,stock_name,dt ) as max_dt,
    max(daily_max_money) over(partition by stock_index,stock_name,dt ORDER BY dt desc) as money_max_today,
    max(daily_max_money) over(partition by stock_index,stock_name ORDER BY dt desc ROWS BETWEEN 1 following AND 6 following) as money_max_5,
    max(daily_max_money) over(partition by stock_index,stock_name ORDER BY dt desc ROWS BETWEEN 1 following AND 8 following) as money_max_7,
    max(daily_max_money) over(partition by stock_index,stock_name ORDER BY dt desc ROWS BETWEEN 1 following AND 15 following) as money_max_14,
    max(daily_max_money) over(partition by stock_index,stock_name ORDER BY dt desc ROWS BETWEEN 1 following AND 31 following) as money_max_30,
    max(daily_max_money) over(partition by stock_index,stock_name ORDER BY dt desc ROWS BETWEEN 1 following AND 61 following) as money_max_60,
    count(daily_max_money) over(partition by stock_index,stock_name ORDER BY dt desc ROWS BETWEEN 1 following AND 6 following) as money_count_5,
    count(daily_max_money) over(partition by stock_index,stock_name ORDER BY dt desc ROWS BETWEEN 1 following AND 8 following) as money_count_7,
    count(daily_max_money) over(partition by stock_index,stock_name ORDER BY dt desc ROWS BETWEEN 1 following AND 15 following) as money_count_14,
    count(daily_max_money) over(partition by stock_index,stock_name ORDER BY dt desc ROWS BETWEEN 1 following AND 31 following) as money_count_30,
    count(daily_max_money) over(partition by stock_index,stock_name ORDER BY dt desc ROWS BETWEEN 1 following AND 61 following) as money_count_60
    from
    (
        select
        stock_index,stock_name,dt,daily_max_money,price
        from stock_dws.dadan_realtime_daily_max
        where dt>=to_date(date_sub(now(),60)) and dt <=now() and status="买盘"
    )

)
where  dt>=to_date(date_sub(now(),7)) and dt <=now()
;

