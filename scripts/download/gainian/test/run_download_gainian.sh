#python make_html.py > gainian_list.csv
source ~/.bashrc
cd `dirname $0`
file1="gainian.txt"
touch valid_url.txt
while read -r line
do
    wget $line -O $file1
    # get the download file size
    if [ `ls -l $file1 | awk '{print $5}'` -lt 300 ];then
        touch a.log
    else
        sed -i 's/var =//g' $file1
        python download_gainian.py
        rm -rf $file1
        echo $line >> valid_url.txt
    fi
    sleep 2.3s
done < gainian_list_bankuai.csv
rm -rf $file1
