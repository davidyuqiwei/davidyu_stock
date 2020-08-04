
use stock_dev;
drop table if exists dazongjiaoyi;

create table  if not exists dazongjiaoyi(
	TDATE	string	comment	'TDATE',
	SECUCODE    string	comment	'SECUCODE',
	SNAME	string	comment	'SNAME',
	PRICE	decimal(38,2)	comment	'PRICE',
	TVOL	decimal(38,2)	comment	'TVOL',
	TVAL	decimal(38,2)	comment	'TVAL',
	BUYERCODE	string	comment	'BUYERCODE',
	BUYERNAME	string	comment	'BUYERNAME',
	SALESCODE	string	comment	'SALESCODE',
	SALESNAME	string	comment	'SALESNAME',
	Stype	string	comment	'Stype',
	Unit	string	comment	'Unit',
	RCHANGE	decimal(38,2)	comment	'RCHANGE',
	CPRICE	decimal(38,2)	comment	'CPRICE',
	YSSLTAG	decimal(38,2)	comment	'YSSLTAG',
	Zyl	decimal(38,2)	comment	'Zyl',
	Cjeltszb	decimal(38,2)	comment	'Cjeltszb',
	RCHANGE1DC	string	comment	'RCHANGE1DC',
	RCHANGE5DC	string	comment	'RCHANGE5DC',
	RCHANGE10DC	string	comment	'RCHANGE10DC',
	RCHANGE20DC	string	comment	'RCHANGE20DC',
	TEXCH	string	comment	'TEXCH',
	stock_date	string	comment	'stock_date',
	day	string	comment	'day'

)
comment 'dazongjiaoyi' 
row format delimited
fields terminated by ','
stored as PARQUET;
    
