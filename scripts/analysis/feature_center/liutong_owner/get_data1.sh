tmp_data_dir=$tmp_data_dir"/baostock/feature_slope"
out_data="hk_increase.csv"
spark-sql -e "select * from stock_test.hk_zhongyang_20180630_20180930"> $out_data
sed -i 's/[\t]/,/g' $out_data

