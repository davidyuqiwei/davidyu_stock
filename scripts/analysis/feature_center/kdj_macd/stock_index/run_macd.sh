source ~/.bashrc
cd `dirname $0`
out_dir="/home/davidyu/stock/data/feature_center/macd/stock_index"

if [ ! -d "$out_dir" ];then
  mkdir -p $out_dir
fi

while read -r line 
do
    if [[ $line == 60* ]] || [[ $line == 00* ]] || [[ $line == 30*  ]];then
        python stock_macd_kdj.py $line $line"_macd.csv" $out_dir
        echo $line
    fi
#done < $stock_list_data
done < $hs_300_list_data
#done < stock_test.sh
#done < $stock_list_data_test



