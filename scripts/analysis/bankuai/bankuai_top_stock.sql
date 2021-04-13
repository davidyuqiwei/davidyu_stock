select * from 
(
    select bankuai,top_stock_name,cnt,
    row_number() over(partition by bankuai order by cnt desc) as rank 
    from
    (
        select bankuai,top_stock_name,count(1) as cnt from
        (
            select distinct *
            from stock_dev.bankuai
            where stock_date in 
            (select dt from stock_dw.stock_index_trade_date)
            and bankuai='水产品'
        )
        group by 1,2
    )
)
where rank<=5 and bankuai='水产品'
order by cnt desc 
limit 30
;





