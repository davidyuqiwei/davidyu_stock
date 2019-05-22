drop table if exists stock_dev.day_history_mv_avg;
create table stock_dev.day_history_mv_avg as
SELECT close,stock_date,stock_index, 
avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 5 PRECEDING AND 1 PRECEDING) AS mv_avg5,
avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 10 PRECEDING AND 1 PRECEDING) AS mv_avg10,
avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 15 PRECEDING AND 1 PRECEDING) AS mv_avg15,
avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 20 PRECEDING AND 1 PRECEDING) AS mv_avg20,
avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 30 PRECEDING AND 1 PRECEDING) AS mv_avg30,
avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 40 PRECEDING AND 1 PRECEDING) AS mv_avg40,
avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 50 PRECEDING AND 1 PRECEDING) AS mv_avg50,
avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 60 PRECEDING AND 1 PRECEDING) AS mv_avg60,
avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 120 PRECEDING AND 1 PRECEDING) AS mv_avg120
from stock_dev.day_history_insert
order by stock_date
;


--select * from stock_dev.day_history_mv_avg limit 10
