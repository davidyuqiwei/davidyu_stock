source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
base_dir=$(dirname "$PWD")

end_date="`date +%Y-%m-%d`"
#end_date="2020-08-17"
start_date=`date -d "$end_date 7 days ago" "+%Y-%m-%d"`
tgt_table="stock_dw.dadan_dfcf_weekly_dadan_cnt"
src_table="stock_dev.dadan_dfcf"
price=30000000

#$cur_date 
#echo $last_week

echo "do" > THIS.log

sql_dir=$base_dir/sql
sql_file=$sql_dir/"dadan_dfcf_weekly_dadan_cnt.sql"
echo $sql_file
spark-sql \
    --conf spark.io.compression.codec=snappy \
    --conf spark.shuffle.manager=sort \
    --conf spark.shuffle.consolidateFiles=true \
    -f $sql_file \
    -d tgt_table=$tgt_table \
    -d src_table=$src_table \
    -d end_date=$end_date \
    -d start_date=$start_date \
    -d price=$price \
    -S -v



