
use stock_test;
drop table if exists DADAN;

create table  if not exists DADAN(
	stock_index	int	comment	stock_index,
	stock_name	str	comment	stock_name,
	trade_time	str	comment	trade_time,
	price	decimal(38,2)	comment	price,
	trade_num	int	comment	trade_num,
	trade_shou	int	comment	trade_shou,
	status	str	comment	status,
	price_change_rate	decimal(38,2)	comment	price_change_rate,
	price_change_ratio	str	comment	price_change_ratio,
	look	str	comment	look

)
comment 'DADAN daily data' 
PARTITIONED BY ( day string comment '日期' )
row format delimited
fields terminated by '\001'
stored as textfile;
    
