alter table stock_dev.baostock_byyear drop partition(year='${year}');
load data local inpath '/home/davidyu/stock/data/history_data/baostock/byyear/2021.csv' overwrite into table stock_dev.baostock_byyear PARTITION(year='${year}');
