drop table stock_test.sample_predNextDayLow;
create table stock_test.sample_predNextDayLow as 
select a.stock_date as today,
b.stock_date as next_day,
a.stock_index,
a.low*a.adj_close/a.close as today_low,
a.high*a.adj_close/a.close as today_high,
a.close*a.adj_close/a.close as today_close,
a.open*a.adj_close/a.close as today_open,
b.low*a.adj_close/a.close as next_low,
b.high*a.adj_close/a.close as next_high
from 
stock_dev.day_history_insert a 
left join
(
    select stock_date,stock_index,low,high
    from stock_dev.day_history_insert
) b
on a.stock_index = b.stock_index and datediff(b.stock_date,a.stock_date)=1
where b.stock_date is not null
order by rand()
limit 200000
;

--select datediff(stock_date,stock_date) from stock_dev.day_history_insert order by stock_date limit 10;
-- select count(*) from stock_test.stock_longterm_data;
