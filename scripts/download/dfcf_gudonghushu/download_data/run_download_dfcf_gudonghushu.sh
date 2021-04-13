#http://data.eastmoney.com/gdhs/

source ~/.bashrc
cd `dirname $0`
download_date=`date +%Y-%m-%d`
#line=1
save_dir=$stock_data"/dfcf_gudonghushu/parse_data"
len=`cat $stock_list_data | wc -l`

for ((i=1; i<=100; i ++))
do
    file_num=`ls $save_dir |wc -l`
    if [ $file_num -le $len ];then
	    while read -r line
	    do
	        parse_file=$save_dir"/"$line".csv"
			save_file=$line".txt"
            if [ ! -f "$parse_file" ]; then
                url1="http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?callback=jQuery112300047349239502487706_1614684122555&st=EndDate&sr=-1&ps=50&p=1&type=HOLDERNUM&sty=detail&filter=(securitycode%3D%27$line%27)&js=%7Bpages%3A(tp)%2Cdata%3A(x)%7D&token=70f12f2f4f091e459a279469fe49eca5"
			    wget $url1 -O $save_file
			    python parse_to_df.py $save_file
                rm -rf $save_file
                sleep 7.21s
            fi
        done<$stock_list_data
    fi
done




