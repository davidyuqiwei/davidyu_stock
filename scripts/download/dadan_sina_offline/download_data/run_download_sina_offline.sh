source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
python download_dadan_sina_offline.py

if [ $? -ne 0  ];then
    echo "failed data download"
else
    echo "OK data download"
fi




