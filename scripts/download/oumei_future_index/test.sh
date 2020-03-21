download_date=`date +%Y-%m-%d`
file1="IF_"$download_date".txt"
wget https://vipmoney.eastmoney.com/Crumbs/Content/data/IF.js?r=3995 -O $file1

sed -i '1d' $file1
sed -i -e s/\",//g -e s/\"//g -e s/#//g $file1 
