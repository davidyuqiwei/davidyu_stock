--  qf2 https://github.com/zzerx/qfii/blob/master/qfii.py
select * from stock_dev.liutong_owner limit 10;

desc stock_dev.liutong_owner;


--owner_sort  int NULL
--owner_name  string  NULL
--amount  int NULL
--ratio   float   NULL
--charac  string  NULL
--dt  date    NULL
--stock_index string  NULL


select stock_index,b.name,ratio,owner_name,dt,b.industry
from stock_dev.liutong_owner a 
left join 
stock.stock_index b 
on b.code = a.stock_index 
where (a.owner_name like concat('%','马来西亚','%') or
a.owner_name like concat('%','高瓴','%') or
a.owner_name like concat('%','淡马锡','%') or
a.owner_name like concat('%','瑞士','%') or
a.owner_name like concat('%','渣打','%') or
a.owner_name like concat('%','Standard','%') or
a.owner_name like concat('%','中国平安','%'))
and a.dt > '2018-08-30'
order by a.ratio desc  
limit 50
;

select stock_index,b.name,ratio,owner_name,dt,b.industry
from stock_dev.liutong_owner a 
left join 
stock.stock_index b 
on b.code = a.stock_index 
where a.owner_name like concat('%','中国平安','%')
and a.dt > '2018-08-30'
order by a.ratio desc  
limit 50
;



