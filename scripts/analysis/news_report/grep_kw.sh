#!/usr/bin/sh
source ~/.bashrc
basedir=`cd $(dirname $0); pwd -P`
#basedir="$( dirname "${BASH_SOURCE[0]}"  )"
echo $basedir

path="/home/davidyu/stock/data/news_report"
cd $path
#curr_dir=`pwd`
#curr_dir=`dirname $0`
#find -name $path/*2018* | xargs grep -r 用途广泛  > $basedir/yongtuguangfan.txt
find -name $path/*2018* | xargs grep -r 氢能  > $result_data/qingneng.txt
#touch $basedir/test_20190320.txt


