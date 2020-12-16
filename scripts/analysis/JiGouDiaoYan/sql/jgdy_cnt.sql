-- get stock index,name, diaoyan_cnt,date
select scode as stock_index,
sname as stock_name,
noticedate as diaoyan_date,
count(sname) as dy_cnt 
from
(
    select distinct * from
    stock_dev.jigoudiaoyan
    where noticedate>='${start_date}' and noticedate<='${end_date}'
    
)
group by scode,sname,noticedate
order by count(sname) desc
;
