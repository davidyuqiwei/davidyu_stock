source ~/.bashrc
cd `dirname $0`


today_date="`date +%Y-%m-%d`"
#today_date="2020-08-25"
tmp_save_dir=$tmp_data_dir"/daily_report"
dadan_dfcf_today_rank_out_data="dadan_dfcf_today_rank_report_"$today_date".csv"

sh run_dadan_dfcf_today_rank.sh $today_date > $dadan_dfcf_today_rank_out_data
mv $dadan_dfcf_today_rank_out_data $tmp_save_dir








