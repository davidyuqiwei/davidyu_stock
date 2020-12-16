stock_index='000917'
input_file=$stock_index".csv"
out_file=$stock_index"_roll_reg.csv"
sql_file="select_data.sql"
save_dir=$tmp_data_dir"/feature_center/roll_reg"

if [ ! -d $save_dir  ];then
  mkdir $save_dir
fi

spark-sql \
    -f $sql_file \
    -d stock_index=$stock_index > $input_file
sed -i 's/[\t]/,/g' $input_file

python stock_roll_regression.py $input_file $out_file
mv $out_file $save_dir
rm -rf $input_file



