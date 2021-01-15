cd /home/davidyu/stock/data/history_data/zhulikongpan
file_in="zhulikongpan_2021-01-05.csv"
out_file=${file_in/.csv/_clean.csv}
#column_names = ["stock_date","stock_index","stock_name","price","kongpan_ratio","kongpan_cn"]
cat $file_in | awk -F "," '{print $1","$2","$3","$4","$9","$10}' > $out_file
