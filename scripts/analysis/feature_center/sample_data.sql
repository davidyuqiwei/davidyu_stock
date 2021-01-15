drop table if exists stock_dev.sample_stock_index;
create table stock_dev.sample_stock_index as 
select lpad(stock_index,6,'0') as stock_index
from
(
    select stock_index_raw as stock_index,sum(amount)
    from stock_dev.baostock_byyear
    where dt>='2020-06-30' and dt<='2020-12-01' and substr(stock_index_raw,1,2) <>'30'
    group by stock_index_raw
    order by sum(amount) desc
    limit 1000
    
)
order by rand()
limit 300
;

