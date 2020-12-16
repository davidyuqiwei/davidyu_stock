grep -r 回购 /home/davidyu/stock/data/news_report_out_data/gufenhuigou.txt  | awk -F "/" '{print $8}'  | awk -F ":" '{print $1}' | awk -F "_" '{print $1,$2}' > huigou.csv
