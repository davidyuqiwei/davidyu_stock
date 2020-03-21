# shell_function

start_date="2020-01-01"
end_date="2020-01-10"

python get_stock_list.py $start_date $end_date
echo "finish get dadan list"

make_file="all.csv"
data_dir="/home/davidyu/stock/data/tmp/dazong_data/"
stock_list_csv="dazong_stock_list.csv"
rm -rf $data_dir$make_file $data_dir$stock_list_csv
sh get_all_csv_process_colname.sh $make_file $data_dir


cd $data_dir
awk -F ',' '{print$1}'  $data_dir$make_file | sort | uniq  > $stock_list_csv
sed -i '/SECUCODE/d' $stock_list_csv

echo "finish get dadan download list"

echo "start download dadan list from wanyi"
## download wangyi dazong stock_list

#sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/day_history_wangyi/run_download_day_history_wangyi.sh $data_dir$stock_list_csv
#echo "finish download"

