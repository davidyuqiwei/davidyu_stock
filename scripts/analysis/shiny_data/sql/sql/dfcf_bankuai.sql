select t1.dt,t1.bankuai_name,t1.change_ratio,t2.top_stock_name,t2.data_type
from stock_dev.dfcf_bankuai t1
left join 
(
    select bankuai_name,data_type,
    concat_ws('_' , collect_set(concat(lead_stock_name,':',cnt))) as top_stock_name 
    from
    (
        select bankuai_name,data_type,lead_stock_name,cnt,
        row_number() over(partition by bankuai_name,data_type order by cnt desc) as rank
        from
        (
            select bankuai_name,data_type,lead_stock_name,count(lead_stock_name) as cnt 
            from
            (
                select distinct *
                from stock_dev.dfcf_bankuai
                where dt in
                (select dt from stock_dw.stock_index_trade_date)
            )
            group by 1,2,3
        )
    )
    where rank<=2 
    group by 1,2
) t2
on t1.bankuai_name=t2.bankuai_name and t1.data_type=t2.data_type
where t1.dt <> 'dt'
;

