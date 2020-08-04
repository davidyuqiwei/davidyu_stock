select a.jijin_name,a.cnt,b.stock_index_list
from
(
    select count(jijin_name) as cnt, jijin_name
    from
    stock_dev.jijin
    where stock_date = "2020-06-30"
    group by jijin_name
    
) a
left join
(
    select jijin_name,
    CONCAT_WS("_", collect_set(stock_index)) as stock_index_list
    from
    stock_dev.jijin 
    where stock_date = "2020-06-30"
    group by jijin_name
    
) b
on a.jijin_name = b.jijin_name
order by a.cnt 
limit 30
;
