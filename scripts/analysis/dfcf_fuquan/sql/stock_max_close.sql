create table stock_dw.stock_max_close as 
select lpad(stock_index,6,'0') as stock_index,max(close) as max_close
from
stock_dev.dfcf_fuquan_byyear
group by lpad(stock_index,6,'0')
;










