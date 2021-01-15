source ~/.bashrc
file_in=$stock_data/basic_info/stock_basic_info.csv
#`awk -F "," '{print $1}' $file_in > stock_list.txt`
#`tail -n 5 $file_in | awk -F "," '{print $1}' > stock_list.txt`  # tail 5 line and print the first column
#echo $stock_list > stock_list.txt
log_file="download.log"
`touch $log_file`
while read -r line 
do 
    if [[ $line != "code" ]];then
        python download_news_report.py $line
        echo $line >> $log_file
        sleep 3s  
    fi
done < stock_list.txt

