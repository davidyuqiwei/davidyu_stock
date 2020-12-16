
use stock_dev;
drop table if exists baostock_tmp;

create table  if not exists baostock_tmp(
	stock_date	string	comment	'date',
	code	string	comment	'code',
	open	decimal(38,2)	comment	'open',
	high	decimal(38,2)	comment	'high',
	low	decimal(38,2)	comment	'low',
	close	decimal(38,2)	comment	'close',
	volume	int	comment	'volume',
	turn	decimal(38,2)	comment	'turn',
	amount	decimal(38,2)	comment	'amount',
	tradestatus	int	comment	'tradestatus',
	pctChg	decimal(38,2)	comment	'pctChg',
	peTTM	decimal(38,2)	comment	'peTTM',
	pbMRQ	decimal(38,2)	comment	'pbMRQ',
	psTTM	decimal(38,2)	comment	'psTTM',
	pcfNcfTTM	decimal(38,2)	comment	'pcfNcfTTM',
	isST	int	comment	'isST'

)
comment 'baostock_tmp' 
row format delimited
fields terminated by ','
stored as PARQUET;
    
