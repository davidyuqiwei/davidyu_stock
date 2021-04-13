select t1.*,t2.new_close as close
from
(
    select dt,lpad(cast(scode as string),6,'0') as stock_index,
    rzmre,rzye,rqye,rzrqye 
    from stock_dev.stock_rzrq 
    where scode=601398
) t1
left join 
(
    select lpad(stock_index,6,'0') as stock_index,
    close as new_close,
    stock_date
    from
    stock_dev.dfcf_fuquan_byyear
    where lpad(stock_index,6,'0')='601398'
) t2
on t1.stock_index=t2.stock_index and to_date(t1.dt)=to_date(t2.stock_date)
where dt>'2018-09-30'
order by dt
;


