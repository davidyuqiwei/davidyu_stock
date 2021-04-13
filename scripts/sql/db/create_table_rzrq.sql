
use stock_dev;
drop table if exists stock_rzrq;

create table  if not exists stock_rzrq(
	dt	string	comment	'DATE',
	MARKET	string	comment	'MARKET',
	SCODE	decimal(38,2)	comment	'SCODE',
	SECNAME	string	comment	'SECNAME',
	RZYE	decimal(38,2)	comment	'RZYE',
	RQYL	decimal(38,2)	comment	'RQYL',
	RZRQYE	decimal(38,2)	comment	'RZRQYE',
	RQYE	decimal(38,2)	comment	'RQYE',
	RQMCL	decimal(38,2)	comment	'RQMCL',
	RZRQYECZ	decimal(38,2)	comment	'RZRQYECZ',
	RZMRE	decimal(38,2)	comment	'RZMRE',
	SZ	decimal(38,2)	comment	'SZ',
	RZYEZB	decimal(38,2)	comment	'RZYEZB',
	RZMRE3D	decimal(38,2)	comment	'RZMRE3D',
	RZMRE5D	decimal(38,2)	comment	'RZMRE5D',
	RZMRE10D	decimal(38,2)	comment	'RZMRE10D',
	RZCHE	decimal(38,2)	comment	'RZCHE',
	RZCHE3D	decimal(38,2)	comment	'RZCHE3D',
	RZCHE5D	decimal(38,2)	comment	'RZCHE5D',
	RZCHE10D	decimal(38,2)	comment	'RZCHE10D',
	RZJME	decimal(38,2)	comment	'RZJME',
	RZJME3D	decimal(38,2)	comment	'RZJME3D',
	RZJME5D	decimal(38,2)	comment	'RZJME5D',
	RZJME10D	decimal(38,2)	comment	'RZJME10D',
	RQMCL3D	decimal(38,2)	comment	'RQMCL3D',
	RQMCL5D	decimal(38,2)	comment	'RQMCL5D',
	RQMCL10D	decimal(38,2)	comment	'RQMCL10D',
	RQCHL	decimal(38,2)	comment	'RQCHL',
	RQCHL3D	decimal(38,2)	comment	'RQCHL3D',
	RQCHL5D	decimal(38,2)	comment	'RQCHL5D',
	RQCHL10D	decimal(38,2)	comment	'RQCHL10D',
	RQJMG	decimal(38,2)	comment	'RQJMG',
	RQJMG3D	decimal(38,2)	comment	'RQJMG3D',
	RQJMG5D	decimal(38,2)	comment	'RQJMG5D',
	RQJMG10D	decimal(38,2)	comment	'RQJMG10D',
	SPJ	decimal(38,2)	comment	'SPJ',
	ZDF	decimal(38,2)	comment	'ZDF',
	RCHANGE3DCP	decimal(38,2)	comment	'RCHANGE3DCP',
	RCHANGE5DCP	decimal(38,2)	comment	'RCHANGE5DCP',
	RCHANGE10DCP	decimal(38,2)	comment	'RCHANGE10DCP',
	KCB	decimal(38,2)	comment	'KCB',
	TRADE_MARKET_CODE	decimal(38,2)	comment	'TRADE_MARKET_CODE',
	TRADE_MARKET	string	comment	'TRADE_MARKET'

)
comment 'rongzirongquan' 
row format delimited
fields terminated by ','
stored as PARQUET;
    
