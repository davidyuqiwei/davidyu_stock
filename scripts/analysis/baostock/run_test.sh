source ~/.bashrc
cd `dirname $0`
while read -r line 
do
    if [[ $line == 60* ]] || [[ $line == 00* ]];then
        python stock_slope.py $line '2020-04-25' 60 >> slope.txt
        #echo $line
        #sleep 2.5s
    fi
done < /home/davidyu/stock/data/tmp/stock_list.txt

