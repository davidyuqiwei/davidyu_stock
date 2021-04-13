select lpad(stock_index,6,'0') from
(
    select stock_index from
    (
        select stock_index,count(distinct jijin_name) 
        from
        stock_dev.jijin 
        where stock_date = '2020-09-30'
        group by stock_index
        order by count(distinct jijin_name) desc
        limit 200
    )
    union all
    select distinct stock_index
    from stock_dev.liutong_owner t1
    where owner_name rlike '全国社保|香港中央结算有限公司|挪威中央银行|阿布达比|UBS|澳门金融|MORGAN|不列颠|加拿大年金|Black|Citi|社会保障' and dt='2020-09-30'
)
where stock_index not like '30%' or stock_index not like '68%'
;


