select a.x94, 
avg(a.x1) as x1,avg(a.x2) as x2 from 
(
select x94,
case x1 when -9999 then NULL ELSE x1 end as x1,
case x2 when -9999 then NULL ELSE x2 end as x2
from stock_dev.fin_report
) a
group by a.x94;
