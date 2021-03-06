--  qf2 https://github.com/zzerx/qfii/blob/master/qfii.py
select * from stock_dev.liutong_owner limit 10;

desc stock_dev.liutong_owner;


select * from stock_test.quanguoshebao limit 10;
select * from stock_test.zhongyanghuijin limit 10;
select * from stock_test.hk_zhongyang limit 10;


select a.stock_index,a.stock_name,
a.ratio_change,a.start_date,a.end_date,a.onwer_name,
ZYHJ.ratio_change,QGSB.ratio_change
from stock_test.hk_zhongyang
full join
stock_test.zhongyanghuijin ZYHJ
on a.stock_index=ZYHJ.stock_index and a.start_date=ZYHJ.start_date and a.end_date=ZYHJ.end_date
full join stock_test.quanguoshebao QGSB
on a.stock_index=QGSB.stock_index and a.start_date=ZYHJ.start_date and a.end_date=ZYHJ.end_date



select * from stock_test.hk_dailiren
where a_ratio is not null and b_ratio is not null
order by ratio_change
limit 20
;





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
and a.dt >= '2019-06-30' 
order by a.ratio desc  
limit 50
;



select stock_index,b.name,owner_name,
concat_ws(',',collect_list(ratio)) as ratio_list,
concat_ws(',',collect_list(dt)) as dt_list 
from stock_dev.liutong_owner a 
left join
stock.stock_index b
on b.code = a.stock_index
where owner_name like concat('%','香港中央结算有限公司','%')
group by stock_index,owner_name,b.name
having dt_list > '2019-06-25'
;

left join 
stock.stock_index b 
on b.code = a.stock_index 
where a.owner_name like concat('%','中国平安','%')
and a.dt >= '2019-06-30' 
order by a.ratio desc  
limit 50
;





select * from 
stock_dev.liutong_owner
where owner_name = '香港中央结算有限公司'
limit 10
;





