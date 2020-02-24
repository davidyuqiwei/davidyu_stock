select
a.stock_index,a.ratio,a.dt
from stock_dev.liutong_owner a
where owner_name like '%全国社保%' and dt='2019-09-30'
;

select
a.stock_index,a.ratio,a.dt
from stock_dev.liutong_owner a
where owner_name like '%全国社保%' and dt='2019-09-30'


drop table if exists stock_test.gudong_shouyi;
create table stock_test.gudong_shouyi
as
select owner_stock_list.owner_name,owner_stock_list.ratio,
aa.* from 
(
select
a.owner_name,a.stock_index,a.ratio,a.dt
from stock_dev.liutong_owner a
where dt='2019-09-30'
) owner_stock_list
left join 
(
select stock_index,(a.end_close-a.start_close)/a.start_close as close_diff
from
(
select 
distinct
stock_index,
stock_date,
first_value(adj_close) over (partition by stock_index order by stock_date ) start_close,
last_value(adj_close) over (partition by stock_index order by stock_date ) end_close,
row_number() over (partition by stock_index order by stock_date desc) row_num
from 
stock_dev.day_history_insert
where stock_date between '2019-09-30' and '2019-11-30'
) a 
where a.row_num=1
) aa
on owner_stock_list.stock_index = aa.stock_index
;

select owner_name,avg(close_diff) as shouyi
from
stock_test.gudong_shouyi
where length(owner_name) >3
group by owner_name
order by shouyi desc 
limit 100
;

select
a.owner_name,a.stock_index,a.ratio,a.dt
from stock_dev.liutong_owner a
where dt='2019-09-30' and owner_name="全国社保基金一零八组合"
;




select if(rank=1,a.close,-999),if(rank<>1,a.close,-999) from
(
    select stock_index,
    close,stock_date,
    row_number() over (partition by stock_index order by stock_date ) rank,
    row_number() over (partition by stock_index order by stock_date desc) rank_d
    from stock_dev.day_history_insert
    where stock_date between '2015-07-01' and '2015-07-20'
) a
where (rank = 1 or rank_d=1)
limit 10
;

