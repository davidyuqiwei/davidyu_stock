# http://data.eastmoney.com/dxf/detail.aspx?market=all
source ~/.bashrc
cd `dirname $0`
file1='test.txt'
wget 'http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?token=70f12f2f4f091e459a279469fe49eca5&st=ltsj&sr=1&p=1&ps=3000000&type=XSJJ_NJ_PC&js=var%20KOnsjkuq={pages:(tp),data:(x),font:(font)}&filter=(mkt=)(ltsj%3E=^2017-05-22^%20and%20ltsj%3C=^2022-05-22^)&rt=53004127' -O $file1

sed -i 's/ //g' $file1
python download_jiejin_history.py
rm -rf $file1
#sed -i s/data/Data\\n/g $file1


