source ~/.bashrc
cd `dirname $0`
stock_date="2020-11-25"
while read -r line 
do
    if [[ $line != "code" ]];then
        python b1.py $line 
        sed -r 's/YEAR/'$line'/g' load_data.sql > run_hive.sql
        hive -f run_hive.sql
        #sleep 0.5s
    fi
done < year.txt




