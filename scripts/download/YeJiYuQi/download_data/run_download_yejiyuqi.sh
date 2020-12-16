source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
python download_yejiyuqi.py
rm -rf geckodriver.log
