source ~/.bashrc
cd `dirname $0`

download_date=`date +%Y-%m-%d`
data_dir="/home/davidyu/stock/data/hk_stock_owner/ownerchange"
the_date=`ls $data_dir | head -n 1 | tr '_' ' ' | awk  '{print $2}'`
history_dir="/home/davidyu/stock/data/history_data/hk_stock_owner"
#echo $year
out_file="hk_stock_ownerchange_"$download_date".csv"
combine_csv_in_folder.sh "/home/davidyu/stock/data/hk_stock_owner/ownerchange" $out_file
cp $data_tmp_dir"/"$out_file $history_dir
mv $data_tmp_dir"/"$out_file $tmp_data_dir"/hk_stock_owner"
cd $data_dir
rm -rf *.txt


data_dir="/home/davidyu/stock/data/hk_stock_owner/ownerlist"
the_date=`ls $data_dir | head -n 1 | tr '_' ' ' | awk  '{print $2}'`
#echo $year
out_file="hk_stock_ownerlist_$the_date.csv"
combine_csv_in_folder.sh "/home/davidyu/stock/data/hk_stock_owner/ownerlist" $out_file
cp $data_tmp_dir"/"$out_file $history_dir
mv $data_tmp_dir"/"$out_file $tmp_data_dir"/hk_stock_owner"
cd $data_dir
rm -rf *.txt 




