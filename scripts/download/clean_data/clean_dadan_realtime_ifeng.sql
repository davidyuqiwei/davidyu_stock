drop table if exists stock_raw.dadan_real_time_ifeng;
create table stock_raw.dadan_real_time_ifeng as
select distinct 
stock_index,     
stock_name,   
trade_time,    
price, 
trade_money_wan,
trade_shou,   
status,  
price_change_rate,     
price_change_ratio,     
dt        
from stock_dev.dadan_real_time_ifeng
where dt <> 'date'
;









