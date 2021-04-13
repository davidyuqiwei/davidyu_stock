source ~/.bashrc
cd `dirname $0`
file_out="../data/dadan_realtime_daily_max.csv"
spark-sql --hiveconf hive.cli.print.header=true -f ../sql/dadan_realtime.sql > $file_out
sed -i 's/[\t]/,/g' $file_out

file_out="../data/dadan_realtime_daily_max_sell.csv"
spark-sql --hiveconf hive.cli.print.header=true -f ../sql/dadan_realtime_sell.sql > $file_out
sed -i 's/[\t]/,/g' $file_out

file_out="../data/dadan_realtime_daily_sum.csv"
spark-sql --hiveconf hive.cli.print.header=true -f ../sql/dadan_realtime_daily_sum.sql > $file_out
sed -i 's/[\t]/,/g' $file_out

#Rscript --slave --no-save --no-restore trans_dadan_data.r
