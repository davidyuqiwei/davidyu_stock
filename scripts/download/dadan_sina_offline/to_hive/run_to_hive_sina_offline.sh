source ~/.bashrc
cd `dirname $0`

sh dadan_sina_to_hive.sh dadan_sina.cfg

if [ $? -ne 0  ];then
    echo "failed to hive"
else
    echo "OK to hive"
fi




