#!/usr/bin/sh
#hive -f create_table_day_history.sql
#hive -f create_table_SH_SZ_index.sql
python create_important_owner_seasonal_change.py > create_important_owner_seasonal_change.sql
