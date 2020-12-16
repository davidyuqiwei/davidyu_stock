out_file="day_history_wangyi.csv"
combine_csv_in_folder.sh "/home/davidyu/stock/data/day_history_wangyi" $out_file
mv $data_tmp_dir"/"$out_file $tmp_data_dir"/day_history_wangyi"

sed -i '/stock_index/d' $tmp_data_dir"/day_history_wangyi/"$out_file


