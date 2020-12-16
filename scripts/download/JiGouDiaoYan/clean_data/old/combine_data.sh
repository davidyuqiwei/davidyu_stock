out_file="jigoudiaoyan.csv"
combine_csv_in_folder.sh "/home/davidyu/stock/data/JiGouDiaoYan" $out_file
mv $data_tmp_dir"/"$out_file $tmp_data_dir"/JiGouDiaoYan"
theFile=$tmp_data_dir"/JiGouDiaoYan/"$out_file
sed -i -e s/^/HEAD/g $theFile
sed -i -e s/,,/,999,/g $theFfile
sed -i -e s/,,/,/g $theFile
sed -i -e s/特定对象调研,会议电话,/会议电话,/g $theFile



