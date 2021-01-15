data_dir="/home/davidyu/stock/data/dadan_real_time_ifeng/"
cd $data_dir
for i in `ls | grep -v "combine_data"`
do 
    out_file=$i".csv"
    echo $i".csv"
    combine_csv_in_folder.sh $data_dir$i $out_file
    mv $data_tmp_dir"/"$out_file $data_dir"combine_data"
done

#out_file="dadan_real_time_ifeng.csv"
#combine_csv_in_folder.sh "/home/davidyu/stock/data/dadan_real_time_ifeng" $out_file
#mv $data_tmp_dir"/"$out_file $tmp_data_dir"/dadan_real_time_ifeng"

