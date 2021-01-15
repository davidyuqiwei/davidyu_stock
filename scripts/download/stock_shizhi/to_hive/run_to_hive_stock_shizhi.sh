source ~/.bashrc
cd `dirname $0`

#sh to_hive.sh stock_shizhi.cfg
hive -f to_hive_local_data.sql
