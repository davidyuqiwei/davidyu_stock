drop table if exists stock_dev.test
create table stock_dev.test as
select *,row_number() over (partition by stock_index,stock_date order by stock_date) test from stock_dev.day_history;


select count(*) as count1 from stock_dev.day_history;
select count(*) as count1 from stock_dev.test;

select * from  stock_dev.test limit 10;

