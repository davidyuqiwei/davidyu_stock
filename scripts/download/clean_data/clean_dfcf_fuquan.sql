set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;

alter TABLE stock_raw.dfcf_fuquan_byyear drop if exists PARTITION (year=2018);

insert into table stock_raw.dfcf_fuquan_byyear partition(year)
select 
stock_date as dt,
open,
close,
high,
low,
volume,
money,
x1,x2,x3,x4,
stock_date,
lpad(stock_index,6,'0') as stock_index,
year
from 
stock_dev.dfcf_fuquan_byyear
where year=2018 and stock_date>='2018-01-01' and stock_date<="2018-12-31"
;


alter TABLE stock_raw.dfcf_fuquan_byyear drop if exists PARTITION (year=2019);
insert into table stock_raw.dfcf_fuquan_byyear partition(year)
select
stock_date as dt,
open,
close,
high,
low,
volume,
money,
x1,x2,x3,x4,
stock_date,
lpad(stock_index,6,'0') as stock_index,
year
from
stock_dev.dfcf_fuquan_byyear
where year=2019 and stock_date>='2019-01-01' and stock_date<="2019-12-31"
;

alter TABLE stock_raw.dfcf_fuquan_byyear drop if exists PARTITION (year=2020);
insert into table stock_raw.dfcf_fuquan_byyear partition(year)
select
stock_date as dt,
open,
close,
high,
low,
volume,
money,
x1,x2,x3,x4,
stock_date,
lpad(stock_index,6,'0') as stock_index,
year
from
stock_dev.dfcf_fuquan_byyear
where year=2020 and stock_date>='2020-01-01' and stock_date<="2020-12-31"
;
