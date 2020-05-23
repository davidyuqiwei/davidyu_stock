download_date=`date +%Y-%m-%d`
j=1032
for ((i=1; i<=j; i++))
do
	url="http://data.eastmoney.com/DataCenter_V3/jgdy/xx.ashx?pagesize=50&page=$i&js=var%20DVlQgtlz&param=&sortRule=-1&sortType=0&rt=52777082"
	# source url :   http://data.eastmoney.com/jgdy/tj.html
	
	file1="data_"$download_date".txt"
	wget $url -O $file1
	sed -i s/data/Data\\n/g $file1
	sed -i '1d' $file1
	sed -i -e s/\\[/{/g  -e s/\\]//g -e s/\;//g -e s/.// -e s/.// -e s/.$// $file1
	# download it
	python download_jigoudiaoyan_history.py
    rm -rf $file1
    sleep 3s
done



#python shijinglv_json_to_df.py
#rm -rf $file1
#python download_dazongjiaoyi.py $file1

