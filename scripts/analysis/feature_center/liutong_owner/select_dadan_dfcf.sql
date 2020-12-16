select
distinct
owner_sort,
owner_name,
amount,
ratio,
charac,
dt,
stock_index
from stock_dev.liutong_owner
where dt>='${start_date}'  and dt<='${end_date}'
and owner_name like concat('%','${owner_name}','%')
;

