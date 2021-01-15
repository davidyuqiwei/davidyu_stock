source ~/.bashrc
cd `dirname $0`
# souce url: http://data.eastmoney.com/stockcomment/002594.html
download_date=`date +%Y-%m-%d`
data_dir="/home/davidyu/stock/data/zhulikongpan"
out_file="zhulikongpan_"$download_date".csv"
combine_csv_in_folder.sh $data_dir $out_file
#cp $data_tmp_dir"/"$out_file $data_dir
mv $data_tmp_dir"/"$out_file /home/davidyu/stock/data/history_data/zhulikongpan
cd $data_dir
rm -rf *.txt

