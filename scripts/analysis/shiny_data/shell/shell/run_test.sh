source ~/.bashrc
cd `dirname $0`

file_out="../data/dadan_realtime_daily_sum.csv"
spark-sql --hiveconf hive.cli.print.header=true -f ../sql/dadan_realtime_daily_sum.sql > $file_out
sed -i 's/[\t]/,/g' $file_out
