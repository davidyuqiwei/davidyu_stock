download_date=`date +%Y-%m-%d`

#file1="data_"$download_date".txt"
file1="data.txt"
url=$1
keyname=$2

wget $url -O $file1
sed -i s/data/Data\\n/g $file1
sed -i '1,3d' $file1
sed -i -e s/\\[/{/g  -e s/\\]//g -e s/\;//g -e s/.// -e s/.// -e s/.$// $file1 

echo "keyname        "$keyname
python download_important_owner.py $keyname

# s/.// rm first string


#rm_str="var _dataUrl = \"http://dcfm.eastmoney.com//em_mutisvcexpandinterface/api/js/get?type=NSHDDETAIL&token=70f12f2f4f091e459a279469fe49eca5&cmd=&st=RDATE,NDATE&sr=3&p=1&ps=100&filter=(SHAREHDCODE='80637337')&js={pages:(tp),data:(x)}\";"

#rm_str1=$rm_str"  var OnJVJVrO = "
#echo $rm_str1

#-e s/\\://g
#sed -i s/://g $file1
#sed -i s/[//g $file1
#sed i /^([^\page]*)\page.*$/ $file1
#python shijinglv_json_to_df.py
#rm -rf $file1
#python download_dazongjiaoyi.py $file1

