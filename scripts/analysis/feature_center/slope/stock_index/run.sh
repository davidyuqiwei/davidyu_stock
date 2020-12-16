source ~/.bashrc
cd `dirname $0`

start_date='2020-05-30'
end_date=`date +%Y-%m-%d`
stat_days=0
pred_days=30
while read -r line 
do
    python s1.py $line $start_date $stat_days $pred_days
done < $stock_list_data
#done < $stock_list_test_data
