source ~/.bashrc
cd `dirname $0`
#download_date=`date +%Y-%m-%d -d "-1day"`
download_date=`date +%Y-%m-%d`
while read -r line 
do
    if [[ $line == 60* ]] || [[ $line == 00* ]] || [[ $line == 30*  ]];then
        python download_volume_price_distr.py $line $download_date
        echo $line
        sleep 2.5s
    fi
done < $stock_list_data

