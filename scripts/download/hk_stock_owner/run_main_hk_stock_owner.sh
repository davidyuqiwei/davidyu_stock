source ~/.bashrc
cd `dirname $0`
project_path=$(cd `dirname $0`; pwd)
project_name="${project_path##*/}"
#echo $project_path

echo $project_name

sh ./download_data/run_download_hk_stock_owner.sh
#sh ./clean_data/run_clean_combine_data.sh 
#sh ./to_hive/run_to_hive_hk_stock_owner.sh


