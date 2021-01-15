source ~/.bashrc
cd `dirname $0`
# souce url: http://data.eastmoney.com/stockcomment/002594.html
download_date=`date +%Y-%m-%d`

file1="tmp.txt"
file2="hangye_sina_"$download_date".txt"
url1="http://money.finance.sina.com.cn/q/view/newFLJK.php?param=industry"
wget $url1 -O $file1
#python download_zhulikongpan.py

sed -i 's/var S_Finance_bankuai_industry = /Data\\\n/g' $file1
sed -i '1d' $file1
#sed -i -e s/\\[/{/g  -e s/\\]//g -e s/\;//g -e s/.// -e s/.// -e s/.$// $file1
iconv -f cp936 -t utf-8 $file1 > $file2
python parse_data.py $file2

rm -rf *.txt
mv *.csv $stock_data"/bankuai_sina"

