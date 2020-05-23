# https://vipmoney.eastmoney.com/Crumbs/Content/qqqz/INDEX.HTML?from=groupmessage
download_time=`date +%Y-%m-%d-%H-%M`
file1="IF_"$download_time".txt"
download_date=`date +%Y-%m-%d`
wget https://vipmoney.eastmoney.com/Crumbs/Content/data/IF.js?r=3995 -O $file1

sed -i '1d' $file1
sed -i -e s/\",//g -e s/\"//g -e s/#//g $file1 

save_dir=$stock_data/oumei_future_index/$download_date
if [ ! -d $save_dir ];then
    mkdir $save_dir
fi
## add date time in the end column
sed -i "s/$/&,$download_time/g"  $file1
datatime="data_time"
sed -i "1s/$download_time/$datatime/g" $file1
sed -i '$d' $file1
#echo $save_dir
mv $file1 $save_dir






