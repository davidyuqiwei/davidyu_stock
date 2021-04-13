source ~/.bashrc
cd `dirname $0`
while read -r line 
do
    python xgb_model.py $line 3
    python xgb_model.py $line 5
done < $hs_300_list_data
