create database if not exists stock_dev;
drop table stock_dev.day_history; 
create table if not exists stock_dev.day_history(
    stock_date date,
    high float,
    low float,
    open float,
    close float,
    volume float,
    adj_close float,
    stock_index string
)
ROW FORMAT DELIMITED FIELDS 
TERMINATED BY ',' 
STORED AS PARQUET;

--truncate table stock_dev.day_history;
--load data local inpath '/home/davidyu/stock/data/day_history_bak/all.csv' into table stock_dev.day_history;
--select * from day_history where stock_date> '2018-12-10' and stock_date < '2018-12-20' limit 10;

--select * from stock_index limit 10;
