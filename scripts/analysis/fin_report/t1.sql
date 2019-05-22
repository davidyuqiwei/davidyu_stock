select x1,x3,x33,x94,b.name,b.industry,b.area 
from stock_dev.fin_report a 
left join stock.stock_index b 
on a.x94 = b.code 
where a.x1='2018-09-30'
order by x33 desc -- '扣除非经常性损益后的净利润(元)',
limit 50
;



select 
a.x94,
avg(a.x36) as profit_mean,   -- 净利润增长率
count(a.x36) as stat_len,
b.name
from stock_dev.fin_report a
left join stock.stock_index b
on a.x94 = b.code
where a.x36 <> -9999 and count(a.x36) > 
group by a.x94,b.name
order by profit_mean desc 
limit 50
;


select x94,x36,x1
from stock_dev.fin_report
where x94 = '000620'
;






select x1,x3,x33,x94,b.name,b.industry,b.area 
from stock_dev.fin_report a 
left join stock.stock_index b 
on a.x94 = b.code 
where b.code='601318'
order by x1 desc -- '扣除非经常性损益后的净利润(元)',
limit 50
;

select x1,x3,x33,x35,x94,b.name,b.industry,b.area 
from stock_dev.fin_report a 
left join stock.stock_index b 
on a.x94 = b.code 
--where a.x1='2018-09-30' and a.x94 = '600487'
where a.x94 = '600487'
--order by x35 desc -- '主营业务收入增长率(%)'
order by x1 desc -- '主营业务收入增长率(%)'
limit 50
;



-- industry 
set variable=x28;
set stk_date='2018-09-30';

select x1,avg(${hiveconf:variable}) as sum1,b.industry
from stock_dev.fin_report a 
left join stock.stock_index b 
on a.x94 = b.code 
where a.x1=${hiveconf:stk_date} and ${hiveconf:variable} > -999
group by a.x1,b.industry
order by sum1 desc 
limit 20
;



-- 摊薄每股收益(元)
set variable=x3;
set stk_date='2018-09-30';

select x1,${hiveconf:variable},x94,b.industry,b.name
from stock_dev.fin_report a 
left join stock.stock_index b 
on a.x94 = b.code 
where a.x1=${hiveconf:stk_date} and ${hiveconf:variable} > -999
order by b.industry,${hiveconf:variable} desc 
limit 100
;

-- change rate 
set start_date='2018-06-30';
set end_date='2018-09-30';

select
min(struct(stock_date,adj_close,stock_index)).stock_index as stock_index,
round((max(struct(stock_date,adj_close,stock_index)).adj_close-min(struct(stock_date,
    adj_close,stock_index)).adj_close)/min(struct(stock_date,adj_close,stock_index)).adj_close,3) as increaseRate,
count(1) as days
from stock_dev.day_history_insert
where stock_date > ${hiveconf:start_date} and stock_date < ${hiveconf:end_date}
group by stock_index
order by increaseRate desc 
limit 10
;


-- 摊薄每股收益(元)
set variable=x3;
set stk_date='2018-09-30';
set start_date='2018-06-30';
set end_date='2018-09-30';

-- 
select c.stock_index,c.increaseRate,c.days,
a.x1,a.${hiveconf:variable},a.x94,
a.x27, -- 主营利润比重
b.industry,b.name 
from 
(
select 
    min(struct(stock_date,adj_close,stock_index)).stock_index as stock_index,
    -- increase rate
    round((max(struct(stock_date,adj_close,stock_index)).adj_close-min(struct(stock_date,
    adj_close,stock_index)).adj_close)/min(struct(stock_date,adj_close,
    stock_index)).adj_close,3) as increaseRate,
count(1) as days
from stock_dev.day_history_insert
where stock_date > ${hiveconf:start_date} and stock_date < ${hiveconf:end_date}
group by stock_index
order by increaseRate desc
) c
left join stock_dev.fin_report a 
on a.x94=c.stock_index
left join stock.stock_index b 
on c.stock_index=b.code
where a.x1=${hiveconf:stk_date} and ${hiveconf:variable} > -999
limit 10
;






select stk_index,change_rate,industry,name,${hiveconf:variable},x1
from 
(
select x1,${hiveconf:variable},x94,b.industry,b.name
from stock_dev.fin_report a 
left join stock.stock_index b 
on a.x94 = b.code 

where a.x1=${hiveconf:stk_date} and ${hiveconf:variable} > -999
order by b.industry,${hiveconf:variable} desc 








where stock_date > ${hiveconf:start_date} and stock_date < ${hiveconf:end_date}
group by stock_index
order by increaseRate desc 


limit 10
)

-- change rate 











select * from stock_dev.fin_report where x94 = '600073'

select * from stock.stock_index
where industry = '食品'
;


select x1,x3,x33,x94
from 
stock_dev.fin_report
where x94 = '601398'
;
