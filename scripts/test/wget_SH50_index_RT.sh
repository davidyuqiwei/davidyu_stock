source ~/.bashrc
cd `dirname $0`
url="https://hq.sinajs.cn/?_=0.6491978721356266&list=sh000016"
file1="data_out_a50.txt"
now_date=$(date "+%Y-%m-%d")
save_folder="SH_index_RT"
save_file="SH50_index_RT_"$now_date".txt"
#save_file=$stock_data/$save_folder/$save_file
save_file=$save_file
echo $save_file
wget $url -O $file1

sed -i 's/var hq_str_s_sh000016="//g' $file1
sed -i 's/,/\n/g' $file1
touch $save_file
a50_value=`cat $file1 | sed -n '4p'`
vol_value=`cat $file1 | sed -n '9p'`
money_value=`cat $file1 | sed -n '10p'`
now_time=$(date "+%Y-%m-%d %H:%M:%S")
out_string=$a50_value","$vol_value","$money_value","$now_time

#echo $out_string
echo $out_string >> $save_file 


