drop table if exists ${database}.${tgt_table};


select 
a.stock_index,
count(1) as cnt,
c.name
from stock_dev.liutong_owner a
left join
stock.stock_index c
on c.code = a.stock_index
where owner_name like '%全国社保%' and dt = '2019-09-30'
group by a.stock_index,c.name
order by cnt desc 
limit 10
;



select 
a.stock_index,
count(1) as cnt,
c.name,
c.industry
from stock_dev.liutong_owner a
left join
stock.stock_index c
on c.code = a.stock_index
where owner_name like '%基本养老保险%' and dt = '2019-09-30'
group by a.stock_index,c.name,c.industry
order by cnt desc 
limit 10
;

select 
a.stock_index,
count(1) as cnt,
c.name,
c.industry
from stock_dev.liutong_owner a
left join
stock.stock_index c
on c.code = a.stock_index
where owner_name like '%新华人寿%' and dt = '2020-03-31'
group by a.stock_index,c.name,c.industry
order by cnt desc 
limit 10
;



create table ${database}.${tgt_table} as
select
COALESCE(a.stock_index,b.stock_index) as stock_index,
COALESCE(c.name,d.name) as stock_name,
COALESCE(c.industry,d.industry) as industry,
a.ratio-b.ratio as ratio_change,
a.ratio as a_ratio,
b.ratio as b_ratio,
a.dt as start_date,
b.dt as end_date,
COALESCE(a.owner_name,b.owner_name) as owner_name
from
(
    select * from
    stock_dev.liutong_owner
    where dt ='${end_date}' and owner_name like '%${owner_name}%'
    
) a
full join
(
    select * from stock_dev.liutong_owner
    where dt ='${start_date}' and owner_name like '%${owner_name}%'
    
) b
on a.stock_index = b.stock_index and a.owner_name  = b.owner_name
left join
stock.stock_index c
on c.code = a.stock_index
left join
stock.stock_index d
on d.code = b.stock_index
order by ratio_change desc
;

