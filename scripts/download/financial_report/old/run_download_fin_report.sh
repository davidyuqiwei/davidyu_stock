source ~/.bashrc
file_in=$stock_data/basic_info/stock_basic_info.csv

#stock_index="601398"
while read -r line 
do
    if [[ $line != "code" ]];then
        python download_fin_report.py $line
        sleep 0.5s
    fi
done < stock_list.txt
#python download_fin_report.py $stock_index
