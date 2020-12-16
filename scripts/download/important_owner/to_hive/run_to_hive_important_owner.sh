source ~/.bashrc
cd `dirname $0`

sh to_hive.sh important_owner.cfg
mv /home/davidyu/stock/data/important_owner/*.csv /home/davidyu/stock/data/history_data/important_owner
