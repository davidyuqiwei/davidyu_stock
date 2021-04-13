
use stock_dt;
drop table if exists stock_liutong_shizhi;

create table  if not exists stock_liutong_shizhi(
	curr_capital	decimal(38,2)	comment	'curr_capital',
	trade	decimal(38,2)	comment	'trade',
	dt	string	comment	'dt',
	stock_index	int comment	'stock_index',
	liutong_capital	decimal(38,2)	comment	'liutong_capital'

)
comment 'stock_liutong_shizhi' 
row format delimited
fields terminated by ','
stored as textfile;
    
