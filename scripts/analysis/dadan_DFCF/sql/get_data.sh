file_out="one_stock_data.csv"
stock_index=$1
spark-sql \
    --hiveconf hive.cli.print.header=true \
    -f get_one.sql \
    -d stock_index=$stock_index > $file_out
sed -i 's/[\t]/,/g' $file_out
