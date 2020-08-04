source ~/.bashrc
cd `dirname $0`
project_path=$(cd `dirname $0`; pwd)
project_name="${project_path##*/}"
#echo $project_path

echo $project_name

sh ./download_data/run_download_dadan_DFCF.sh
sh ./clean_data/run_clean_combine_data.sh dadan_DFCF
sh ./to_hive/run_to_hive_dadan_DFCF.sh


