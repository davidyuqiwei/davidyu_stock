source ~/.bashrc
cd `dirname $0`

#sh to_hive.sh baostock.cfg
sql_file="update_data_test.sql"
year=`date +%Y`
hive \
    -f $sql_file \
    -d year=${year} 
