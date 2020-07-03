sh tt.sh
echo $?


select a.stock_index,a.stock_date,
if(a.adj_close-b.adj_close is null,0,a.adj_close-b.adj_close) as ss 
from stock_dev.day_history_insert a
left join stock_dev.day_history_insert b
on a.stock_index=b.stock_index and datediff(a.stock_date,b.stock_date)=1
limit 10
;
