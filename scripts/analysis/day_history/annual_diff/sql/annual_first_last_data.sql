-- ======================================================
-- script name : annual_first_last_data.sql
--
-- Souce Table : stock_dev.day_history_insert
--
-- Target Table : stock_dev.annual_first_last_data
--
-- Description: annual first and last value and  last value- first value ,diff
--
-- ---------------- change log -------------------------
-- 2019-12-31  davidyu   initial version
drop table if exists ${tgt_database}.${tgt_table};


create table ${tgt_database}.${tgt_table} as
select a.*,
round(a.last_adj-a.first_adj,3) as annual_diff,
round((a.last_adj-a.first_adj)/a.first_adj,3) as annual_diff_ratio
from
(
select distinct stock_index,substr(stock_date,1,4) as year,
first_value(adj_close) over(partition by 
    stock_index,substr(stock_date,1,4) order by stock_date) first_adj,
first_value(adj_close) over(partition 
    by stock_index,substr(stock_date,1,4) order by stock_date desc) last_adj
from ${src_database}.${src_table}
) a
;



