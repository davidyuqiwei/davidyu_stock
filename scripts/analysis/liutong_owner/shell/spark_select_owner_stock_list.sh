source ~/.bashrc
cd `dirname $0`
#curr_dir=`pwd`
base_dir=$(dirname "$PWD")

sql_dir=$base_dir"/sql"
sql_file_raw="run_select_owner_stock_list.sql"
sql_file=$sql_dir"/"$sql_file_raw
sql_file_name=${sql_file_raw%.*}

save_dir=$stock_data"/stock_list/"
save_file=$sql_file_name".txt"
save_it=$save_dir$save_file
#echo $sql_file
spark-sql \
    -f $sql_file > $save_it


:<<!
select_owner_stock_list.sql



source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
base_dir=$(dirname "$PWD")

database="stock_test"
tgt_table="hk_dailiren_change"
owner_name="香港中央"
start_date="2019-03-31"
end_date="2019-06-30"


sql_dir=$base_dir/sql
sql_file=$sql_dir/"owner_compare.sql"
echo $sql_file
spark-sql \
        -f $sql_file \
            -d database=${database} \
                -d tgt_table=${tgt_table} \
                    -d owner_name=${owner_name} \
                        -d start_date=${start_date} \
                            -d end_date=${end_date} \
                                -S
!
