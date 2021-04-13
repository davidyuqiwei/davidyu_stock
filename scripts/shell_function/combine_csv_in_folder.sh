## 
## use:  combine_csv_in_folder.sh /home/davidyu/stock/data/fenhong all_bankuai.csv
## out:  data save in the $stockdata/tmp  directory
##
source ~/.bashrc

csv_folder=$1
save_file=$2
out_dir=$data_tmp_dir
out_file=$out_dir"/"$save_file
cd $csv_folder
#find $csv_folder | xargs cat  *.csv *.txt > $out_file 
find ./ -regex ".*\.txt\|.*\.csv" -exec cat {} \; >  $out_file
#cat  *.csv *.txt > $out_file 
echo "the data is in "$out_dir

#sed -e '/0,1,2/d'  %s/all.csv 
#sed -e '/基金名称/d'  all_jijin.csv > jijin.csv
