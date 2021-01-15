save_dir=$stock_data"/test/"
mv_avg_raw_name="sh_index_mv_avg"
out_file=${save_dir}${mv_avg_raw_name}.csv

spark-sql -f mv_avg_sh_index.sql
sh get_data.sh $out_file
python mv_avg_shift.py ${mv_avg_raw_name}.csv
