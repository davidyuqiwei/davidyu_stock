
use stock_dev;
drop table if exists yejiyuqi;

create table  if not exists yejiyuqi(
	stock_index	int	comment	'stock_index',
	stock_name	string	comment	'stock_name',
	yeji_predict	string	comment	'yeji_predict',
	yeji_abstract	string	comment	'yeji_abstract',
	profit_change_ratio	string	comment	'profit_change_ratio',
	profit_change	string	comment	'profit_change',
	stock_date	string	comment	'stock_date'

)
comment 'yejiyuqi' 
row format delimited
fields terminated by ','
stored as PARQUET;
    
