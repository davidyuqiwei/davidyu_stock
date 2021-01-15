download_date=`date +%Y-%m-%d`
out_file="stock_shizhi.csv"
combine_csv_in_folder.sh "/home/davidyu/stock/data/stock_shizhi/parse_data" $out_file
cp $data_tmp_dir"/"$out_file /home/davidyu/stock/data/history_data/stock_shizhi # save history folder
mv $data_tmp_dir"/"$out_file $tmp_data_dir"/stock_shizhi"  # to csv folder
rm -rf /home/davidyu/stock/data/stock_shizhi/parse_data/*.txt

