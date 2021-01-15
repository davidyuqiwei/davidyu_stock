use stock_dev;


select  t1.stock_index,
round((t1.x3-t2.x3)/t2.x3,3) as pe_increase_ratio
from
(
select 
x94 as stock_index,
x1,
x3,x4,x5 
from fin_report 
where x1 ='2020-09-30'
) t1
inner join
(
select 
x94 as stock_index,
x1,
x3,x4,x5 
from fin_report 
where x1 ='2019-09-30'
) t2
on t1.stock_index = t2.stock_index
order by round((t1.x3-t2.x3)/t2.x3,3) desc 
limit 30;

select 
x2,
x94 as stock_index,
x1,
x3,x4,x5 
from stock_dev.fin_report t1
where x1 ='2020-09-30'
and x94='601318'
;

