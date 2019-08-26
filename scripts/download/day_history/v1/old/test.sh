file_in=$stock_data/basic_info/stock_basic_info.csv
stk_count=`wc -l $file_in`
## how many rows in the file and assign to the parameter
stk_index_count=`echo $stk_count | awk '{print $1}'`

a1=$((stk_index_count-1))
echo $a1
for i in $(seq 2300 $a1)
do
    echo $i
done
