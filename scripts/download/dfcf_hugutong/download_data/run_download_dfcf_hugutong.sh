source ~/.bashrc
cd `dirname $0`
#http://data.eastmoney.com/hsgtcg/StockHdDetail.aspx?stock=600519
#http://data.eastmoney.com/hsgtcg/StockHdDetail.aspx?stock=002594
#save_file="hugutong.txt"
download_date=$(date -d "yesterday" +%Y-%m-%d)
save_dir=$stock_data"/dfcf_hugutong/raw_data"
while read -r line 
do
    if [[ $line == 60*  ]];then
        type="HSGTHHDDET"
    fi
    if [[ $line == 00*  ]];then
        type="HSGTSHHDDET"
    fi
    file1=$line"_hugangtong.txt"
    url1="http://dcfm.eastmoney.com//em_mutisvcexpandinterface/api/js/get?type=$type&token=70f12f2f4f091e459a279469fe49eca5&st=HDDATE,SHAREHOLDPRICE&sr=3&p=1&ps=5000&js=var%20xVVnIfvh={pages:(tp),data:(x)}&filter=(SCODE=%27$line%27)(HDDATE=^$download_date^)&rt=53886432"
    wget $url1 -O $file1
    sleep 3.3s
    mv *.txt $save_dir
done<$sh_sz_index

python parse_data.py
