out_file="fenhong.csv"
combine_csv_in_folder.sh "/home/davidyu/stock/data/fenhong/parse_data" $out_file
mv $data_tmp_dir"/"$out_file $tmp_data_dir"/fenhong"

