download_date=`date +%Y-%m-%d`
url="http://push2.eastmoney.com/api/qt/clist/get?pn=1&pz=500&po=1&np=1&fields=f12,f13,f14,f62&fid=f62&fs=m:90+t:3&ut=b2884a393a59ad64002292a3e90d46a5&cb=jQuery183025601260987668906_1584755440696&_=1584755442502"
# source url :  http://data.eastmoney.com/bkzj/gn.html

file1="data_"$download_date".txt"
wget $url -O $file1
sed -i 's/var PcBIadJC=//g' $file1


file1="data_"$download_date".txt"
wget $url -O $file1
sed -i s/diff/Data\\n/g $file1
sed -i '1d' $file1
sed -i -e s/\\[/{/g  -e s/\\]//g -e s/\;//g -e s/.// -e s/.// -e s/.$// $file1



#python shijinglv_json_to_df.py
#rm -rf $file1


#python download_dazongjiaoyi.py $file1

