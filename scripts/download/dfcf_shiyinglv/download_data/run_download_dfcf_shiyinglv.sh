# http://data.eastmoney.com/xuangu/#Yz1bY3pfZ3p6YjAxKDR8LTk5OSldfHM9Y3pfZ3p6YjAxKDR8LTk5OSl8c3Q9MQ==

file1="shiyinglv.txt"
url1="http://xuanguapi.eastmoney.com/Stock/JS.aspx?type=xgq&sty=xgq&token=eastmoney&c=[cz_gzzb01(4|-999)]&p=1&jn=wSiEXzqI&ps=5000&s=cz_gzzb01(4|-999)&st=-1&r=1615117717234"

wget $url1 -O $file1
sed -i 's/var wSiEXzqI=//g' $file1

python parse_data.py
