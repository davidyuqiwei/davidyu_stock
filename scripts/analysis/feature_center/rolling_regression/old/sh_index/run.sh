#stock_index='000917'
input_file="sh_index_4_rollreg.csv"
sql_file="select_data.sql"
save_dir=$stock_data"/test"
out_file="sh_index_rollreg_result.csv"
if [ ! -d $save_dir  ];then
  mkdir $save_dir
fi

spark-sql \
    -f $sql_file > $input_file
sed -i 's/[\t]/,/g' $input_file
#mv $input_file $save_dir

python stock_roll_regression.py $input_file $out_file
mv $input_file $out_file $save_dir
#rm -rf $input_file



