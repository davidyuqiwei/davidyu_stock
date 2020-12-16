curr_dir=`pwd`
echo $curr_dir
#data_dir
important_data_dir=$stock_data"/important_owner"
cd $important_data_dir
out_file="owner_change.csv"
# stock_index,stock_name,owner_name,change_type,notice_date,change_num

grep -r 2020-06-30 | grep 增加 | awk -F "," '{print $7 "," $8 "," $3 "," $14 "," $13 "," $18}' | uniq  > $out_file
mv $important_data_dir"/"$out_file $curr_dir




