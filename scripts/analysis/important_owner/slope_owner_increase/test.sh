OLD_IFS="$IFS"
IFS="," 
while read -r line 
do
    arr=($line)
    stock_index=${arr[0]}
    date1=${arr[1]}
    report_date=${date1:0:10}
    #echo $stock_index
    #echo $report_date
    python b1.py $stock_index $report_date 7
done < data.out
