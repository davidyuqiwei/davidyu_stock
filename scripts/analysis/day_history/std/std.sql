set table=stock_analysis.day_history_std;
set start_date='2018-06-01';
set end_date='2018-11-30';


drop table if exists ${hiveconf:table};

create table ${hiveconf:table} as
select stock_index,round(stddev(nor_close),2) std_close from
(
SELECT stock_index,
adj_close/max(adj_close) OVER (PARTITION BY stock_index) as nor_close,
max(adj_close) OVER (PARTITION BY stock_index) as max_close,
min(adj_close) OVER (PARTITION BY stock_index) as min_close
from stock_dev.day_history_insert  
where stock_date >= ${hiveconf:start_date}
and stock_date <= ${hiveconf:end_date}
)
where (max_close-min_close)/max_close < 0.2
group by stock_index
;




