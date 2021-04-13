source ~/.bashrc
cd `dirname $0`
rm -rf predict_out.csv
while read -r line 
do
    python predict.py $line 3
    python predict.py $line 5
done < $hs_300_list_data
