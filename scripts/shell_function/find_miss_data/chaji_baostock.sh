ls /home/davidyu/stock/data/history_data/baostock | cut -c1-6 > d1.txt
cp $stock_data"/common/stock_list.txt" .
grep -F -v -f d1.txt stock_list.txt | sort | uniq > chaji.txt

