tmp_data_dir=$tmp_data_dir"/feature_center"
out_data="jijin_data.csv"
jijin_date="2019-03-31"
sh run_stk_jj_cnt.sh $jijin_date > $out_data
sed -i 's/[\t]/,/g' $out_data
mv $out_data $tmp_data_dir


