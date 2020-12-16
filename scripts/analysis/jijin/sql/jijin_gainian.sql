
select 
distinct 
t1.jijin_name,
t1.stock_index,
t2.gainian,
t3.name
from 
stock_dev.jijin t1
left join
stock_dev.gainian_bankuai t2
on t1.stock_index=t2.stock_index
left join stock.stock_index t3
on t1.stock_index = t3.code
where t1.stock_date='2020-03-31' 
limit 10
;


select gainian,count(1) as gainian_cnt
from
(
    select
    distinct
    t1.jijin_name,
    t1.stock_index,
    t2.gainian,
    t3.name
    from
    stock_dev.jijin t1
    left join
    stock_dev.gainian_bankuai t2
    on t1.stock_index=t2.stock_index
    left join stock.stock_index t3
    on t1.stock_index = t3.code
    where t1.stock_date='2020-06-30'
    
) a 
group by gainian
order by count(1)  desc
limit 30
;



select gainian,count(distinct jijin_name) as jijin_cnt
from
(
    select
    distinct
    t1.jijin_name,
    t1.stock_index,
    t2.gainian,
    t3.name
    from
    stock_dev.jijin t1
    left join
    stock_dev.gainian_bankuai t2
    on t1.stock_index=t2.stock_index
    left join stock.stock_index t3
    on t1.stock_index = t3.code
    where t1.stock_date='2020-06-30'
    
) a 
group by gainian
order by count(distinct jijin_name)  desc
limit 30
;


select * from
stock_dev.gainian_bankuai
where gainian='养老金'
limit 100
;





