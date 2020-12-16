#!/usr/bin/sh
save_dir=$stock_data"/test/"
file_name="sh_index_mv_avg"
f1=${save_dir}${file_name}.csv


## run hive to export data
hive -e "set hive.cli.print.header=true;
set hive.exec.compress.output=false;
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;

select * from 
stock_feature.sh_index_mv_avg
where dt>='2000-01-01'
order by dt
;
" \
| sed 's/[\t]/,/g' > $f1
echo $f1
