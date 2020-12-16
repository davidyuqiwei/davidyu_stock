select 
a.stock_index,
c.name,
a.amount*b.close as total_money
from
(
    select
    owner_name,
    stock_index,
    amount,
    dt
    from stock_dev.liutong_owner
    where dt = '2020-03-31' and owner_name="香港中央结算有限公司"
    
) a
left join stock_dev.day_history_wangyi b
on a.stock_index=b.stock_index and a.dt=b.stock_date
left join stock_dt.stock_index c
on a.stock_index=c.code
order by a.amount*b.close desc
limit 50
;
