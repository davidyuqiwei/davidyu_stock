#http://data.eastmoney.com/yjfp/
download_date=`date +%Y-%m-%d`

source ~/.bashrc
cd `dirname $0`

while read -r line 
do
        echo $stock_index
        file1=$line"_fenhong.txt"
        url1="http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get?callback=jQuery1123017395947543722357_1615894889025&st=YAGGR&sr=-1&ps=5000&p=1&type=DCSOBS&js=%7B%22data%22%3A(x)%2C%22pages%22%3A(tp)%7D&token=894050c76af8597a853f5b408b759f5d&filter=(ReportingPeriod%3D%5E$line%5E)"
        wget $url1 -O $file1
        mv *.txt /home/davidyu/stock/data/fenhong/raw_data
        sleep 6.5s
done <date_in.sh
#done <$stock_list_data
python parse_data.py

#wget http://f10.eastmoney.com/BonusFinancing/BonusFinancingAjax?code=SH601398
