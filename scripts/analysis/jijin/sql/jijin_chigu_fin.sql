-- 基金持股平均
--每股收益,主营业务利润率,每股净资产_调整前,每股净资产_调整后 
select jijin_name,
round(avg(case when x3>-9998 then x3 else null end),2) as x3, 
round(avg(case when x15>-9998 then x15 else null end),2) as x15,
round(avg(case when x7>-9998 then x7 else null end),2),
round(avg(case when x8>-9998 then x8 else null end),2),
round(avg(case when x9>-9998 then x9 else null end),2) as x9,
concat_ws('_',collect_set(t2.name)) as stock_name_list,
concat_ws('_',collect_set(t2.code)) as stock_name_list
from
(
    select jijin_name,lpad(stock_index,6,'0') as stock_index
    from stock_dev.jijin 
    where stock_date = '2020-09-30' 
    and jijin_name like '%指数%'
    
) t1
left join
stock.stock_index t2
on t1.stock_index = lpad(t2.code,6,'0')
left join 
(
    select x1,x3,x15,x7,x8,x9,x94 as stock_index
    from 
    stock_dev.fin_report where x1='2020-09-30'
    
) t3
on t1.stock_index=t3.stock_index
group by jijin_name
;

