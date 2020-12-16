select
distinct
stock_index,
stock_date,
dadan_liuru
from stock_raw.dadan_dfcf
where stock_date>='${start_date}'  and stock_date<='${end_date}'
and dadan_liuru > ${money}
;

