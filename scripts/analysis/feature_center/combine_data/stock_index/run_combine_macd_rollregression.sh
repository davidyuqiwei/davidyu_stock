source ~/.bashrc
cd `dirname $0`
window=$1
while read -r line 
do
    python combine_macd_rollregression.py $line $window
done<$hs_300_list_data
