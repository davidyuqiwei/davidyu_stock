
use stock_dev;
drop table if exists baostock;

create table  if not exists baostock(
	stock_index	string	comment	'stock_index',
	dt	string	comment	'dt',
	open	decimal(38,2)	comment	'open',
	high	decimal(38,2)	comment	'high',
	close	decimal(38,2)	comment	'close',
	low	decimal(38,2)	comment	'low',
	volume	int	comment	'volume'

)
comment 'baostock' 
row format delimited
fields terminated by ','
stored as PARQUET;
    
