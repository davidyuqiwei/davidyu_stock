source ~/.bashrc
cd `dirname $0`

# source url :  http://data.eastmoney.com/jgdy/tj.html
download_date=`date +%Y-%m-%d`
for((i=1;i<=2000;i++)); 
do
    url="http://data.eastmoney.com/DataCenter_V3/jgdy/xx.ashx?pagesize=50&page=$i&js=var%20DVlQgtlz&param=&sortRule=-1&sortType=0&rt=52777082"
	file1="data_"$download_date".txt"
	wget $url -O $file1
	## sed
	sed -i s/data/Data\\n/g $file1
	sed -i '1d' $file1
	sed -i -e s/\\[/{/g  -e s/\\]//g -e s/\;//g -e s/.// -e s/.// -e s/.$// $file1
	sed -i '2d' $file1
	python download_jigoudiaoyan.py
	rm -rf $file1
    sleep 5s
done


