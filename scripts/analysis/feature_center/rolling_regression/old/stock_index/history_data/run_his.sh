source ~/.bashrc
cd `dirname $0`
window=30
while read -r line 
do
    if [[ $line == 60* ]] || [[ $line == 00* ]] || [[ $line == 30*  ]];then
        python stock_roll_regression_his.py $line".csv" $line"_roll_reg_"$window".csv" $window
        echo $line
    fi
done < $stock_list_data



