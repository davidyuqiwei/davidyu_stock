drop table if exists stock_raw.dazongjiaoyi;
create table stock_raw.dazongjiaoyi as
select distinct 
TDATE,
SECUCODE as stock_index,
SNAME as stock_name,
PRICE as price,
TVOL as total_volume,
TVAL as total_money,
BUYERCODE as buyercode,
BUYERNAME as buyername,
SALESCODE as salecode,
SALESNAME as salename,
Stype,Unit,
RCHANGE,CPRICE,YSSLTAG,Zyl,Cjeltszb,RCHANGE1DC,RCHANGE5DC,RCHANGE10DC,RCHANGE20DC,TEXCH,
stock_date,
substr(TDATE,1,10) as dt,
from_unixtime(unix_timestamp(), 'yyyy-MM-dd HH:mm:ss') as update_time
from stock_dev.dazongjiaoyi
;

