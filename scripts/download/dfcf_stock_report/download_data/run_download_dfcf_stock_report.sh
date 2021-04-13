download_date=`date +%Y-%m-%d`
# source
# http://data.eastmoney.com/report/stock.jshtml
source ~/.bashrc
cd `dirname $0`
start_date="2012-01-01"
end_date="2021-01-17"
save_dir=$stock_data"/dfcf_stock_report/raw_data"
while read -r line
do
    url1="http://reportapi.eastmoney.com/report/list?cb=datatable6425962&industryCode=*&pageSize=50&industry=*&rating=&ratingChange=&beginTime=$start_date&endTime=$end_date&pageNo=$line&fields=&qType=0&orgCode=&code=*&rcode=&p=5&pageNum=5&_=161089643217"
    file1="dfcf_stock_report_"$start_date"_"$end_date"_"$line".txt"
    wget $url1 -O $file1
    #clean_data.sh $file1
    #python parse_to_df.py $file1
    mv *.txt $save_dir
    sleep 5s
done<page_list.sh

