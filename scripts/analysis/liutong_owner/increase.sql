select ll.owner_name,a1.diff_ratio,a1.stock_index
from stock_dev.liutong_owner  ll
left join 
(
select 
    min(struct(stock_date,adj_close,stock_index)).stock_index as stock_index,
    min(struct(stock_date,adj_close,stock_index)).stock_date as min_date,
    min(struct(stock_date,adj_close,stock_index)).adj_close as min_value,
    max(struct(stock_date,adj_close,stock_index)).stock_date as max_date,
    max(struct(stock_date,adj_close,stock_index)).adj_close as max_value,
    round((max(struct(stock_date,adj_close,stock_index)).adj_close-min(struct(stock_date,adj_close,stock_index)).adj_close)/min(struct(stock_date,adj_close,stock_index)).adj_close,3) as diff_ratio,
    count(1) as days,
    b.name
    from stock_dev.day_history_insert a
    left join 
    stock.stock_index b
    on cast(b.code as string) = a.stock_index
    where a.stock_date > "2018-06-30" and a.stock_date < "2018-12-31"
    group by a.stock_index,b.name
    order by diff_ratio
) a1
on ll.stock_index = a1.stock_index
limit 20
;

