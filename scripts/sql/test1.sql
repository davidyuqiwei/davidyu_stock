use stock_dev;
drop table if exists hexinticai;

create table  if not exists hexinticai(
    ticai   string  comment 'ticai',
    stock_index string  comment 'stock_index'

)
comment 'hexinticai'
row format delimited
fields terminated by ','
stored as PARQUET;

