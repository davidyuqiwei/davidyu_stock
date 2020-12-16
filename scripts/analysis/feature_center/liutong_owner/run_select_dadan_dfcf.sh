source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
base_dir=$(dirname "$PWD")

sql_file="select_dadan_dfcf.sql"
start_date="2018-06-01"
end_date="2018-07-20"
owner_name='香港中央结算有限公司'
spark-sql \
    --conf spark.io.compression.codec=snappy \
    --conf spark.shuffle.manager=sort \
    --conf spark.shuffle.consolidateFiles=true \
    -f $sql_file \
    -d start_date=$start_date \
    -d end_date=$end_date \
    -d owner_name=$owner_name \
    -S

