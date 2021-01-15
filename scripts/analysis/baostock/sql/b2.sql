select t1.code,t2.name,sum(amount)
from stock_dev.baostock_byyear t1
left join
stock.stock_index t2
on substr(t1.code,4,7) = t2.code
where dates>='2020-09-30'
group by t1.code,t2.name
order by sum(amount) desc
limit 100 
;
