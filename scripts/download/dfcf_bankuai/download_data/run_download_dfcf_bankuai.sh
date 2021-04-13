download_date=`date +%Y-%m-%d`

source ~/.bashrc
cd `dirname $0`

file1="dfcf_bankuai_"$download_date".txt"

url1="http://push2.eastmoney.com/api/qt/clist/get?cb=jQuery112307450807467238565_1610970772802&fid=f62&po=1&pz=5000&pn=1&np=1&fltt=2&invt=2&ut=b2884a393a59ad64002292a3e90d46a5&fs=m%3A90+t%3A3&fields=f12%2Cf14%2Cf2%2Cf3%2Cf62%2Cf184%2Cf66%2Cf69%2Cf72%2Cf75%2Cf78%2Cf81%2Cf84%2Cf87%2Cf204%2Cf205%2Cf124"


wget $url1 -O $file1
sh clean_data.sh $file1
python parse_to_df.py $file1
mv *.txt /home/davidyu/stock/data/dfcf_bankuai/raw_data
sleep 3s

############################################################
file1="dfcf_hangye_"$download_date".txt"
url1="http://push2.eastmoney.com/api/qt/clist/get?cb=jQuery112304260933344733444_1610974633817&fid=f62&po=1&pz=5000&pn=1&np=1&fltt=2&invt=2&ut=b2884a393a59ad64002292a3e90d46a5&fs=m%3A90+t%3A2&fields=f12%2Cf14%2Cf2%2Cf3%2Cf62%2Cf184%2Cf66%2Cf69%2Cf72%2Cf75%2Cf78%2Cf81%2Cf84%2Cf87%2Cf204%2Cf205%2Cf124"


wget $url1 -O $file1
sh clean_data.sh $file1
python parse_to_df.py $file1
mv *.txt /home/davidyu/stock/data/dfcf_bankuai/raw_data
sleep 3s

#############################
file1="dfcf_diyu_"$download_date".txt"
url1="http://push2.eastmoney.com/api/qt/clist/get?cb=jQuery112304407394164811651_1610974808056&fid=f62&po=1&pz=50&pn=1&np=1&fltt=2&invt=2&ut=b2884a393a59ad64002292a3e90d46a5&fs=m%3A90+t%3A1&fields=f12%2Cf14%2Cf2%2Cf3%2Cf62%2Cf184%2Cf66%2Cf69%2Cf72%2Cf75%2Cf78%2Cf81%2Cf84%2Cf87%2Cf204%2Cf205%2Cf124"


wget $url1 -O $file1
sh clean_data.sh $file1
python parse_to_df.py $file1
mv *.txt /home/davidyu/stock/data/dfcf_bankuai/raw_data



