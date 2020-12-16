source ~/.bashrc
cd `dirname $0`
while read -r line 
do
    if [[ $line == 60* ]] || [[ $line == 00* ]];then
        python download_day_history_wangyi_today.py $line
        echo $line
        sleep 2.5s
    fi
done < /home/davidyu/stock/data/tmp/stock_list.txt
#done < $stock_data/tmp/"stock_index_list.csv"


#python download_day_history_wy.py 000917
