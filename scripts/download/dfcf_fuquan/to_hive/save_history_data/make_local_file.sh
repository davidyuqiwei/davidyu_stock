data_dir="/home/davidyu/stock/data/history_data/dfcf_fuquan/"
cd $data_dir
for ((i=2000;i<2021;i++))
do   
    echo "load data local inpath '$data_dir$i.csv' overwrite into table stock_dev.dfcf_fuquan_byyear PARTITION(year='$i');"
done   
