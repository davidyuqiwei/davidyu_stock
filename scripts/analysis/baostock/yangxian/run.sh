source ~/.bashrc
cd `dirname $0`

while read -r line 
do
    if [[ $line != "code" ]];then
        python yangxian.py $line
        #echo $line 
    fi
done <$stock_list_data


