-- ======================================================
-- script name : stock_change_interval.sql
--
-- Souce Table : stock_dev.day_history_insert
--
-- Target Table : stock_test.stock_change_interval
--
-- Description: Calculate the stock price change over a period  P(last)-P(first)
--
-- ---------------- change log -------------------------
-- 2019-07-10  davidyu   initial version

drop table if exists stock_test.first_last_price;
drop table if exists stock_test.stock_change_interval;

create table stock_test.first_last_price as 
select * from
(
select stock_index,
close,stock_date,
row_number() over (partition by stock_index order by stock_date ) rank,
row_number() over (partition by stock_index order by stock_date desc) rank_d
from stock_dev.day_history_insert
where stock_date between '${startDate}' and '${endDate}'
)
where (rank = 1 or rank_d=1)
;

create table stock_test.stock_change_interval as
select a.stock_index,a.close as first_price,b.close as last_price,
b.close-a.close as change_price
from 
(select stock_index,close from stock_test.first_last_price where rank=1) a
left join 
(select stock_index,close from stock_test.first_last_price where rank_d=1) b
on a.stock_index = b.stock_index
;







