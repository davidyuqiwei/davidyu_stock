url="http://xuanguapi.eastmoney.com/Stock/JS.aspx?type=xgq&sty=xgq&token=eastmoney&c=[gbzb03(2|5000w)]&p=1&jn=QponjoJU&ps=1000&s=gbzb03(2|5000w)&st=-1&r=1582035861681"
# source url :   http://data.eastmoney.com/xuangu/#Yz1bZ2J6YjAzKDJ8NTAwMHcpXXxzPWdiemIwMygyfDUwMDB3KXxzdD0tMQ==
file1="xiaopangu.txt"

wget $url -O $file1
sed -i 's/var QponjoJU=//g' $file1
