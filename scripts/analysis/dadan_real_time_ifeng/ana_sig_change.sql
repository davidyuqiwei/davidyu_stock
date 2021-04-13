select t2.ticai,count(distinct t1.stock_index) as cnt,
concat_ws(',',collect_set(t1.stock_name)) as stock_name_list,
concat_ws(',',collect_set(t1.stock_index)) as stock_index_list
 from 
(   
    select stock_index,stock_name,
    max(case when status='买盘' then money_max_1 else 0 end) as buy1,
    max(case when status='卖盘' then money_max_1 else 0 end) as sell1,
    max(case when status='买盘' then money_max_13 else 0 end) as buy13
    from stock_test.dadan_realtime_period_max
    group by 1,2
    having buy1>sell1 and buy1>buy13*2
) t1
left join stock_dev.hexinticai t2
on t1.stock_index=t2.stock_index
group by 1
order by 2 desc 
limit 50
; 
