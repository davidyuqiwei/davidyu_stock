source ~/.bashrc
cd `dirname $0`
python download_all_news.py
kill_web_files=$stock_script"kill_webcontent/kill_webcontent.sh"
sh $kill_web_files




