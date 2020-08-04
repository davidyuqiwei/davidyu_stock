source ~/.bashrc
cd `dirname $0`
project_path=$(cd `dirname $0`; pwd)
project_name="${project_path##*/}"
#echo $project_path
echo $project_name

#python download_jijin.py 601398
sh ./download_data/run_download_liutong_owner.sh
#sh ./clean_data/run_clean_combine_data.sh $project_name
#sh ./to_hive/run_jijin_scala.sh

