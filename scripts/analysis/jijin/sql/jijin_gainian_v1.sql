select gainian,stock_date,gainian_cnt,gainian_cnt_rank from
(
    select gainian,stock_date,gainian_cnt,
    row_number() over (partition by stock_date order by gainian_cnt desc ) as gainian_cnt_rank
    from
    (
        select gainian,stock_date,count(1) as gainian_cnt
        from
        (
            select
            distinct
            t1.jijin_name,
            t1.stock_index,
            t1.stock_date,
            t2.gainian,
            t3.name
            from
            stock_dev.jijin t1
            left join
            stock_dev.gainian_bankuai t2
            on t1.stock_index=t2.stock_index
            left join stock.stock_index t3
            on t1.stock_index = t3.code
            where t1.stock_date in ('2020-09-30','2020-06-30','2020-03-31','2019-12-31','2019-09-30','2019-06-30')
        ) a
    group by gainian,stock_date
    ) b
) c
where gainian_cnt_rank<=20 and gainian is not null
order by stock_date,gainian_cnt desc
;
