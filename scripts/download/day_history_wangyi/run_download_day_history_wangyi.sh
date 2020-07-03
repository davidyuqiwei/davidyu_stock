source ~/.bashrc
cd `dirname $0`
while read -r line 
do
    if [[ $line != "code" ]];then
        python download_day_history_wangyi.py $line
        sleep 10s
    fi
done < $1
#done < $stock_data/tmp/"stock_index_list.csv"


#python download_day_history_wy.py 000917
