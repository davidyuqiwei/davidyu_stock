drop table if exists stock_test.dadan_daily_sum;
create table stock_test.dadan_daily_sum as 
select stock_index,stock_name,dt,status,
sum(trade_money_wan) as money_sum
from stock_raw.dadan_real_time_ifeng
where dt>=to_date(date_sub(now(),60)) and dt <=now()
group by 1,2,3,4
;

drop table if exists stock_test.dadan_realtime_period_max;
create table stock_test.dadan_realtime_period_max as
select stock_index,stock_name,status,obs_dt,
max(case when 1_days is not null then money_sum else 0 end) as money_max_1,
max(case when 3_days is not null then money_sum else 0 end) as money_max_3,
max(case when 5_days is not null then money_sum else 0 end) as money_max_5,
max(case when 13_days is not null then money_sum else 0 end) as money_max_13,
max(case when 21_days is not null then money_sum else 0 end) as money_max_21,
max(case when 30_days is not null then money_sum else 0 end) as money_max_30
from
(

    select t1.*,t2.obs_dt as obs_dt,
    case when t2.row_num=1 then '1_days' end as 1_days,
    case when t2.row_num>=2 and t2.row_num<=3 then '3_days' end as 3_days,
    case when t2.row_num>=2 and t2.row_num<=5 then '5_days' end as 5_days,
    case when t2.row_num>=2 and t2.row_num<=13 then '13_days' end as 13_days,
    case when t2.row_num>=2 and t2.row_num<=21 then '21_days' end as 21_days,
    case when t2.row_num>=2 and t2.row_num<=30 then '30_days' end as 30_days
    from
    stock_test.dadan_daily_sum t1
    left join
    (
        select dt,row_number() over (order by stock_date desc) as row_num,
        max(dt) over (order by stock_date desc)  as obs_dt
        from
        stock_dw.stock_index_trade_date
        where dt<=to_date(now())
    ) t2
    on t1.dt=t2.dt
)
group by 1,2,3,4
;

-- drop table if exists stock_test.dadan_realtime_ticai_sig_change;
-- create table stock_test.dadan_realtime_ticai_sig_change as 
-- select t2.ticai,obs_dt,count(distinct t1.stock_index) as cnt,
-- concat_ws('_',collect_set(t1.stock_name)) as stock_name_list,
-- concat_ws('_',collect_set(t1.stock_index)) as stock_index_list
--  from 
-- (
--     select stock_index,stock_name,obs_dt,
--     max(case when status='买盘' then money_max_1 else 0 end) as buy1,
--     max(case when status='卖盘' then money_max_1 else 0 end) as sell1,
--     max(case when status='买盘' then money_max_30 else 0 end) as buy13
--     from stock_test.dadan_realtime_period_max
--     group by 1,2,3
--     having buy1>sell1 and buy1>buy13*1.5
-- ) t1
-- left join stock_dev.hexinticai t2
-- on t1.stock_index=t2.stock_index
-- group by 1,2
-- order by 3 desc 
-- limit 50
-- ; 



insert into table stock_test.dadan_realtime_ticai_sig_change 
select t2.ticai,obs_dt,count(distinct t1.stock_index) as cnt,
concat_ws('_',collect_set(t1.stock_name)) as stock_name_list,
concat_ws('_',collect_set(t1.stock_index)) as stock_index_list
 from 
(
    select stock_index,stock_name,obs_dt,
    max(case when status='买盘' then money_max_1 else 0 end) as buy1,
    max(case when status='卖盘' then money_max_1 else 0 end) as sell1,
    max(case when status='买盘' then money_max_30 else 0 end) as buy13
    from stock_test.dadan_realtime_period_max
    group by 1,2,3
    having buy1>sell1 and buy1>buy13*1.5
) t1
left join stock_dev.hexinticai t2
on t1.stock_index=t2.stock_index
group by 1,2
order by 3 desc 
limit 50
; 


