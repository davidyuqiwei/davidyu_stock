source ~/.bashrc
cd `dirname $0`

#stock_index="601398"
while read -r line 
do
    if [[ $line != "code" ]];then
        python download_fin_report.py $line
        sleep 1s
    fi
done < $stock_list_data
#python download_fin_report.py $stock_index
