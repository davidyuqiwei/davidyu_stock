source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
while read -r line 
do
    python download_dadan_real_time_ifeng.py $line
    sleep 2.5s
done < page_list.sh

