## load system souce file
source ~/.bashrc
echo $stock_data
# get the script current dir
this_dir=`cd $(dirname $0); pwd -P`
echo $this_dir
##----------------------------------------------------------
##  the news report dir and save dir ##
save_dir=$stock_data"/news_report_out_data"
news_report_dir=$stock_data"/news_report"
echo $news_report_dir


## grep it
#grep -r "氢能" $news_report_dir > $save_dir"/qingneng.txt"

kw_list=("氢能,qingneng" "纤维素醚,xianweisumi" "白酒,baijiu" "半导体,bandaoti" "刻蚀机,keshiji")
k=-1
for i in ${kw_list[*]};do
    k=$((k+1))
    echo $i
    grep_str=`echo $i | cut -d ',' -f1`
    save_file_name=`echo $i | cut -d ',' -f2`
    echo $grep_str
    echo "=================="
    grep -r $grep_str $news_report_dir > $save_dir"/"$save_file_name".txt"
done
#echo ${kw_list[1]}
