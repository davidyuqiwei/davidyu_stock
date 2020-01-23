source ~/.bashrc
file_in=$stock_data/basic_info/stock_basic_info.csv
`awk -F "," '{print $1}' $file_in > stock_list.txt`
#`tail -n 5 $file_in | awk -F "," '{print $1}' > stock_list.txt`  # tail 5 line and print the first column
#echo $stock_list > stock_list.txt
while read -r line 
do 
    if [[ $line != "code" ]];then
        python download_news_report.py $line
        sleep 3s  
    fi
done < stock_list.txt

