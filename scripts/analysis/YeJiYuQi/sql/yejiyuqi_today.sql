select * from
stock_dev.yejiyuqi
where yeji_predict in ("业绩预盈","业绩大幅上升") and 
stock_date = "${today_date}"
;



