
use stock_dev;
drop table if exists gainian_bankuai;

create table  if not exists gainian_bankuai(
	id	int	comment	'id',
	stock_index	string	comment	'stock_index',
	stock_name	string	comment	'stock_name',
	gainian	string	comment	'gainian',
	stock_date	string	comment	'stock_date'

)
comment 'gainian_bankuai' 
row format delimited
fields terminated by ','
stored as PARQUET;
    
