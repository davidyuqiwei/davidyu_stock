drop table if exists ${database}.${tgt_table};

create table ${database}.${tgt_table} as
select
COALESCE(a.stock_index,b.stock_index) as stock_index,
COALESCE(c.name,d.name) as stock_name,
COALESCE(c.industry,d.industry) as industry,
a.ratio-b.ratio as ratio_change,
a.ratio as a_ratio,
b.ratio as b_ratio,
a.dt as start_date,
b.dt as end_date,
COALESCE(a.owner_name,b.owner_name) as owner_name
from
(
    select * from
    stock_dev.liutong_owner
    where dt ='2019-06-30' and owner_name='${owner_name}'
    
) a
full join
(
    select * from stock_dev.liutong_owner
    where dt ='2019-03-31' and owner_name ='${owner_name}'
    
) b
on a.stock_index = b.stock_index and a.owner_name  = b.owner_name
left join
stock.stock_index c
on c.code = a.stock_index
left join
stock.stock_index d
on d.code = b.stock_index
order by ratio_change desc
;

