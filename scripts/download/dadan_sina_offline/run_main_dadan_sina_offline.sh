source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
#cd $curr_dir
#ll
sh ./download_data/run_download_sina_offline.sh
sh ./clean_data/run_clean_combine_data.sh
sh ./to_hive/run_to_hive_sina_offline.sh

