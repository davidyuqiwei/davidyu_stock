download_date=`date +%Y-%m-%d`

source ~/.bashrc
cd `dirname $0`
file1="a_hk_"$download_date".txt"

url1="http://6.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112404938258627832648_1610758898329&pn=1&pz=300&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=b:DLMK0101&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152,f191,f192,f193,f186,f185,f187,f189,f188&_=1610758898331"


wget $url1 -O $file1



