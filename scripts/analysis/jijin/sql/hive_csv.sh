#!/usr/bin/sh
save_dir=$stock_data"/test/"
file_name="zengqiang"
#file_name=$stk_index"fin_report"
f1=${save_dir}${file_name}.csv
#final_file=${file_name}_f1.csv


## run hive to export data
hive -e "set hive.cli.print.header=true;
set hive.exec.compress.output=false;
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;

select jijin_name,
    concat_ws(',',collect_set(t2.name)) as stock_name_list
    from
    stock_dev.jijin t1
    left join
    stock.stock_index t2
    on t1.stock_index = t2.code
    where stock_date = '2020-09-30' and jijin_name like '%指数增强%'
    group by jijin_name
    limit 100

;
" \
| sed 's/[\t]/,/g' > $f1

#python ./functions/trans_csv_to_xlsx.py -f $f1
#| sed 's/[\t]/\t/g' > $f1
