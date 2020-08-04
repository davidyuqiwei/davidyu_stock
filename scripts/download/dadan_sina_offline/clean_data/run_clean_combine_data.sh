source ~/.bashrc
cd `dirname $0`
sh combine_data.sh
python clean_data.py

if [ $? -ne 0  ];then
    echo "failed data clean & combine"
else
    echo "OK data clean & combine"
fi

echo "=============================================================="
echo "=============================================================="

