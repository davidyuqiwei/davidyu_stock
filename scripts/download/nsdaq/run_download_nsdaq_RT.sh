source ~/.bashrc
cd `dirname $0`

download_time=`date +%Y-%m-%d-%H-%M`
download_date=`date +%Y-%m-%d`
file1="nsdaq_"$download_time".txt"
url="https://w.sinajs.cn/?_=0.8646089742362744&list=gb_$ixic,gb_ixic"

wget $url -O $file1
#iconv $file1 -f utf-8 -t gb2312 -o $file1
sed -i '1d' $file1
sed -i 's/var hq_str_gb_ixic=//g' $file1
sed -i -e s/\",//g -e s/\"//g -e s/#//g -e s/\;//g -e s/\"//g $file1
## add date time in the end column
sed -i "s/$/&,$download_time/g"  $file1
datatime="data_time"
sed -i "1s/$download_time/$datatime/g" $file1
save_dir=$stock_data/nsdaq/$download_date
if [ ! -d $save_dir  ];then
    mkdir $save_dir
fi
mv $file1 $save_dir





#sed -i s/纳斯达克,/\\n/g $file1
#iconv $file1 -f iso-8859-1  -t gb2312 -o a.log

