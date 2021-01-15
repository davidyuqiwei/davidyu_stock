
x94 as stock_index,
    x1,
    x3,x4,x5
    from stock_dev.fin_report
    where x1 ='2019-09-30'
    
) t2
on t1.stock_index = t2.stock_index
inner join 
(
    select stock_index,peTTM
    from stock_dev.baostock
    where dt = '2020-09-30'
    
) t3
on t3.stock_index=t1.stock_index
where (t1.x3-t2.x3)>0 and peTTM>0
order by t3.peTTM/round((t1.x3-t2.x3)/t2.x3,3) 
m
(
    select
    x94 as stock_index,
    x1,
    x3,x4,x5
    from stock_dev.fin_report
    where x1 ='2020-09-30'
    
) t1
inner join
(
    select
    x94 as stock_index,
    x1,
    x3,x4,x5
    from stock_dev.fin_report
    where x1 ='2019-09-30'
    
) t2
on t1.stock_index = t2.stock_index
inner join 
(
    select stock_index,peTTM
    from stock_dev.baostock
    where dt = '2020-09-30' and stock_index like '60%'
    
) t3
on t3.stock_index=t1.stock_index
where (t1.x3-t2.x3)>0 and peTTM>0
order by t3.peTTM/round((t1.x3-t2.x3)/t2.x3,3) 
limit 30
;
limit 30
;


