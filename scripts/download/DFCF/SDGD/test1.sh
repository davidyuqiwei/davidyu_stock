file1="shidagudong.txt"
wget "http://xuanguapi.eastmoney.com/Stock/JS.aspx?type=xgq&sty=xgq&token=eastmoney&c=[gbzb06(4|0.3)]&p=1&jn=APEXBIGi&ps=4000&r=1581956855733" -O $file1

sed -i 's/var APEXBIGi=//g' $file1
