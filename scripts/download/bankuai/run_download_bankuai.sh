source ~/.bashrc
cd `dirname $0`

download_txt="bankuai_"$(date "+%Y%m%d")".txt"
wget http://money.finance.sina.com.cn/q/view/newFLJK.php?param=class -O $download_txt
sed -i 's/var S_Finance_bankuai_class = //g' $download_txt
python download_bankuai.py $download_txt
status=`echo $?`
#echo $status

if [ $status -eq 0 ];then
    rm -rf *.txt
    echo "OK"
else
    echo "process error"
fi
#rm -rf *.txt
