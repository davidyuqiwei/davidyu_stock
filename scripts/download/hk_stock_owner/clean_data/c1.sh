download_date=`date +%Y-%m-%d`

source ~/.bashrc
cd `dirname $0`

save_dir="/home/davidyu/stock/data/hk_stock_owner/v1/ownerchange/"
raw_dir="/home/davidyu/stock/data/hk_stock_owner/ownerchange/"
while read -r line 
do
    mkdir $save_dir$line
    #cp -f $raw_dir$line"*" $save_dir$line
    find $raw_dir -name "$line*" | xargs -t -i cp -rf {} $save_dir"$line"
    #mv /home/davidyu/stock/data/hk_stock_owner/ownerlist
done<$hk_index_list
#done<test.sh


#cp -f /home/davidyu/stock/data/hk_stock_owner/ownerlist/00860* $save_dir$line

