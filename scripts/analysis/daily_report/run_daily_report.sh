source ~/.bashrc
cd `dirname $0`

py_log="/home/davidyu/stock/data/tmp_py_log/pylog.log"
python dazong_statistics.py
python DADAN_statistics.py
sh important_owner_statistics.sh
cat $py_log
echo "" > $py_log


