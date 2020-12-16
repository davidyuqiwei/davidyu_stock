source ~/.bashrc
cd `dirname $0`

download_date=`date +%Y-%m-%d`
url="http://data.eastmoney.com/DataCenter_V3/jgdy/xx.ashx?pagesize=50&page=1&js=var%20DVlQgtlz&param=&sortRule=-1&sortType=0&rt=52777082"
# source url :  http://data.eastmoney.com/jgdy/tj.html


file1="data_"$download_date".txt"
wget $url -O $file1

#sed -i 's/var DVlQgtlz=//g' $file1
#file1="data_"$download_date".txt"
#wget $url -O $file1
##    

sed -i s/data/Data\\n/g $file1
sed -i '1d' $file1
sed -i -e s/\\[/{/g  -e s/\\]//g -e s/\;//g -e s/.// -e s/.// -e s/.$// $file1


#sed -i s/\\,"/\\}/g $file1
sed -i '2d' $file1
python download_jigoudiaoyan.py
rm -rf $file1
