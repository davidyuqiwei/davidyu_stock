download_date=`date +%Y-%m-%d`
url="http://xuanguapi.eastmoney.com/Stock/JS.aspx?type=xgq&sty=xgq&token=eastmoney&c=[cz_gzzb02(2|20)]&p=1&jn=PcBIadJC&ps=5000&r=1582306269701"
# source url :   http://data.eastmoney.com/dzjy/dzjy_mrmxa.aspx

file1="data_"$download_date".txt"
wget $url -O $file1
sed -i 's/var PcBIadJC=//g' $file1

#python shijinglv_json_to_df.py
#rm -rf $file1
#python download_dazongjiaoyi.py $file1

