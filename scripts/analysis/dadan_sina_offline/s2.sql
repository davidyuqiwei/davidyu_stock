-- 当天主力流入排行
select stock_name,stock_index, 
avg_price*zhuli_buy_vol as zhuli_money
from stock_dev.dadan_sina 
where stock_date = "2020_07_31"
order by zhuli_money desc 
limit 30
;


--


