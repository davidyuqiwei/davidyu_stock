source ~/.bashrc
cd `dirname $0`

project_path=$(cd `dirname $0`; pwd)
project_name="${project_path##*/}"
#echo $project_path

echo $project_name



#python download_jijin.py 601398
sh ./donwload_data/run_dowload_jijin.sh
sh ./clean_data/run_clean_combine_data.sh
sh ./to_hive/run_to_hive_jijin.sh



