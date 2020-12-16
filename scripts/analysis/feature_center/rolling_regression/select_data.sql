select code as stock_index,close,stockdate as stock_date from 
stock_dev.baostock
where code = '${stock_index}'
;



