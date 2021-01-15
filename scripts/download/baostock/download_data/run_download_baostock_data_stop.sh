source ~/.bashrc
cd `dirname $0`
while read -r line 
do
    if [[ $line != "code" ]];then
        python download_baostock_data_today.py $line
        echo $line 
        sleep 2s
    fi
done < stock_stop.sh




