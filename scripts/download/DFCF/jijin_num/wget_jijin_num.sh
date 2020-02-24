url="http://xuanguapi.eastmoney.com/Stock/JS.aspx?type=xgq&sty=xgq&token=eastmoney&c=[jgcg02]&p=1&jn=xujXylKN&ps=5000&s=jgcg02&st=-1&r=1582209308674"
# source url :  http://data.eastmoney.com/dzjy/dzjy_mrmxa.aspx
file1="jijin_num.txt"

wget $url -O $file1
sed -i 's/var xujXylKN=//g' $file1
