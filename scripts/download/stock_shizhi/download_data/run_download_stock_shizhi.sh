download_date=`date +%Y-%m-%d`

source ~/.bashrc
cd `dirname $0`
while read -r line 
do
    if [[ $line == 60* ]];then
        stock_index="sh"$line
    fi
    if [[ $line == 00* ]] || [[ $line == 30* ]];then
        stock_index="sz"$line
    fi
    file1=$line"_shizhi.txt"
    url1="https://vip.stock.finance.sina.com.cn/quotes_service/api/jsonp.php/var%20moneyFlowData=/MoneyFlow.ssi_ssfx_flzjtj?daima=$stock_index&gettime=1"
    wget $url1 -O $file1
    sh clean_data.sh $file1
    mv *.txt /home/davidyu/stock/data/stock_shizhi/raw_data
    sleep 4.5s
done < $stock_list_data
#done < stock_list_data_test.sh
#mv *.txt /home/davidyu/stock/data/stock_shizhi/raw_data
