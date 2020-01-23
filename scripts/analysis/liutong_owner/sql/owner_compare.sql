--set spark.sql.shuffle.partitions=100;
set hive.exec.dynamic.partition.mode=nonstrict;

--alter table ${database}.${tgt_table} drop if exists partition(day='${end_date}',owner_name='${owner_name_en}');

insert into table ${database}.${tgt_table} partition(day,owner_name)
select
COALESCE(a.stock_index,b.stock_index) as stock_index,
COALESCE(c.name,d.name) as stock_name,
COALESCE(c.industry,d.industry) as industry,
COALESCE(a.ratio,0)-COALESCE(b.ratio,0) as ratio_change,
a.ratio as a_ratio,
b.ratio as b_ratio,
'${start_date}' as start_date,
'${end_date}' as end_date,
'${end_date}' as day,
'${owner_name_en}' as owner_name
from
(
    select 
    case when ratio is null then 0 else ratio end as ratio,
    dt,stock_index,owner_name
    from
    stock_dev.liutong_owner
    where dt ='${end_date}' and owner_name like '%${owner_name}%'
) a
full join
(
    select case when ratio is null then 0 else ratio end as ratio,
    dt,stock_index,owner_name
    from stock_dev.liutong_owner
    where dt ='${start_date}' and owner_name like '%${owner_name}%'
) b
on a.stock_index = b.stock_index and a.owner_name  = b.owner_name
left join
stock.stock_index c
on c.code = a.stock_index
left join
stock.stock_index d
on d.code = b.stock_index
;

