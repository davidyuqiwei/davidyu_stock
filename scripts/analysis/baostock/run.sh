source ~/.bashrc
cd `dirname $0`
while read -r line 
do
    if [[ $line == 60* ]] || [[ $line == 00* ]];then
        python stock_return.py $line
    fi
done < $stock_list_data
