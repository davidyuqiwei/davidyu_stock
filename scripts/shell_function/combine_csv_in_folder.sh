cat
## 
## use:  combine_csv_in_folder.sh /home/davidyu/stock/data/fenhong
## out:  data save in the $stockdata/tmp  directory
##
source ~/.bashrc

csv_folder=$1
save_file="all_jijin.csv"
out_dir=$data_tmp_dir
out_file=$out_dir"/"$save_file
find $csv_folder | xargs cat  *.csv > $out_file 


#sed -e '/0,1,2/d'  %s/all.csv 
#sed -e '/基金名称/d'  all_jijin.csv > jijin.csv
