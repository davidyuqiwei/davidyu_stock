save_dir=$stock_data"/test/"
stk_index="dfcf_fuquan_kline_cluster"
file_name=$stk_index
f1=${save_dir}${file_name}.csv
#final_file=${file_name}_f1.csv


## run hive to export data
hive -e "set hive.cli.print.header=true;
set hive.exec.compress.output=false;
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;


select stock_index,dt,
open,close,high,low
from stock_raw.dfcf_fuquan_byyear
where year >2018
order by rand()
limit 100000
;
" \
| sed 's/[\t]/,/g' > $f1
