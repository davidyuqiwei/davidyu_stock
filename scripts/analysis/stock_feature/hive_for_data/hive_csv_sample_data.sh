#!/usr/bin/sh
save_dir=$stock_data"/tmp_data/stock_feature/"
if [ ! -d $save_dir ];then
    mkdir $save_dir
fi

stk_index="6000_data"
file_name=$stk_index
f1=${save_dir}${file_name}.csv
#final_file=${file_name}_f1.csv


## run hive to export data
hive -e "set hive.cli.print.header=true;
set hive.exec.compress.output=false;
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;
set hive.resultset.use.unique.column.names=false;

select * from stock_dev.day_history_insert 
where stock_index like '6000%';
;
" \
| sed 's/[\t]/,/g' > $f1
echo $f1
#| sed 's/[\t]/\t/g' > $f1
