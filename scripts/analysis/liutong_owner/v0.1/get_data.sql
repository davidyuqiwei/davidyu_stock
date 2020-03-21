select * from stock_dev.liutong_owner
where owner_name like concat('%','香港中央结算(代理人)有限公司','%')
and stock_index ='000756'
order by dt
;

