source ~/.bashrc
cd `dirname $0`
time2=$(date "+%Y-%m-%d-%H%M%S")
echo $time2 > dw.log
spark-sql -f dw_stock_trade_date.sql
#park-sql -f dws_dadan_realtime_ifeng.sql












