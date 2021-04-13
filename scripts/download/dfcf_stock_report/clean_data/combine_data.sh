out_file="dfcf_stock_report.csv"
combine_csv_in_folder.sh "/home/davidyu/stock/data/dfcf_stock_report" $out_file
mv $data_tmp_dir"/"$out_file $tmp_data_dir"/dfcf_stock_report"

