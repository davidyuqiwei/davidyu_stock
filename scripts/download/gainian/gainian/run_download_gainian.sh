#python make_html.py > gainian_list.csv
file1="gainian.txt"
touch a.log
while read -r line
do
    wget $line -O $file1
    if [ `ls -l $file1 | awk '{print $5}'` -lt 300 ];then
        echo "not dowload "$line
    else
        sed -i 's/var =//g' $file1
        python download_gainian.py
        echo $line > a.log
        rm -rf $file1
    fi
    sleep 1.3s
done < gainian_list_gainian.csv

