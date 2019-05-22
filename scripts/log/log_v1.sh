#!/usr/bin/sh
check_dir=/home/davidyu/stock/data/all_news
#find $check_dir -type f -mtime -1 -size +100k -size -400k | xargs ls -l 
# find -mtime , search in the yesterday range
find $check_dir -type f -mtime -1 -size -2k | xargs ls -l 

