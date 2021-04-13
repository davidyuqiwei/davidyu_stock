select * from stock_raw.dadan_dfcf
where dt>=to_date(date_sub(now(),30))
;
