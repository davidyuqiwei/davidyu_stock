create table stock_dev.QF2(
    index_in int,
    ch_name string,
    en_name string,
    country string,
    bank string,
    date_set string
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' ;

--truncate table stock_dev.day_history;
--load data local inpath '/home/davidyu/stock/data/day_history_bak/all.csv' into table stock_dev.day_history;
--select * from day_history where stock_date> '2018-12-10' and stock_date < '2018-12-20' limit 10;

--select * from stock_index limit 10;
