file_out="bankuai_zde.csv"
spark-sql --hiveconf hive.cli.print.header=true -f bankuai_zde.sql> $file_out
sed -i 's/[\t]/,/g' $file_out

