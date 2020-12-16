
use stock_dt;
drop table if exists gainian;

create table  if not exists gainian(
	id	int	comment	'id',
	stock_index	int	comment	'stock_index',
	stock_name	string	comment	'stock_name',
	gainian	string	comment	'gainian',
	stock_date	string	comment	'stock_date'

)
comment 'gainian' 
row format delimited
fields terminated by ','
stored as PARQUET;
    
