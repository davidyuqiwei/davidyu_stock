tmp_data_dir=$tmp_data_dir"/feature_center"
out_data="dadan_data.csv"
sh run_select_dadan_dfcf.sh > $out_data
sed -i 's/[\t]/,/g' $out_data
mv $out_data $tmp_data_dir










