select jijin_name,
concat_ws('_',collect_set(t2.name)) as stock_name_list,
concat_ws('_',collect_set(t2.code)) as stock_name_list
from
(
    select jijin_name,lpad(stock_index,6,'0') as stock_index
    from stock_dev.jijin
    where stock_date = '2020-12-31'
    and jijin_name like '%高股息%'

) t1
left join
stock.stock_index t2
on t1.stock_index = lpad(t2.code,6,'0')
group by jijin_name
;

