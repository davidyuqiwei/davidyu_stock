source ~/.bashrc
cd `dirname $0`
while read -r line 
do
    if [[ $line != "code" ]];then
        python wy_regression.py $line
        sleep 0.5s
    fi
done < stock_list.txt

