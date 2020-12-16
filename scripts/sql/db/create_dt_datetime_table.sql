use stock_dt;
set hivevar:start_day=2000-01-01;
set hivevar:end_day=2050-12-31;
set hivevar:timeDimTable=default.timeDim;

drop table if exists datetime_table;
 
-- create datetime table
create table if not exists datetime_table(
    stock_date                      string      comment     '日期',
    year                    int         comment     '年',
    month                   int         comment     '月',
    day                     int         comment     '日',
    daynumber_of_week       string      comment     '星期几',
    dayname_of_week         string      comment     '星期几字符',
    daynumber_of_year       string      comment     '一年中的第几天'
)
comment '日期维表'
row format delimited 
fields terminated by '\001'
stored as textfile
;


-- insert datetime
with dates as (
select date_add("${start_day}", a.pos) as d
from (select posexplode(split(repeat("o", datediff("${end_day}", "${start_day}")), "o"))) a
)
insert into datetime_table
select
    d as d
  , year(d) as year
  , month(d) as month
  , day(d) as day
  , date_format(d, 'u') as daynumber_of_week
  , date_format(d, 'EEEE') as dayname_of_week
  , date_format(d, 'D') as daynumber_of_year
from dates
sort by d
;
