#!/usr/bin/sh
basedir=`cd $(dirname $0); pwd -P`
#basedir="$( dirname "${BASH_SOURCE[0]}"  )"
#echo $basedir
out_dir="/home/davidyu/stock/data/news_report_out_data"
data_path="/home/davidyu/stock/data/news_report"
#find $data_path -name "*2018*" | xargs grep -r 用途广泛  > $basedir/yongtuguangfan.txt
find $data_path -name "*2019*" | xargs grep -r 新材料  > $out_dir/xincailiao.txt
#find $data_path -name "*2018*" | xargs grep -r 铋  > $out_dir/JinShuBi.txt
#touch $basedir/test_20190320.txt
#cd $data_path
#curr_dir=`pwd`
#curr_dir=`dirname $0`



