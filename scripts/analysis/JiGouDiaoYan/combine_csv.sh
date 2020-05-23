## 
## use:  combine_csv.sh /home/davidyu/stock/data/fenhong all_JiGouDiaoYan.csv
## out:  data save in the $stockdata/tmp  directory
##
source ~/.bashrc

csv_folder=$1
save_file=$2
out_dir=$data_tmp_dir
out_file=$out_dir"/"$save_file
find $csv_folder | xargs cat  *.csv > $out_file

#sed -e '/Close/d'  all_JiGouDiaoYan.csv > all_all_JiGouDiaoYan_v1.csv  
