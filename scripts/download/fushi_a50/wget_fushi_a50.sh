source ~/.bashrc
cd `dirname $0`
url="https://hq.sinajs.cn/?_=0.3592639216974387&list=hf_CHA50CFD,hf_CHA50CFD_i"
file1="data_out.txt"
now_date=$(date "+%Y-%m-%d")
save_folder="fushi_a50"
save_file="a50_"$now_date".txt"
save_file=$stock_data/$save_folder/$save_file
echo $save_file
wget $url -O $file1

sed -i 's/var hq_str_hf_CHA50CFD="//g' $file1
sed -i 's/,/\n/g' $file1
touch $save_file
a50_value=`head -1 $file1`
now_time=$(date "+%Y-%m-%d %H:%M:%S")
out_string=$a50_value","$now_time

#echo $out_string
echo $out_string >> $save_file 


