file_out="owner_select_data.csv"
spark-sql --hiveconf hive.cli.print.header=true -f select_stock_index.sql> $file_out
sed -i 's/[\t]/,/g' $file_out
sed -i '1d' $file_out
mv $file_out /home/davidyu/stock/data/common



