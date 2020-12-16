source ~/.bashrc
cd `dirname $0`


today_date="`date +%Y-%m-%d`"
#today_date="2020-09-09"
tmp_save_dir=$tmp_data_dir"/daily_report"
yejiyuqi_today="yejiyuqi_today_"$today_date".csv"

sh run_yejiyuqi_today.sh $today_date > $yejiyuqi_today
mv $yejiyuqi_today $tmp_save_dir

