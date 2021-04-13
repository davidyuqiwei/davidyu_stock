source ~/.bashrc
cd `dirname $0`
time2=$(date "+%Y-%m-%d-%H%M%S")
echo $time2 > a.log
spark-sql -f clean_dadan_dfcf.sql
spark-sql -f clean_dazongjiaoyi.sql
spark-sql -f clean_important_owner.sql
spark-sql -f clean_stock_base.sql
spark-sql -f clean_dadan_realtime_ifeng.sql
spark-sql -f clean_sh_index.sql


spark-sql -f dws_dadan_realtime_ifeng.sql
spark-sql -f dws_dadan_realtime_period.sql











