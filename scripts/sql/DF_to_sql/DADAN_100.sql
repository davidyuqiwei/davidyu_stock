
use stock_test;
drop table if exists DADAN_100;

create table  if not exists DADAN_100(
	stock_index	int	comment	'stock_index',
	stock_name	string	comment	'stock_name',
	trade_time	string	comment	'trade_time',
	price	decimal(38,2)	comment	'price',
	trade_num	int	comment	'trade_num',
	trade_shou	int	comment	'trade_shou',
	status	string	comment	'status',
	price_change_rate	decimal(38,2)	comment	'price_change_rate',
	price_change_ratio	string	comment	'price_change_ratio',
	look	string	comment	'look',
	stock_date	string	comment	'stock_date'

)
comment 'DADAN_100' 
PARTITIONED BY ( day string comment '日期' )
row format delimited
fields terminated by '\001'
stored as textfile;
    
