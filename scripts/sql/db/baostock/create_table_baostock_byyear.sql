
use stock_dev;
drop table if exists baostock_byyear;

create table  if not exists baostock_byyear(
	dates	string	comment	'date',
	code	string	comment	'code',
	open	decimal(38,2)	comment	'open',
	high	decimal(38,2)	comment	'high',
	low	decimal(38,2)	comment	'low',
	close	decimal(38,2)	comment	'close',
	volume	int	comment	'volume',
	amount	int	comment	'amount',
	turn	decimal(38,2)	comment	'turn',
	tradestatus	int	comment	'tradestatus',
	pctChg	decimal(38,2)	comment	'pctChg',
	peTTM	decimal(38,2)	comment	'peTTM',
	psTTM	decimal(38,2)	comment	'psTTM',
	pcfNcfTTM	decimal(38,2)	comment	'pcfNcfTTM',
	pbMRQ	decimal(38,2)	comment	'pbMRQ',
	isST	int	comment	'isST',
    stock_index_raw string comment 'stock_index_raw',
    dt	string	comment	'dt'
)
comment 'baostock' 
PARTITIONED BY ( year string comment 'year')
row format delimited
fields terminated by ','
stored as textfile;
    
