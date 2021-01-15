data_dir="/home/davidyu/stock/data/history_data/baostock/byyear/"
cd $data_dir
for ((i=2015;i<2021;i++))
do   
    echo "load data local inpath '$data_dir$i.csv' overwrite into table stock_dev.baostock_byyear PARTITION(year='$i');"
done   
