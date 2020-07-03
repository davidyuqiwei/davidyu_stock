source ~/.bashrc
cd `dirname $0`
download_date=`date +%Y-%m-%d`
url="http://push2.eastmoney.com/api/qt/clist/get?pn=1&pz=30000&po=1&np=1&ut=b2884a393a59ad64002292a3e90d46a5&fltt=2&invt=2&fid0=f4001&fid=f62&fs=m:0+t:6+f:!2,m:0+t:13+f:!2,m:0+t:80+f:!2,m:1+t:2+f:!2,m:1+t:23+f:!2,m:0+t:7+f:!2,m:1+t:3+f:!2&stat=1&fields=f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124&rt=52770721&cb=jQuery18304435578038144832_1583121630507&_=1583121630983"
# source url :   http://data.eastmoney.com/zjlx/detail.html

file1="data_"$download_date".txt"
wget $url -O $file1
sed -i s/diff/Data\\n/g $file1
sed -i '1d' $file1
sed -i -e s/\\[/{/g  -e s/\\]//g -e s/\;//g -e s/.// -e s/.// -e s/.$// $file1
python download_dadan_DFCF.py
rm -rf $file1
#sed -i 's/var PcBIadJC=//g' $file1

#python shijinglv_json_to_df.py
#python download_dazongjiaoyi.py $file1

