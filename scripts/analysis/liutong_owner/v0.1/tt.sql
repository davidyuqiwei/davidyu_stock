select * from stock_dev.liutong_owner
where owner_name like concat('%','香港中央结算(代理人)有限公司','%')
and stock_index ='000756'
order by dt
limit 50
;

select stock_index,owner_name,count(distinct dt) as cnt 
from stock_dev.liutong_owner
where owner_name like concat('%','香港中央结算','%')
group by stock_index,owner_name
order by cnt desc 
limit 40
;

