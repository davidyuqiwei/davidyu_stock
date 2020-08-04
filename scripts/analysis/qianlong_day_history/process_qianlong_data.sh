#!/usr/bin/sh
data_path="/home/davidyu/stock/data/tmp_data/qianlong_day_history/"
move_path="process"
cd $data_path
for file in *.txt 
do 
    echo $file
    sed -i '1,3d' $file
    cp $file $data_path$move_path
done
#sed -i '1,3d' $file1
