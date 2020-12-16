select 
scode,
sname,
count(sname) as dy_cnt,
concat_ws('__' , collect_set(orgname)) as companyname_list
from
(
    select distinct * from 
    stock_dev.jigoudiaoyan
    where noticedate='${today_date}'
)
group by scode,sname
;
