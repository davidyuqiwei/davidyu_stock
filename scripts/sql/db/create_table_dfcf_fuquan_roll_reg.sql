
use stock_dw;
drop table if exists dfcf_fuquan_roll_reg;

create table  if not exists dfcf_fuquan_roll_reg(
	dt	string	comment	'dt',
	stock_index	int	comment	'stock_index',
	slopes	decimal(38,2)	comment	'slopes',
	slope_num_in	int	comment	'slope_num_in',
	days_default	int	comment	'days_default'

)
comment 'dfcf_fuquan_roll_reg' 
row format delimited
fields terminated by ','
stored as PARQUET;
    
