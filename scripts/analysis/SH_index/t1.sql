drop table if exists stock_analysis.SH_index_mv_avg;

create table stock_analysis.SH_index_mv_avg as
SELECT stock_date,adj_close,volume,
round(avg(adj_close) OVER (ORDER BY stock_date ROWS BETWEEN 5 PRECEDING AND 1 PRECEDING),2) AS mv_avg5,
round(avg(adj_close) OVER (ORDER BY stock_date ROWS BETWEEN 10 PRECEDING AND 1 PRECEDING),2) AS mv_avg10,
round(avg(adj_close) OVER (ORDER BY stock_date ROWS BETWEEN 15 PRECEDING AND 1 PRECEDING),2) AS mv_avg15,
round(avg(adj_close) OVER (ORDER BY stock_date ROWS BETWEEN 20 PRECEDING AND 1 PRECEDING),2) AS mv_avg20,
round(avg(adj_close) OVER (ORDER BY stock_date ROWS BETWEEN 30 PRECEDING AND 1 PRECEDING),2) AS mv_avg30,
round(avg(adj_close) OVER (ORDER BY stock_date ROWS BETWEEN 40 PRECEDING AND 1 PRECEDING),2) AS mv_avg40,
round(avg(adj_close) OVER (ORDER BY stock_date ROWS BETWEEN 50 PRECEDING AND 1 PRECEDING),2) AS mv_avg50,
round(avg(adj_close) OVER (ORDER BY stock_date ROWS BETWEEN 60 PRECEDING AND 1 PRECEDING),2) AS mv_avg60,
round(avg(adj_close) OVER (ORDER BY stock_date ROWS BETWEEN 120 PRECEDING AND 1 PRECEDING),2) AS mv_avg120,
round(avg(adj_close) OVER (ORDER BY stock_date ROWS BETWEEN 150 PRECEDING AND 1 PRECEDING),2) AS mv_avg150,
round(avg(adj_close) OVER (ORDER BY stock_date ROWS BETWEEN 200 PRECEDING AND 1 PRECEDING),2) AS mv_avg200,
round(avg(adj_close) OVER (ORDER BY stock_date ROWS BETWEEN 300 PRECEDING AND 1 PRECEDING),2) AS mv_avg300,
round(avg(volume) OVER (ORDER BY stock_date ROWS BETWEEN 300 PRECEDING AND 1 PRECEDING),2) AS mv_avg300_vol
from stock_dev.SH_index
order by stock_date
;





stock_dev.day_history_insert

