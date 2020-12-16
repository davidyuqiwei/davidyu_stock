select stock_index,report_date,
owner_name,change_type,stock_name,
num,liutong_ratio,num_change,change_date
from
stock_dev.important_owner
where
substr(change_date,1,10) = "2020-03-31" and
(change_type = "增加" or change_type = "新进")
and owner_name like '%香港%'
;


