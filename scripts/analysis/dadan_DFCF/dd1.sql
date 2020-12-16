select 
a.stock_name,a.stock_index,
b.cnt,
b.stock_date_list,
b.stock_dadan_liuru_list
from
(
select stock_name,stock_index,
today_increase_ratio,dadan_liuru,stock_date
from stock_dev.dadan_dfcf
where stock_date="2020-08-10"
) a
join dadan_dfcf_weekly_dadan_cnt b
on a.stock_index = b.stock_index and a.stock_date=b.day
order by b.cnt
limit 30
;

select 
stock_name,
today_increase_ratio,
dadan_liuru,
stock_date
from stock_dev.dadan_dfcf
where stock_date>"2020_07_20" and stock_date<="2020_08_05"
order by dadan_liuru desc
limit 10
;



select count(stock_name) as cnt,
stock_name,
concat_ws(',' , collect_set(stock_date)) as stock_date_list
from stock_dev.dadan_dfcf
where stock_date>"2020_07_27" and stock_date<="2020_08_05"
and dadan_liuru > 100000000
group by stock_name
order by cnt desc  
limit 50
;



