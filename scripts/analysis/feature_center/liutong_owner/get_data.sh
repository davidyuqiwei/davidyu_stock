tmp_data_dir=$tmp_data_dir"/baostock/feature_slope"
out_data="liutong_data.csv"
sh run_select_dadan_dfcf.sh > $out_data
sed -i 's/[\t]/,/g' $out_data

