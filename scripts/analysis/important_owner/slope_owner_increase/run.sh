file_out="data.out"
spark-sql -f hk_increase_list.sql > $file_out
sed -i 's/[\t]/,/g' $file_out

input_file=$file_out
predict_slope_days=60
slope_out_file="data_slope_"$predict_slope_days".csv"

touch $slope_out_file
sh slope_calculate.sh $input_file $slope_out_file $predict_slope_days



