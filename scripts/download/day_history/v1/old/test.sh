file_in=$stock_data/basic_info/stock_basic_info.csv
echo $file_in
a2=`wc -l $file_in`
a1=`echo $a2 | awk '{print $1}'`
echo $a1
for i in $(seq 0 $a1)
do
    echo $i
done

