select 
x1 as dt,
x3 as meigushouyi,
x11 as meiguweifenpeilirun,
x15 as zhuyingyewulirunlv,
x28 as guxifafanglv,
x30 as zhuyingyewulirun,
x36 as jinglirunzengzhanglv,
x67 as zichanfuzhailv,
x94 as stock_index
from 
stock_dev.fin_report 
where x1 >= '2018-01-01'
order by x1
;
