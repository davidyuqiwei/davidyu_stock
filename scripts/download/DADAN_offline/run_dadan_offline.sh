source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
while read -r line 
do
    python download_DADAN_100.py $line
    sleep 2.5s
done < page_list.sh

