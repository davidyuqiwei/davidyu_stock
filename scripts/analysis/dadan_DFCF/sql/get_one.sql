select *
from stock_raw.dadan_dfcf
where 
stock_index = '${stock_index}'
order by REPLACE(stock_date,"_","-")
;
