url="http://xuanguapi.eastmoney.com/Stock/JS.aspx?type=xgq&sty=xgq&token=eastmoney&c=[cz_hqzb01]&p=1&jn=QAhPgnED&ps=1000&s=cz_hqzb01&st=-1&r=158216"
# source url :  http://data.eastmoney.com/dzjy/dzjy_mrmxa.aspx
file1="pofa.txt"

wget $url -O $file1
sed -i 's/var QAhPgnED=//g' $file1
