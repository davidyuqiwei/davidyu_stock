-- ======================================================
-- script name : 
--
-- Souce Table : stock_dev.dadan_dfcf
--
-- Target Table : stock_dw.dadan_dfcf_today_dadan_weekly_dadan_cnt
--
-- Description: today dadan and cnt dadan over a week,rank by cnt
--
-- ---------------- change log -------------------------
-- 2020-08-10  davidyu   initial version

set hive.exec.dynamic.partition.mode=nonstrict;

alter table ${tgt_table}
drop if exists partition(day='${start_date}');

alter table ${tgt_table}
drop if exists partition(day='${today_date}');

insert into table ${tgt_table} partition (day)
select
a.stock_name,
a.stock_index,
a.today_increase_ratio,
a.dadan_liuru as today_liuru,
b.cnt as weekly_dadan_cnt,
b.stock_date_list,
b.stock_dadan_liuru_list,
'${today_date}' as stock_date,
'${today_date}' as day
from
(
    select stock_name,stock_index,
    today_increase_ratio,dadan_liuru,stock_date
    from ${src_table}
    where stock_date='${today_date}' 
) a
join stock_dw.dadan_dfcf_weekly_dadan_cnt b
on a.stock_index = b.stock_index and a.stock_date=b.stock_date
order by b.cnt
;

