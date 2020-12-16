select secucode,sname,sum(tval) as sum_tval
from stock_dev.dazongjiaoyi
where tdate <> 'TDATE' and substr(tdate,1,10)>="2020-08-17"
and substr(tdate,1,10)<="2020-08-18"
group by secucode,sname
order by secucode
limit 10
;

select secucode,sname,tval,zyl as sum_tval
from stock_dev.dazongjiaoyi
where tdate <> 'TDATE' and substr(tdate,1,10)>="2020-08-17"
and substr(tdate,1,10)<="2020-08-18"
order by secucode
limit 10
;

select secucode,sname from
dazongjiaoyi 
where substr(tdate,1,10)="2020-08-18" and 
zyl>0
order by zyl desc 
limit 10
;

select secucode,sname,count(zyl) as zyl_cnt from
dazongjiaoyi 
where tdate <> 'TDATE' and substr(tdate,1,10)>="2020-08-01"
and substr(tdate,1,10)<="2020-08-18" and 
zyl>0
group by secucode,sname
order by zyl_cnt desc
limit 10
;

select * from dadan_dfcf_weekly_dadan_cnt where stock_date = "2020-08-18" and cnt = 1 ;
