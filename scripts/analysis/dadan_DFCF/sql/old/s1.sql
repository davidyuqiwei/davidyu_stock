-- ======================================================
-- script name : 
--
-- Souce Table : stock_dev.dadan_dfcf
--
-- Target Table : stock_dw.
--
-- Description: list the owner count in a period
--
-- ---------------- change log -------------------------
-- 2020-08-10  davidyu   initial version

drop table if exists ${tgt_table};

create table ${tgt_table} as
select count(stock_name) as cnt,
stock_name,
concat_ws(',' , collect_set(stock_date)) as stock_date_list
from ${src_table}
where stock_date>'${start_date}' and stock_date<='${end_date}'
and dadan_liuru > ${price}
group by stock_name
order by cnt desc
;

