select jijin_name,count(jijin_name) as cnt
from
stock_dev.jijin
where stock_date = "2020-09-30"
group by jijin_name
order by cnt desc
limit 30
;


select t1.*,t2.name
from
stock_dev.jijin t1
left join
stock.stock_index t2
on t1.stock_index = t2.code
where t1.stock_date in ('2020-09-30','2020-06-30','2020-03-31','2019-12-31','2019-09-30','2019-06-30')
and jijin_name like '%农银汇理%'
order by stock_date 
;



select jijin_name,
concat_ws(',',collect_set(t2.name)) as stock_name_list
from 
stock_dev.jijin t1
left join
stock.stock_index t2
on t1.stock_index = t2.code
where stock_date = '2020-09-30' and jijin_name like '%指数增强%'
group by jijin_name
limit 100
;

select t2.name,t2.code,
count(distinct jijin_name) as jijin_cnt
from
stock_dev.jijin t1
left join
stock.stock_index t2
on t1.stock_index = t2.code
where stock_date = '2020-09-30' and jijin_name like '%指数增强%'
group by t2.name,t2.code
order by count(distinct jijin_name) desc
limit 50
;


select t2.name,t2.code,
count(distinct jijin_name) as jijin_cnt
from
stock_dev.jijin t1
left join
stock.stock_index t2
on t1.stock_index = t2.code
where stock_date = '2020-06-30' 
group by t2.name,t2.code
order by count(distinct jijin_name) desc
limit 50
;



select t2.name,t2.code,
concat_ws(',',collect_set(jijin_name)) as jj_name_list
from
stock_dev.jijin t1
left join
stock.stock_index t2
on t1.stock_index = t2.code
where stock_date = '2020-09-30' and t1.stock_index='002271'
group by t2.name,t2.code
limit 50
;









