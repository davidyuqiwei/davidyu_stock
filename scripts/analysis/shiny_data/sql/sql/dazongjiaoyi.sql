with table1 as 
(
    select stock_index,
    stock_name,
    dt,
    count(1) as dazongjiaoyi_cnt,
    sum(total_money) as total_money,
    'no' as buyercode,'no' as buyername,'no' as salecode,'no' as salename,
    'pos_zyl' as data_type
    from
    stock_raw.dazongjiaoyi
    where dt >=date_sub(now(),30) and dt<=now() 
    and Zyl>0
    group by 1,2,3
    
),
table2 as 
(
    select stock_index,
    stock_name,
    dt,
    count(1) as dazongjiaoyi_cnt,
    sum(total_money) as total_money,
    'no' as buyercode,'no' as buyername,'no' as salecode,'no' as salename,
    'all' as data_type
    from
    stock_raw.dazongjiaoyi
    where dt >=date_sub(now(),30) and dt<=now() 
    group by 1,2,3
    
),
table3 as 
(
    select stock_index,stock_name,total_money,
    0 as dazongjiaoyi_cnt,
    total_money,
    buyercode,buyername,salecode,salename,
    'detail' as data_type
    from
    stock_raw.dazongjiaoyi
    where dt >=date_sub(now(),30) and dt<=now() 
    
)
select * from table1 union all select * from table2 union all select * from table3;

