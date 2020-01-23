source ~/.bashrc
file_in=$stock_data/basic_info/stock_basic_info.csv
`awk -F "," '{print $1}' $file_in > stock_list.txt`
#echo $stock_list > stock_list.txt
while read -r line 
do 
    if [[ $line != "code" ]];then
        echo $line
        sleep 3s  
    fi
done < stock_list.txt

