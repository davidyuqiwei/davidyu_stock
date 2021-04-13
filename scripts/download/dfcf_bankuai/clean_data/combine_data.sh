source ~/.bashrc
cd `dirname $0`
save_dir="/home/davidyu/stock/data/dfcf_bankuai/parse_data/"
find $save_dir -maxdepth 1 -type f -name *bankuai* -exec mv {} $save_dir"bankuai"  \;
find $save_dir -maxdepth 1 -type f -name *diyu* -exec mv {} $save_dir"diyu"  \;
find $save_dir -maxdepth 1 -type f -name *hangye* -exec mv {} $save_dir"hangye"  \;

out_file="dfcf_bankuai.csv"
combine_csv_in_folder.sh "/home/davidyu/stock/data/dfcf_bankuai/parse_data/bankuai" $out_file
mv $data_tmp_dir"/"$out_file $tmp_data_dir"/dfcf_bankuai"


out_file="dfcf_diyu.csv"
combine_csv_in_folder.sh "/home/davidyu/stock/data/dfcf_bankuai/parse_data/diyu" $out_file
mv $data_tmp_dir"/"$out_file $tmp_data_dir"/dfcf_bankuai"


out_file="dfcf_hangye.csv"
combine_csv_in_folder.sh "/home/davidyu/stock/data/dfcf_bankuai/parse_data/hangye" $out_file
mv $data_tmp_dir"/"$out_file $tmp_data_dir"/dfcf_bankuai"
