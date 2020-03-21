download_date=`date +%Y-%m-%d`
url="http://push2.eastmoney.com/api/qt/clist/get?pn=1&pz=50&po=1&np=1&ut=b2884a393a59ad64002292a3e90d46a5&fltt=2&invt=2&fid=f62&fs=m:90+t:2&stat=1&fields=f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124&rt=52754727&cb=jQuery18301708861095278762_1582641833533&_=1582641834285"
# source url :  http://data.eastmoney.com/bkzj/hy.html

file1="data_"$download_date".txt"

wget $url -O $file1
sed -i s/diff/Data\\n/g $file1
sed -i '1d' $file1
sed -i -e s/\\[/{/g  -e s/\\]//g -e s/\;//g -e s/.// -e s/.// -e s/.$// $file1
#sed -i 's/\\]}});//g' $file1

#python shijinglv_json_to_df.py
#rm -rf $file1
#python download_dazongjiaoyi.py $file1

