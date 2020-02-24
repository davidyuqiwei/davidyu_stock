#!/usr/bin/sh
basedir=`cd $(dirname $0); pwd -P`
#basedir="$( dirname "${BASH_SOURCE[0]}"  )"
#echo $basedir
out_dir="/home/davidyu/stock/data/news_report_out_data"
data_path="/home/davidyu/stock/data/news_report"
input_string="钨"
out_file="jinshuwu.txt"
#find $data_path -name "*2018*" | xargs grep -r 用途广泛  > $basedir/yongtuguangfan.txt
#find $data_path -name "*2019*" | xargs grep -r $input_string > $out_dir/$out_file
find $data_path -name "*2019*" | xargs grep -r $input_string > $out_dir/$out_file
# add input_string in the first line
sed -i 1i$input_string $out_dir/$out_file
echo "finish"


# "/" 分隔符取第七个
#  grep -r data/news_report chaoyingcailiao.txt | awk -F "\/" '{print $7}' | sort | uniq -c


#find $data_path -name "*2018*" | xargs grep -r 铋  > $out_dir/JinShuBi.txt
#touch $basedir/test_20190320.txt
#cd $data_path
#curr_dir=`pwd`
#curr_dir=`dirname $0`



