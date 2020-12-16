#!/usr/bin/sh
cd `dirname $0`
python stock_index.py
hive -f create_stock_basic_table.sql
/usr/bin/cp -f stock_basic_info.csv $stock_data"/basic_info"
rm -rf stock_basic_info.csv stock_basic_info_nohead.csv

