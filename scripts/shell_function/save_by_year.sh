dir1="/home/davidyu/stock/data/history_data/rongzirongquan/"
cd $dir1
for i in `seq 2010 2020`
do
    echo $i
    mkdir $i
    find $dir1 -name "*$i*" -exec mv {} $dir1$i \;
done
