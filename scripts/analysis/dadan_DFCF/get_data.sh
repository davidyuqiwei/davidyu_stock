#!/usr/bin/sh
save_dir=$stock_data"/test/"
stk_index="dadan_601668"
file_name=$stk_index
f1=${save_dir}${file_name}.csv
#final_file=${file_name}_f1.csv


## run hive to export data
spark-sql  --hiveconf hive.cli.print.header=true \
-e "
select *,REPLACE(stock_date,'_','-') as dt
from stock_dev.dadan_dfcf
where 
stock_index = '601668'
order by REPLACE(stock_date,'_','-')
;
" \
| sed 's/[\t]/,/g' > $f1
#echo $f1
