file_out="rzrq_close.csv"
spark-sql --hiveconf hive.cli.print.header=true -f rzrq_close.sql> $file_out
sed -i 's/[\t]/,/g' $file_out
