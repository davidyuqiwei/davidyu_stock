
use stock_test;
drop table if exists stock_slope;

create table  if not exists stock_slope(
	stock_index	string	comment	'stock_index',
	start_date	string	comment	'start_date',
	end_date	string	comment	'end_date',
	pred_days	int	comment	'pred_days',
	slope	float	comment	'slope'

)
comment 'stock_slope' 
row format delimited
fields terminated by ','
stored as textfile;


load data local inpath '/home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/baostock/slope.txt' into table stock_test.stock_slope;

