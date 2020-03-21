source ~/.bashrc
#python download_jijin.py 601398
while read -r line 
do
    if [[ $line != "code" ]];then
        python download_day_history_yahoo.py $line
        sleep 2.5s
    fi
done < stock_list.txt

