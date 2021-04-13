select stock_index,stock_name,zhuli_liuru,chaodadan_liuru,
dadan_liuru,zhongdan_liuru,xiaodan_liuru,stock_date,dt
from stock_raw.dadan_dfcf
where dt>="2020-09-30"
;
