use stock_dev;
drop table if exists dadan_DFCF;

create table  if not exists dadan_DFCF(
	new_price	float	comment	'new_price',
	today_increase_ratio	float   comment	'today_increase_ratio',
	stock_index	int	comment	'stock_index',
	stock_name	string	comment	'stock_name',
	zhuli_liuru	float	comment	'zhuli_liuru',
	chaodadan_liuru	float	comment	'chaodadan_liuru',
	chaodadan_liuru_ratio	float	comment	'chaodadan_liuru_ratio',
	dadan_liuru	float	comment	'dadan_liuru',
	dadan_liuru_ratio   float	comment	'dadan_liuru_ratio',
	zhongdan_liuru	float	comment	'zhongdan_liuru',
	zhongdan_liuru_ratio	float	comment	'zhongdan_liuru_ratio',
	xiaodan_liuru	float	comment	'xiaodan_liuru',
	xiaodan_liuru_ratio	float	comment	'xiaodan_liuru_ratio',
	test1	int	comment	'test1',
	zhuli_liuru_ratio	float	comment	'zhuli_liuru_ratio',
	test2	string	comment	'test2',
	test3	string	comment	'test3',
	test4	string	comment	'test4',
	stock_date	string	comment	'stock_date'

)
comment 'dadan_DFCF' 
row format delimited
fields terminated by ','
stored as PARQUET;
    
