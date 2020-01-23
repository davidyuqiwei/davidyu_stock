drop table if exists stock_analysis.long_data_mv_avg;

create table stock_analysis.long_data_mv_avg as
SELECT stock_date,stock_index,adj_close,
avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 5 PRECEDING AND 1 PRECEDING) AS mv_avg5,
avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 10 PRECEDING AND 1 PRECEDING) AS mv_avg10,
avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 15 PRECEDING AND 1 PRECEDING) AS mv_avg15,
avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 20 PRECEDING AND 1 PRECEDING) AS mv_avg20,
avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 30 PRECEDING AND 1 PRECEDING) AS mv_avg30,
avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 40 PRECEDING AND 1 PRECEDING) AS mv_avg40,
avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 50 PRECEDING AND 1 PRECEDING) AS mv_avg50,
avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 60 PRECEDING AND 1 PRECEDING) AS mv_avg60,
avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 120 PRECEDING AND 1 PRECEDING) AS mv_avg120,
avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 150 PRECEDING AND 1 PRECEDING) AS mv_avg150,
avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 200 PRECEDING AND 1 PRECEDING) AS mv_avg200,
avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 300 PRECEDING AND 1 PRECEDING) AS mv_avg300
from stock_dev.stock_longterm_data
order by stock_date
;


