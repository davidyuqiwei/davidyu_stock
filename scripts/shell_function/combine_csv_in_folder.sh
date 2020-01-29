## 
## use:  combine_csv_in_folder.sh /home/davidyu/stock/data/fenhong
## out:  data save in the $stockdata/tmp  directory
##
source ~/.bashrc
out_dir=$data_tmp_dir
out_file=$out_dir"/2020_01_23.csv"
csv_folder=$1
find $csv_folder | xargs cat  *.csv > $out_file 
