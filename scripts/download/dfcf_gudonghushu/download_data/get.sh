save_file="test.txt"
#python parse_to_df.py $save_file
url1="http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?callback=jQuery112300047349239502487706_1614684122555&st=EndDate&sr=-1&ps=50&p=1&type=HOLDERNUM&sty=detail&filter=(securitycode%3D%27600903%27)&js=%7Bpages%3A(tp)%2Cdata%3A(x)%7D&token=70f12f2f4f091e459a279469fe49eca5"

#wget $url1 -O $save_file
len=`cat $stock_list_data | wc -l`
echo $len
save_dir=$stock_data"/dfcf_gudonghushu/parse_data"
file_num=`ls $save_dir |wc -l`
if [ $file_num -le $len ];then
    echo "do"
fi

