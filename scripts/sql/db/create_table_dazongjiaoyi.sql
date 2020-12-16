
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
    


--tdate   string  TDATE
--secucode    string  SECUCODE
--sname   string  SNAME
--price   decimal(38,2)   PRICE  "成交价"
--tvol    decimal(38,2)   TVOL   "成交量"
--tval    decimal(38,2)   TVAL   "成交额"
--buyercode   string  BUYERCODE  "买方代码"
--buyername   string  BUYERNAME  "买方名字"
--salescode   string  SALESCODE  "卖方代码"
--salesname   string  SALESNAME  "卖房名字"
--stype   string  Stype
--unit    string  Unit
--rchange decimal(38,2)   RCHANGE  "涨跌幅"
--cprice  decimal(38,2)   CPRICE   "收盘价"
--yssltag decimal(38,2)   YSSLTAG
--zyl decimal(38,2)   zyl          "折益率"
--cjeltszb    decimal(38,2)   Cjeltszb
--rchange1dc  string  RCHANGE1DC
--rchange5dc  string  RCHANGE5DC
--rchange10dc string  RCHANGE10DC
--rchange20dc string  RCHANGE20DC
--texch   string  TEXCH
--stock_date  string  stock_date

