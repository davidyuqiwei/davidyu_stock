## 
## use:  combine_csv.sh /home/davidyu/stock/data/JiGouDiaoYan all_JiGouDiaoYan.csv
## out:  data save in the $stockdata/tmp  directory
##
source ~/.bashrc

csv_folder=$1
save_file=$2
out_dir=$tmp_data_dir
out_file=$out_dir"/JiGouDiaoYan/"$save_file
find $csv_folder | xargs cat  *.csv > $out_file
echo "save file $out_file"
#sed -i -e s/^/HEAD/g $out_file
sed -i -e s/,,/,999,/g -e s/,,/,999,/g $out_file
#sed -i -e s/,,/,/g $out_file
sed -i -e s/特定对象调研,会议电话,/会议电话,/g $out_file
#-e s/[[:space:]][[:space:]]*//g $out_file

#sed -i -e s/ //g $out_file
#sed -e '/Close/d'  all_JiGouDiaoYan.csv > all_all_JiGouDiaoYan_v1.csv  
