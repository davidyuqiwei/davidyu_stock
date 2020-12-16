#source ~/.bashrc
cd `dirname $0`
echo "=============================================="
echo "=============================================="
echo "=========== start pirnt data status =========="
echo "=============================================="
echo "=============================================="
while read -r line 
do
    if [[ -d $line ]];then
        echo "++++      "$line
        ls $line -ltr | tail -1
        echo "=============================================="
    fi
done < DATA_DIR.py

echo " =========== check dazongjiaoyi ================="
#spark-sql -f check_dazongjiaoyi.sql
spark-sql -e 'select stock_date from stock_dev.dazongjiaoyi where stock_date <> "stock_date" order by stock_date desc limit 2;'
echo " =========== check dadan_DFCF ================="
#spark-sql -f check_dadan_DFCF.sql
spark-sql -e 'select stock_date from stock_dev.dadan_DFCF where stock_date <> "stock_date" order by stock_date desc limit 2;'

echo " =========== check day_history_wangyi ================="
#spark-sql -f day_history_wangyi.sql
spark-sql -e 'select stock_date from stock_dev.day_history_wangyi where stock_date <> "stock_date" order by stock_date desc limit 2;'

echo " =========== check jigoudiaoyan ================="
spark-sql -e 'select stock_date from stock_dev.jigoudiaoyan where stock_date <> "stock_date" order by stock_date desc limit 2;'


echo " =========== check yejiyuqi ================="
spark-sql -e 'select stock_date from stock_dev.yejiyuqi where stock_date <> "stock_date" order by stock_date desc limit 2;'


echo " =========== check important owner ================="
spark-sql -e 'select stock_date from stock_dev.important_owner where stock_date <> "stock_date" order by stock_date desc limit 2;'

