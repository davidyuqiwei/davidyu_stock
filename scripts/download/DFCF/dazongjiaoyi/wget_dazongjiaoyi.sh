download_date=`date +%Y-%m-%d`
url="http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?type=DZJYXQ&token=70f12f2f4f091e459a279469fe49eca5&cmd=&st=SECUCODE&sr=1&p=1&ps=1000&js=var%20eYXsjQKi={pages:(tp),data:(x)}&filter=(Stype=%27EQA%27)(TDATE=^$download_date^)&rt=52737067"
# source url :   http://data.eastmoney.com/dzjy/dzjy_mrmxa.aspx

file1="data_"$download_date".txt"
wget $url -O $file1
sed -i 's/var eYXsjQKi={pages:1,data:/{"pages":/g' $file1


python download_dazongjiaoyi.py $file1

