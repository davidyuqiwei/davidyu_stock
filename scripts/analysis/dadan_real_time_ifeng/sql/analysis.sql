select t1.stock_index,t1.stock_name,dt,price,money_max_today,money_max_5,money_max_7,money_max_30,
round(increase_ratio,2) as increase_ratio,
concat_ws('_',collect_set(t2.gainian)) as gainian_set
from 
(
    select
    stock_index,stock_name,dt,price,money_max_today,money_max_5,money_max_7,money_max_30,
    money_max_today/money_max_5 as increase_ratio
    from stock_dws.dadan_realtime_period_max
    where dt>=to_date(date_sub(now(),5)) and money_max_today/money_max_30>2
    
) t1
left join 
stock_dev.gainian t2
on t1.stock_index=t2.stock_index
group by 1,2,3,4,5,6,7,8,9
order by dt desc,money_max_today/money_max_30 desc
limit 30
;












select 
stock_index,stock_name,dt,price,money_max_today,money_max_5,money_max_7,money_max_30,
money_max_today/money_max_5 as increase_ratio
from stock_dws.dadan_realtime_period_max
where dt='2021-03-11' and money_max_today/money_max_30>2
order by money_max_today/money_max_30 desc
;



select
stock_index,stock_name,dt,price,money_max_today,money_max_5,money_max_7,money_max_30,
money_max_today/money_max_5 as increase_ratio
from stock_dws.dadan_realtime_period_max
where stock_index=2380
limit 100
;


