select stock_index, count(substr(owner_name,4)) as SB_cnt
from
stock_test.QGSB
group by stock_index
order by SB_cnt desc 
limit 30
;

