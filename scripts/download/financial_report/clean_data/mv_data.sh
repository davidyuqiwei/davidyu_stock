tgt_dir="/home/davidyu/stock/data/history_data/financial_report/"
src_dir="/home/davidyu/stock/data/financial_report/"
for i in `ls $src_dir`
do
    if [ ! -d $tgt_dir$i ];then
        mkdir $tgt_dir$i
    fi
    cp -f $src_dir$i/*.csv $tgt_dir$i
done


