
select tt1.*,tt1.jijin_cnt_dur2-tt1.jijin_cnt_dur1 as jijin_num_increase
from 
(
    select t2.name,t2.code,
    count(distinct case when stock_date='2020-09-30' then jijin_name else null end) as jijin_cnt_dur1,
    count(distinct case when stock_date='2020-12-31' then jijin_name else null end) as jijin_cnt_dur2
    from
    stock_dev.jijin t1
    left join
    stock.stock_index t2
    on t1.stock_index = t2.code
    where stock_date in ('2020-09-30','2020-12-31')
    group by t2.name,t2.code
) tt1
order by (tt1.jijin_cnt_dur2-tt1.jijin_cnt_dur1)/tt1.jijin_cnt_dur1 desc
limit 50
;

