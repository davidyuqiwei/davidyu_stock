#!/usr/bin/sh
source ~/.bashrc
cd `dirname $0`
sh run_download_day_history_yahoo.sh
sh run_scala.sh
#nohup ./run.sh & echo $! > pidfile.txt
#nohup sh run_python.sh & echo $! > pidfile.txt
