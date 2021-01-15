
use stock_dev;
drop table if exists dfcf_fuquan;

create table  if not exists dfcf_fuquan(
	dt	string	comment	'dt',
	open	decimal(38,2)	comment	'open',
	close	decimal(38,2)	comment	'close',
	high	decimal(38,2)	comment	'high',
	low	decimal(38,2)	comment	'low',
	volume	decimal(38,2)	comment	'volume',
	money	decimal(38,2)	comment	'money',
	x1	decimal(38,2)	comment	'x1',
	x2	decimal(38,2)	comment	'x2',
	x3	decimal(38,2)	comment	'x3',
	x4	decimal(38,2)	comment	'x4',
	stock_date	string	comment	'stock_date',
	stock_index	int	comment	'stock_index'

)
comment 'dfcf_fuquan' 
row format delimited
fields terminated by ','
stored as PARQUET;
    
