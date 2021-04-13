source ~/.bashrc
cd `dirname $0`
file_out="../data/stock_name.csv"
file_out2=$stock_data"/common/stock_name.csv"
spark-sql --hiveconf hive.cli.print.header=true -f ../sql/stock_name.sql > $file_out
sed -i 's/[\t]/,/g' $file_out
sed -i 's/[\t]/,/g' $file_out2
#script --slave --no-save --no-restore trans_dadan_data.r
