create table stock_test.stock_longterm_data as
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
;


-- select count(*) from stock_test.stock_longterm_data;
