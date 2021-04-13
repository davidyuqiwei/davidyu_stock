
use stock_dev;
drop table if exists gainian;

create table  if not exists gainian(
	stock_index	string	comment	'stock_index',
	stock_name	string	comment	'stock_name',
	gainian	string	comment	'gainian'

)
comment 'gainian' 
row format delimited
fields terminated by ','
stored as PARQUET;
    
