use stock_dw;
drop table if exists dadan_dfcf_weekly_dadan_cnt;

create table if not exists dadan_dfcf_weekly_dadan_cnt(
    stock_index     string  comment 'TDATE',
    stock_name      string  comment 'TDATE',
    cnt             int     comment 'cnt',
    stock_date_list  string comment 'stock_date_list',
    stock_dadan_liuru_list string comment 'stock_dadan_liuru_list',
    stock_date string comment 'stock_date'
)
comment 'dadan_dfcf_weekly_dadan_cnt' 
PARTITIONED BY ( day string comment '日期' )
row format delimited
fields terminated by '\\001'
stored as textfile;


