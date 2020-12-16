source ~/.bashrc
cd `dirname $0`
#download_date=`date +%Y-%m-%d`
download_date=$1
page=$2
url="http://datacenter.eastmoney.com/api/data/get?callback=datatable3319302&type=RPTA_WEB_RZRQ_GGMX&sty=ALL&source=WEB&p=$page&ps=5000&st=RZJME&sr=-1&filter=(date%3D%27$download_date%27)&pageNo=1&_=1607562655494"
# source url :  http://data.eastmoney.com/rzrq/detail/all.html
file1="rongzirongquan_"$download_date"_"$page".txt"

wget $url -O $file1
sed -i s/data\"/Data\\n/g $file1
sed -i '1d' $file1
sed -i -e s/\\[/{/g  -e s/\\]//g -e s/\;//g -e s/.// -e s/.// -e s/.$// $file1

python d1.py

mv *.txt /home/davidyu/stock/data/raw_data/rongzirongquan


