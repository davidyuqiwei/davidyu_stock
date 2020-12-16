
use stock_dev;
drop table if exists important_owner;

create table  if not exists important_owner(
	id	int	comment	'id',
	id2	decimal(38,2)	comment	'id2',
	owner_name	string	comment	'owner_name',
	owner_type	string	comment	'owner_type',
	stock_type	string	comment	'stock_type',
	gudong_rank	decimal(38,2)	comment	'gudong_rank',
	stock_index	int	comment	'stock_index',
	stock_name	string	comment	'stock_name',
	change_date	string	comment	'change_date',
	num	decimal(38,2)	comment	'num',
	chigu_ratio	decimal(38,2)	comment	'chigu_ratio',
	liutong_ratio	decimal(38,2)	comment	'liutong_ratio',
	report_date	string	comment	'report_date',
	change_type	string	comment	'change_type',
	change_ratio	string	comment	'change_ratio',
	test1	int	comment	'test1',
	test2	decimal(38,2)	comment	'test2',
	num_change	decimal(38,2) comment	'num_change',
	stock_date	string	comment	'stock_date'
)
comment 'important_owner' 
row format delimited
fields terminated by ','
stored as PARQUET;
    
