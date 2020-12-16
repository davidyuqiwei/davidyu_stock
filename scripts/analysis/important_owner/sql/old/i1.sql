select owner_name,change_type,stock_index,stock_name,
num,liutong_ratio,num_change
from 
stock_dev.important_owner
where
substr(report_date,1,10) = "2020-08-19" and 
(change_type = "增加" or change_type = "新进")
limit 10
;




select owner_name,change_type,stock_index,stock_name,
num,liutong_ratio,num_change,change_date,report_date
from
stock_dev.important_owner
where
substr(change_date,1,10) = "2020-03-31" and
(change_type = "增加" or change_type = "新进")
and owner_name like '%香港%'
limit 10
;



