create table stock_test.stock_change_rate_20170101_20171231 as 
select a.stock_index,a.adj_close as start_close,b.adj_close as end_close,a.stock_date as start_date,
b.stock_date as end_date,
a.cnt,
round((b.adj_close-a.adj_close)/a.adj_close,2) as change_rate
from
(
    select stock_index,
    adj_close,stock_date,
    row_number() over (partition by stock_index order by stock_date ) rank,
    count(stock_index) over (partition by stock_index) cnt
    from stock_dev.day_history_insert
    where stock_date >= '2017-01-01' and stock_date <= '2017-12-31'
    
) a
left join
(
    select stock_index,
    adj_close,stock_date,
    row_number() over (partition by stock_index order by stock_date desc) rank_d
    from stock_dev.day_history_insert
    where stock_date >= '2017-01-01' and stock_date <= '2017-12-31'
    
) b
on a.stock_index = b.stock_index
where a.rank=1 and b.rank_d=1
;

