--select stock_index,stock_name from stock.stock_name;
select
stock_index,stock_name
from
stock_raw.dadan_dfcf
where
dt<=now() and dt>=to_date(date_sub(now(),30))
;

