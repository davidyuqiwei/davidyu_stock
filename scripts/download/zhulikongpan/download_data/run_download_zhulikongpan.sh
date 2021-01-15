source ~/.bashrc
cd `dirname $0`
# souce url: http://data.eastmoney.com/stockcomment/002594.html
download_date=`date +%Y-%m-%d`

while read -r line 
do
    if [[ $line != "code" ]];then
        stock_index=$line
        echo $stock_index
        file1=$stock_index"_zhulikongpan_"$download_date".txt"
        url1="http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?type=QGQP_LB&CMD=$stock_index&token=70f12f2f4f091e459a279469fe49eca5&callback=jQuery1123048223496594506776_1609067355341&_=1609067355343"
        wget $url1 -O $file1
        sleep 4s
        python download_zhulikongpan.py
        mv $file1 $stock_data"/zhulikongpan"
    fi
done <$stock_list_data

