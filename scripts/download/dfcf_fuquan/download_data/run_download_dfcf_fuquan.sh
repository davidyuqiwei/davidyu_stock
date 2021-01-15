download_date=`date +%Y-%m-%d`

source ~/.bashrc
cd `dirname $0`
#file_in=$stock_data/basic_info/stock_basic_info.csv
#`awk -F "," '{print $1}' $file_in > stock_list.txt`
#./run_get_stock_list.sh
while read -r line 
do
    if [[ $line == 60* ]];then
        stock_index="1."$line
    fi
    if [[ $line == 00* ]] || [[ $line == 30* ]];then
        stock_index="0."$line
    fi
        echo $stock_index
        file1=$line"_fuquan.txt"
        url1="http://93.push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery112409381248828282374_1609254428957&secid=$stock_index&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61&klt=101&fqt=1&end=20500101&lmt=300&_=1609254428987"
        wget $url1 -O $file1
        mv *.txt /home/davidyu/stock/data/dfcf_fuquan/raw_data
        sleep 3.5s
done <$stock_list_data



