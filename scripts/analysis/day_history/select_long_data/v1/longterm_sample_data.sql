-- select long term data
-- level : stock index


create table stock_dev.stock_longterm_data as
select * from
stock_dev.day_history_insert a
left semi join
(
    select stock_index,count(stock_index) as cnt
    from stock_dev.day_history_insert
    group by stock_index
    having cnt > 3000

) b
on a.stock_index = b.stock_index
limit 20
;


create table stock_dev.long_term_sample_data
select *
from
stock_dev.stock_longterm_data a
left semi join
stock_test.SH_50index b
on a.stock_index=b.stock_index
;

