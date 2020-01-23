create table stock_dev.long_term_sample_data
select * 
from
stock_dev.stock_longterm_data a 
left semi join
stock_test.SH_50index b
on a.stock_index=b.stock_index
;

select * from 
stock_analysis.day_history_mv_avg a
left join 
stock_dev.long_term_sample_data b
on a.stock_date = b.stock_date and a.stock_index = b.stock_index
limit 10
;

select * from 
stock_dev.long_term_sample_data a
left join 
stock_analysis.day_history_mv_avg b
on a.stock_date = b.stock_date and a.stock_index = b.stock_index
limit 10
;


create table stock_dev.long_term_sample_data_mv_avg as 
select 
a.stock_date,
a.stock_index,
a.high,
a.low,
a.open,
a.close,
a.volume,
a.adj_close,
b.mv_avg5,
b.mv_avg10,
b.mv_avg15,
b.mv_avg20,
b.mv_avg30,
b.mv_avg40,
b.mv_avg50,
b.mv_avg60,
b.mv_avg120,
b.mv_avg150,
b.mv_avg200,
b.mv_avg300
from 
stock_dev.long_term_sample_data a
left join 
stock_analysis.day_history_mv_avg b
on a.stock_date = b.stock_date and a.stock_index = b.stock_index
;




