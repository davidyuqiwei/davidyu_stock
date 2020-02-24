source ~/.bashrc
cd `dirname $0`
python combine_today_data.py
sh run_scala_insert.sh
echo $?

