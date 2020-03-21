source ~/.bashrc
cd `dirname $0`
url="http://hq.sinajs.cn/rn=1583892244314&list=s_sh000001,s_sz399001,nf_IF0,rt_hkHSI,gb_$dji,gb_ixic,b_SX5E,b_UKX,b_NKY,hf_CL,hf_GC,hf_SI,hf_CAD"
file1="data_out.txt"
now_date=$(date "+%Y-%m-%d")
save_folder="SH_index_RT"
save_file="SH_index_amount_RT_"$now_date".txt"
save_file=$stock_data/$save_folder/$save_file
echo $save_file
wget $url -O $file1

sed -i 's/var hq_str_s_sh000001="//g' $file1
sed -i 's/,/\n/g' $file1
touch $save_file
a50_value=`cat $file1 | sed -n '2p'`
chengjiao_amount=`cat $file1 | sed -n '6p' | sed s/\"//g | sed s/\;//g`
now_time=$(date "+%Y-%m-%d %H:%M:%S")
out_string=$a50_value","$chengjiao_amount","$now_time

#echo $out_string
echo $out_string >> $save_file


