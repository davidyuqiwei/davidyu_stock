## 净资产收益率
download_date=`date +%Y-%m-%d`
url="http://xuanguapi.eastmoney.com/Stock/JS.aspx?type=xgq&sty=xgq&token=eastmoney&c=[cz_ylnl01(1|0.05)]&p=1&jn=VVpgTupj&ps=3000&r=1582308669348"
# source url :  http://data.eastmoney.com/dzjy/dzjy_mrmxa.aspx 

file1="data_"$download_date".txt"
wget $url -O $file1
sed -i 's/var VVpgTupj=//g' $file1

python jzcsyl_json_to_df.py
rm -rf $file1
#python download_dazongjiaoyi.py $file1

