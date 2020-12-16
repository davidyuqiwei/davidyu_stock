file_out="bankuai_test_data.csv"
spark-sql --hiveconf hive.cli.print.header=true -f bankuai_test_data.sql > $file_out
sed -i 's/[\t]/,/g' $file_out

