source ~/.bashrc
cd `dirname $0`
py_log="/home/davidyu/stock/data/tmp_py_log/pylog.log"
python dazong_statistics.py
cat $py_log
echo "" > $py_log


