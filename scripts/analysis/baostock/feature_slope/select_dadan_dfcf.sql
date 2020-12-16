select
distinct
stock_index,
stock_date,
dadan_liuru
from stock_dev.dadan_DFCF
where stock_date>='${start_date}'  and stock_date<='${end_date}'
and dadan_liuru > ${money}
;

