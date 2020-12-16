source ~/.bashrc
cd `dirname $0`
today_date="`date +%Y-%m-%d`"

tmp_save_dir=$tmp_data_dir"/important_owner"

cd /home/davidyu/stock/data/important_owner
grep -r 2020-11-24 | grep 增加 | awk -F "," '{print $7 "," $8 "," $3 "," $14 "," $13 "," $18}'
