source ~/.bashrc
cd `dirname $0`
# make stock_list
#file_in=$stock_data/basic_info/stock_basic_info.csv
#`awk -F "," '{print $1}' $file_in | sed '1d' > stock_list.txt`

##---------- test -----------------
#`awk -F "," '{print $1}' $file_in | sed '1d' | head -10 > stock_list.txt`

while read -r line 
do
    if [[ $line != "code" ]];then
        python download_liutong_owner.py $line
        sleep 4.5s
    fi
done < $stock_list_data



