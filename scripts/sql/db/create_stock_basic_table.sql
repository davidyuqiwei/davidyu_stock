create table stock.stock_index(
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


load data local inpath '/home/davidyu/data/basic_info/stock_basic_info.csv' into table stock.stock_index;
select * from stock_index limit 10;
