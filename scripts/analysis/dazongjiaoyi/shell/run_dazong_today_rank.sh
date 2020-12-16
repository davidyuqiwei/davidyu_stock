source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
base_dir=$(dirname "$PWD")

#today_date="`date +%Y-%m-%d`"
today_date=$1

echo "do" >  THIS.log

sql_dir=$base_dir/sql
sql_file=$sql_dir/"dazong_today_rank.sql"

spark-sql \
    --conf spark.io.compression.codec=snappy \
    --conf spark.shuffle.manager=sort \
    --conf spark.shuffle.consolidateFiles=true \
    -f $sql_file \
    -d today_date=$today_date \
    -S

