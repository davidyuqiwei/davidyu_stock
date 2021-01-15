load data local inpath '/home/davidyu/stock/data/history_data/baostock/byyear/2015.csv' overwrite into table stock_dev.baostock_byyear PARTITION(year='2015');
load data local inpath '/home/davidyu/stock/data/history_data/baostock/byyear/2016.csv' overwrite into table stock_dev.baostock_byyear PARTITION(year='2016');
load data local inpath '/home/davidyu/stock/data/history_data/baostock/byyear/2017.csv' overwrite into table stock_dev.baostock_byyear PARTITION(year='2017');
load data local inpath '/home/davidyu/stock/data/history_data/baostock/byyear/2018.csv' overwrite into table stock_dev.baostock_byyear PARTITION(year='2018');
load data local inpath '/home/davidyu/stock/data/history_data/baostock/byyear/2019.csv' overwrite into table stock_dev.baostock_byyear PARTITION(year='2019');
load data local inpath '/home/davidyu/stock/data/history_data/baostock/byyear/2020.csv' overwrite into table stock_dev.baostock_byyear PARTITION(year='2020');
