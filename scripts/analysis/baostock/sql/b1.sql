select t1.owner_name,
round(avg(slope),3) as avg_slope,
concat_ws(',',collect_set(t3.name)) as stock_name_list,
concat_ws(',',collect_set(t1.stock_index)) as stock_index_list
from 
stock_dev.liutong_owner t1
left join 
stock_test.stock_slope t2
on t1.stock_index = t2.stock_index
left join stock.stock_index t3
on t1.stock_index = t3.code
where t1.dt='2020-03-31' and slope <> -999 and slope <> 0 
group by t1.owner_name
having count(distinct t3.name) >=3
order by avg_slope desc
limit 100
;


select t1.jijin_name,
round(avg(slope),3) as avg_slope,
concat_ws(',',collect_set(t3.name)) as stock_name_list,
concat_ws(',',collect_set(t1.stock_index)) as stock_index_list
from 
stock_dev.jijin t1
left join 
stock_test.stock_slope t2
on t1.stock_index = t2.stock_index
left join stock.stock_index t3
on t1.stock_index = t3.code
where t1.stock_date='2020-03-31' and slope <> -999 and slope <> 0 
group by t1.jijin_name
having count(distinct t3.name) >=3
order by avg_slope desc
limit 100
;


select * from stock_dev.liutong_owner
where owner_name = '杨力' and dt='2020-09-30';


