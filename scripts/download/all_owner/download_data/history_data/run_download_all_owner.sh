#http://data.eastmoney.com/gdfx/HoldingDetail.html
source ~/.bashrc
cd `dirname $0`
file1="test.txt"
url="http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?callback=jQuery1123033332600084176844_1615001606339&st=NDATE&sr=-1&ps=300000&p=1&js=%7Bpages%3A(tp)%2Cdata%3A(x)%7D&token=70f12f2f4f091e459a279469fe49eca5&type=NSHDDETAILLA"

wget $url -O $file1
python parse_data.py

#rm -rf $file1


