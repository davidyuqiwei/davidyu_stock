
data_dir="/home/davidyu/stock/data/dadan_DFCF"
cd $data_dir
mv_dir="/home/davidyu/stock/data/dadan_DFCF_bak"
find -name '*1558*' |xargs -i mv {} $mv_dir


