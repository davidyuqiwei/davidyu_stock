select stock_index,substr(trade_time,1,5),
stock_date,status,
sum(trade_num) as mint_trade_num,
sum(trade_shou) as mint_trade_shou,
avg(price) as avg_price
from stock_test.dadan_100 
where day>='2020-01-01'  and day <='2020-02-19'
and stock_index='601398'
group by stock_index,substr(trade_time,1,5),stock_date,status
order by mint_trade_num desc 
limit 50
;
