#!/bin/bash
find . -type d 
find . -type f -maxdepth 1
du -sh *   ## all folder size
du -h -d 1  ## for hidden file to check the size
du -h -d 1 | sort -nr #  size and sort by size
du -s * | sort -nr



ls -al /home/davidyu/stock/outside_data | grep "^d"  ## list the directory of the path
ls -al /home/davidyu/stock/data | grep "^d"  ## list the directory of the path

find ./ -regex ".*\.Rout\|.*\.csv"  # find some extension files

#find ./ -regex ".*\.log" -exec rm -rf{} \
find ./ -regex ".*\.log\|.*\.csv\|.*\.txt\|.*\.out" | xargs rm -rf
find ./ -regex ".*\.log\|.*\.csv" | xargs rm -rf

find ./ -regex ".*\.log\|.*\.csv\|.*\.txt\|.*\.out"   -exec du -sh {} \; | sort -nr

# before 150 min update, and count
find ./  -cmin -150 |wc -l
## before 60 min update
find . -mmin -60 -type f

# delete first line of file
sed -i '1d' <file>

# every file number of rows and sort
find . -name "*.csv" |xargs wc -l | sort -n

# find and copy file
find . -name "60*" | xargs -t -i cp -rf {} /home/davidyu/stock/data//day_history/

# find modified before n days
find ./  -mtime +100
find ./  -mtime +100 |  cut -d "." -f2 | sed -e 's/\///'   

# find folder and rm
find ./  -maxdepth 1 -type d  -exec rm -rf {} \;
# add permission to david for the foler
chown -R david elasticsearch-7.6.2/

