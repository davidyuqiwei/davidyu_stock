
use stock_test;
drop table if exists day_history_wangyi;

create table  if not exists day_history_wangyi(
	stock_date	string	comment	'stock_date',
	open	decimal(38,2)	comment	'open',
	high	decimal(38,2)	comment	'high',
	low	decimal(38,2)	comment	'low',
	close	decimal(38,2)	comment	'close',
	change_price	decimal(38,2)	comment	'change_price',
	change_ratio	decimal(38,2)	comment	'change_ratio',
	trade_num	string	comment	'trade_num',
	trade_price	string	comment	'trade_price',
	variatio	decimal(38,2)	comment	'variatio',
	turnover_rate	decimal(38,2)	comment	'turnover_rate'

)
comment '网易日交易数据' 
PARTITIONED BY ( day string comment '日期',owner_name string comment 'owner_name' )
row format delimited
fields terminated by '\001'
stored as textfile;
    
