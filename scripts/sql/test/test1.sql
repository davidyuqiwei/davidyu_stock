use stock_test;
drop table if exists baostock_test;

create table  if not exists baostock_test(
    stockdate   string  comment 'stock_date',
    code    string  comment 'code',
    open    decimal(38,2)   comment 'open',
    high    decimal(38,2)   comment 'high',
    low decimal(38,2)   comment 'low',
    close   decimal(38,2)   comment 'close',
    volume  int comment 'volume'

)
comment 'baostock'
PARTITIONED BY ( year string comment 'year' )
row format delimited
fields terminated by ','
stored as textfile;

