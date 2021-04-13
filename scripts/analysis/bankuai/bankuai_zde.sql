select bankuai,stock_date,round(zhangdiee,3) as zhangdiee
from stock_dev.bankuai
where stock_date >=to_date(date_sub(now(),50))  and stock_date<= to_date(now())
;
