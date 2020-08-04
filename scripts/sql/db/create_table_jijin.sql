
use stock_dev;
drop table if exists jijin;

create table  if not exists jijin(
	jijin_name	string	comment	'基金名称',
	jijin_code	string	comment	'基金代码',
	chigu_num	int	comment	'持仓数量',
	liutong_ratio	decimal(38,2)	comment	'占流通股比例',
	chigu_money	decimal(38,2)	comment	'持股市值',
	jinzhi_ratio	decimal(38,2)	comment	'占净值比例',
	stock_date	string	comment	'stock_date',
	stock_index	int	comment	'stock_index'

)
comment 'jijin' 
row format delimited
fields terminated by ','
stored as PARQUET;
    
