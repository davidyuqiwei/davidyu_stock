-- ======================================================
-- script name : run_liutong_owner_cnt.sql
--
-- Souce Table : stock_dev.liutong_owner
--
-- Target Table : stock_analysis.owner_cnt
--
-- Description: list the owner count in a period
--
-- ---------------- change log -------------------------
-- 2019-09-23  davidyu   initial version

drop table if exists ${database}.${tgt_table};

create table ${database}.${tgt_table} as
select 
owner_name,
count(owner_name) as cnt,
dt
from stock_dev.liutong_owner
where dt = '${datetimes}'
group by owner_name,dt
order by cnt desc
;



