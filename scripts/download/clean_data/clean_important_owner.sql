drop table if exists stock_raw.important_owner;
create table stock_raw.important_owner as
select distinct
lpad(stock_index,6,'0') as stock_index,
stock_name,
substr(report_date,1,10) as report_date,
substr(change_date,1,10) as change_date,
gudong_rank,stock_type,
owner_name,change_type,
change_ratio,
num,liutong_ratio,chigu_ratio,
num_change,
substr(report_date,1,10) as dt,
from_unixtime(unix_timestamp(), 'yyyy-MM-dd HH:mm:ss') as update_time
from
stock_dev.important_owner
;

