drop table if exists stock_dw.stock_index_trade_date;
create table stock_dw.stock_index_trade_date as
select stock_date,stock_date as dt,
row_number() over (order by stock_date desc) as row_num,
from_unixtime(unix_timestamp(), 'yyyy-MM-dd HH:mm:ss') as update_time
from 
(
    select distinct regexp_replace(stock_date,"_","-") as stock_date
    from
    stock_dev.SH_index
    union
    select distinct regexp_replace(stock_date,"_","-") as stock_date
    from stock_dev.dadan_dfcf
) t1
where stock_date <> 'date' and stock_date <> 'stock-date'
order by stock_date desc
;


