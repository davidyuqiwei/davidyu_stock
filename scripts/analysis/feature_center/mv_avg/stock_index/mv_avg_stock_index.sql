drop table if exists stock_feature.stock_index_mv_avg;

create table stock_feature.stock_index_mv_avg as
SELECT stock_date,stock_index,close,dt,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 3 PRECEDING AND 1 PRECEDING),2) AS mv_avg3,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 5 PRECEDING AND 1 PRECEDING),2) AS mv_avg5,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 8 PRECEDING AND 1 PRECEDING),2) AS mv_avg8,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 13 PRECEDING AND 1 PRECEDING),2) AS mv_avg13,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 21 PRECEDING AND 1 PRECEDING),2) AS mv_avg21,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 34 PRECEDING AND 1 PRECEDING),2) AS mv_avg34,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 10 PRECEDING AND 1 PRECEDING),2) AS mv_avg10,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 15 PRECEDING AND 1 PRECEDING),2) AS mv_avg15,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 20 PRECEDING AND 1 PRECEDING),2) AS mv_avg20,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 30 PRECEDING AND 1 PRECEDING),2) AS mv_avg30,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 40 PRECEDING AND 1 PRECEDING),2) AS mv_avg40,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 50 PRECEDING AND 1 PRECEDING),2) AS mv_avg50,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 60 PRECEDING AND 1 PRECEDING),2) AS mv_avg60,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 120 PRECEDING AND 1 PRECEDING),2) AS mv_avg120,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 150 PRECEDING AND 1 PRECEDING),2) AS mv_avg150,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 200 PRECEDING AND 1 PRECEDING),2) AS mv_avg200,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 300 PRECEDING AND 1 PRECEDING),2) AS mv_avg300
from stock_raw.baostock
where stock_index in ('601398','000917','000333','601318')
order by dt
;






