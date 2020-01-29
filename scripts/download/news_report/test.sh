#source ~/.bashrc
#file_in=$stock_data/basic_info/stock_basic_info.csv
#`awk -F "," '{print $1}' $file_in > stock_list.txt`
log_file="download.log"
`touch $log_file`
a1="tt"
echo $a1 >> $log_file
