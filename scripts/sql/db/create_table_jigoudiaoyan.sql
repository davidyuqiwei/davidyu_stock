
use stock_dev;
drop table if exists jigoudiaoyan;

create table  if not exists jigoudiaoyan(
	ChangePercent	decimal(38,2)	comment	'ChangePercent',
	Close	decimal(38,2)	comment	'Close',
	CompanyCode	decimal(38,2)	comment	'CompanyCode',
	CompanyName	string	comment	'CompanyName',
	OrgCode	decimal(38,2)	comment	'OrgCode',
	OrgName	string	comment	'OrgName',
	OrgSum	decimal(38,2)	comment	'OrgSum',
	SCode	decimal(38,2)	comment	'SCode',
	SName	string	comment	'SName',
	NoticeDate	string	comment	'NoticeDate',
	StartDate	string	comment	'StartDate',
	EndDate	decimal(38,2)	comment	'EndDate',
	Place	string	comment	'Place',
	Description	string	comment	'Description',
	Orgtype	decimal(38,2)	comment	'Orgtype',
	OrgtypeName	string	comment	'OrgtypeName',
	Personnel	decimal(38,2)	comment	'Personnel',
	Licostaff	string	comment	'Licostaff',
	Maincontent	decimal(38,2)	comment	'Maincontent',
	stock_date	string	comment	'date'
)
comment 'jigoudiaoyan' 
row format delimited
fields terminated by ','
stored as PARQUET;
    
