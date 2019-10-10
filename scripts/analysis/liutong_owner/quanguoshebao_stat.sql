select stock_index,stock_name,
sum(ratio_change) as sum_change_ratio,
count(case when ratio_change>0 then 1 else 0 end) as increase_num
from 
stock_test.quanguoshebao
where a_ratio is not NULL and b_ratio is not NULL
group by stock_index,stock_name
order by sum_change_ratio desc
limit 50
;





