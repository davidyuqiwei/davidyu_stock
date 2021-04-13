
use stock_dev;
drop table if exists stock_volume_price_distr;

create table  if not exists stock_volume_price_distr(
	price	decimal(38,2)	comment	'price',
	vol	decimal(38,2)	comment	'vol',
	stock_index	string	comment	'stock_index',
	dt	string	comment	'dt'

)
comment 'volume_price_distr' 
row format delimited
fields terminated by ','
stored as PARQUET;
    
