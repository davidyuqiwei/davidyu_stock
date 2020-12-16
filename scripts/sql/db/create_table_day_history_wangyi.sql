use stock_dev;
drop table if exists day_history_wangyi;

create table  if not exists day_history_wangyi(
    stock_date   string   comment 'stock_date',
    open    float   comment 'open',
    high float comment 'high',
    low  float  comment 'low',
    close float   comment 'close',
    change_price float   comment 'change_price',
    change_ratio   float   comment 'change_ratio',
    trade_num string   comment 'trade_num',
    trade_price   string   comment 'trade_price',
    variation  float   comment 'variation',
    turnover_rate  float   comment 'turnover_rate',
    stock_index     string   comment 'stock_index'
)
comment 'day_history_wangyi'
row format delimited 
fields terminated by ','
stored as PARQUET;

