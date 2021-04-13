file_out="dazongjiaoyi_select_data.csv"
spark-sql --hiveconf hive.cli.print.header=true -f stat_v1.sql > $file_out
sed -i 's/[\t]/,/g' $file_out
#sed -i '1d' $file_out
#mv $file_out /home/davidyu/stock/data/common
