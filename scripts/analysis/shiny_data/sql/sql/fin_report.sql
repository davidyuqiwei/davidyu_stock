select 
x1 as dt,
x3 as meigushouyi,
x11 as meiguweifenpeilirun,
x15 as zhuyingyewulirunlv,
x24 as maolirun,
x28 as guxifafanglv,
x30 as zhuyingyewulirun,
x32 as jinzichanshouyilv,
x36 as jinglirunzengzhanglv,
x67 as zichanfuzhailv,
x94 as stock_index
from 
stock_dev.fin_report 
where x1 >= '2008-01-01' and  substr(x1,1,1)='2'
order by x1
;
