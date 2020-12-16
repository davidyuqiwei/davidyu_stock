drop table if exists stock_raw.sh_index;
create table stock_raw.sh_index as
select t1.*,
'sh_index' as stock_index,
stock_date as dt
from
(
select distinct
stock_date,
open,
high,
low,
close,
volume,
adj_close
from 
stock_dev.sh_index
) t1
;
