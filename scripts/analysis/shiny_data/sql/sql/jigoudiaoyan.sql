select
scode as stock_index,
sname as stock_name,
noticedate,
count(distinct orgname) as dy_cnt,
concat_ws('_' , collect_set(regexp_replace(orgname,",","_"))) as companyname_list
--concat_ws('_' , collect_set(noticedate)) as dy_date
from
(
    select distinct * from
    stock_dev.jigoudiaoyan
    where noticedate>date_sub(now(),60)
                
)
group by 1,2,3
order by noticedate desc,dy_cnt desc
;
