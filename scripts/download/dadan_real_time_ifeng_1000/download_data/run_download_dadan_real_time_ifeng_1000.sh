## sometime we miss some data
## this script loop to download the data
source ~/.bashrc
cd `dirname $0`
download_date=`date +%Y-%m-%d`
save_dir=$stock_data"/dadan_real_time_ifeng_1000/"$download_date
mkdir $save_dir
curr_dir=`pwd`
for ((i=1; i<=100; i ++))
do
    file_num=`ls $save_dir |wc -l`
    if [ $file_num -le 300  ];then
        while read -r line 
        do
            save_file=$save_dir"/"$line".csv"
            if [ ! -f "$save_file"  ]; then  # if data not exists then download
                python download_dadan_real_time_ifeng_1000.py $line
                sleep 6.567s
            fi
        done < page_list.sh
    fi
done

