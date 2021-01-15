source ~/.bashrc
out_file="financial_report.csv"
combine_csv_in_folder.sh $history_data_dir"/financial_report" $out_file
mv $data_tmp_dir"/"$out_file $tmp_data_dir"/financial_report"

