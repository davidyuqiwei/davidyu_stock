drop table if exists stock_dt.stock_index;
create table stock_dt.stock_index(
    code string,
    name string,
    industry string,
    area string,
    pe string,
    outstanding float,
    totals float,
    totalAssets float,
    liquidAssets float,
    fixedAssets float,
    reserved float,
    reservedPerShare float,
    esp float,
    bvps float,
    pb float,
    timeToMarket float,
    undp float,
    perundp float,
    rev float,
    profit float,
    gpr float,
    npr float,
    holders float
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' ;


load data local inpath 'stock_basic_info_nohead.csv' into table stock_dt.stock_index;
select * from stock_dt.stock_index limit 10;
