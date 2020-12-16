-- ======================================================
-- script name : 
--
-- Souce Table : stock_dev.dazongjiaoyi
--
-- Target Table : output for daily report 
--
-- Description: today dazongjiaoyi rank sum buy stock index
--
-- ---------------- change log -------------------------
-- 2020-08-26  davidyu   initial version
select secucode,sname,sum(tval) as sum_tval
from
(
    select distinct *
    from stock_dev.dazongjiaoyi
    where tdate <> 'TDATE' and substr(tdate,1,10)="${today_date}"
    and substr(tdate,1,10)<="${today_date}"
    
)
group by secucode,sname
order by sum_tval desc
;
