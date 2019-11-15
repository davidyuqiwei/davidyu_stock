create database if not exists stock_dev;
drop table stock_dev.SH_index; 
create table if not exists stock_dev.SH_index(
    stock_date date,
    open float,
    high float,
    low float,
    close float,
    volume float,
    adj_close float
)
ROW FORMAT DELIMITED FIELDS 
TERMINATED BY ',' 
STORED AS PARQUET;


drop table stock_dev.SZ_index; 
create table if not exists stock_dev.SZ_index(
    stock_date date,
    open float,
    high float,
    low float,
    close float,
    volume float,
    adj_close float
)
ROW FORMAT DELIMITED FIELDS 
TERMINATED BY ',' 
STORED AS PARQUET;


--truncate table stock_dev.day_history;
--load data local inpath '/home/davidyu/stock/data/day_history_bak/all.csv' into table stock_dev.day_history;
--select * from day_history where stock_date> '2018-12-10' and stock_date < '2018-12-20' limit 10;

--select * from stock_index limit 10;
