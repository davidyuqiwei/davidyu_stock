-- cocant the ratio list of the owner ratio 
drop table if exists stock_analysis.liutong_owner_ratio_list;

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


drop table if exists stock_test.hk_2019;
create table stock_test.hk_2019 as 
select 
COALESCE(a.stock_index,b.stock_index) as stock_index,
COALESCE(c.name,d.name) as stock_name,
COALESCE(c.industry,d.industry) as industry,
a.ratio-b.ratio as ratio_change,
a.ratio as a_ratio,
b.ratio as b_ratio,
a.dt as start_date,
b.dt as end_date,
a.owner_name
from 
(
select * from 
stock_dev.liutong_owner
where dt ='2019-06-30' and owner_name like concat('%','香港中央结算有限公司','%')
) a
full join 
(
select * from stock_dev.liutong_owner 
where dt ='2019-03-31' and owner_name like concat('%','香港中央结算有限公司','%')
) b
on a.stock_index = b.stock_index and a.owner_name  = b.owner_name
left join
stock.stock_index c
on c.code = a.stock_index
left join 
stock.stock_index d
on d.code = b.stock_index
order by ratio_change desc 
;


中央汇金资产管理有限责任公司    213
香港中央结算有限公司    208
中国证券金融股份有限公司    93
中国农业银行股份有限公司－中证500交易型开放式指数证券投资基金   75
领航投资澳洲有限公司－领航新兴市场股指基金(交易所)  17
招商银行股份有限公司－博时中证央企结构调整交易型开放式指数证券投资基金 15
嘉实基金－农业银行－嘉实中证金融资产管理计划    15
全国社保基金一零七组合  14
中欧基金－农业银行－中欧中证金融资产管理计划    14
挪威中央银行－自有资金  14



select substr(owner_name,1,4),count(owner_name) as cnt,
dt
from stock_dev.liutong_owner
where owner_name like concat('%','全国社保','%') and 
dt > '2005-01-01'
group by substr(owner_name,1,4),dt
order by dt desc
;

select substr(owner_name,1,4),count(owner_name) as cnt,
dt
from stock_dev.liutong_owner
where owner_name like concat('%','香港中央结算有限公司','%') and
dt > '2005-01-01'
group by substr(owner_name,1,4),dt
having cnt > 5
order by dt desc
;


select owner_name,count(owner_name) as cnt
from stock_dev.liutong_owner
where dt = '2019-06-30'
group by owner_name
order by cnt desc
;




select stock_index,b.name,owner_name,
concat_ws(',',collect_list(ratio)) as ratio_list,
max(dt) as max_date,
concat_ws(',',collect_list(dt)) as dt_list
from stock_dev.liutong_owner a
left join
stock.stock_index b
on b.code = a.stock_index
where owner_name like concat('%','香港中央结算有限公司','%')
group by stock_index,owner_name,b.name
having max_date < '2019-03-25' and max_date> '2018-12-20'
;

