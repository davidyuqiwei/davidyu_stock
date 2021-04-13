out_file="dfcf_hexinticai.csv"
combine_csv_in_folder.sh "/home/davidyu/stock/data/dfcf_hexinticai/parse_data" $out_file
mv $data_tmp_dir"/"$out_file $tmp_data_dir"/dfcf_hexinticai"

