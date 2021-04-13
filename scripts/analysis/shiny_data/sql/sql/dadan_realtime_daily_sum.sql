select stock_index,stock_name,dt,status,
sum(trade_money_wan) as money_sum
from stock_raw.dadan_real_time_ifeng
where dt>=to_date(date_sub(now(),60)) and dt <=now()
group by 1,2,3,4
order by dt desc 
;
