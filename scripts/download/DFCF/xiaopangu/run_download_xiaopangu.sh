source ~/.bashrc
cd `dirname $0`
sh wget_xiaopangu.sh
if [ $? -ne 0 ];then
    echo "wget error"
    exit 2
else
    python download_xiaopangu_json_to_df.py
    rm -rf *.txt  
fi

