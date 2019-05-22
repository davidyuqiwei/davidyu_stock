#!/usr/bin/sh
cd `dirname $0`
curr_dir=`pwd`
sep="_____"
programName=${0##*/}   ### filename without type e.g.  test.sh  test
file_name=${programName%.*} ## filename   'test.sh'
date_run=`date +"%Y-%m-%d" `
#`sh clean_dir.sh`
python download_fin_report.py > $curr_dir/python.log



