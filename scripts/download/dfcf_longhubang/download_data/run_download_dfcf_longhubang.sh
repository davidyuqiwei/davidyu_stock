source ~/.bashrc
cd `dirname $0`
download_date=`date +%Y-%m-%d`

url1="http://data.eastmoney.com/DataCenter_V3/stock2016/TradeDetail/pagesize=200,page=1,sortRule=-1,sortType=,startDate=2021-03-12,endDate=2021-03-12,gpfw=0,js=var%20data_tab_1.html?rt=26928868"

save_file="longhubang_"$download_date".txt"
file1="longhubang_"$download_date".txt"

wget $url1 -O $save_file

sed -i s/data/Data\\n/g $file1
sed -i '1,2d' $file1
sed -i -e s/\\[/{/g  -e s/\\]//g -e s/\;//g -e s/.// -e s/.// -e s/.$// $file1

python parse_to_df.py $file1
mv *.txt $stock_data"/dfcf_longhubang/raw_data"
mv *.csv $stock_data"/dfcf_longhubang/parse_data"
