select
stock_index,
stock_name,
sum(zhongdan_liuru) as zhongdan_liuru
from 
stock_dev.dadan_dfcf
where regexp_replace(stock_date,"_","-")>='2020-08-01'
and regexp_replace(stock_date,"_","-")<="2020-08-31"
and regexp_replace(stock_date,"_","-") in 
(select dt from stock_dw.stock_index_trade_date where
    dt>='2020-08-01' and dt<='2020-08-31')
group by stock_index,stock_name
order by sum(zhongdan_liuru) desc
limit 100
;
