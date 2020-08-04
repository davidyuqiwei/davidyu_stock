source ~/.bashrc
cd `dirname $0`
sh combine_data.sh
python clean_data.py
