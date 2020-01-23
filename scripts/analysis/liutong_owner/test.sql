select * 
from stock_dev.liutong_owner
where owner_name like '%全国社保%'
and dt='2019-09-30'
limit 10
;

--select distinct owner_name 
select owner_name,count(owner_name) as owner_name_cnt
from stock_dev.liutong_owner
where owner_name like '%全国社保%'
and dt='2019-09-30'
group by owner_name
limit 10
;

select * 
from stock_dev.liutong_owner
where owner_name like '%基本养老%'
and dt='2019-09-30'
limit 10
;

select concat_ws('_',collect_list(owner_name)),
concat_ws('_',collect_list(ratio)),
stock_index from
stock_dev.liutong_owner
where dt ='2019-09-30'
group by stock_index
limit 10
;





select a.stock_index,c.name,c.industry,
a.dt,a.ratio_sum
from 
(
select stock_index,dt,round(sum(ratio),3) as ratio_sum
from 
stock_dev.liutong_owner 
where owner_name like '%全国社保%'
and dt='2019-06-30'
group by stock_index,substr(owner_name,1,4),dt
) a 
left join
stock.stock_index c
on a.stock_index = c.code
order by ratio_sum desc
limit 10
;




--  基本养老, 全国社保
