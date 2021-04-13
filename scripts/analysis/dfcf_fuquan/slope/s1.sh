source ~/.bashrc
cd `dirname $0`

#cd /home/davidyu/stock/scripts/davidyu_stock/scripts/functions/common/slope

while read -r line
do
    python dfcfStockSlope_date.py $line "2020-11-08" "2020-12-31"
done<stk_list.txt
