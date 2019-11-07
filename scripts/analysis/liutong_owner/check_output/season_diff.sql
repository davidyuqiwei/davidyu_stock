select * from stock_test.hk_zhongyang
where a_ratio is not null and b_ratio is not null
order by ratio_change desc
limit 20
;




select * from stock_test.hk_zhongyang
where a_ratio is not null and b_ratio is null
order by ratio_change
limit 20
;

select count(1)
from stock_test.hk_zhongyang
where b_ratio is not null
;

select count(1) 
from stock_dev.liutong_owner
where dt='2019-09-30' and owner_name like '%香港中央结算有限公司%'
;

