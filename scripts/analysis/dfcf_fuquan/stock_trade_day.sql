create table stock_dw.stock_trade_day as
select distinct stock_index_raw as stock_index,dt
from stock_dev.baostock_byyear 
where tradestatus=1 and year>=2017 and stock_index_raw in (select stock_index from stock_dev.sample_stock_index)
;
