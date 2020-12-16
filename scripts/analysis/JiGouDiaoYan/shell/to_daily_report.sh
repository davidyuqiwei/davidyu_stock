source ~/.bashrc
cd `dirname $0`


today_date="`date +%Y-%m-%d`"
#today_date="2020-08-28"
echo "+++check+++"$today_date > a.log
tmp_save_dir=$tmp_data_dir"/daily_report"
out_file1="jigoudiaoyan_today_cnt_"$today_date".csv"

sh run_jigoudiaoyan_today_cnt.sh $today_date > $out_file1
mv $out_file1 $tmp_save_dir

