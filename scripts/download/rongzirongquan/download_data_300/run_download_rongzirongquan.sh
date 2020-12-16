source ~/.bashrc
cd `dirname $0`
#download_date=`date +%Y-%m-%d`
page=$1
url="http://datacenter.eastmoney.com/api/data/get?callback=datatable2031983&type=RPTA_RZRQ_LSHJ&sty=ALL&source=WEB&st=dim_date&sr=-1&p=$page&ps=500&filter=&pageNo=1&_=1607570467755"
# source url :  http://data.eastmoney.com/rzrq/total.html
file1="rongzirongquan_shIndex_"$page".txt"

wget $url -O $file1
sed -i s/data\"/Data\\n/g $file1
sed -i '1d' $file1
sed -i -e s/\\[/{/g  -e s/\\]//g -e s/\;//g -e s/.// -e s/.// -e s/.$// $file1

python d1.py

mv *.txt /home/davidyu/stock/data/raw_data/rongzirongquan/sh_index


