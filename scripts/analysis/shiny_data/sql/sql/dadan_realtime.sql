select stock_index,stock_name,dt,status,
daily_max_money,price
from stock_dws.dadan_realtime_daily_max
where dt>=to_date(date_sub(now(),60)) and dt <=now()
and status="买盘"
;
