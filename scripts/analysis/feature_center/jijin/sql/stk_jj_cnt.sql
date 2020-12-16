select 
a.stock_index,
'${jijin_date}' as jijin_date,
b.name,
a.cnt
from 
(
	select 
	stock_index,
	count(distinct jijin_code) as cnt
	from
	stock_dev.jijin
	where stock_date = '${jijin_date}'
	group by stock_index
) a
left join
stock_dt.stock_index b
on a.stock_index=b.code
order by a.cnt desc
;



