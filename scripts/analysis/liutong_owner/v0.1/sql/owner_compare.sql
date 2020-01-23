-- ======================================================
-- script name : owner_compare.sql
--
-- Souce Table : stock_dev.liutong_owner
--
-- Target Table : stock_test.important_owner_seasonal_change
--
-- Description: important owner seasonal change
--
-- ---------------- change log -------------------------
-- 2020-01-19  davidyu   initial version

--drop table if exists ${database}.${tgt_table};
set hive.exec.dynamic.partition.mode=nonstrict;
--create table ${database}.${tgt_table} as
insert overwrite table ${database}.${tgt_table} partition (day,owner_name)
select
COALESCE(a.stock_index,b.stock_index) as stock_index,
COALESCE(c.name,d.name) as stock_name,
COALESCE(c.industry,d.industry) as industry,
a.ratio-b.ratio as ratio_change,
a.ratio as a_ratio,
b.ratio as b_ratio,
a.dt as start_date,
b.dt as end_date,
'${end_date}' as day,
'${owner_name_en}' as owner_name
from
(
    select * from
    stock_dev.liutong_owner
    where dt ='${end_date}' and owner_name like '%${owner_name}%'
    
) a
full join
(
    select * from stock_dev.liutong_owner
    where dt ='${start_date}' and owner_name like '%${owner_name}%'
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

