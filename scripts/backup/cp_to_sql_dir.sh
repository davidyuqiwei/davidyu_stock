#!/usr/bin/sh
### find csv in folder and copy to another folder
find /cygdrive/g/stock/data/stock_owner_liutong -name '*.csv' -exec cp -n -r {} /cygdrive/g/stock/data_to_sql_owner \;
