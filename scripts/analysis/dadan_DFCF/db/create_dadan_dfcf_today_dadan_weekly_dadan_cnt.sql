use stock_dw;
drop table if exists dadan_dfcf_today_dadan_weekly_dadan_cnt;

create table if not exists dadan_dfcf_today_dadan_weekly_dadan_cnt(
    stock_index     string  comment 'stock_index',
    stock_name      string  comment 'stock_name',
    today_increase_ratio    string  comment 'today_increase_ratio',
    today_liuru     int     comment  'today_liuru',
    cnt             int     comment 'cnt',
    stock_date_list  string comment 'stock_date_list',
    stock_dadan_liuru_list string comment 'stock_dadan_liuru_list',
    stock_date  string  comment 'stock_date'
)
comment '' 
PARTITIONED BY ( day string comment '日期' )
row format delimited
fields terminated by '\\001'
stored as textfile;


