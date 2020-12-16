source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
base_dir=$(dirname "$PWD")

start_date="`date +%Y-%m-%d`"
end_date=`date -d "-7 days" +"%Y-%m-%d"`
tgt_table=stock_dw.dadan_dfcf_weekly_dadan_cnt
src_table=stock_dev.dadan_dfcf
price=100000000
#echo $cur_date 
#echo $last_week



sql_dir=$base_dir/sql
sql_file=$sql_dir/"dadan_dfcf_weekly_dadan_cnt.sql"

spark-sql \
    -f $sql_file \
    -d tgt_table=$tgt_table \
    -d src_table=$src_table \
    -d start_date=$start_date \
    -d end_date=$end_date \
    -d price=$price\
    -S



