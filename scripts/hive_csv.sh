#!/usr/bin/sh
save_dir=$stock_data"/test/"
stk_index="hk_000756"
file_name=$stk_index
f1=${save_dir}${file_name}.csv
#final_file=${file_name}_f1.csv


## run hive to export data
hive -e "set hive.cli.print.header=true;
set hive.exec.compress.output=false;
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;

select * from stock_dev.liutong_owner
where owner_name like concat('%','香港中央结算(代理人)有限公司','%')
and stock_index ='000756'
order by dt
;
" \
| sed 's/[\t]/\t/g' > $f1
echo $f1
#| sed 's/[\t]/\t/g' > $f1

python ./functions/trans_csv_to_xlsx.py -f $f1
