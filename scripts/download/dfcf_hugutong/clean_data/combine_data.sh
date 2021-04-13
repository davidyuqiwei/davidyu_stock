download_date=`date +%Y-%m-%d`
out_file="dfcf_hugutong_"$download_date".csv"
combine_csv_in_folder.sh "/home/davidyu/stock/data/dfcf_hugutong/parse_data" $out_file
mv $data_tmp_dir"/"$out_file $stock_data"/history_data/dfcf_hugutong"

