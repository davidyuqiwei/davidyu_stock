#today_date=`date +%Y_%m_%d`
#yesterday_date=`date -d "last day" +%Y-%m-%d`
#file="DADAN_"$yesterday_date".csv"

#echo $file
#echo "今天日期是: `date +%Y_%m_%d`"  

sh run_scala_insert.sh
echo $? 

