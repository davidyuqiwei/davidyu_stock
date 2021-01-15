select 
t1.stock_index,
t1.stock_name,
chaodadan_liuru/liutong_capital
from 
(
    select
    stock_index,
    stock_name,
    sum(chaodadan_liuru) as chaodadan_liuru
    from
    stock_dev.dadan_dfcf
    where regexp_replace(stock_date,"_","-")>='2020-12-01'
    and regexp_replace(stock_date,"_","-")<="2020-12-31"
    and regexp_replace(stock_date,"_","-") in
    (
        select dt from stock_dw.stock_index_trade_date where
        dt>='2020-12-01' and dt<='2020-12-31'
        
    )
    group by stock_index,stock_name
) t1
inner join
(
    select stock_index,liutong_capital
    from
    stock_dt.stock_liutong_shizhi
    where liutong_capital > 300
) t2
on t1.stock_index=lpad(t2.stock_index,6,'0')
order by chaodadan_liuru/liutong_capital desc 
limit 50 
;
