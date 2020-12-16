source ~/.bashrc
cd `dirname $0`

cd /home/davidyu/stock/data/important_owner
grep -r $1 | grep 增加 | awk -F "," '{print $7 "," $8 "," $3 "," $14 "," $13 "," $18}'
