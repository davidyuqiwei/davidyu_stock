select a.x94, 
avg(a.x1) as x1,avg(a.x2) as x2 from 
(
select x94,
case x1 when -9999 then NULL ELSE x1 end as x1,
case x2 when -9999 then NULL ELSE x2 end as x2
from stock_dev.fin_report
) a
group by a.x94;


select x3,x4,x5,x9 from stock_dev.fin_report
limit 10
;

select 
count(if(x3 >-999, x3, 0))
count(if(x3 >-999, x4, 0))
count(if(x3 >-999, x5, 0))
count(if(x3 >-999, x6, 0))
count(if(x3 >-999, x7, 0))
count(if(x3 >-999, x8, 0))
count(if(x3 >-999, x9, 0))
count(if(x3 >-999, x10, 0))
from stock_dev.fin_report
where x94 = '601398'
limit 10
;




