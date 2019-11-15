
use stock_test;
drop table if exists hk_dailiren_change;

create table  if not exists hk_dailiren_change(
	stock_index	int	comment	'stock_index',
	stock_name	string	comment	'stock_name',
	industry	string	comment	'industry',
	ratio_change	decimal(38,2)	comment	'ratio_change',
	start_ratio	decimal(38,2)	comment	'start_ratio',
	end_ratio	decimal(38,2)	comment	'end_ratio',
	start_date	string	comment	'start_date',
	end_date	string	comment	'end_date',
	owner_name	string	comment	'owner_name'

)
comment '香港代理人持股变化' 
PARTITIONED BY ( day string comment '日期' )
row format delimited
fields terminated by '\001'
stored as textfile;
    
