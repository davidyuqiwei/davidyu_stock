source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
base_dir=$(dirname "$PWD")


today_date=$1

sql_dir=$base_dir/sql
sql_file=$sql_dir/"jigoudiaoyan_today_cnt.sql"
#echo $sql_file
spark-sql \
    --conf spark.io.compression.codec=snappy \
    --conf spark.shuffle.manager=sort \
    --conf spark.shuffle.consolidateFiles=true \
    -f $sql_file \
    -d today_date=$today_date \
    -S -v 



