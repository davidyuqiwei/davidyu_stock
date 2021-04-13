source ~/.bashrc
cd `dirname $0`
window=5
out_dir="/home/davidyu/stock/data/feature_center/rolling_regression/stock_index/5days_update"
while read -r line 
do
    if [[ $line == 60* ]] || [[ $line == 00* ]] || [[ $line == 30*  ]];then
        python stock_roll_regression_his.py $line"_fuquan.csv" $line"_roll_reg_"$window".csv" $window $out_dir
        echo $line
    fi
done < $hs_300_list_data
#done < stock_test.sh
#done < $stock_list_data_test



