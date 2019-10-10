#!/usr/bin/sh
data_dir="/home/davidyu/stock/data/news_report"
#data_dir="grep -r 5G /home/davidyu/stock/data/news_report"
#grep -r 5G $data_dir
#grep -o 增长 $data_dir |wc -l
rm -rf text.log
touch text.log

for file in $data_dir/*/*
do 
    a1=`grep -o 甲醇 $file |wc -l`
    file_name=${file##*/}
    echo ${file_name:0:6} $a1  >> jiachun.log
done
awk '{sum[$1]+=$2}END{for(c in sum){print c,sum[c]}}' jiachun.log > jiachun_stat.txt
