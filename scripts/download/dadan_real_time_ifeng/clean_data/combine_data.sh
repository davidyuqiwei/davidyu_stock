source ~/.bashrc
cd `dirname $0`
data_dir=$stock_data"/dadan_real_time_ifeng"
download_date=`date +%Y-%m-%d`
save_dir=$data_dir"/combine_data"

out_file=$download_date".csv"
combine_csv_in_folder.sh "/home/davidyu/stock/data/dadan_real_time_ifeng/"$download_date $out_file
#mv $data_tmp_dir"/"$out_file $tmp_data_dir"/dadan_real_time_ifeng"
mv $data_tmp_dir"/"$out_file $save_dir

