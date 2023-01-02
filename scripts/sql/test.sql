
use stock_dev;
drop table if exists bankuai;

create table  if not exists bankuai(
	bk_en	string	comment	'bk_en',
	bankuai	string	comment	'bankuai',
	company_no	string	comment	'公司家数',
	avg_price	string	comment	'平均价格',
	zhangdiee	string	comment	'涨跌额',
	zhangdiefu	string	comment	'涨跌幅',
	total_vol	string	comment	'总成交量',
	total_money	string	comment	'总成交额',
	stock_index	string	comment	'stock_index',
	zhangdiefu_top	string	comment	'领涨股涨跌幅',
	curr_price	string	comment	'领涨股当前价',
	zhangdiee_top	string	comment	'领涨股涨跌额',
	top_stock_name	string	comment	'领涨股',
	top_stock_index	string	comment	'领涨股_stock_index',
	day	string	comment	'day',
	stock_date	string	comment	'stock_date'

)
comment 'bankuai' 
row format delimited
fields terminated by ','
stored as PARQUET;
    
