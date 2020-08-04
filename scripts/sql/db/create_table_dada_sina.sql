use stock_dev;
drop table if exists dadan_sina;

create table  if not exists dadan_sina(
	stock_name	string	comment	'stock_name',
	stock_index	string	comment	'stock_index',
	detail	string	comment	'detail',
	total_trade_vol	decimal(38,2)	comment	'total_trade_vol',
	total_trade_vol_ratio	decimal(38,2)	comment	'total_trade_vol_ratio',
	total_trade_money	decimal(38,2)	comment	'total_trade_money',
	total_trade_money_ratio	decimal(38,2)	comment	'total_trade_money_ratio',
	avg_price	decimal(38,2)	comment	'avg_price',
	zhuli_buy_vol	decimal(38,2)	comment	'zhuli_buy_vol',
	zhongxing_vol	decimal(38,2)	comment	'zhongxing_vol',
	zhuli_sale_vol	decimal(38,2)	comment	'zhuli_sale_vol',
	date_time	string	comment	'date_time',
	stock_date	string	comment	'stock_date'

)
comment 'dadan_sina' 
row format delimited
fields terminated by ','
stored as PARQUET;
    
