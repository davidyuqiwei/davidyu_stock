out_file="volume_price_distr.csv"
combine_csv_in_folder.sh "/home/davidyu/stock/data/volume_price_distr" $out_file
mv $data_tmp_dir"/"$out_file $tmp_data_dir"/volume_price_distr"

