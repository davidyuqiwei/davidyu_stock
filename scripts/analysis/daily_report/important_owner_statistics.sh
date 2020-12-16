source ~/.bashrc
cd `dirname $0`

today_date="`date +%Y-%m-%d`"
#today_date="2020-08-26"

out_data="important_owner_today_report_"$today_date".csv"
daily_report_dir=$stock_data"/daily_report/"$today_date


cd /home/davidyu/stock/data/history_data/important_owner
grep -r $today_date | grep 增加 | awk -F "," '{print $7 "," $8 "," $3 "," $14 "," $13 "," $18}' > $out_data

mv $out_data $daily_report_dir






