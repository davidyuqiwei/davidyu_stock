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
done < data_dir.py

