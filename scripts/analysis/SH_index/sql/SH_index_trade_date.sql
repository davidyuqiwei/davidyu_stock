drop table if exists stock_dw.stock_index_trade_date;
create table stock_dw.stock_index_trade_date as 
select distinct stock_date,stock_date as dt,
from_unixtime(unix_timestamp(), 'yyyy-MM-dd HH:mm:ss') as update_time
from 
stock_dev.SH_index 
order by stock_date desc 
;

