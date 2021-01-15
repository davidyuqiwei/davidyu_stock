drop table if exists stock_raw.baostock;
create table stock_raw.baostock as
select t1.*,
stock_date as dt
from
(
select distinct
stock_date,
substr(code,4,9) as stock_index,
open,
high,
low,
close,
volume,
turn,
amount,
tradestatus,
pctchg,
pettm,
pbmrq,
psttm,
pcfncfttm,
isst
from 
stock_dev.baostock_tmp
) t1
;
