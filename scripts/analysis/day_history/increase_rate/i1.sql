drop table if exists stock_test.first_last_price;
create table stock_test.first_last_price 
as 
select * from 
(
	select stock_index,
	close,stock_date,
	row_number() over (partition by stock_index order by stock_date ) rank,
	row_number() over (partition by stock_index order by stock_date desc) rank_d
	from stock_dev.day_history_insert
	where stock_date between '2017-01-01' and '2017-12-31'
)
where (rank = 1 or rank_d=1)
;


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
limit 20
;

select stock_index,
first_value(close) over (partition by stock_index order by stock_date desc) as start_price,
last_value(close) over (partition by stock_index order by stock_date) as start_price
from stock_dev.day_history_insert
where stock_date >= '2017-01-01' and stock_date <= '2017-12-31'
limit 10
;






create table stock_test.stock_change_interval 
as
select a.stock_index,a.close,b.close from 
(select stock_index,close from stock_test.first_last_price where rank=1) a
left join 
(select stock_index,close from stock_test.first_last_price where rank_d=1) b
on a.stock_index = b.stock_index
limit 10
;





select * from 
(



)
where (rank = 1 or rank_d=1) and stock_index = "002366"
limit 10
;

select close,stock_index,stock_date,
row_number() over (partition by stock_index order by stock_date desc) rank
from 
stock_dev.day_history_insert
where stock_date between '2015-07-01' and '2015-12-31' and rank < 2
limit 10
;



select * from 
(


select close,stock_index,stock_date,
first_value(close) over (partition by stock_index order by stock_date ) first_val,
last_value(close) over (partition by stock_index order by stock_date ) last_val
from stock_dev.day_history_insert
where stock_date between '2015-07-01' and '2015-07-20'
limit 40
;

select stock_index,
first_value(close) over (partition by stock_index order by stock_date ) first_val,
last_value(close) over (partition by stock_index order by stock_date ) last_val
from stock_dev.day_history_insert
where stock_date between '2015-07-01' and '2015-07-20'
limit 40
;

select * from stock_dev.day_history_insert









) 
where rank <2
limit 10
;


(
    select  from stock_dev.day_history_insert
    where stock_date between '2015-07-01' and '2015-12-31'
)
limit 10
;




