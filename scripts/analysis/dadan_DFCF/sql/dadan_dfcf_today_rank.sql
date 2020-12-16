-- ======================================================
-- script name : 
--
-- Souce Table : stock_dev.dadan_dfcf
--
-- Target Table : output for daily report 
--
-- Description: today dadan rank by dadan liuru
--
-- ---------------- change log -------------------------
-- 2020-08-17  davidyu   initial version

select 
stock_index,
stock_name,
new_price,
today_increase_ratio,
chaodadan_liuru
chaodadan_liuru_ratio,
dadan_liuru,
dadan_liuru_ratio,
zhuli_liuru,
zhuli_liuru_ratio
from
stock_dev.dadan_dfcf
where stock_date='${today_date}'
order by dadan_liuru desc
;

