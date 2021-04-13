download_date=`date +%Y-%m-%d`

source ~/.bashrc
cd `dirname $0`

save_dir="/home/davidyu/stock/data/dfcf_bankuai_zijin/raw_data"
url1="http://push2.eastmoney.com/api/qt/clist/get?cb=jQuery112308966923211600797_1610903033053&pn=1&pz=500&po=1&np=1&fields=f12%2Cf13%2Cf14%2Cf62&fid=f62&fs=m%3A90%2Bt%3A2&ut=b2884a393a59ad64002292a3e90d46a5&_=1610903033054"
file1="dfcf_bankuai_zijin_"$download_date".txt"


wget $url1 -O $file1
sh clean_data.sh $file1
python parse_to_df.py $file1

mv *.txt $save_dir



