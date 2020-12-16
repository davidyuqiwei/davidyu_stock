#http://finance.sina.com.cn/stock/sl/#concept_1
source ~/.bashrc
cd `dirname $0`

download_txt="bankuai_"$(date "+%Y%m%d")".txt"
out_file_name="bankuai_"$(date "+%Y-%m-%d")".csv"
save_dir=$stock_data"/bankuai"

wget http://money.finance.sina.com.cn/q/view/newFLJK.php?param=class -O $download_txt
sed -i 's/var S_Finance_bankuai_class = //g' $download_txt

/usr/bin/cp -f $download_txt $raw_data_dir
python download_bankuai.py $download_txt $out_file_name
mv $out_file_name $save_dir
status=`echo $?`
#echo $status
if [ $status -eq 0 ];then
    rm -rf *.txt
    echo "OK"
else
    echo "process error"
fi



#rm -rf *.txt
