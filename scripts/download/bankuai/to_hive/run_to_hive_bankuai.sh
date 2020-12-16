source ~/.bashrc
cd `dirname $0`

sh to_hive.sh bankuai.cfg
mv /home/davidyu/stock/data/bankuai/*.csv /home/davidyu/stock/data/history_data/bankuai
