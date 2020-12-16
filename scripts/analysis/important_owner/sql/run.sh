file_out="data.out"
spark-sql -f hk_increase_list.sql > $file_out
sed -i 's/[\t]/,/g' $file_out


