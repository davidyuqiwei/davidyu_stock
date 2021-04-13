download_date=`date +%Y-%m-%d`
save_dir="/home/davidyu/stock/data/hk_stock_owner/"
source ~/.bashrc
cd `dirname $0`

while read -r line 
do
    stock_index=$line
    echo $line
    file1=$stock_index".txt"
    url1="http://emweb.securities.eastmoney.com/PC_HKF10/MajorShareholder/PageAjax?code=$stock_index"
    wget $url1 -O $file1
    python parse_data.py $file1
    mv *.txt $save_dir
    mv *ownerchange* $save_dir"ownerchange"
    mv *ownerlist* $save_dir"ownerlist"
    sleep 4.36s
done<$hk_index_list
#done<test.sh
    #done<$hk_index_list

