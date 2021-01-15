source ~/.bashrc
cd `dirname $0`
#file_in=$stock_data/basic_info/stock_basic_info.csv
#`awk -F "," '{print $1}' $file_in > stock_list.txt`
#./run_get_stock_list.sh
while read -r line 
do
    if [[ $line != "code" ]];then
        python download_baostock_data.py $line
        #echo $line 
        sleep 2s
    fi
done <$stock_list_data




