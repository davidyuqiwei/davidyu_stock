load data local inpath '/home/davidyu/stock/data/baostock/000001.csv' into table stock_dev.baostock PARTITION(stock_index='000001');
load data local inpath '/home/davidyu/stock/data/baostock/000002.csv' into table stock_dev.baostock PARTITION(stock_index='000002');
load data local inpath '/home/davidyu/stock/data/baostock/000005.csv' into table stock_dev.baostock PARTITION(stock_index='000005');
load data local inpath '/home/davidyu/stock/data/baostock/000006.csv' into table stock_dev.baostock PARTITION(stock_index='000006');
