source ~/.bashrc
cd `dirname $0`
current_dir=$(pwd)
data_dir="/home/davidyu/stock/data/volume_price_distr/"
save_dir="/home/davidyu/stock/data/shiny_data/data/vol_prirce_distr/"
echo $data_dir
#cd $data_dir
#out_file="pv_dist_all.csv"
#echo $data_dir$f1


for line in `ls $data_dir | head -n 10`
do
    stock_dir=$data_dir$line
    out_file="pv_dist_"$line".csv"
    combine_csv_in_folder.sh $stock_dir $out_file
    tmp_out_file=$data_tmp_dir"/"$out_file
    save_file=$save_dir$out_file
    python clean_vol_price_distr.py $tmp_out_file $save_file
    rm -rf $tmp_out_file
done


##combine_csv_in_folder.sh $data_dir$f1 $out_file
#mv $data_tmp_dir"/"$out_file $current_dir
#python $current_dir"/clean_vol_price_distr.py" $save_dir$out_file

#python clean_vol_price_distr.py
#rm $out_file
