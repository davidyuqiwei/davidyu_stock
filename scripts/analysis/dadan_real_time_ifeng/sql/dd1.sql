
select stock_index,stock_name,
round(avg(trade_money_wan),1) as avg_trade_money,
round(std(trade_money_wan),1) as std_trade_money
from
stock_dev.dadan_real_time_ifeng
group by 1,2
limit 40
;



select t1.stock_index,t1.stock_name,t1.max_trade_money,
avg_trade_money,
round(t2.avg_trade_money+std_trade_money,1) as std_trade_money,
round(t2.avg_trade_money+2*std_trade_money,1) as std2_trade_money
from
(
select stock_index,stock_name,
max(trade_money_wan) as max_trade_money
from
stock_dev.dadan_real_time_ifeng
where dt=to_date(date_sub(now(),1))
group by 1,2
) t1
left join
(
select stock_index,stock_name,
round(avg(trade_money_wan),1) as avg_trade_money,
round(std(trade_money_wan),1) as std_trade_money
from
stock_dev.dadan_real_time_ifeng
group by 1,2
) t2
on t1.stock_index=t2.stock_index and t1.stock_name = t2.stock_name
limit 40
;

















