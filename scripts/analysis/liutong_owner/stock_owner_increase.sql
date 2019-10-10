drop table if exists stock_test.owner_cnt_increase;
create table stock_test.owner_cnt_increase as
select c.stock_index,
sum(case when c.ratio_change is not NULL and c.ratio_change >0 then 1 else 0 end) as increase_cnt,
d.name,d.industry,
concat_ws(',',collect_set(c.owners)) as owner_list
from
( 
select
COALESCE(a.stock_index,b.stock_index) as stock_index,
a.owner_name as owners,
--COALESCE(c.name,d.name) as stock_name,
--COALESCE(c.industry,d.industry) as industry,
a.ratio-b.ratio as ratio_change,
a.ratio as a_ratio,
b.ratio as b_ratio,
a.dt as start_date,
b.dt as end_date,
a.owner_name
from
(
    select * from
    stock_dev.liutong_owner
    where dt ='2019-06-30' 
    
) a
left join
(
    select * from stock_dev.liutong_owner
    where dt ='2019-03-31' 
    
) b
on a.stock_index = b.stock_index and a.owner_name  = b.owner_name
) c 
left join
stock.stock_index d
on c.stock_index = d.code
group by c.stock_index,d.name,d.industry
order by increase_cnt desc
;




