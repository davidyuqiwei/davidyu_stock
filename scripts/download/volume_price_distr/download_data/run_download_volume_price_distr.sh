source ~/.bashrc
cd `dirname $0`
#download_date=`date +%Y-%m-%d -d "-1day"`
download_date=`date +%Y-%m-%d`
#download_date='2021-03-31'
save_dir=$stock_data"/volume_price_distr/"
for ((i=1; i<=5; i ++))
do
    while read -r line 
	do
	    if [[ $line == 60* ]] || [[ $line == 00* ]] || [[ $line == 30*  ]];then
	        save_file=$save_dir$line"/"$line"_"$download_date".csv"
            if [ ! -f "$save_file" ];then
                echo $save_file
                python download_volume_price_distr.py $line $download_date
            fi
	        #sleep 2.5s
	    fi
	done < $stock_list_data
done
