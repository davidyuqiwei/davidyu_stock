source ~/.bashrc
cd `dirname $0`
cat  a.log | grep -n '^2021' > b.log
