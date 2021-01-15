#!/usr/bin/sh
save_dir=$stock_data"/test/"
file_name="jijin_name"
#file_name=$stk_index"fin_report"
f1=${save_dir}${file_name}.csv
#final_file=${file_name}_f1.csv


## run hive to export data
hive -e "set hive.cli.print.header=true;
set hive.exec.compress.output=false;
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;

select distinct jijin_name
    from stock_dev.jijin 
    where stock_date = '2020-09-30' 

;
" \
| sed 's/[\t]/,/g' > $f1

#python ./functions/trans_csv_to_xlsx.py -f $f1
#| sed 's/[\t]/\t/g' > $f1
