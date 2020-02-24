create table stock_index(
    code string,
    name string,
    industry string,
    area string,
    pe string,
    outstanding string,
    totals string,
    totalAssets string,
    liquidAssets string,
    fixedAssets string,
    reserved string,
    reservedPerShare string,
    esp string,
    bvps string,
    pb string,
    timeToMarket string,
    undp string,
    perundp string,
    rev string,
    profit string,
    gpr string,
    npr string,
    holders string
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' ;


load data local inpath '/home/davidyu/data/basic_info/stock_basic_info.csv' into table stock1.stock_index;
select * from stock_index limit 10;
