out_file="volume_price_distr.csv"

data_dir="/home/davidyu/stock/data/volume_price_distr/"
echo $data_dir
cd $data_dir
for f1 in `ls`;
do
    echo $f1
    out_file="pv_dist_"$f1".csv"
    echo $data_dir$f1
    combine_csv_in_folder.sh $data_dir$f1 $out_file
    mv $data_tmp_dir"/"$out_file $tmp_data_dir"/volume_price_distr"
done
