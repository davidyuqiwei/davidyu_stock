url="http://push2ex.eastmoney.com/getStockFenShi?pagesize=3000&ut=7eea3edcaed734bea9cbfc24409ed989&dpt=wzfscj&cb=jQuery112409157883647752747_1608038109103&pageindex=0&id=6013981&sort=1&ft=5&code=601398&market=1&_=1608038109108"
file1="test.txt"
wget $url -O $file1

sed -i s/data/Data\\n/g $file1
sed -i '1d' $file1
sed -i '1d' $file1
sed -i -e s/\\[/{/g  -e s/\\]//g -e s/\;//g -e s/.// -e s/.// -e s/.$// $file1
