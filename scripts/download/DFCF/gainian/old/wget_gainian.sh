url="http://xuanguapi.eastmoney.com/Stock/JS.aspx?type=xgq&sty=xgq&token=eastmoney&c=[gfzs8(BK0170)]"
# source url :   http://data.eastmoney.com/xuangu/#Yz1bZ2J6YjAzKDJ8NTAwMHcpXXxzPWdiemIwMygyfDUwMDB3KXxzdD0tMQ==
file1="gainian.txt"

wget $url -O $file1
sed -i 's/var =//g' $file1
