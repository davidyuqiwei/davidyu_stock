year=`date +%Y`
#echo $year
out_file=$year".csv"
combine_csv_in_folder.sh "/home/davidyu/stock/data/baostock" $out_file
mv $data_tmp_dir"/"$out_file $tmp_data_dir"/baostock"

