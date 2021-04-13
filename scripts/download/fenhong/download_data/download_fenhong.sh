download_date=`date +%Y-%m-%d`

source ~/.bashrc
cd `dirname $0`

while read -r line 
do
    if [[ $line == 60* ]];then
        stock_index="SH"$line
    fi
    if [[ $line == 00* ]] || [[ $line == 30* ]];then
        stock_index="SZ"$line
    fi
        echo $stock_index
        file1=$line"_fenhong.txt"
        url1="http://f10.eastmoney.com/BonusFinancing/BonusFinancingAjax?code="$stock_index
        wget $url1 -O $file1
        mv *.txt /home/davidyu/stock/data/fenhong/raw_data
        sleep 6.5s
done <$stock_list_data
#done <$stock_list_data


#wget http://f10.eastmoney.com/BonusFinancing/BonusFinancingAjax?code=SH601398
