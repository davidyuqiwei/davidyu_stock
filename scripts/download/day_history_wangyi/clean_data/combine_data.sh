out_file="day_history_wangyi.csv"
search_date=`date +%Y-%m-%d`
#search_date="2020-08-18"
save_file=$tmp_data_dir"/day_history_wangyi/"$out_file
cd /home/davidyu/stock/data/day_history_wangyi 
grep -rh $search_date > $save_file


#combine_csv_in_folder.sh "/home/davidyu/stock/data/day_history_wangyi" $out_file
#mv $data_tmp_dir"/"$out_file $tmp_data_dir"/day_history_wangyi"
#sed -i '/stock_index/d' $tmp_data_dir"/day_history_wangyi/"$out_file


