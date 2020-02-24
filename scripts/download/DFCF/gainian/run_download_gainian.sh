#python make_html.py > gainian_list.csv
file1="gainian.txt"
while read -r line
do
    wget $line -O $file1
    if [ `ls -l $file1 | awk '{print $5}'` -lt 300 ];then
        echo $line"++++"
        echo 'error'
    else
        sed -i 's/var =//g' $file1
        python download_gainian.py
        rm -rf $file1
    fi
    sleep 1.3s
done < gainian_list_gainian.csv

