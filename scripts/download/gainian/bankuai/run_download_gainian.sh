#python make_html.py > gainian_list.csv
source ~/.bashrc
cd `dirname $0`
file1="gainian.txt"
while read -r line
do
    wget $line -O $file1
    if [ `ls -l $file1 | awk '{print $5}'` -lt 300 ];then
        #echo $line"++++"
        touch a.log
        #echo 'error'
    else
        sed -i 's/var =//g' $file1
        python download_gainian.py
        rm -rf $file1
        echo $line
    fi
    sleep 1.3s
done < gainian_list_bankuai.csv
rm -rf $file1
rm -rf pidfile.txt
