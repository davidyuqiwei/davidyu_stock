download_date=`date +%Y-%m-%d`

source ~/.bashrc
cd `dirname $0`
#file_in=$stock_data/basic_info/stock_basic_info.csv
#`awk -F "," '{print $1}' $file_in > stock_list.txt`
#./run_get_stock_list.sh
while read -r line 
do
    if [[ $line == 60* ]];then
        stock_index="SH"$line
    fi
    if [[ $line == 00* ]] || [[ $line == 30* ]];then
        stock_index="SZ"$line
    fi
        echo $stock_index
        file1=$line"_hexinticai.txt"
        url1="http://f10.eastmoney.com/CoreConception/CoreConceptionAjax?code="$stock_index
        wget $url1 -O $file1
        mv *.txt /home/davidyu/stock/data/dfcf_hexinticai
        sleep 10.51s
done <$stock_list_data
