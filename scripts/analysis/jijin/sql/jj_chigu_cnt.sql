select jijin_name,count(jijin_name) as cnt
from
stock_dev.jijin
where stock_date = "2020-06-30"
group by jijin_name
order by cnt 
limit 30
;


