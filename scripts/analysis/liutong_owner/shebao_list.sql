select owner_name,count(owner_name) as owner_name_cnt,
concat_ws(',',collect_set(t2.name)) as owner_list
from stock_dev.liutong_owner t1
left join stock.stock_index t2
on t1.stock_index = t2.code
where owner_name like '%全国社保%' and dt='2020-06-30'
group by owner_name
order by count(owner_name) desc
;


select stock_index,count(distinct owner_name) as owner_name_cnt,
t2.name
from stock_dev.liutong_owner t1
left join stock.stock_index t2
on t1.stock_index = t2.code
where owner_name like '%全国社保%' and dt='2020-09-30'
group by t1.stock_index,t2.name
having owner_name_cnt >=2
order by owner_name_cnt desc
;

select owner_name,dt,count(1) as cnt
from stock_dev.liutong_owner
where owner_name like '%全国社保基金四一三组合%'
group by owner_name,dt
order by dt desc
limit 10;

select owner_name,dt,count(1) as cnt,
concat_ws(',',collect_list(t2.name)) as ratio_list
from stock_dev.liutong_owner t1
left join 
stock.stock_index t2
on t1.stock_index = t2.code
where owner_name like '%养老金%' and dt>='2020-09-30'
group by owner_name,dt
order by count(1) desc
limit 100;

select owner_name,dt,count(1) as cnt,
concat_ws(',',collect_list(t2.name)) as ratio_list,
concat_ws(',',collect_list(t1.stock_index)) as stock_index_list
from stock_dev.liutong_owner t1
left join 
stock.stock_index t2
on t1.stock_index = t2.code
where owner_name like '%NOMURA%' and dt>='2020-09-30'
group by owner_name,dt
order by count(1) desc
limit 100;













select stock_index,t2.name,sum(ratio) as ratio_sum
from stock_dev.liutong_owner t1
left join 
stock.stock_index t2 
on t1.stock_index = t2.code
where dt='2020-09-30'
group by stock_index,t2.name
order by sum(ratio) desc
limit 50
;



















