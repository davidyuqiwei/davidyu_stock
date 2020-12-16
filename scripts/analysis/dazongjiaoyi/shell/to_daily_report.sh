source ~/.bashrc
cd `dirname $0`

tmp_save_dir=$tmp_data_dir"/daily_report"

#today_date="`date +%Y-%m-%d`"
today_date="2020-10-30"
dazongjiaoyi_today_rank_out_data="dazongjiaoyi_today_rank_"$today_date".csv"

sh run_dazong_today_rank.sh $today_date > $dazongjiaoyi_today_rank_out_data
mv $dazongjiaoyi_today_rank_out_data $tmp_save_dir

