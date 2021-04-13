
use stock_dev;
drop table if exists all_owner_dfcf;

create table  if not exists all_owner_dfcf(
	gudong_name	string	comment	'gudong_name',
	gudong_type	string	comment	'gudong_type',
	rank	decimal(38,2)	comment	'rank',
	stock_index	string	comment	'stock_index',
	stock_name	string	comment	'stock_name',
	end_chigu_num_wan	decimal(38,2)	comment	'end_chigu_num_wan',
	ratio	decimal(38,2)	comment	'ratio',
	last_chigu_num_wan	decimal(38,2)	comment	'last_chigu_num_wan',
	change_type	string	comment	'change_type',
	change_num	string	comment	'change_num',
	report_date	string	comment	'report_date',
	end_date	string	comment	'end_date'

)
comment 'all_owner_dfcf' 
row format delimited
fields terminated by ','
stored as PARQUET;
    
