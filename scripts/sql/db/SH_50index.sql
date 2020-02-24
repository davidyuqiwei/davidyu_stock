
use stock_test;
drop table if exists SH_50index;

create table  if not exists SH_50index(
	stock_date	string	comment	'stock_date',
	index_code	int	comment	'index_code',
	index_name	string	comment	'index_name',
	index_name_en	string	comment	'index_name_en',
	stock_index	int	comment	'stock_index',
	stock_name	string	comment	'stock_name',
	stock_name_en	string	comment	'stock_name_en',
	info	string	comment	'info'

)
comment 'SH_50index' 
PARTITIONED BY ( day string comment '日期' )
row format delimited
fields terminated by '\001'
stored as textfile;
    
