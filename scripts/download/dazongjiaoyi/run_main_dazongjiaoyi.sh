source ~/.bashrc
# source url :   http://data.eastmoney.com/dzjy/dzjy_mrmxa.aspx

cd `dirname $0`
project_path=$(cd `dirname $0`; pwd)
project_name="${project_path##*/}"
#echo $project_path

echo $project_name

sh ./download_data/run_download_dazongjiaoyi.sh
#sh ./clean_data/run_clean_combine_data.sh 
sh ./to_hive/run_to_hive_dazongjiaoyi.sh


