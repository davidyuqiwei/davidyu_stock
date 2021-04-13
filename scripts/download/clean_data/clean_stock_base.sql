drop table if exists stock.stock_name;
create table  stock.stock_name as 
select
distinct lpad(stock_index,6,'0') as stock_index,
stock_name,
from_unixtime(unix_timestamp(), 'yyyy-MM-dd HH:mm:ss') as update_time
from
stock_dev.dadan_dfcf
where stock_date>=to_date(date_sub(now(),7)) and stock_date<=to_date(date_sub(now(),1))
;
