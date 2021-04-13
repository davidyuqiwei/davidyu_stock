
select secucode as stock_index,count(1) as dazongjiaoyi_cnt,sum(TVAL) as tval_sum
from
(
    select distinct TDATE,SECUCODE,SNAME,PRICE,TVOL,TVAL,BUYERCODE,BUYERNAME,SALESCODE,SALESNAME,Stype,Unit,
    RCHANGE,CPRICE,YSSLTAG,Zyl,Cjeltszb,RCHANGE1DC,RCHANGE5DC,RCHANGE10DC,RCHANGE20DC,TEXCH,stock_date,day from 
    from stock_dev.dazongjiaoyi 
    where stock_date >="2020-11-01" and stock_date<="2020-11-07"
)
group by secucode
order by sum(TVAL)  desc
;



