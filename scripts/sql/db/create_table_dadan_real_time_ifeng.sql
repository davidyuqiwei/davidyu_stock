
use stock_dev;
drop table if exists dadan_real_time_ifeng;

create table  if not exists dadan_real_time_ifeng(
	stock_index	int	comment	'stock_index',
	stock_name	string	comment	'stock_name',
	trade_time	string	comment	'trade_time',
	price	decimal(38,2)	comment	'price',
	trade_money_wan	int	comment	'trade_money_wan',
	trade_shou	int	comment	'trade_shou',
	status	string	comment	'status',
	price_change_rate	decimal(38,2)	comment	'price_change_rate',
	price_change_ratio	string	comment	'price_change_ratio',
	look	string	comment	'look',
	dt	string	comment	'date'

)
comment 'dadan_real_time_ifeng' 
row format delimited
fields terminated by ','
stored as PARQUET;
    
