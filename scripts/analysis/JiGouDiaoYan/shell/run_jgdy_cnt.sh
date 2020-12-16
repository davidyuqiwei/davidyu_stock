source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
base_dir=$(dirname "$PWD")


start_date="2020-09-01"
end_date="2020-11-01"
outfile="jgdy_cnt.csv"

sql_dir=$base_dir/sql
sql_file=$sql_dir/"jgdy_cnt.sql"
#echo $sql_file
spark-sql \
    --conf spark.io.compression.codec=snappy \
    --conf spark.shuffle.manager=sort \
    --conf spark.shuffle.consolidateFiles=true \
    -f $sql_file \
    -d start_date=$start_date \
    -d end_date=$end_date \
    -S > $outfile
sed -i 's/[\t]/,/g' $outfile



