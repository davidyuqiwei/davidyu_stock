select t1.*,t2.liutong_capital
from
(
    select
    stock_index,
    stock_name,
    chaodadan_liuru,
    dadan_liuru,
    zhuli_liuru
    zhongdan_liuru,
    xiaodan_liuru,
    dt
    from
    stock_raw.dadan_dfcf
    where 
    dt<="2020-12-31" and dt>="2020-04-01"
    and dt in
    (
        select dt from stock_dw.stock_index_trade_date where
        dt<='2020-12-31'
    )
) t1
inner join
(
    select stock_index,liutong_capital
    from
    stock_dt.stock_liutong_shizhi
    where liutong_capital > 100
) t2
on t1.stock_index=t2.stock_index
order by stock_index,dt
;

