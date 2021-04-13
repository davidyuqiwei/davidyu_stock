source ~/.bashrc
cd `dirname $0`
#download_date=`date +%Y-%m-%d`
download_date="2021-02-26"
save_dir=$stock_data"/dadan_real_time_ifeng/"$download_date
file_num=`ls $save_dir |wc -l`
echo $file_num

if [ $file_num -le 3000 ];then
    echo "need download"
fi 
save_file=$save_dir"/9.csv"
if [ ! -f "$save_file"   ]; then
    echo $save_file
fi

