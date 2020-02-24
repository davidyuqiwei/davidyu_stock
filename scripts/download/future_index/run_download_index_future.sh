source ~/.bashrc
cd `dirname $0`
python download_index_future.py
status=`echo $?`
if [ $status -eq 0 ];then
    rm -rf geckodriver.log
    echo "OK"
else
    echo "process error"
fi


