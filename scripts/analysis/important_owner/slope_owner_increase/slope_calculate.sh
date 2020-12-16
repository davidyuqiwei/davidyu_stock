OLD_IFS="$IFS"
IFS="," 

input_file=$1
slope_out_file=$2
predict_slope_days=$3
while read -r line 
do
    arr=($line)
    stock_index=${arr[0]}
    date1=${arr[1]}
    report_date=${date1:0:10}
    #echo $stock_index
    #echo $report_date
    python b1.py $stock_index $report_date $predict_slope_days >> $slope_out_file
done < $input_file
