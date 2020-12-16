source ~/.bashrc
cd `dirname $0`
stock_date="2020-11-25"
while read -r line 
do
    if [[ $line != "code" ]];then
        python kdj_macd_feature.py $line $stock_date
        #sleep 0.5s
    fi
done < stock_list.txt

