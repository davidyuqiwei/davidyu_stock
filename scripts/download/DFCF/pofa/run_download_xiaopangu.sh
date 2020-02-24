source ~/.bashrc
cd `dirname $0`
sh wget_xiaopangu.sh
python download_xiaopangu_json_to_df.py 
rm -rf *.txt *.csv

