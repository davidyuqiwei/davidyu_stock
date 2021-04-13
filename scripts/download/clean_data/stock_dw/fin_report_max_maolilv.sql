create table stock_dw.fin_report_max_maolilv as
select t1.dt,t1.x94 as stock_index,t2.stock_name,
t1.maolilv 
from 
(
    select x1 as dt,x94,x24 as maolilv
    from
    stock_dev.fin_report
    where x1='2019-06-30'
) t1
left join stock.stock_name t2
on t1.x94=t2.stock_index 
;

