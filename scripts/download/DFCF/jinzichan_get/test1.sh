file1="jinzichan_ratio.txt"
wget "http://xuanguapi.eastmoney.com/Stock/JS.aspx?type=xgq&sty=xgq&token=eastmoney&c=[cz_ylnl01(1|0.2)]&p=1&jn=fJrXYcPa&ps=1000&r=1582003227234" -O $file1

sed -i 's/var fJrXYcPa=//g' $file1
