drop table if exists stock_raw.dadan_dfcf;
create table stock_raw.dadan_dfcf as
select distinct 
new_price,today_increase_ratio,
lpad(stock_index,6,'0') as stock_index ,
stock_name,zhuli_liuru,chaodadan_liuru,
chaodadan_liuru_ratio,dadan_liuru,dadan_liuru_ratio,zhongdan_liuru,zhongdan_liuru_ratio,xiaodan_liuru,
xiaodan_liuru_ratio,test1,zhuli_liuru_ratio,test2,test3,test4,
REPLACE(stock_date,'_','-') as stock_date,
REPLACE(stock_date,'_','-') as dt
from stock_dev.dadan_dfcf
;
