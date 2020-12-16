-- ======================================================
-- script name : 
--
-- Souce Table : stock_dev.dadan_dfcf
--
-- Target Table : stock_dw.dadan_dfcf_weekly_dadan_cnt
--
-- Description: cnt dadan, over a week
--
-- ---------------- change log -------------------------
-- 2020-08-10  davidyu   initial version



--drop table if exists ${tgt_table};
set hive.exec.dynamic.partition.mode=nonstrict;


-- make sure update table is the newest
alter table ${tgt_table}
drop if exists partition(day='${end_date}');

-- remove the partitoin is a week ago
alter table ${tgt_table}
drop if exists partition(day='${start_date}');


insert into table ${tgt_table} partition (day)
select
stock_index,
stock_name,
count(stock_name) as cnt,
concat_ws(',' , collect_set(stock_date)) as stock_date_list,
concat_ws(',' , collect_set(dadan_liuru/10000)) as stock_dadan_liuru_list,
'${end_date}' as stock_date,
'${end_date}' as day
from ${src_table}
where stock_date>='${start_date}'  and stock_date<='${end_date}'
and dadan_liuru > ${price}
group by stock_name,stock_index
order by cnt desc
;




