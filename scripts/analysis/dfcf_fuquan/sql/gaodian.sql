select t1.stock_index,new_close/max_close
from
(
    select lpad(stock_index,6,'0') as stock_index,close as new_close from
    stock_dev.dfcf_fuquan_byyear
    where stock_date='2021-01-06'
    
) t1
inner join stock_dw.stock_max_close t2
on t1.stock_index=t2.stock_index
where new_close/max_close >0.8 and new_close/max_close<1
order by new_close/max_close desc 
limit 30
;

