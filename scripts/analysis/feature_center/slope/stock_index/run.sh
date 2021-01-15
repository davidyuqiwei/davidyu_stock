source ~/.bashrc
cd `dirname $0`

start_date='2015-06-30'
end_date=`date +%Y-%m-%d`
stat_days=0
pred_days=60
out_file="stock_index_slope_"$start_date"_"$pred_days".csv"
rm -rf $out_file
while read -r line 
do
    python stockIndexSlope.py $line $start_date $stat_days $pred_days >> $out_file 
done < $stock_list_data
#done < $stock_list_test_data
