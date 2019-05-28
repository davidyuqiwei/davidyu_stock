#!/bin/bash
find . -type d 
du -sh *   ## all folder size
du -h -d 1  ## for hidden file to check the size
du -h -d 1 | sort -nr #  size and sort by size

ls -al /home/davidyu/stock/outside_data | grep "^d"  ## list the directory of the path
ls -al /home/davidyu/stock/data | grep "^d"  ## list the directory of the path

find ./ -regex ".*\.Rout\|.*\.csv"  # find some extension files

#find ./ -regex ".*\.log" -exec rm -rf{} \
find ./ -regex ".*\.log\|.*\.csv\|.*\.txt" | xargs rm -rf





