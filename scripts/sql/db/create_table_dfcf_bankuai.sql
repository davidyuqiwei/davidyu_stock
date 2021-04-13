
use stock_dev;
drop table if exists dfcf_bankuai;

create table  if not exists dfcf_bankuai(
	x1	decimal(38,2)	comment	'x1',
	change_ratio	decimal(38,2)	comment	'change_ratio',
	bankuai_no	string	comment	'bankuai_no',
	bankuai_name	string	comment	'bankuai_name',
	x2	decimal(38,2)	comment	'x2',
	x3	decimal(38,2)	comment	'x3',
	x4	decimal(38,2)	comment	'x4',
	x5	decimal(38,2)	comment	'x5',
	x6	decimal(38,2)	comment	'x6',
	x7	decimal(38,2)	comment	'x7',
	x8	decimal(38,2)	comment	'x8',
	x9	decimal(38,2)	comment	'x9',
	x10	decimal(38,2)	comment	'x10',
	x11	int	comment	'x11',
	x12	decimal(38,2)	comment	'x12',
	lead_stock_name	string	comment	'lead_stock_name',
	lead_stock_index	int	comment	'lead_stock_index',
	x15	int	comment	'x15',
	dt	string	comment	'dt',
	data_type	string	comment	'data_type'

)
comment 'dfcf_bankuai' 
row format delimited
fields terminated by ','
stored as PARQUET;
    
