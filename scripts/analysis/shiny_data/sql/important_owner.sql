select distinct 
lpad(stock_index,6,'0') as stock_index,
stock_name,
substr(report_date,1,10) as report_date,
substr(change_date,1,10) as change_date,
owner_name,change_type
num,liutong_ratio,num_change
from
stock_dev.important_owner
where
substr(report_date,1,10) >= date_sub(to_date(now()),14) and
(change_type = "增加" or change_type = "新进")
order by liutong_ratio desc
;

