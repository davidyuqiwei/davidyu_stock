-- ======================================================
-- script name : run_liutong_owner_owner_number_sort_list.sql
--
-- Souce Table : stock_dev.liutong_owner
--
-- Target Table : stock_analysis.liutong_owner_owner_number_sort_list
--
-- Description: list the owner number in a datetime
--
-- ---------------- change log -------------------------
-- 2019-09-23  davidyu   initial version

drop table if exists stock_analysis.liutong_owner_owner_number_sort_list;


create table stock_analysis.liutong_owner_owner_number_sort_list as
select owner_name,count(owner_name) as cnt
from stock_dev.liutong_owner
where dt = '2019-06-30'
group by owner_name
order by cnt desc
;


