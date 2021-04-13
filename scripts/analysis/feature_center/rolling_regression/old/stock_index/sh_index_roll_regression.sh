
input_file=$stock_data"/test/stock_index_daily_data.csv"
out_file=$stock_data"/test/stock_index_rollreg_result.csv"


python stock_roll_regression.py $input_file $out_file



