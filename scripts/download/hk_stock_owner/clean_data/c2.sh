save_dir="/home/davidyu/stock/data/hk_stock_owner/v1/ownerlist/"
#cp -f "/home/davidyu/stock/data/hk_stock_owner/ownerlist/00860*" $save_dir$line
raw_dir="/home/davidyu/stock/data/hk_stock_owner/ownerlist"

find $raw_dir -name "00860*" | xargs -t -i cp -rf {} $save_dir"00860"

