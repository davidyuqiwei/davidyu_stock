drop table if exists stock_analysis.day_history_mv_avg;

create table ${tgt_database}.${tgt_table} as
SELECT stock_date,stock_index,adj_close,
round(avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 5 PRECEDING AND 1 PRECEDING),2) AS mv_avg5,
round(avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 10 PRECEDING AND 1 PRECEDING),2) AS mv_avg10,
round(avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 15 PRECEDING AND 1 PRECEDING),2) AS mv_avg15,
round(avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 20 PRECEDING AND 1 PRECEDING),2) AS mv_avg20,
round(avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 30 PRECEDING AND 1 PRECEDING),2) AS mv_avg30,
round(avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 40 PRECEDING AND 1 PRECEDING),2) AS mv_avg40,
round(avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 50 PRECEDING AND 1 PRECEDING),2) AS mv_avg50,
round(avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 60 PRECEDING AND 1 PRECEDING),2) AS mv_avg60,
round(avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 120 PRECEDING AND 1 PRECEDING),2) AS mv_avg120,
round(avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 150 PRECEDING AND 1 PRECEDING),2) AS mv_avg150,
round(avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 200 PRECEDING AND 1 PRECEDING),2) AS mv_avg200,
round(avg(adj_close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 300 PRECEDING AND 1 PRECEDING),2) AS mv_avg300
from ${src_database}.${src_table}
order by stock_date
;




