create table stock_test.owner_merge_stat as 
select a.stock_index,a.stock_name,
a.ratio_change,a.start_date,a.end_date,a.owner_name,
ZYHJ.ratio_change as ratio_change1,
ZYHJ.owner_name as name1,
QGSB.ratio_change as ratio_change2,
QGSB.owner_name as name2
from stock_test.hk_zhongyang a
full join
stock_test.zhongyanghuijin ZYHJ
on a.stock_index=ZYHJ.stock_index and a.start_date=ZYHJ.start_date and a.end_date=ZYHJ.end_date
full join stock_test.quanguoshebao QGSB
on a.stock_index=QGSB.stock_index and a.start_date=ZYHJ.start_date and a.end_date=ZYHJ.end_date
;






