source ~/.bashrc
cd `dirname $0`
python parse_dfcf_fuquan.py
sh combine_data.sh
#python clean_data.py

