save_dir="/home/davidyu/stock/data/dfcf_bankuai/parse_data/"
#mv $save_dir"*bankuai*" $save_dir"bankuai"
#mv $save_dir"*diyu*" $save_dir"diyu"
#mv $save_dir"*hangye*" $save_dir"hangye"
find $save_dir -maxdepth 1 -type f -name *bankuai* -exec mv {} $save_dir"bankuai"  \;
find $save_dir -maxdepth 1 -type f -name *diyu* -exec mv {} $save_dir"diyu"  \;
find $save_dir -maxdepth 1 -type f -name *hangye* -exec mv {} $save_dir"hangye"  \;
